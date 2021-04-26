from entities.course import Course
from database_connection import get_database_connection


CREATE_COURSE = "INSERT OR IGNORE INTO courses (name, credit, grade, status, user) VALUES (?, ?, ?, ?, ?);"

FIND_COURSE = "SELECT * FROM courses WHERE name = ? and user = ?;"

DELETE_ALL_COURSES = "DELETE FROM courses WHERE user = ?;"

EMPTY_COURSES = "DELETE FROM courses;"  # käytetään testien alustamiseen

DELETE_ONE_COURSE = "DELETE FROM courses WHERE name = ? AND user = ?;"

FIND_ALL_COURSES = "SELECT * FROM courses;"

UPDATE_COURSE_INFO = "UPDATE courses SET name = ?, credit = ?, grade = ?, status = ? WHERE id = ? AND user = ?;"


class CourseRepo:
    def __init__(self, connection):
        self._connection = connection

    def create_course(self, new_course):
        cursor = self._connection.cursor()

        course = cursor.execute(
            CREATE_COURSE, (new_course.name, new_course.credit, new_course.grade, new_course.status, new_course.user))

        self._connection.commit()

        return course

    def find_course(self, name, user):
        cursor = self._connection.cursor()

        cursor.execute(FIND_COURSE, (name, user))

        self._connection.commit()

        course_info = cursor.fetchone()

        if course_info:
            return course_info
        else:
            return None

    def find_all_courses(self):
        cursor = self._connection.cursor()

        cursor.execute(FIND_ALL_COURSES)

        self._connection.commit()

        course_info = cursor.fetchall()

        return course_info

    def delete_all(self, user):
        cursor = self._connection.cursor()

        course = cursor.execute(DELETE_ALL_COURSES, (user, ))

        self._connection.commit()

    def delete_one_course(self, name, user):
        cursor = self._connection.cursor()

        course = cursor.execute(DELETE_ONE_COURSE, (name, user))

        self._connection.commit()

    def update_course_info(self, id, name, credit, grade, status, user):
        cursor = self._connection.cursor()

        course = cursor.execute(
            UPDATE_COURSE_INFO, (name, credit, grade, status, id, user))

        self._connection.commit()

    def empty_courses(self):
        cursor = self._connection.cursor()

        course = cursor.execute(EMPTY_COURSES)

        self._connection.commit()


course_repository = CourseRepo(get_database_connection())
