import unittest
from services.course_service import course_service, ExistingUsernameError, LoginError, CourseUpdateError
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

        self.course_test4 = Course(
            "Ohjelmistotekniikka", 6, 5, "Completed", self.user_test2.username, "")

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

    def test_login_exisiting_user(self):
        course_service.create_new_user("test1", "test123")
        user = course_service.login_user("test1", "test123")

        self.assertEqual(user["username"], "test1")

    def test_login_invalid_password(self):
        course_service.create_new_user("test1", "test123")

        self.assertRaises(
            LoginError, lambda: course_service.login_user("test1", "wrong123"))

    def test_current_user(self):

        course_service.create_new_user("test1", "test123")
        user = course_service.login_user("test1", "test123")
        self.assertEqual(course_service.current_user(), user["username"])

    def test_logout_user(self):

        course_service.create_new_user("test1", "test123")
        user = course_service.login_user("test1", "test123")
        course_service.logout_user()

        self.assertEqual(course_service._user, None)

    def test_remove_all_courses(self):

        course_service.create_new_user("test1", "test123")
        user = course_service.login_user("test1", "test123")

        name = self.course_test1.name
        credit = self.course_test1.credit
        grade = self.course_test1.grade
        status = self.course_test1.status
        url = self.course_test1.url

        course_service.create_new_course(name, str(credit), grade, status, url)

        name = self.course_test2.name
        credit = self.course_test2.credit
        grade = self.course_test2.grade
        status = self.course_test2.status
        url = self.course_test2.url

        course_service.create_new_course(name, str(credit), grade, status, url)

        # Checks if remove_all_courses worked
        self.assertEqual(course_service.remove_all_courses(), True)

        # Checks that course_test1 is not found anymore for user test1
        self.assertEqual(course_service._c_repo.find_course(
            self.course_test2.name, "test1"), None)

    def test_remove_one_course(self):

        course_service.create_new_user("test1", "test123")
        user = course_service.login_user("test1", "test123")

        name = self.course_test1.name
        credit = self.course_test1.credit
        grade = self.course_test1.grade
        status = self.course_test1.status
        url = self.course_test1.url

        course_service.create_new_course(name, str(credit), grade, status, url)

        self.assertEqual(course_service.remove_one_course(name), True)

    def test_fail_remove_one_course(self):

        course_service.create_new_user("test1", "test123")
        user = course_service.login_user("test1", "test123")

        name = self.course_test1.name
        credit = self.course_test1.credit
        grade = self.course_test1.grade
        status = self.course_test1.status
        url = self.course_test1.url

        course_service.create_new_course(name, str(credit), grade, status, url)

        self.assertEqual(course_service.remove_one_course(
            "wrong_course_name"), False)

    def test_display_all_courses(self):

        course_service.create_new_user("test1", "test123")
        user = course_service.login_user("test1", "test123")

        name = self.course_test1.name
        credit = self.course_test1.credit
        grade = self.course_test1.grade
        status = self.course_test1.status
        url = self.course_test1.url

        course_service.create_new_course(name, str(credit), grade, status, url)

        name = self.course_test2.name
        credit = self.course_test2.credit
        grade = self.course_test2.grade
        status = self.course_test2.status
        url = self.course_test2.url

        course_service.create_new_course(name, str(credit), grade, status, url)

        course_list = course_service.display_all_courses()

        self.assertEqual(len(course_list), 2)

    def test_display_courses_empty(self):

        course_list = course_service.display_all_courses()

        self.assertEqual(course_list, None)

    def test_statistics(self):
        course_service.create_new_user("test2", "test123")
        user = course_service.login_user("test2", "test123")

        name = self.course_test4.name
        credit = self.course_test4.credit
        grade = self.course_test4.grade
        status = self.course_test4.status
        url = self.course_test4.url

        course_service.create_new_course(name, str(credit), grade, status, url)

        self.assertEqual(course_service.statistics(), (1, 6, 5))
