import unittest
from unitest1 import TournamentTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TournamentTest))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
