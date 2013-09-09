import pickle

def list_pickler(path, my_list):
   f = open(path, 'wb')
   pickle.dump(test_list, f)
   f.close()
   
def unpickler(path):
   f = open(path, 'rb')
   test_list = pickle.load(f)
   f.close()
   return test_list