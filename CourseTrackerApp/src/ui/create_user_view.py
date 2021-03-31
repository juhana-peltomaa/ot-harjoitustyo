from tkinter import ttk, constants


class CreateView:
    def __init__(self, root, show_login_view):
        self._root = root
        self._frame = None

        self._show_login_view = show_login_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Heading label, joka kertoo mitä tällä sivulla tehdään
        heading_label = ttk.Label(master=self._frame, text="Create User")

        # Testataan käyttäjänimen kirjaamista UI:hin
        new_username = ttk.Label(master=self._frame, text="Set new username")
        new_username_entry = ttk.Entry(master=self._frame)

        # Testataan salasanan kirjaamista UI:hin
        new_password = ttk.Label(master=self._frame, text="Set new password")
        new_password_entry = ttk.Entry(master=self._frame)

        # Testataan kirjautumispainikkeen lisäämistä
        new_create_user_button = ttk.Button(
            master=self._frame, text="Create")

        # Takaisin Login-näkymään
        back_to_login_view_button = ttk.Button(
            master=self._frame, text="Back to Login", command=self._show_login_view)

        # Harjoitellaan gridin luomista näkymään
        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=(constants.W), padx=5, pady=5)

        # nämä parametrit voidaan poistaa tarvittaessa
        new_username.grid(row=1, column=0, padx=5, pady=5)
        new_username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        new_password.grid(row=2, column=0, padx=5, pady=5)
        new_password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        # Jää oudosti login-painikkeen viereen, korjaa myöhemmin!!
        new_create_user_button.grid(
            row=3, column=1, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        back_to_login_view_button.grid(
            row=4, column=1, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        # Sarakkeet ottavat kaiken jäljelle jäävän tilan, kun ikkunan kokoa muutetaan
        # yhdessä elementtien sticky-parametrien kanssa
        self._frame.columnconfigure(1, weight=1, minsize=400)
