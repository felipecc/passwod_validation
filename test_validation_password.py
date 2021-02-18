import unittest
import validation_password

class TestValidPassword(unittest.TestCase):

    def setUp(self): 
        self.passwd_default = '1234PASSWD@@@@'
        self.passwd_more = 'asbasasa' 
        self.passwd_less = 'as'
        self.passwd_equals= '123456'

    def test_number(self):
        req = [('NUMBERS', '>', 1)]
        self.assertEqual(validation_password.validate(self.passwd_default,req),[True])

    def test_letter(self):
        req = [('LETTERS', '>', 1)]
        self.assertEqual(validation_password.validate(self.passwd_default,req),[True])

    def test_specials(self):
        req = [('SPECIALS', '>', 1)]        
        self.assertEqual(validation_password.validate(self.passwd_default,req),[True])

    def test_len_letter_number_specials(self):
        req = [('LEN', '>', 1),('LETTERS', '>', 1),('NUMBERS', '>', 1),('SPECIALS', '>', 1)]        
        self.assertEqual(validation_password.validate(self.passwd_default,req),[True,True,True,True])

    def test_operator_more_than(self):
        req = [('LEN', '>', 1)]        
        self.assertEqual(validation_password.validate(self.passwd_more,req),[True])        
        
    def test_operator_less_than(self):
        req = [('LEN', '<', 3)]        
        self.assertEqual(validation_password.validate(self.passwd_less,req),[True])        

    def test_operator_equals(self):
        req = [('LEN', '=', 6)]        
        self.assertEqual(validation_password.validate(self.passwd_equals,req),[True])        



if __name__ == '__main__':
    unittest.main()
