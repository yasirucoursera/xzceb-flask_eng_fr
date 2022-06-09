import unittest
class TestMyModule (unittest.TestCase):
    def test_en_fr(self):
        #self.assertEqual(french_to_english(""),"")
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_en_fr(self):
        #self.assertEqual(english_to_french(""),"")
        self.assertEqual(english_to_french('Hello'),'Bonjour')
from translator import english_to_french, french_to_english
        
if __name__=='__main__':
    unittest.main()