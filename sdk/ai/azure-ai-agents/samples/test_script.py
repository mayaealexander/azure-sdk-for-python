
def sample_add(a, b):
  return a + b  

def test_add():
  assert sample_add(2, 3) == 5 

def test_add2():
  assert sample(6, 1) == 7  # This line contains an error; it should be `sample_add(6, 1) == 7`
