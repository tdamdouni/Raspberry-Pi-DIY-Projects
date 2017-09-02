import unittest
from collections import namedtuple
from handlers import *
from psmqtt import *


def get_subtopic(topic, param):
    t = Topic(topic)
    return t.get_subtopic(param) if t.is_multitopic() else topic


class TestMain(unittest.TestCase):
    def test_get_subtopic(self):
        self.assertEqual("/haha", get_subtopic('/haha', 'a'))
        self.assertEqual("/a", get_subtopic('/*', 'a'))
        self.assertEqual("/a", get_subtopic('/**', 'a'))
        self.assertEqual("/a/*", get_subtopic('/*/*', 'a'))
        self.assertEqual("/a/**", get_subtopic('/*/**', 'a'))
        self.assertEqual("/a/**", get_subtopic('/**/**', 'a'))

        # wildcard inside brackets
        self.assertEqual("/name[ppp*]/a", get_subtopic('/name[ppp*]/**', 'a'))
        self.assertEqual("/name[ppp*]/*;", get_subtopic('/name[ppp*]/*;', 'a'))
        self.assertEqual("/name[ppp*]/haha", get_subtopic('/name[ppp*]/haha', 'a'))
        self.assertEqual("/a/name[ppp*]/**", get_subtopic('/*/name[ppp*]/**', 'a'))
        self.assertEqual("/a/name[ppp*]/**", get_subtopic('/**/name[ppp*]/**', 'a'))
        self.assertEqual("/*;/name[ppp*]/a", get_subtopic('/*;/name[ppp*]/**', 'a'))
        self.assertEqual("/**;/name[ppp*]/a", get_subtopic('/**;/name[ppp*]/**', 'a'))
        self.assertEqual("/**;/name[ppp*]/*;", get_subtopic('/**;/name[ppp*]/*;', 'a'))

        # wildcard with ;
        self.assertEqual("/*;", get_subtopic('/*;', 'a'))
        self.assertEqual("/**;", get_subtopic('/**;', 'a'))
        self.assertEqual("/*;/a", get_subtopic('/*;/*', 'a'))
        self.assertEqual("/*;/a", get_subtopic('/*;/**', 'a'))
        self.assertEqual("/*;/*;", get_subtopic('/*;/*;', 'a'))
        self.assertEqual("/*;/**;", get_subtopic('/*;/**;', 'a'))


