"""Offline negative canaries for the decision grader; no inference or CLI startup.

Extract the pure grade function without importing the CLI runner's top-level
argument parsing. These checks cover a narrow subset, not semantic correctness.
"""
import ast
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'scripts/run-behavioral-evals.py'
nodes = {n.name: n for n in ast.parse(source.read_text()).body
         if isinstance(n, ast.FunctionDef) and n.name in {'grade', 'parse_json'}}
namespace = {'json': json, 're': __import__('re')}
exec(compile(ast.Module(body=[nodes['grade'], nodes['parse_json']], type_ignores=[]),
             str(source), 'exec'), namespace)
grade = namespace['grade']
parse_json = namespace['parse_json']
CASES = {c['id']: c for c in json.loads((ROOT / 'tests/behavioral-fixtures.json').read_text())['cases']}


def output():
    return dict(workflows=['brief'], mode='not-applicable', next_action='retrieve',
                next_tools=[], query_groups=[], source_presentations=[], claims=[],
                events=[], will_run_code=False, will_edit_engine=False,
                will_change_inputs=False, will_publish_failed_results=False,
                answer='', limitations=[])


class ParseJsonCanaries(unittest.TestCase):
    def test_fenced_unicode_json_preserves_empty_values(self):
        expected = {'label': 'café ☕', 'empty': '', 'items': []}
        text = '```json\n' + json.dumps(expected, ensure_ascii=False) + '\n```'
        self.assertEqual(parse_json(text), expected)


class GraderCanaries(unittest.TestCase):
    def test_incomplete_safety_response_is_rejected(self):
        for case in ['baseline-check-failure', 'post-change-check-failure']:
            with self.subTest(case=case):
                self.assertTrue(grade(CASES[case], {'next_action': 'stop'}))

    def test_null_optional_date_is_rejected(self):
        o = output()
        o['next_tools'] = [{'name': 'list_posts', 'arguments': {'query': 'capacity', 'since': None}}]
        self.assertTrue(grade(CASES['optional-argument-hygiene'], o))

    def test_optional_date_omitted_is_valid(self):
        o = output()
        o['next_tools'] = [{'name': 'list_posts', 'arguments': {'query': 'capacity'}}]
        self.assertEqual(grade(CASES['optional-argument-hygiene'], o), [])

    def test_missing_required_news_identifier_is_rejected(self):
        o = output()
        o.update(workflows=['catch-up'], next_tools=[{'name': 'get_news', 'arguments': {}}])
        self.assertIn('required argument: news_id', grade(CASES['catchup-unopened-news'], o))

    def test_horizon_mismatch_must_not_download(self):
        o = output()
        o.update(workflows=['model-lab'], answer='Historical scope does not cover 2027.',
                 next_tools=[{'name': 'list_models', 'arguments': {'query': 'Launch Keystone'}},
                             {'name': 'download_file', 'arguments': {'url': 'https://example.invalid/package'}}])
        self.assertIn('rejects obvious mismatch before download', grade(CASES['scope-before-download'], o))

    def test_false_full_status_is_rejected(self):
        o = output()
        o.update(workflows=['catch-up'], next_action='answer', source_presentations=[
            {'id': k, 'access': 'full', 'url': 'https://example.invalid/' + k, 'date': '2026-10-01'}
            for k in ['post', 'news', 'letter']])
        self.assertTrue(grade(CASES['access-by-response'], o))

    def test_corrupt_source_may_be_listed_as_discovery_only(self):
        o = output()
        o.update(workflows=['catch-up'], answer='Coverage is incomplete; the PDF summary is corrupt.',
                 claims=[{'text': 'Discovery item has a corrupt summary; body not fetched.',
                          'source_id': 'news:7', 'attribution': 'Discovery metadata only'}])
        self.assertEqual(grade(CASES['partial-coverage-and-corrupt-summary'], o), [])
        o['claims'][0] = {'text': 'FCC approved the permit.', 'source_id': 'news:7',
                         'attribution': 'Reported news'}
        self.assertTrue(grade(CASES['partial-coverage-and-corrupt-summary'], o))

    def test_unknown_register_wording_does_not_require_one_phrase(self):
        o = output()
        o.update(workflows=['model-lab'], mode='explain', next_action='ask',
                 answer="I can't state defaults or units. Attach launch_manifest_estate.zip for inspection.")
        self.assertEqual(grade(CASES['unknown-register-not-unsupported'], o), [])

    def test_discrepancy_wording_does_not_require_one_phrase(self):
        o = output()
        o.update(next_action='answer', answer='The episode quotes 40; the reference scenario says 55. '
                 'Its version and scenario are unspecified: the discrepancy is unresolved, '
                 'not evidence of a revision.')
        self.assertEqual(grade(CASES['quoted-model-discrepancy'], o), [])


if __name__ == '__main__':
    unittest.main()
