# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:45:32 2023

@author: 700001473
"""

# simple file containing a function & associated test
# the test can be autodetected by pytest
# go to folder where this file resides & execute pytest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
