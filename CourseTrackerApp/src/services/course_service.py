from entities.course import Course
from entities.user import User

from repositories.course_repo import course_repository as c_repo
from repositories.user_repo import user_repository as u_repo


class ExistingUsernameError(Exception):
    pass


class LoginError(Exception):
    pass


class CourseService:

    def __init__(self, course_repository=c_repo, user_repository=u_repo):
        self._user = None
        self._c_repo = course_repository
        self._u_repo = user_repository

    def login_user(self, username, password):

        # palauttaa nimen, salasanan ja käyttäjä Olion jos ne löytyvät, muuten None
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


course_service = CourseService()
