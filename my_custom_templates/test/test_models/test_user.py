# coding: utf-8

"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""

import unittest

import kinde_sdk
from kinde_sdk.model.user import User
from kinde_sdk import schemas


class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def test_user(self):
        inst = User({})
        with self.assertRaises(KeyError):
            inst["id"]
        assert inst.get_item_oapg("id") is schemas.unset
        with self.assertRaises(AttributeError):
            inst.id

        inst = User(id="")
        id = inst["id"]
        assert id == ""


if __name__ == "__main__":
    unittest.main()