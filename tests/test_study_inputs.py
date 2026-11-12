import json
import unittest
from pathlib import Path


class StudyInputTests(unittest.TestCase):
    def test_domain_references_and_units(self):
        data=json.loads((Path(__file__).resolve().parents[1]/'fixtures/study-input.json').read_text())
        from researchmesh.contracts import source_contract
        keys={r['source']+':'+r['id'] for r in data['records']}
        for row in data['records']:
            source_contract(row['data'])
        for edge in data['citations']:
            self.assertIn(edge['citing'],keys)
            self.assertIn(edge['cited'],keys)
        for member in data['family_membership']:
            self.assertIn(member['record'],keys)
            self.assertAlmostEqual(sum(x['share'] for x in member['fields']),1)
