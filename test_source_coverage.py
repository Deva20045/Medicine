"""Regression tests for evidence freshness/order, not visual or medical validation."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import build_content
from check_source_coverage import audit, content_digest, validate_manifest, write_report

ROOT = Path(__file__).resolve().parent


class SourceCoverageTests(unittest.TestCase):
    def setUp(self):
        self.chapter = json.loads((ROOT / 'data/ch01.json').read_text())
        self.manifest = json.loads((ROOT / 'data/source_review/ch01.json').read_text())

    def check(self):
        return validate_manifest(self.manifest, self.chapter, 705, 710)

    def test_reviewed_chapters_are_valid(self):
        for number, first, last in [(1, 705, 710), (2, 711, 716), (3, 717, 725),
                                    (4, 726, 729), (5, 730, 733)]:
            with self.subTest(chapter=number):
                chapter = json.loads((ROOT / f'data/ch{number:02d}.json').read_text())
                manifest = json.loads((ROOT / f'data/source_review/ch{number:02d}.json').read_text())
                self.assertEqual(validate_manifest(manifest, chapter, first, last), [])

    def test_same_page_question_swap_is_rejected_even_with_updated_hash(self):
        qs = self.chapter['questions']
        qs[0], qs[1] = qs[1], qs[0]
        self.manifest['contentSha256'] = content_digest(self.chapter)
        self.assertTrue(any('book order' in e for e in self.check()))

    def test_same_page_checklist_swap_is_rejected(self):
        elements = self.manifest['pages'][0]['elements']
        elements[0], elements[1] = elements[1], elements[0]
        self.assertTrue(any('reading order' in e for e in self.check()))

    def test_missing_element_is_rejected(self):
        self.manifest['pages'][0]['elements'].pop()
        self.assertTrue(any('exactly once' in e for e in self.check()))

    def test_duplicate_question_reference_is_rejected(self):
        elements = self.manifest['pages'][0]['elements']
        elements[1]['questionIds'] = elements[0]['questionIds'][:]
        self.assertTrue(any('exactly once' in e for e in self.check()))

    def test_unknown_question_reference_is_rejected(self):
        self.manifest['pages'][0]['elements'][0]['questionIds'] = ['MED-C1-999']
        self.assertTrue(any('unknown question' in e for e in self.check()))

    def test_stale_answer_or_guide_requires_source_recheck(self):
        self.chapter['questions'][0]['ans'] = (self.chapter['questions'][0]['ans'] + 1) % 4
        self.assertTrue(any('stale review' in e for e in self.check()))
        self.chapter = json.loads((ROOT / 'data/ch01.json').read_text())
        self.chapter['units'][0]['guide'] += ' changed'
        self.assertTrue(any('stale review' in e for e in self.check()))

    def test_missing_page_is_rejected(self):
        self.manifest['pages'].pop()
        self.assertTrue(any('every chapter page' in e for e in self.check()))

    def test_missing_traversal_is_rejected(self):
        self.manifest['pages'][0]['traversal'] = ''
        self.assertTrue(any('traversal' in e for e in self.check()))

    def test_wrong_pdf_mapping_or_source_is_rejected(self):
        self.manifest['pages'][0]['pdfPage'] = 1
        self.manifest['pdf'] = 'uploads/Medicine_Vol3_Part5_pages_965-1034.pdf'
        errors = self.check()
        self.assertTrue(any('page map mismatch' in e for e in errors))
        self.assertTrue(any('wrong source PDF' in e for e in errors))

    def test_mismatched_question_page_is_rejected(self):
        self.chapter['questions'][0]['page'] = 706
        self.manifest['contentSha256'] = content_digest(self.chapter)
        self.assertTrue(any('different page' in e for e in self.check()))

    def test_unit_reordering_is_rejected(self):
        ids = self.chapter['units'][0]['qs']
        ids[0], ids[1] = ids[1], ids[0]
        self.manifest['contentSha256'] = content_digest(self.chapter)
        self.assertTrue(any('unit playback' in e for e in self.check()))

    def test_caveats_cannot_be_hidden_under_plain_reviewed_status(self):
        self.manifest['status'] = 'reviewed'
        self.assertTrue(any('caveats' in e for e in self.check()))

    def make_fixture(self, root):
        (root / 'data/source_review').mkdir(parents=True)
        (root / 'uploads').mkdir()
        pdf = b'test source bytes; no rendering is claimed by these tests'
        (root / self.manifest['pdf']).write_bytes(pdf)
        self.manifest['pdfSha256'] = hashlib.sha256(pdf).hexdigest()
        (root / 'data/ch01.json').write_text(json.dumps(self.chapter))
        (root / 'data/source_review/ch01.json').write_text(json.dumps(self.manifest))

    def test_inventory_never_certifies_unbuilt_chapters(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            rows, errors = audit(root)
            self.assertEqual(errors, [])
            self.assertEqual(len(rows), 74)
            self.assertEqual(sum(bool(r['manifest']) for r in rows), 1)
            self.assertEqual(rows[1]['status'], 'not-built')
            write_report(rows, errors, root)
            report = (root / 'SOURCE_REVIEW.md').read_text()
            self.assertIn('1/74 chapters', report)
            self.assertIn('Next in order: Ch 2', report)

    def test_changed_pdf_invalidates_review(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / self.manifest['pdf']).write_bytes(b'changed')
            rows, errors = audit(root)
            self.assertTrue(any('source PDF changed' in e for e in errors))
            self.assertEqual(rows[0]['status'], 'invalid-review')

    def test_build_rejects_stale_review_before_writing_app(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            self.chapter['questions'][0]['exp'] += ' changed'
            (root / 'data/ch01.json').write_text(json.dumps(self.chapter))
            with patch.object(build_content, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'stale review'):
                    build_content.main()
            self.assertFalse((root / 'pulse-medicine.html').exists())

    def test_malformed_review_is_reported_not_certified(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / 'data/source_review/ch01.json').write_text('{')
            rows, errors = audit(root)
            self.assertTrue(errors)
            self.assertFalse(rows[0]['manifest'])


if __name__ == '__main__':
    unittest.main()
