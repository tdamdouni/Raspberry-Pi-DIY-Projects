import unittest
from pathMaker import pathMaker

class test_pathMaker(unittest.TestCase):

	def test_pathMaker_get_parts_empty(self):
		empty = ''
		p=pathMaker()
		pts = p.get_parts(empty)
		self.assertEquals(len(pts), 1, 'Value = ')

	def test_pathMaker_get_parts(self):
		withYear = '/tmp/flash/2014'
		p=pathMaker()
		pts = p.get_parts(withYear)
		self.assertEquals('tmp', pts[0])
		self.assertEquals('flash', pts[1])
		self.assertEquals('2014', pts[2])
		self.assertEquals(len(pts), 3)

	def test_get_paths(self):
		withYear = '/tmp/flash/2014/3/11'
		p=pathMaker()
		paths = p.get_paths(withYear)
		self.assertEquals( len(paths), 5 )
		self.assertEquals("/tmp", paths[0])
		self.assertEquals("/tmp/flash", paths[1])
		self.assertEquals("/tmp/flash/2014", paths[2])
		self.assertEquals("/tmp/flash/2014/3", paths[3])
		self.assertEquals("/tmp/flash/2014/3/11", paths[4])



if __name__ == '__main__':
    unittest.main()