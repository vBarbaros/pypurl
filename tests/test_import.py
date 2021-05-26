import unittest
import purl as P

class PurlTestCase(unittest.TestCase):
    def setUp(self):
        self.purl_obj = P.Purl()

if __name__ == '__main__':
    unittest.main()
