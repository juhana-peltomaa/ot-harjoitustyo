from tkinter import ttk, constants

# Harjoitellaan vielä UI:n rakentamista - tod.näk erotetaan kaikki näkymät omiksi luokikseen,
# joita UI käyttää lopulta.


class UI:

    def __init__(self, root):
        self._root = root

    def start(self):

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

        # Harjoitellaan gridin luomista näkymään
        heading_label.grid(row=0, column=0, columnspan=2, sticky=(constants.W))

        username.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W))

        password.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W))

        login_button.grid(row=3, column=0, columnspan=2,
                          sticky=(constants.E, constants.W))

        # Sarakkeet ottavat kaiken jäljelle jäävän tilan, kun ikkunan kokoa muutetaan
        # yhdessä elementtien sticky-parametrien kanssa
        self._root.grid_columnconfigure(1, weight=1)
