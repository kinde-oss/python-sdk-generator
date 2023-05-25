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
from kinde_sdk.model.organization import Organization
from kinde_sdk import schemas


class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def test_organization(self):
        inst = Organization({})
        with self.assertRaises(KeyError):
            inst["code"]
        assert inst.get_item_oapg("code") is schemas.unset
        with self.assertRaises(AttributeError):
            inst.code

        inst = Organization(code="")
        code = inst["code"]
        assert code == ""


if __name__ == "__main__":
    unittest.main()
