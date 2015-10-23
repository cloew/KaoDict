from kao_dict import KaoDict
import unittest

class getattrTest(unittest.TestCase):
    """ Test cases of getattr """
        
    def test_retrieved(self):
        """ Test that a value is retrieved properly """
        key = 'test'
        d = {key:1}
        kd = KaoDict(d)
        
        self.assertEqual(d[key], getattr(kd, key))
        
    def test_notInDict(self):
        """ Test that a value is retrieved properly """
        key = 'test'
        kd = KaoDict()
        
        self.assertRaises(AttributeError, getattr, kd, key)

class setattrTest(unittest.TestCase):
    """ Test cases of setattr """
        
    def test_set(self):
        """ Test that a value is set properly """
        key = 'test'
        d = {key:1}
        kd = KaoDict(d)
        setattr(kd, key, d[key])
        self.assertEqual(d[key], getattr(kd, key))