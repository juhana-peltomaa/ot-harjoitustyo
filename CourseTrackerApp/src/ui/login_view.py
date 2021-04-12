from tkinter import ttk, constants
from repositories.user_repo import UserRepo

# väliaikaisesti täällä ennenkuin sovelluslogiikka on eritelty - huomaa _create_new_user kommentit
from database_connection import get_database_connection


class LoginView:
    def __init__(self, root, show_course_view, show_create_user_view):
        self._root = root
        self._show_create_user_view = show_create_user_view
        self._show_course_view = show_course_view  # lisätään kurssi-näkymään pääsy

        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    # Sovelluslogiikkaa ei ole vielä eritelty - joten kirjautuminen hoidettu vielä täällä

    def _login_user(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        # muista, että nämä on vielä importattu
        database = UserRepo(get_database_connection())

        # palauttaa käyttäjän ja salasanan, jos ne löytyvät, muuten None, None
        username_check, password_check = database.find_user(username, password)

        if username_check == username and password_check == password:
            self._show_course_view()
        else:
            # erotetaan viestit omaksi näkymäksi jossain välissä
            print("Some error happend in login")

    # Näkymän alustaminen
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Heading label, joka kertoo mitä tällä sivulla tehdään
        heading_label = ttk.Label(master=self._frame, text="Login")

        # Testataan käyttäjänimen kirjaamista UI:hin
        username = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        # Testataan salasanan kirjaamista UI:hin
        password = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        # Testataan kirjautumispainikkeen lisäämistä
        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._login_user)

        create_user_button = ttk.Button(
            master=self._frame, text="Create User", command=self._show_create_user_view)

        # Harjoitellaan gridin luomista näkymään
        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=(constants.EW), padx=5, pady=5)

        # nämä parametrit voidaan poistaa tarvittaessa
        username.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        login_button.grid(row=3, column=1, columnspan=2,
                          sticky=(constants.E, constants.W),  padx=5, pady=5)

        create_user_button.grid(
            row=4, column=1, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        # Sarakkeet ottavat kaiken jäljelle jäävän tilan, kun ikkunan kokoa muutetaan
        # yhdessä elementtien sticky-parametrien kanssa
        self._frame.columnconfigure(1, weight=1, minsize=400)
