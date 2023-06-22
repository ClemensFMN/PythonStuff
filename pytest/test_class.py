# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 13:48:41 2023

@author: 700001473
"""

class TestClass:
    def test_one(self):
        assert 1 == 2
    
    def test_two(self):
        assert 2 == 2
        
    def someOtherMethod(self):
        # this one is not picked up by pytest!
        assert 4 == 5
