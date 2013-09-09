import unittest, os, shutil
import time
from pickler import list_pickler, unpickler

class PickleTester(unittest.TestCase):

 def init(self):
 	self.test_list = [1, 2, 3, ['a',2,'z'], 'hello']
 	self.path = './pickles'
 	os.makedirs(self.path)
 	self.file = os.path.join(self.path, 'list.p')
 

 def compare_pick_to_unpick_lists(self):
     list_pickler(self.file, self.test_list)
     unpicked_list = unpickler(self.file)
     self.assertEqual(self.test_list, unpicked_list)
     
  def tearDown(self):
     shutil.rmtree(self.path)