class TestHandlers(unittest.TestCase):
    def test_value_command_handler(self):
        handler = type("TestHandler", (ValueCommandHandler, object),
                       {"get_value": lambda s: 50})('test')
        # normal execution
        self.assertEqual(50, handler.handle(''))
        # exceptions
        self.assertRaises(Exception, handler.handle, 'a')
        self.assertRaises(Exception, handler.handle, '/')
        self.assertRaises(Exception, handler.handle, '*')

    def test_index_command_handler(self):
        handler = type("TestHandler", (IndexCommandHandler, object),
                       {"get_value": lambda s: [5, 6, 7]})('test')
        # normal execution
        self.assertEqual(5, handler.handle('0'))
        self.assertEqual([5, 6, 7], handler.handle('*'))
        self.assertEqual("[5, 6, 7]", handler.handle('*;'))
        self.assertEqual(3, handler.handle('count'))
        # exceptions
        self.assertRaises(Exception, handler.handle, '')
        self.assertRaises(Exception, handler.handle, '3')
        self.assertRaises(Exception, handler.handle, '/')
        self.assertRaises(Exception, handler.handle, '*/')
        self.assertRaises(Exception, handler.handle, '/*')
        self.assertRaises(Exception, handler.handle, 'blabla')
        self.assertRaises(Exception, handler.handle, 'bla/bla')
        self.assertRaises(Exception, handler.handle, 'bla/')
        self.assertRaises(Exception, handler.handle, '/bla')

    def test_tuple_command_handler(self):
        handler = type("TestHandler", (TupleCommandHandler, object),
                       {"get_value": lambda s: namedtuple('test', 'a b')(10, 20)})('test')
        # normal execution
        self.assertEqual(10, handler.handle('a'))
        self.assertEqual({'a': 10, 'b': 20}, handler.handle('*'))
        self.assertEqual('{"a": 10, "b": 20}', handler.handle('*;'))
        # exceptions
        self.assertRaises(Exception, handler.handle, '')
        self.assertRaises(Exception, handler.handle, '/')
        self.assertRaises(Exception, handler.handle, '*/')
        self.assertRaises(Exception, handler.handle, '/*')
        self.assertRaises(Exception, handler.handle, 'blabla')
        self.assertRaises(Exception, handler.handle, 'bla/bla')
        self.assertRaises(Exception, handler.handle, 'bla/')
        self.assertRaises(Exception, handler.handle, '/bla')

    def test_index_tuple_command_handler(self):
        r = [namedtuple('test', 'a b')(1, 2), namedtuple('test', 'a b')(3, 4)]
        handler = type("TestHandler", (IndexTupleCommandHandler, object),
                       {"get_value": lambda s: r})('test')
        # normal execution
        self.assertEqual([1, 3], handler.handle('a/*'))
        self.assertEqual("[1, 3]", handler.handle('a/*;'))
        self.assertEqual(3, handler.handle('a/1'))
        self.assertEqual({'a': 3, 'b': 4}, handler.handle('*/1'))
        self.assertEqual('{"a": 3, "b": 4}', handler.handle('*;/1'))
        # exceptions
        self.assertRaises(Exception, handler.handle, '')
        self.assertRaises(Exception, handler.handle, '*')
        self.assertRaises(Exception, handler.handle, '*;')
        self.assertRaises(Exception, handler.handle, 'a')
        self.assertRaises(Exception, handler.handle, 'a/')
        self.assertRaises(Exception, handler.handle, '/')
        self.assertRaises(Exception, handler.handle, '*/')
        self.assertRaises(Exception, handler.handle, '/*')
        self.assertRaises(Exception, handler.handle, 'blabla')
        self.assertRaises(Exception, handler.handle, 'bla/bla')
        self.assertRaises(Exception, handler.handle, 'bla/')
        self.assertRaises(Exception, handler.handle, '/bla')

    def test_index_or_total_command_handler(self):
        handler = type("TestHandler", (IndexOrTotalCommandHandler, object),
                       {"get_value": lambda s, t: 5 if t else [1, 2, 3]})('test')
        # normal execution
        self.assertEqual(5, handler.handle(''))
        self.assertEqual(1, handler.handle('0'))
        self.assertEqual(3, handler.handle('2'))
        self.assertEqual([1, 2, 3], handler.handle('*'))
        self.assertEqual("[1, 2, 3]", handler.handle('*;'))
        self.assertEqual(3, handler.handle('count'))
        # exceptions
        self.assertRaises(Exception, handler.handle, '/')
        self.assertRaises(Exception, handler.handle, '*-')
        self.assertRaises(Exception, handler.handle, '*/')
        self.assertRaises(Exception, handler.handle, '/*')
        self.assertRaises(Exception, handler.handle, '3')
        self.assertRaises(Exception, handler.handle, 'blabla')
        self.assertRaises(Exception, handler.handle, 'bla/bla')
        self.assertRaises(Exception, handler.handle, 'bla/')
        self.assertRaises(Exception, handler.handle, '/bla')

    def test_index_or_total_tuple_command_handler(self):
        total = namedtuple('test', 'a b')(10, 20)
        single = [namedtuple('test', 'a b')(1, 2), namedtuple('test', 'a b')(3, 4)]
        handler = type("TestHandler", (IndexOrTotalTupleCommandHandler, object),
                       {"get_value": lambda s, t: total if t else single})('test')
        # normal execution
        self.assertEqual({'a': 10, 'b': 20}, handler.handle('*'))
        self.assertEqual('{"a": 10, "b": 20}', handler.handle('*;'))
        self.assertEqual(10, handler.handle('a'))
        self.assertEqual([1, 3], handler.handle('a/*'))
        self.assertEqual("[1, 3]", handler.handle('a/*;'))
        self.assertEqual(3, handler.handle('a/1'))
        self.assertEqual({'a': 3, 'b': 4}, handler.handle('*/1'))
        self.assertEqual('{"a": 3, "b": 4}', handler.handle('*;/1'))
        # exceptions
        self.assertRaisesRegexp(Exception, "Element '' in '' is not supported", handler.handle, '')
        self.assertRaises(Exception, handler.handle, '/')
        self.assertRaisesRegexp(Exception, "Cannot list all elements and parameters at the same.*", handler.handle, '*/*')
        self.assertRaises(Exception, handler.handle, '*-')
        self.assertRaises(Exception, handler.handle, '/*')
        self.assertRaises(Exception, handler.handle, '3')
        self.assertRaises(Exception, handler.handle, '/3')
        self.assertRaises(Exception, handler.handle, 'blabla')
        self.assertRaises(Exception, handler.handle, 'bla/bla')
        self.assertRaises(Exception, handler.handle, 'bla/')
        self.assertRaises(Exception, handler.handle, '/bla')
        self.assertRaises(Exception, handler.handle, '*/5')

    def test_name_or_total_tuple_command_handler(self):
        total = namedtuple('test', 'a b')(10, 20)
        single = {"x":  namedtuple('test', 'a b')(1, 2), "y": namedtuple('test', 'a b')(3, 4)}
        handler = type("TestHandler", (NameOrTotalTupleCommandHandler, object),
                       {"get_value": lambda s, t: total if t else single})('test')
        # normal execution
        self.assertEqual({'a': 10, 'b': 20}, handler.handle('*'))
        self.assertEqual('{"a": 10, "b": 20}', handler.handle('*;'))
        self.assertEqual(10, handler.handle('a'))
        self.assertEqual({"x": 1, "y": 3}, handler.handle('a/*'))
        self.assertEqual('{"y": 3, "x": 1}', handler.handle('a/*;'))
        self.assertEqual(3, handler.handle('a/y'))
        self.assertEqual({'a': 3, 'b': 4}, handler.handle('*/y'))
        self.assertEqual('{"a": 3, "b": 4}', handler.handle('*;/y'))
        # exceptions
        self.assertRaisesRegexp(Exception, "Element '' in '' is not supported", handler.handle, '')
        self.assertRaises(Exception, handler.handle, '/')
        self.assertRaisesRegexp(Exception, "Cannot list all elements and parameters at the same.*", handler.handle, '*/*')
        self.assertRaises(Exception, handler.handle, '*-')
        self.assertRaises(Exception, handler.handle, '/*')
        self.assertRaises(Exception, handler.handle, '3')
        self.assertRaises(Exception, handler.handle, '/3')
        self.assertRaises(Exception, handler.handle, 'a/0')
        self.assertRaises(Exception, handler.handle, 'c/x')
        self.assertRaises(Exception, handler.handle, 'blabla')
        self.assertRaises(Exception, handler.handle, 'bla/bla')
        self.assertRaises(Exception, handler.handle, 'bla/')
        self.assertRaises(Exception, handler.handle, '/bla')
        self.assertRaises(Exception, handler.handle, '*/5')

    def test_disk_usage_command_handler(self):
        disk = '/'
        handler = type("TestHandler", (DiskUsageCommandHandler, object),
                       {"get_value": lambda s,d: self._disk_usage_get_value(disk, d)})('test')
        # normal execution
        self.assertEqual(10, handler.handle('a//'))
        self.assertEqual({'a': 10, 'b': 20}, handler.handle('*//'))
        self.assertEqual('{"a": 10, "b": 20}', handler.handle('*;//'))
        self.assertEqual('{"a": 10, "b": 20}', handler.handle('*;/|'))  # vertical slash
        disk = 'c:'
        self.assertEqual(10, handler.handle('a/c:'))
        disk = 'c:/'
        self.assertEqual(10, handler.handle('a/c:/'))
        # exceptions
        disk = None     # do not validate disk, only parameters
        self.assertRaises(Exception, handler.handle, 'a')
        self.assertRaises(Exception, handler.handle, 'a/')
        self.assertRaises(Exception, handler.handle, 'a/')
        self.assertRaises(Exception, handler.handle, '/')
        self.assertRaises(Exception, handler.handle, '*/')
        self.assertRaises(Exception, handler.handle, '/*')
        self.assertRaises(Exception, handler.handle, 'blabla')
        self.assertRaises(Exception, handler.handle, 'bla/bla')
        self.assertRaises(Exception, handler.handle, 'bla/')
        self.assertRaises(Exception, handler.handle, '/bla')

    def _disk_usage_get_value(self, disk, d):
        if disk is not None:
            self.assertEqual(disk, d)
        return namedtuple('test', 'a b')(10, 20)


