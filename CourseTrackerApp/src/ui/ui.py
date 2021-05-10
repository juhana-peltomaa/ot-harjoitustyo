from ui.login_view import LoginView
from ui.create_user_view import CreateView
from ui.course_view import CourseView


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    # nykyisen näkymän piilottaminen ja "tuhoaminen"
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    # LoginView -luokan kutsuminen
    def _show_login_view(self): 
        self._hide_current_view()

        self._current_view = LoginView(
            self._root, self._show_course_view, self._show_create_user_view)

        self._current_view.pack()

    # CreateUserView -luokan kutsuminen
    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateView(self._root, self._show_login_view)

        self._current_view.pack()

    # CourseView -luokan kutsuminen
    def _show_course_view(self): 
        self._hide_current_view()

        self._current_view = CourseView(self._root, self._show_login_view)

        self._current_view.pack()
