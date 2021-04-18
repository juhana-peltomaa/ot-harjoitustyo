from tkinter import ttk, constants, messagebox

from services.course_service import course_service, ExistingUsernameError


class CreateView:
    def __init__(self, root, show_login_view):
        self._root = root
        self._frame = None

        self._new_username_entry = None
        self._new_username_password = None

        self._show_login_view = show_login_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    # Erotellaan käyttäjän luomisen logiikkaa omaan luokkaan
    def _create_new_user(self):
        username = self._new_username_entry.get()
        password = self._new_password_entry.get()

        if len(username) > 3 and len(password) > 3:
            try:
                course_service.create_new_user(username, password)
                messagebox.showinfo(
                    "Regisration", f"Successfully registered user: {username}!")
            except ExistingUsernameError:
                messagebox.showinfo(
                    "Regisration", f"Username {username} is already in-use!")
        else:
            messagebox.showinfo(
                "Regisration", "Both username and password must be over three characters long!")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Heading label, joka kertoo mitä tällä sivulla tehdään
        heading_label = ttk.Label(master=self._frame, text="Create User")

        # Testataan käyttäjänimen kirjaamista UI:hin
        username_label = ttk.Label(master=self._frame, text="Set new username")
        self._new_username_entry = ttk.Entry(master=self._frame)

        # Testataan salasanan kirjaamista UI:hin
        password_label = ttk.Label(master=self._frame, text="Set new password")
        self._new_password_entry = ttk.Entry(master=self._frame)

        # Testataan kirjautumispainikkeen lisäämistä
        new_create_user_button = ttk.Button(
            master=self._frame, text="Create", command=self._create_new_user)

        # Takaisin Login-näkymään
        back_to_login_view_button = ttk.Button(
            master=self._frame, text="Back to Login", command=self._show_login_view)

        # Harjoitellaan gridin luomista näkymään
        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=(constants.W), padx=5, pady=5)

        # nämä parametrit voidaan poistaa tarvittaessa
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._new_username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._new_password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        # Jää oudosti login-painikkeen viereen, korjaa myöhemmin!!
        new_create_user_button.grid(
            row=3, column=1, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        back_to_login_view_button.grid(
            row=4, column=1, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        # Sarakkeet ottavat kaiken jäljelle jäävän tilan, kun ikkunan kokoa muutetaan
        # yhdessä elementtien sticky-parametrien kanssa
        self._frame.columnconfigure(1, weight=1, minsize=400)
