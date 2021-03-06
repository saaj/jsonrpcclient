"""test_exceptions.py"""
# pylint: disable=missing-docstring

from unittest import TestCase, main

from jsonrpcclient import exceptions


class TestExceptions(TestCase):

    def test_ParseResponseError(self):
        with self.assertRaises(exceptions.ParseResponseError):
            raise exceptions.ParseResponseError

    def test_ReceivedErrorResponse(self):
        with self.assertRaises(exceptions.ReceivedErrorResponse):
            raise exceptions.ReceivedErrorResponse(1, 'foo', 'bar')


if __name__ == '__main__':
    main()
