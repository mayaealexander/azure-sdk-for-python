# DOC_TITLE: Sample Addition Functions and Tests
# DOC_SUMMARY: Provides a simple addition function and corresponding test cases.
# DOC_STEPS: 1. Define the addition function. 2. Write test cases to validate the function.
# DOC_LINKS: None

def sample_add(a, b):
    # Returns the sum of two numbers a and b
    return a + b  

def test_add():
    # Tests sample_add with positive integers
    assert sample_add(2, 3) == 5 

def test_add2():
    # Tests sample_add with a positive and a negative integer
    assert sample_add(12, -2) == 10