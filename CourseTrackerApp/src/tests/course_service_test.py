import unittest
from services.course_service import course_service, ExistingUsernameError
from repositories.course_repo import course_repository
from repositories.user_repo import user_repository
from entities.course import Course
from entities.user import User


class TestCourseService(unittest.TestCase):
    def setUp(self):
        course_repository.empty_courses()
        user_repository.delete_all()

        self.user_test1 = User('test1', 'test123')
        self.user_test2 = User('test2', 'test234')

        self.course_test1 = Course(
            "Ohjelmistotekniikka", 5, " ", " ", self.user_test1.username, "")
        self.course_test2 = Course(
            "Ohjelmistotuotanto", 6, 5, True, self.user_test1.username, "")
        self.course_test3 = Course(
            "Ohjelmistotuotanto", 6, 4, True, self.user_test2.username, "")

    def test_create_new_user(self):
        course_service.create_new_user("test3", "test123")

        search_existing_user = user_repository.find_username("test3")
        search_missing_user = user_repository.find_username("test2")

        self.assertEqual(search_existing_user, True)
        self.assertEqual(search_missing_user, None)

    def test_create_exisiting_user(self):
        course_service.create_new_user("test3", "test123")

        self.assertRaises(ExistingUsernameError, lambda: course_service.create_new_user(
            "test3", "test123"))
