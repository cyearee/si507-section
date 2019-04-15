
def subtract_one(num): # this function should return the input, minus 1
  return num - 2 # This function code isn't what we want -- it should fail a test!

def add_one(num): # this function should return the input, plus 1
  return num+1

class SampleTest(unittest.TestCase):
  def test_1(self):
    self.assertEqual(subtract_one(4),3)
    self.assertEqual(add_one(3),4)

