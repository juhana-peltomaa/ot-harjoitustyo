import unittest
from repositories.user_repo import user_repository
from entities.user import User


class TestUserRepositio(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_testi1 = User('testi1', 'testi123')
        self.user_testi2 = User('testi2', 'testi234')

    def test_create(self):
        user_repository.create_user(
            self.user_testi1.username, self.user_testi1.password)

        users = user_repository.find_user(
            self.user_testi1.username, self.user_testi1.password)

        self.assertEqual(users[0], self.user_testi1.username)
        self.assertEqual(users[1], self.user_testi1.password)

    def test_find_all_users(self):
        user_repository.create_user(
            self.user_testi1.username, self.user_testi1.password)

        user_repository.create_user(
            self.user_testi2.username, self.user_testi2.password)

        users = user_repository.find_all_users()

        self.assertAlmostEqual(len(users), 2)
        self.assertEqual(users[0]["username"], self.user_testi1.username)
        self.assertEqual(users[1]["username"], self.user_testi2.username)