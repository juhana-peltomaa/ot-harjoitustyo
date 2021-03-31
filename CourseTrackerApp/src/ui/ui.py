from tkinter import ttk, constants
from ui.login_view import LoginView
from ui.create_user_view import CreateView


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()  # erotetiin LoginView omaksi olioksi!

    # toteutettiin nykyisen näkymän piilottaminen ja "tuhoaminen"
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):    # login-näkymän näyttäminen
        self._hide_current_view()  # kutsuu hide-metodin kautta yksittäisiä destroy metodeja

        self._current_view = LoginView(self._root, self._show_create_user_view)

        self._current_view.pack()

    def _show_create_user_view(self):   # create user-näkymän näyttäminen
        self._hide_current_view()

        self._current_view = CreateView(self._root, self._show_login_view)

        self._current_view.pack()
