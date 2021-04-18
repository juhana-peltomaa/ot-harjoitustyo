from entities.course import Course
from database_connection import get_database_connection


CREATE_COURSE = "INSERT INTO courses (name, credit, grade, status, user) VALUES (?, ?, ?, ?, ?);"

FIND_COURSE = "SELECT * FROM courses WHERE name = ?;"

DELETE_ALL_COURSES = "DELETE FROM courses;"

FIND_ALL_COURSES = "SELECT * FROM courses;"


class CourseRepo:
    def __init__(self, connection):
        self._connection = connection

    def create_course(self, new_course):
        cursor = self._connection.cursor()

        course = cursor.execute(
            CREATE_COURSE, (new_course.name, new_course.credit, new_course.grade, new_course.status, new_course.user))

        self._connection.commit()

        return course

    def find_course(self, name):
        cursor = self._connection.cursor()

        cursor.execute(FIND_COURSE, (name, ))

        self._connection.commit()

        course_info = cursor.fetchone()

        if course_info:
            coursename_check = course_info["name"]

            return True
        else:
            return None

    def find_all_courses(self):
        cursor = self._connection.cursor()

        cursor.execute(FIND_ALL_COURSES)

        self._connection.commit()

        course_info = cursor.fetchone()

        return course_info

    def delete_all(self):
        cursor = self._connection.cursor()

        course = cursor.execute(DELETE_ALL_COURSES)

        self._connection.commit()


course_repository = CourseRepo(get_database_connection())
