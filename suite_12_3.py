import unittest
import tests_12_3


abcST = unittest.TestSuite()
abcST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
abcST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(abcST)