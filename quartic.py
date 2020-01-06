# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:51:39 2017

@author: Brandon
"""
from sympy import factor
from sympy import init_printing
from sympy import solve

init_printing()

eq = input("Enter a quartic equation: ")

print("Equation factors as: " + str(factor(eq)))

print("Solutions to equation are: " + str(solve(eq)))