
# Code is more often read than written !
# Main PEP 8 Style guide

# snake_case : variable
i_am_a_variable : "Hello Network Team"

# MAJ_MAJ : constant
DEFAULT_CONCENTRATOR = "&@$#"

# CapitalizedCase : object / class
class AirCraft:
    pass

class SpaceShip:
    pass

# Write module name in lowercase
import os
import sys
import shutil  
import pathlib

# Comments convention

# Avoid comment on the same line as code
# Put a single space between # and first word
# Put the # at the same level of indentation as the code commented
# Use docstrings everywhere according to PEP 257
# If you modify the code, don't forget to update comments
def multiply(first, second=1):
    """Multiply two numbers.
 
    Args:
        first -- the multiplicand
        second -- the multiplicator (default 1)
    """
    return first * second
 
print(multiply(42, 5))
print(multiply.__doc__)

# Spaces

# One space in affectation but no space in function default affectation 
input_ratio = 5 
def input_ratio(value=5):
    pass
# No space between () and [] : (an expression), [0]
# One space between if/for etc... and first parenthesis
# two spaces before definition of a class or a function 

class Switch:
    pass

def route(param=None):
    pass

# One space before definition of a method
class Switch:

    def route(param=None):
        pass

# Line length : limit line length to 79 caracters

super_long_password = (
    "erfzfefrzvterbytnrezrtvbytyruetrgtrth"
    "zeergvzreafz'((-'eg'((yhvgbrz'trvytrh"
    "zerbetrtzbrtyezegbyebzrtbrebrtberbtrg"
    "zevrebtniukoy;i;yu,yt,trntehtrgegretr"
)

# One parameter per line and the ending parenthesis at the same indentation level as the function definition
def function_with_a_rather_long_name(
    parameter_number_1,
    parameter_number_2,
    Parameter_number_3,
):
    pass

# File organisation 

# 1 File comments
# 2 standard library imports
# 3 third party module imports
# 4 local module imports
# 5 constant imports
# 6 code

# Return

# All instruction shall return or none
# Return type should be same
# Return None rather than a simple return



