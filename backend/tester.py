import unittest

# tests = unittest.TestLoader().discover("tests/models", pattern="*.py")
# result = unittest.TextTestRunner(verbosity=2).run(tests)
tests = unittest.TestLoader().discover("tests/schemas", pattern="*.py")
result = unittest.TextTestRunner(verbosity=2).run(tests)
