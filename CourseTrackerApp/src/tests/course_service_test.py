import unittest
from services.course_service import course_service
from repositories.course_repo import course_repository
from repositories.user_repo import user_repository
from entities.course import Course
from entities.user import User


class TestCourseService(unittest.TestCase):
    def setUp(self):
        course_repository.empty_courses()
        user_repository.delete_all()

        self.user_test1 = User('testi1', 'testi123')
        self.user_test2 = User('testi2', 'testi234')

        self.course_test1 = Course(
            "Ohjelmistotekniikka", 5, " ", " ", self.user_test1.username)
        self.course_test2 = Course(
            "Ohjelmistotuotanto", 6, 5, True, self.user_test1.username)
        self.course_test3 = Course(
            "Ohjelmistotuotanto", 6, 4, True, self.user_test2.username)
