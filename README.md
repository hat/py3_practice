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

### Using Coverage for Testing

* Coverage is a python libarary which will check what percentage of code is tested
* Install via `pip install coverage`
* `coverage run tests.py`: Run coverage to show percentage of code tested
* `coverage report -m`: Show results, -m flag will show lines without coverage
* Show coverage report in HTML for added benefits such as links
    * `python -m http.server`: Open document tree to localhost for viewing
