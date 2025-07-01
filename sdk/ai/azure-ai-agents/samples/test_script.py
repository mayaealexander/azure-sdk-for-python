# DOC_TITLE: Sample Addition Functions
# DOC_SUMMARY: Functions to perform addition and test their correctness.
# DOC_STEPS: Define an addition function and write test cases to verify its behavior.
# DOC_LINKS: None

def sample_add(a, b):
    # Returns the sum of two numbers a and b.
    return a + b  

def test_add():
    # Tests sample_add with positive integers.
    assert sample_add(2, 3) == 5 

def test_add2():
    # Tests sample_add with a positive and a negative integer.
    assert sample_add(12, -2) == 10