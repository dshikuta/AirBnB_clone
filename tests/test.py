#!/usr/bin/python3
"""
Base model $ storage tests
"""
import unnittest
import pycodestyle

class test-base_model (unittest.TestCase):
    """tests for base_model.py"""
    def test-pep8_self (self):
        """
        Test that checks pycodestyle
        """
        syntax=pycodesytle.StyleGuide (quit=True)
        check=syntax.check-files (['tests/test.py'])
        self.assert Equal (
                check.total_error,0,
                "pycodestyle errors found in test.py"
                )
