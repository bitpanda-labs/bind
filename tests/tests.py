import unittest

from bind import bind

BIND_DATA = ['castable', 0, False, None, 's t r i n g.', 45, '"hi"', 0.25, '/slash.', 'http://']


class TestBind(unittest.TestCase):

    def test_default(self):
        bound = bind(BIND_DATA)
        self.assertEqual(bound, 'castable/0/s+t+r+i+n+g./45/%22hi%22/0.25/slash./http:')

    def test_unpacked(self):
        bound = bind(*BIND_DATA)
        self.assertEqual(bound, 'castable/0/s+t+r+i+n+g./45/%22hi%22/0.25/slash./http:')

    def test_url_false(self):
        bound = bind(*BIND_DATA, url=False)
        self.assertEqual(bound, 'castable/0/s t r i n g./45/"hi"/0.25/slash./http:')

    def test_diff_sep(self):
        bound = bind(*BIND_DATA, sep='.')
        self.assertEqual(bound, 'castable.0.s+t+r+i+n+g.45.%22hi%22.0.25./slash.http://')

    def test_blank_sep(self):
        bound = bind(*BIND_DATA, sep='')
        self.assertEqual(bound, 'castable0s+t+r+i+n+g.45%22hi%220.25/slash.http://')

    def test_multi_sep(self):
        bound = bind(*BIND_DATA, sep='WHY')
        self.assertEqual(bound, 'castableWHY0WHYs+t+r+i+n+g.WHY45WHY%22hi%22WHY0.25WHY/slash.WHYhttp://')
