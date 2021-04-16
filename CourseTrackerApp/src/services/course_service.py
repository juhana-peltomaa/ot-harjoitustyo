from entities.course import Course
from entities.user import User

from repositories.course_repo import course_repository as c_repo
from repositories.user_repo import user_repository as u_repo


class CourseService:

    def __init__(self, course_repository=c_repo, user_repository=u_repo):
        self._user = None
        self._c_repo = course_repository
        self._u_repo = user_repository

    def login_user(self, username, password):

        # palauttaa nimen, salasanan ja käyttäjä Olion jos ne löytyvät, muuten None
        username_check, password_check, User = self._u_repo.find_user(
            username, password)

        if username_check == username and password_check == password:
            self._user = User  # tämä pitää vielä miettiä
            return self._user
        else:
            # erotetaan viestit omaksi näkymäksi jossain välissä
            print("Some error happend in login")

    def current_user(self):
        return self._user

    def logout_user(self):
        self._user = None


course_service = CourseService()
