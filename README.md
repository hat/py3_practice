# py3_practice

Practicing some concepts of Python3

### Python Testing with Doctests

* Doctests: write inside the python code comments
* No output means tests were succesful
* Run with `python -m doctest` use flag `-v` for verbose
* Add to main.py with `import doctest` and call with `doctest.testmod()`

Example:
```
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
```

### Python Testing with Unittest

* Unittests is a separate .py file unlike Doctests
* Class must have unittest.TestCase passed in
* All test functions must begin with naming convention `test_`
* assert is reserved keywork for checking validity
* Run via command line ```python -m unittest test_module1 test_module2```

Example:
```
import unittest

class TestMethods(unittest.TestCase):

    def test_five_plus_five(self):
      assert 5 + 5 == 10

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```
