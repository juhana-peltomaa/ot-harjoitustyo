from tkinter import ttk, constants
from ui.login_view import LoginView

# Harjoitellaan vielä UI:n rakentamista - tod.näk erotetaan kaikki näkymät omiksi luokikseen,
# joita UI käyttää lopulta.


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()  # erotetiin LoginView omaksi olioksi!

    def _show_login_view(self):
        self._current_view = LoginView(self._root)
