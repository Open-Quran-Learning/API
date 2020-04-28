from ayat.authorization.authorization_decorators import admin_required
from ayat.authentication_routes import get_all_users

import unittest


class DecoratorsTests(unittest.TestCase):

    @admin_required
    def test_get_all_users(self):
        get_all_users()
