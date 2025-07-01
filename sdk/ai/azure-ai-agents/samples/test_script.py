# DOC_TITLE: Sample Addition Functions
# DOC_SUMMARY: Defines a simple addition function and tests for its correctness.
# DOC_STEPS: 1. Implement addition function. 2. Write test cases to validate functionality.

def sample_add(a, b):
    # Adds two numbers and returns the result
    return a + b  

def test_add():
    # Tests sample_add with 2 and 3, expecting the result to be 5
    assert sample_add(2, 3) == 5 

def test_add2():
    # Tests sample_add with 12 and 2, expecting the result to be 14
    assert sample_add(12, 2) == 14