class TestFormatter(unittest.TestCase):
    def test_get_format(self):
        f = Formatter.get_format("123/ddd/ddd{{sdd}}/444")
        self.assertEqual("123/ddd", f[0])
        self.assertEqual("ddd{{sdd}}/444", f[1])

        f = Formatter.get_format("123/ddd/ddd{sdd}}/444")
        self.assertEqual("123/ddd/ddd{sdd}}/444", f[0])
        self.assertEqual(None, f[1])

        f = Formatter.get_format("ddd{{sdd}}/444")
        self.assertEqual("ddd{{sdd}}/444", f[0])
        self.assertEqual(None, f[1])

    def test_format(self):
        self.assertEqual("10", Formatter.format("{{a}}", {"a": 10}))
        self.assertEqual("10", Formatter.format("{{x}}", 10))
        self.assertEqual("3", Formatter.format("{{x[2]}}", [1, 2, 3]))
        self.assertEqual("2.0", Formatter.format("{{a/5}}", {"a": 10}))
        self.assertEqual("15", Formatter.format("{{a+b}}", {"a": 10, "b": 5}))
        self.assertEqual("1.2 MB", Formatter.format("{{a/1000000}} MB", {"a": 1200000}))
        self.assertEqual("1 MB", Formatter.format("{{a|MB}}", {"a": 1200000}))

    def test_format_uptime(self):
        import time
        n = int(time.time())
        self.assertEqual("0 min", Formatter.format("{{x|uptime}}", n))
        self.assertEqual("1 min", Formatter.format("{{x|uptime}}", n - 60))
        self.assertEqual("1:00", Formatter.format("{{x|uptime}}", n - 1*60*60))
        self.assertEqual("1:40", Formatter.format("{{x|uptime}}", n - 1*60*60 - 40*60))
        self.assertEqual("1 day, 0 min", Formatter.format("{{x|uptime}}", n - 24*60*60))
        self.assertEqual("1 day, 40 min", Formatter.format("{{x|uptime}}", n - 24*60*60 - 40*60))
        self.assertEqual("1 day, 1:40", Formatter.format("{{x|uptime}}", n - 25*60*60 - 40*60))
        self.assertEqual("2 days, 1:40", Formatter.format("{{x|uptime}}", n - 49*60*60 - 40*60))
        self.assertEqual("2 days, 1:39", Formatter.format("{{x|uptime}}", n - 49*60*60 - 40*60+30))
        self.assertEqual("2 days, 1:40", Formatter.format("{{x|uptime}}", n - 49*60*60 - 40*60-30))

if __name__ == '__main__':
    unittest.main()