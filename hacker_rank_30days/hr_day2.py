# Task:
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and 
# tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
#
# Note: Be sure to use precise values for calculations, or you end up with an incorrectly rounded result!
#
# Input Format:
# There are 3 lines of numeric input:
# The first line has a double, mealCost (the cost of the meal before tax and tip).
# The second line has an integer, tipPercent (the percentage of mealCost being added as tip).
# The third line has an integer, taxPercent (the percentage of mealCost being added as tax).
#
# Output Format:
# Print the total cost, where totalCost is the rounded integer result of the entire bill (mealCost with added tax and tip)
#
# Sample Input:
# 12.00
# 20
# 8
#
# Sample Output:
# 15
#
# Explanation: 
# Given:
# mealCost = 12*tipPercent = 20*taxPercent = 8
# Calculations:
# tip = 12 * 20/100 = 2.4
# tax = 12 * 8/100 = 0.96
# totalCost = mealCost + tip + tax = 12 + 2.4 + 0.96 = 15.36
# round(totalCost) = 15
# We found totalCost to the nearest dollar (integer) and then print our result, 15.
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    totalCost = meal_c + (meal_c * tip_p / 100) + (meal_c * tax_p / 100)
    print(round(totalCost))
meal_c = float(input())
tip_p = int(input())
tax_p = int(input())
solve(meal_c, tip_p, tax_p)