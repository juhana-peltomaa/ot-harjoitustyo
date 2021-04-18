import unittest
from repositories.course_repo import course_repository
from repositories.user_repo import user_repository
from entities.course import Course
from entities.user import User


class TestCourseRepositio(unittest.TestCase):
    def setUp(self):
        course_repository.delete_all()
        user_repository.delete_all()

        self.user_testi1 = User('testi1', 'testi123')
        self.user_testi2 = User('testi2', 'testi234')

        self.course_test1 = Course(
            "Ohjelmistotekniikka", 5, None, False, self.user_testi1.username)
        self.course_test2 = Course(
            "Ohjelmistotuotanto", 6, 5, True, self.user_testi1.username)
        self.course_test3 = Course(
            "Ohjelmistotuotanto", 6, 4, True, self.user_testi2.username)

    def test_create_course(self):
        course_repository.create_course(self.course_test1)

        course_info = course_repository.find_course("Ohjelmistotekniikka")

        self.assertEqual(course_info[0], self.course_test1.name)

    def test_find_all_courses(self):
        course_repository.create_course(self.course_test1)
        course_repository.create_course(self.course_test2)
        course_repository.create_course(self.course_test3)

        courses_info = course_repository.find_all_courses()

        self.assertEqual(len(courses_info), 3)
        self.assertEqual(courses_info[0]["name"], self.course_test1.name)
        self.assertEqual(courses_info[2]["name"], self.course_test3.name)

    def test_find_not_existing_course(self):
        course_repository.create_course(self.course_test1)

        course_info = course_repository.find_course("Ohjelmistotuotanto")

        self.assertEqual(course_info, None)
