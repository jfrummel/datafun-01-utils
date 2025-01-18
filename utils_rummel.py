"""
Module: utils_rummel

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 

Author: Jeremy Rummel

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_domestic_clients: bool = True

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
number_of_clients:int = 34

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_weekly_hours_studying:float = 8.3

# declare a list of strings
# TODO: Add or replace this with your own list  
favorite_sport_teams:list = ["Chelsea", "Cubs", "Bulls"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
player_ratings:list = [8.3, 7.5, 9.0, 6.9, 7.7]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_rating: float = min(player_ratings)  
max_rating: float = max(player_ratings)  
mean_rating: float = statistics.mean(player_ratings)  
stdev_rating: float = statistics.stdev(player_ratings)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Rummel Analytics: Delivering Professional Insights
---------------------------------------------------------
Has Domestic Clients:  {has_domestic_clients}
Numnber of Clients:    {number_of_clients}
Favorite Teams:        {favorite_sport_teams}
Player Ratings:        {player_ratings}
Minimum Rating: {min_rating}
Maximum Rating: {max_rating}
Mean Rating: {mean_rating:.2f}
Standard Deviation of Rating: {stdev_rating:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
