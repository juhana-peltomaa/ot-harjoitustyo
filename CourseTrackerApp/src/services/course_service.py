from entities.course import Course
from entities.user import User

from repositories.course_repo import course_repository as c_repo
from repositories.user_repo import user_repository as u_repo
import re


class ExistingUsernameError(Exception):
    pass


class LoginError(Exception):
    pass


class ExistingCourseError(Exception):
    pass


class CourseEntryError(Exception):
    pass


class CourseUpdateError(Exception):
    pass


class CourseValueError(Exception):
    pass


class CourseService:

    def __init__(self, course_repository=c_repo, user_repository=u_repo):
        self._user = None
        self._c_repo = course_repository
        self._u_repo = user_repository

    def login_user(self, username, password):

        # palauttaa User:in tietokannasta, jos löytyy
        user = self._u_repo.find_user(username, password)

        if user:
            username_check = user["username"]
            password_check = user["password"]

            if str(username_check) != str(username) or str(password_check) != str(password):
                raise LoginError("Login failed! Invalid username or password.")

            self._user = user
            return user

        raise LoginError("Login failed! Invalid username or password.")

    def create_new_user(self, username, password):

        exists = self._u_repo.find_username(username)

        if exists:
            raise ExistingUsernameError(
                f"Username {username} is already in-use!")

        new_user = self._u_repo.create_user(User(username, password))
        return new_user

    def current_user(self):
        return self._user["username"]

    def logout_user(self):
        self._user = None

    def create_new_course(self, name, credit, grade, status):

        exists = self._c_repo.find_course(name, self.current_user())

        if len(name) <= 0 or len(credit) <= 0:
            raise CourseEntryError()

        if exists:
            raise ExistingCourseError()

        if self.validate_credit(str(credit)) is not True:
            raise CourseValueError()

        if self.validate_grade(str(grade)) is not True:
            raise CourseValueError()

        course = Course(name, credit, grade, str(
            status), user=self.current_user())
        course = self._c_repo.create_course(course)
        return course

    def validate_credit(self, credit):
        accepted = re.compile(r'^([0-9]|1[0]|\s)$')
        if accepted.match(credit):
            return True
        return False

    def validate_grade(self, grade):
        # hyväksytään tyhjä syöte
        if len(grade) == 0:
            grade = " "

        accepted = re.compile(r'([0-5]|\s)$')

        if accepted.match(grade):
            return True
        return False

    def display_all_courses(self):
        course_list = []
        courses = self._c_repo.find_all_courses()

        if courses:
            for row in courses:
                id = row["id"]
                name = row["name"]
                credit = row["credit"]
                grade = row["grade"]
                status = row["status"]
                user = row["user"]

                if user == self.current_user():
                    course_list.append([id, name, credit, grade, status, user])

            return course_list

        else:
            return None

    def remove_all_courses(self):

        try:
            self._c_repo.delete_all(self._user["username"])
            return True
        except Exception:
            raise CourseUpdateError()

    def remove_one_course(self, name):
        try:
            self._c_repo.delete_one_course(name, self.current_user())
            return True
        except Exception:
            print("Error in deleting selected course!")
            return False

    def update_course_info(self, id, name, credit, grade, status):
        try:
            if self.validate_credit(str(credit)) is not True:
                raise CourseValueError()
            if self.validate_grade(str(grade)) is not True:
                raise CourseValueError()
            self._c_repo.update_course_info(
                id, name, credit, grade, str(status), self.current_user())
            return True
        except Exception:
            raise CourseUpdateError()


course_service = CourseService()
