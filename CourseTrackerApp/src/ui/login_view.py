from tkinter import ttk, constants


class LoginView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Heading label, joka kertoo mitä tällä sivulla tehdään
        heading_label = ttk.Label(master=self._root, text="Login")

        # Testataan käyttäjänimen kirjaamista UI:hin
        username = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)

        # Testataan salasanan kirjaamista UI:hin
        password = ttk.Label(master=self._root, text="Password")
        password_entry = ttk.Entry(master=self._root)

        # Testataan kirjautumispainikkeen lisäämistä
        login_button = ttk.Button(master=self._root, text="Login")

        create_user_button = ttk.Button(master=self._root, text="Create User")

        # Harjoitellaan gridin luomista näkymään
        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=(constants.W), padx=5, pady=5)

        # nämä parametrit voidaan poistaa tarvittaessa
        username.grid(row=1, column=0, padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password.grid(row=2, column=0, padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        login_button.grid(row=3, column=0, columnspan=1,
                          sticky=constants.EW,  padx=5, pady=5)

        # Jää oudosti login-painikkeen viereen, korjaa myöhemmin!!!
        create_user_button.grid(
            row=3, column=1, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        # Sarakkeet ottavat kaiken jäljelle jäävän tilan, kun ikkunan kokoa muutetaan
        # yhdessä elementtien sticky-parametrien kanssa
        self._root.grid_columnconfigure(1, weight=1, minsize=300)
