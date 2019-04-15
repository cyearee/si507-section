from sec2_poss_solution import *
import unittest # can do this within any Python file -- it's in the standard library

# depending on other code

class TestBeveverage(unittest.TestCase): # making a subclass of unittest.TestCase
	def setUp(self): # create a method with a name. Must begin with "test"
	# any setup code for this test method
		self.bev1 = Beverage('lemonade',1.5,'juice')
		self.bev2 = Beverage('...',0.0)
		self.cof = Coffee('kona',2.0,3)
		self.milk1 = Milk('fat-free',True)
		self.milk2 = Milk('coconut',False,1.0)

	def tearDown(self):
		pass

	def test_constructor(self):
		self.assertEqual(self.bev1.name,'lemonade','Got the first one')
		self.assertEqual(self.bev2.name,'...')
		self.assertEqual(self.bev1.cost,1.5)
		self.assertEqual(type(self.bev2.cost),type(1.9))
		self.assertEqual(self.bev1.type,'juice')
		self.assertEqual(self.bev2.type,'unknown')

class TestMenu(unittest.TestCase):
	def setUp(self):
		self.file = open('menu.csv','r')
		self.rows = self.file.readlines()
		self.row = self.rows[1]
		self.header = self.rows[0]

	def test_headers(self):
		self.assertEqual(self.header,'Name,Cost,Type\n')

	def test_rows(self):
		self.assertIn('\n',self.row)
		self.assertIsInstance(float(self.row.split(',')[1]),float)

	def tearDown(self):
		self.file.close()
 
# at the very end of your file
unittest.main(verbosity=2) #verbosity determines how much info you get