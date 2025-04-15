import sys
import os

from cryptid_assistant.Modules.tileNode import Structure

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from cryptid_assistant.scripts import clues


class ClueTestCase(unittest.TestCase):
    def test_alpha_clue_index(self):
        alpha = clues.alpha
        self.assertEqual(alpha.get(20)['structure'][0].color, 'green')
        self.assertEqual(len(alpha.get(91)['territory']), 1)
        self.assertEqual(max(alpha.get(91)['range']), 2)

    def test_beta_clue_index(self):
        beta = clues.beta
        self.assertEqual(beta.get(5)['structure'][0].color, 'green')
        self.assertEqual(len(beta.get(80)['territory']), 0)
        self.assertEqual(max(beta.get(80)['range']), 1)

    def test_gamma_clue_index(self):
        gamma = clues.gamma
        self.assertEqual(gamma.get(20)['range'][0], 0)
        self.assertEqual(len(gamma.get(50)['territory']), 1)
        self.assertEqual(gamma.get(50)['territory'][0], 'cougar')

    def test_delta_clue_index(self):
        delta = clues.delta
        self.assertEqual(delta.get(25)['terrain'], ['s', 'm'])
        self.assertEqual(len(delta.get(73)['structure']), 2)
        self.assertEqual(delta.get(73)['structure'][1], Structure('abandoned_shack', 'blue'))

    def test_epsilon_clue_index(self):
        epsilon = clues.epsilon
        self.assertEqual(len(epsilon.get(16)['structure']), 2)
        self.assertEqual(len(epsilon.get(16)['territory']), 0)
        self.assertEqual(max(epsilon.get(16)['range']), 3)


if __name__ == '__main__':
    unittest.main()
