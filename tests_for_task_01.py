import unittest
import task_01
 
class TestStringMethods(unittest.TestCase):
      
    def setUp(self):
        pass
  
    # standart "abc"
    def test_strings_abc(self):
        self.assertEqual( task_01.main('abc'), ['abc', 'acb', 'bac', 'bca', 'cba', 'cab'])
  
    # input number
    def test_strings_number(self):
        self.assertEqual( task_01.main(27), "Please, input string!")

    #repeating letters
    # it will be permutations because there is no requirements for such cases
    def test_strings_repeating(self):
        self.assertEqual( task_01.main('aa'), ['aa', 'aa'])

if __name__ == '__main__':
    unittest.main()