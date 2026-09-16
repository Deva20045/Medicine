#!/usr/bin/env node
/*
 * Dependency-free runtime smoke test for the standalone PULSE Medicine app.
 * It runs the inline application script against a minimal DOM shim, then checks
 * the full roadmap (live + "Soon") and a live Chapter 1 quiz flow. It complements
 * the structural checks in check_integrity.py; it is not a visual-browser test.
 */
'use strict';

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const appPath = path.join(__dirname, 'pulse-medicine.html');
const html = fs.readFileSync(appPath, 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) throw new Error('No inline application script found.');

class FakeClassList {
  constructor() { this.values = new Set(); }
  add(...values) { values.forEach((value) => this.values.add(value)); }
  remove(...values) { values.forEach((value) => this.values.delete(value)); }
  toggle(value, force) {
    if (force === true) { this.add(value); return true; }
    if (force === false) { this.remove(value); return false; }
    if (this.values.has(value)) { this.remove(value); return false; }
    this.add(value);
    return true;
  }
  contains(value) { return this.values.has(value); }
}

class FakeElement {
  constructor(tagName = 'div') {
    this.tagName = tagName;
    this.classList = new FakeClassList();
    this.style = {};
    this.children = [];
    this.textContent = '';
    this.disabled = false;
    this.onclick = null;
    this._innerHTML = '';
  }
  set innerHTML(value) {
    this._innerHTML = String(value);
    this.children = [];
  }
  get innerHTML() { return this._innerHTML; }
  appendChild(child) { this.children.push(child); return child; }
  querySelector() { const child = new FakeElement(); this.appendChild(child); return child; }
  getBoundingClientRect() { return { left: 0, top: 0, width: 100 }; }
  remove() {}
}

const elements = new Map();
for (const match of html.matchAll(/id="([^"]+)"/g)) {
  elements.set(match[1], new FakeElement());
}
for (const match of scriptMatch[1].matchAll(/\$\('([^']+)'\)/g)) {
  if (!elements.has(match[1])) elements.set(match[1], new FakeElement());
}

const document = {
  body: new FakeElement('body'),
  getElementById(id) {
    if (!elements.has(id)) elements.set(id, new FakeElement());
    return elements.get(id);
  },
  createElement(tagName) { return new FakeElement(tagName); },
  addEventListener() {},
};
const localStorage = {
  values: new Map(),
  getItem(key) { return this.values.has(key) ? this.values.get(key) : null; },
  setItem(key, value) { this.values.set(key, String(value)); },
};
const context = {
  document, localStorage, console, Math, Date, setTimeout: () => {},
  window: { scrollY: 0 },
};
vm.createContext(context);
vm.runInContext(`${scriptMatch[1]}

globalThis.__PULSE_SMOKE__ = {
  QUESTIONS, UNITS, CHAPTERS, QBYID, unitsOf,
  chapters() { renderChapters(); },
  path(number) { curCh = number; renderPath(); },
  start(number) { curCh = number; curUnit = unitsOf(number)[0]; beginUnit(); return curUnit; }
};`, context, { filename: appPath });

const pulse = context.__PULSE_SMOKE__;
function assert(condition, message) {
  if (!condition) throw new Error(message);
}

// Expectations are derived from the chapter source artifacts in data/, so the
// smoke test never drifts when questions are added or reordered.
const dataDir = path.join(__dirname, 'data');
const source = fs
  .readdirSync(dataDir)
  .filter((name) => /^ch\d{2}\.json$/.test(name))
  .sort()
  .map((name) => JSON.parse(fs.readFileSync(path.join(dataDir, name), 'utf8')));
const sourceQuestions = source.flatMap((chapter) => chapter.questions);
const sourceUnits = source.flatMap((chapter) => chapter.units);
const liveCount = source.length;
const lastId = (number) => sourceQuestions.filter((q) => q.id.startsWith(`MED-C${number}-`)).pop().id;
const unitCount = (number) => sourceUnits.filter((u) => u.ch === number).length;
const firstUnitSize = (number) => sourceUnits.find((u) => u.ch === number && u.n === 1).qs.length;
const firstPage = (number) => source.find((c) => c.chapter === number).pageRange.split('-')[0];
const lastPage = (number) => source.find((c) => c.chapter === number).pageRange.split('-')[1];

assert(pulse.QUESTIONS.length === sourceQuestions.length,
  `Expected ${sourceQuestions.length} questions, found ${pulse.QUESTIONS.length}.`);
assert(pulse.UNITS.length === sourceUnits.length,
  `Expected ${sourceUnits.length} units, found ${pulse.UNITS.length}.`);
assert(pulse.CHAPTERS.length >= 2, 'Roadmap should list the whole book from day one.');
assert(pulse.CHAPTERS.filter((chapter) => chapter.live).length === liveCount,
  `Expected ${liveCount} live chapters, found ${pulse.CHAPTERS.filter((c) => c.live).length}.`);

pulse.chapters();
assert(elements.get('chList').children.length === pulse.CHAPTERS.length,
  `Roadmap did not render all ${pulse.CHAPTERS.length} chapter rows.`);
assert(elements.get('chList').children[0].innerHTML.includes('units'),
  'Live Chapter 1 row did not render its unit progress.');
const soonRows = elements.get('chList').children.slice(1).filter((row) => row.innerHTML.includes('Soon'));
assert(soonRows.length === pulse.CHAPTERS.length - liveCount,
  'Not every non-live chapter shows a "Soon" badge.');

// Every live chapter renders its path and starts a quiz at runtime.
for (const chapter of source) {
  const number = chapter.chapter;
  pulse.path(number);
  assert(pulse.unitsOf(number).length === unitCount(number),
    `Chapter ${number} unit lookup did not return ${unitCount(number)} units.`);
  assert(elements.get('pathTitle').textContent === pulse.CHAPTERS[number - 1].t,
    `Chapter ${number} path title did not render.`);
  const started = pulse.start(number);
  assert(started.id === `MED-U${number}-1`, `Chapter ${number} first unit did not start.`);
  assert(elements.get('qcount').textContent === `QUESTION 1 OF ${firstUnitSize(number)}`,
    `Quiz count did not render the Chapter ${number} unit.`);
  assert(elements.get('qtext').textContent.length > 20, 'Quiz did not render a question stem.');
  assert(elements.get('opts').children.length === 4, `Chapter ${number} quiz did not render four options.`);
  assert(pulse.QBYID[lastId(number)].page === Number(lastPage(number)),
    `Final Chapter ${number} question ${lastId(number)} is unavailable.`);
  assert(pulse.QBYID[started.qs[0]].page === Number(firstPage(number)),
    `First Chapter ${number} question does not start at its Book page.`);
}

console.log(`PASS: roadmap of ${pulse.CHAPTERS.length} chapters (${liveCount} live, rest "Soon"), ` +
  `Chapter ${source.map((c) => c.chapter).join(', ')} path data and quiz starts, and final ` +
  `questions render at runtime.`);
