from tkinter import ttk, constants


class LoginView:
    def __init__(self, root, show_create_user_view):
        self._root = root
        self._frame = None

        self._show_create_user_view = show_create_user_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Heading label, joka kertoo mitä tällä sivulla tehdään
        heading_label = ttk.Label(master=self._frame, text="Login")

        # Testataan käyttäjänimen kirjaamista UI:hin
        username = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame)

        # Testataan salasanan kirjaamista UI:hin
        password = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame)

        # Testataan kirjautumispainikkeen lisäämistä
        login_button = ttk.Button(master=self._frame, text="Login")

        create_user_button = ttk.Button(
            master=self._frame, text="Create User", command=self._show_create_user_view)

        # Harjoitellaan gridin luomista näkymään
        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=(constants.EW), padx=5, pady=5)

        # nämä parametrit voidaan poistaa tarvittaessa
        username.grid(row=1, column=0, padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password.grid(row=2, column=0, padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        login_button.grid(row=3, column=1, columnspan=2,
                          sticky=(constants.E, constants.W),  padx=5, pady=5)

        create_user_button.grid(
            row=4, column=1, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        # Sarakkeet ottavat kaiken jäljelle jäävän tilan, kun ikkunan kokoa muutetaan
        # yhdessä elementtien sticky-parametrien kanssa
        self._frame.columnconfigure(1, weight=1, minsize=400)
