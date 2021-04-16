from tkinter import ttk, constants
from repositories.course_repo import CourseRepo
from ui.login_view import LoginView
from entities.course import Course
from services.course_service import course_service


class CourseView:
    def __init__(self, root, show_login_view):
        self._root = root
        self._frame = None

        self._course_name_entry = None
        self._course_credit_entry = None

        self._show_login_view = show_login_view

        self._user = course_service.current_user()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    # kurssien lisääminen onnistuu nyt! Huomaa, että sovelluslogiikkaa ei ole vielä eritelty!
    def _create_new_course(self):
        course_name = self._course_name_entry.get()
        course_credit = self._course_credit_entry.get()

        database = CourseRepo(get_database_connection())
        new_course = Course(course_name, course_credit, user=self._user)

        database.create_course(new_course)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Heading label, joka kertoo mitä tällä sivulla tehdään
        heading_label = ttk.Label(
            master=self._frame, text="Soon you will be able to add new courses in this view!")

        current_user_label = ttk.Label(
            master=self._frame, text=f"Logged in as: {self._user}")

        # Testataan käyttäjänimen kirjaamista UI:hin
        course_name_label = ttk.Label(
            master=self._frame, text="Name of new course")
        self._course_name_entry = ttk.Entry(master=self._frame)

        # Testataan salasanan kirjaamista UI:hin
        course_credit_label = ttk.Label(
            master=self._frame, text="Credits of new course")
        self._course_credit_entry = ttk.Entry(master=self._frame)

        # Testataan kirjautumispainikkeen lisäämistä
        create_new_course_button = ttk.Button(
            master=self._frame, text="Add new course", command=self._create_new_course)

        # Takaisin Login-näkymään
        back_to_login_view_button = ttk.Button(
            master=self._frame, text="Back to Login", command=self._show_login_view)

        # Harjoitellaan gridin luomista näkymään
        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=(constants.W), padx=5, pady=5)

        current_user_label.grid(row=1, column=0, columnspan=2,
                                sticky=(constants.W), padx=5, pady=5)

        # nämä parametrit voidaan poistaa tarvittaessa
        course_name_label.grid(row=2, column=0, padx=5, pady=5)
        self._course_name_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        course_credit_label.grid(row=3, column=0, padx=5, pady=5)
        self._course_credit_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        # Jää oudosti login-painikkeen viereen, korjaa myöhemmin!!
        create_new_course_button.grid(
            row=4, column=1, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        back_to_login_view_button.grid(
            row=4, column=1, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        # Sarakkeet ottavat kaiken jäljelle jäävän tilan, kun ikkunan kokoa muutetaan
        # yhdessä elementtien sticky-parametrien kanssa
        self._frame.columnconfigure(1, weight=1, minsize=400)
