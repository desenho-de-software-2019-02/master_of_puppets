import unittest

if __name__ == '__main__':
    testsuite = unittest.TestLoader().discover('.')
    print(testsuite)
    unittest.TextTestRunner(verbosity=1).run(testsuite)