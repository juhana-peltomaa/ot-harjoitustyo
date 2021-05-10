from tkinter import ttk, constants, messagebox, StringVar
from services.course_service import course_service, ExistingCourseError, CourseEntryError, CourseUpdateError, CourseValueError, InvalidUrlError, DeleteUserError


OPTIONS = ["          ", "Registered", "On-going", "Completed"]


class CourseView:
    """ Luokka, joka luo näkymän, missä käyttäjä voi lisätä uusia, hallita omia kurssejaan sekä lukea statistiikkaa suoritetusta kursseista. 
        Käyttäjä voi myös poistaa tietonsa sekä kirjautua ulos.

    Attributes:
        root: UI:n juuri
        frame: Frame -olio, johon liitetään näkymän komponentteja.

        _course_info_labels = Ensin None, mutta alustamisen jälkeen LabelFrame -olio, johon liitetään kurssien tietoja esittäviä komponenteja.
        _update_course_buttons = Ensin None, mutta alustamisen jälkeen LabelFrame -olio, johon liitetään sovelluslogiikan mahdollistavat painikkeet.
        _course_statistics_labels = Ensin None, mutta alustamisen jälkeen LabelFrame -olio, johon liitetään kurssien statisiikkaa esittäviä komponenteja.

        self._current_courses = Ensin None, mutta alustamisen jälkeen Treeview -olio, jossa esitetään käyttäjän nykyisten kurssien tietoja.

        self._course_id_entry = Ensin None, mutta alustamisen jälkeen Entry -olio, johon voidaan esittää kurssin id.
        self._course_name_entry = Ensin None, mutta alustamisen jälkeen Entry -olio, johon voidaan esittää yksittäisen kurssin nimi.
        self._course_credit_entry = Ensin " ", mutta alustamisen jälkeen Entry -olio, johon voidaan esittää kurssin opintopistemäärä.
        self._course_grade_entry = Ensin "", mutta alustamisen jälkeen Entry -olio, johon voidaan esittää kurssin arvosana.
        self._course_status_entry = Ensin None, mutta alustamisen jälkeen Entry -olio, johon voidaan esittää yksittäisen kurssin status.
        self._course_url_entry = Ensin "", mutta alustamisen jälkeen Entry -olio, johon voidaan esittää kurssiin liittyvä URL.

        self._course_status = StringVar() -olio, joka esittää kurssin statusta
        self._course_id = StringVar() -olio, joka esittää kurssin arvosanaa

        self._completed_courses_label = StringVar() -olio, joka esittää suoritettujen kurssien lukumäärää.
        self._completed_credits_label = StringVar() -olio, joka esittää suoritettujen kurssien opintopisteitä
        self._average_gpa_label = StringVar() -olio, joka esittää suoritettujen kurssien painoetettua keskiarvoa

        self._show_login_view = show_login_view -metodi, jota kutsuttaessa näytetään LoginView -näkymä

        self._user = course_service.current_user(), hakee nykyisen käyttäjän nimen kutsumalla sovelluslogiikan metodia
        self._initialize(), kutsuu luokan metodia, jolla näkymä alustetaan
        self._display_all_courses(), kutsuu luokan metodia, joka näyttää kaikki käyttäjän kurssit
        self._display_statistics(), kutsuu luokan metodia, joka näyttää käyttäjän kurssien statistiikan

    """

    def __init__(self, root, show_login_view):
        """Luokan konstruktori. Alustaa kaikki tarvittavat muuttujat sekä oliot ja luo kurssinäkymästä vastaavan luokan. 

        """

        self._root = root
        self._frame = None

        self._course_info_labels = None
        self._update_course_buttons = None
        self._course_statistics_labels = None

        self._current_courses = None

        self._course_id_entry = None
        self._course_name_entry = None
        self._course_credit_entry = " "
        self._course_grade_entry = ""
        self._course_status_entry = None
        self._course_url_entry = ""

        self._course_status = StringVar()
        self._course_id = StringVar()

        self._completed_courses_label = StringVar()
        self._completed_credits_label = StringVar()
        self._average_gpa_label = StringVar()

        self._show_login_view = show_login_view

        self._user = course_service.current_user()
        self._initialize()
        self._display_all_courses()
        self._display_statistics()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _create_new_course(self):
        """ Luo uuden kurssin kurssinäkymään hakemalla käyttäjän lisäämät syötteet ja antamalla ne parametriksi sovelluslogiikan create_new_course -metodille.
            Jos lisääminen ei onnistu annetuilla syötteillä, käyttäjä saa virhe ilmoituksen, jossa ohjataan oikean syötteen antamisessa.

        """

        course_name = self._course_name_entry.get()
        course_credit = self._course_credit_entry.get()
        course_grade = self._course_grade_entry.get()
        course_status = self._course_status.get()
        course_url = self._course_url_entry.get()
        self._course_id.set(OPTIONS[0])

        try:
            new_course = course_service.create_new_course(
                course_name, course_credit, course_grade, course_status, course_url)

            if new_course:
                self._display_all_courses()
                self._display_statistics()
            else:
                messagebox.showinfo("Course registration",
                                    f"Something went wrong in adding course {course_name}!")

        except ExistingCourseError:
            messagebox.showinfo("Course registration",
                                f"Course registration failed.\nCourse {course_name} has already been added!")

        except CourseEntryError:
            messagebox.showinfo("Course registration",
                                "Course registration failed.\nEnter both course name and credits!")

        except CourseValueError:
            messagebox.showinfo("Course registration",
                                "Course registration failed.\nEnter valid input for credits and grade!\n\nCourses marked as 'Completed' must have a valid grade!")

        except InvalidUrlError:
            messagebox.showinfo(("Course registration",
                                 f"Something went wrong..\nURL {course_url} is not valid.\n\nMake sure the URL is given in its complete form i.e. 'https://www.google.com'."))

    def _update_course_info(self):
        """ Päivittää valitun kurssin tiedot kutsumalla sovelluslogiikan metodia update_course_info käyttäjän antamilla syötteillä.
            Jos kurssin tietojen päivittäminen ei onnistu, käyttäjä saa virhe ilmoituksen, jossa ohjataan oikeanlaisen syötteen antamisessa.

        """
        course_name = self._course_name_entry.get()
        course_credit = self._course_credit_entry.get()
        course_grade = self._course_grade_entry.get()
        course_status = self._course_status.get()
        course_url = self._course_url_entry.get()

        course_id = self._course_id_entry.get()

        try:
            if course_service.update_course_info(course_id, course_name, course_credit, course_grade, course_status, course_url) is True:
                self._display_all_courses()
                self._display_statistics()
        except CourseUpdateError:
            messagebox.showinfo("Course registration",
                                "Course update failed.\nMake sure all inputs have correct values!")
        except InvalidUrlError:
            messagebox.showinfo("Course registration",
                                f"Something went wrong..\nURL {course_url} is not valid.\n\nMake sure the URL is given in its complete form i.e. 'https://www.google.com'.")

        except CourseValueError:
            messagebox.showinfo("Course registration",
                                "Course registration failed.\nEnter valid input for credits and grade!\n\nCourses marked as 'Completed' must have a valid grade!")

    def _remove_one_course(self):
        """ Poistaa käyttäjän valitseman kurssien näkymästä sekä tietokannasta hyödyntämällä sovelluslogiikan metodeja.
            Samalla päivitetään näkymän kurssit sekä niihin liittyvän statistiikan esittäminen.

        """
        course_name = self._course_name_entry.get()

        if course_service.remove_one_course(course_name) is True:
            self._course_id.set(OPTIONS[0])
            self._display_all_courses()
            self._display_statistics()

    def _remove_all_courses(self):
        """ Poistaa kaikki käyttäjän kurssit näkymästä sekä tietokannasta hyödyntämällä sovelluslogiikan metodeja.
            Samalla päivitetään näkymän kurssit sekä niihin liittyvän statistiikan esittäminen.

        """
        if course_service.remove_all_courses() is True:
            self._course_id.set(OPTIONS[0])
            self._display_all_courses()
            self._display_statistics()

    def callback(self, selection):
        self._course_status.set(selection)
        return selection

    def _clear_entry_input(self):
        """ Tyhjentää syötekentissä olevat tiedot.

        """

        self._course_id.set(OPTIONS[0])
        self._course_name_entry.delete(0, constants.END)
        self._course_credit_entry.delete(0, constants.END)
        self._course_grade_entry.delete(0, constants.END)
        self._course_status.set(OPTIONS[0])
        self._course_url_entry.delete(0, constants.END)

        self._course_grade_entry.insert(0, "")
        self._course_url_entry.insert(0, "")

    def _select_course(self, e):
        """ Hakee käyttäjän näkymässä klikkaaman kurssin kaikki tiedot ja asettaa ne näkyville syötekenttiin. 
           Syötekentät on tyhjennetty ennen uudelleen täyttämistä kutsumalla _clear_entry_input -metodia.

        Args:
            e: bind -metodin mahdollistava parametrisyöte, jotta hiiren klikkaus kutsuu funktiota.
        """
        # kutsutaan kentät tyhjentävää metodia
        self._clear_entry_input()

        # haetaan valitun rivin arvot
        select = self._current_courses.focus()

        values = self._current_courses.item(select, "values")

        # sisällytetään valitun rivin arvot entry-kenttiin
        try:
            self._course_id.set(values[0])
            self._course_name_entry.insert(0, values[1])
            self._course_credit_entry.insert(0, values[2])
            self._course_grade_entry.insert(0, values[3])
            self._course_status.set(values[4])
            self._course_url_entry.insert(0, values[6])
        except:
            pass

    def link_tree(self, event):
        """ Avaa näkymässä olevan linkin verkkoselaimessa, kun käyttäjä tuplaklikkaa linkkiä.

        Args:
            event: bind -metodin mahdollistava parametrisyöte, jotta hiiren tuplaklikkaus kutsuu funktiota.
        """
        select = self._current_courses.focus()
        values = self._current_courses.item(select, "values")

        try:
            url = values[6]
            import webbrowser
            webbrowser.open('{}'.format(url))
        except:
            pass

    def _display_all_courses(self):
        """ Hakee kaikki käyttäjän kurssit hyödyntämällä sovelluslogiikan metodia ja lisää ne _current_courses -olioon.

        Returns:
            None, jos kurssien näkymän päivittäminen sovelluslogiikassa ei onnistnut
        """

        # tyhjennetään treeview ennen kurssien näyttämistä
        for course in self._current_courses.get_children():
            self._current_courses.delete(course)

        courses = course_service.display_all_courses()

        if courses is not None:
            for row in courses:
                self._current_courses.insert(parent="", index="end", text="", values=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return None

    def _display_statistics(self):
        """ Hakee käyttäjän suorittamien kurssien statistiikkaa ja asettaa ne näkyvillä niille varattuihin kenttiin

        """

        completed_courses, credit_amount, gpa = course_service.statistics()

        if completed_courses == 0:
            self._completed_courses_label["text"] = "Completed courses: - "
            self._completed_credits_label["text"] = "Completed credits: - "
            self._average_gpa_label["text"] = "Weighted GPA: - "

        else:
            self._completed_courses_label["text"] = "Completed courses: " + str(
                completed_courses)
            self._completed_credits_label["text"] = "Completed credits: " + str(
                credit_amount)
            self._average_gpa_label["text"] = "Weighted GPA: " + str(gpa)

    def _delete_user(self):
        """ Poistaa käyttäjän sekä kaikki käyttäjän kurssit. Metodi varmistaa ennen poistamista käyttäjältä, haluaako tämä todella poistaa tiedot.
            Jos käyttäjä vastaa myöntävästi, tiedot poistetaan, muuten sovellus jatkaa toimintaa normaalisti.

        """
        result = messagebox.askquestion(
            title="Delete User", icon="question", message="Are you sure you want to delete your account? \n\nChoosing 'Yes' will delete your account forever, there is no going back. Please be certain. \n")
        try:
            if result == "yes":
                if course_service.delete_user() is True:
                    course_service.logout_user()
                    self._show_login_view()
            else:
                pass

        except DeleteUserError:
            messagebox.showinfo("Delete user",
                                "Deleting user failed.\n")

    def _initialize_heading(self):
        """ Alustaa näkymän yläosion tekstin ja kirjautuneen käyttäjän esittämisen

        """
        # Heading label, joka kertoo mitä tällä sivulla tehdään
        heading_label = ttk.Label(
            master=self._frame, text="Add new courses and view all of your existing courses!")

        current_user_label = ttk.Label(
            master=self._frame, text=f"Logged in as: {self._user}")

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=(constants.W), padx=5, pady=5)

        current_user_label.grid(row=1, column=0, columnspan=2,
                                sticky=(constants.W), padx=5, pady=5)

    def _initialize_treeview(self):
        """ Alustaa käyttäjän tallentamien kurssien tietojen esittämisen ja siihen liittyvän muotoilun.

        """

        # Kurssit lisätään treeview-näkymään
        self._current_courses = ttk.Treeview(master=self._frame)

        # Treeview:n muotoilua
        self._current_courses["columns"] = (
            "ID", "Course Name", "Credits", "Grade", "Status", "Owner", "URL")
        self._current_courses.column("#0", width=0, stretch=constants.NO)
        self._current_courses.column("ID", width=30, stretch=constants.NO)
        self._current_courses.column(
            "Course Name", width=50, stretch=constants.YES)
        self._current_courses.column(
            "Credits", anchor=constants.CENTER, width=30, stretch=constants.YES)
        self._current_courses.column(
            "Grade", anchor=constants.CENTER, width=10, stretch=constants.YES)
        self._current_courses.column(
            "Status", anchor=constants.CENTER, width=40, stretch=constants.YES)
        self._current_courses.column(
            "Owner", anchor=constants.CENTER, width=50, stretch=constants.YES)
        self._current_courses.column(
            "URL", anchor=constants.CENTER, minwidth=200, stretch=constants.YES)

        self._current_courses.heading("#0", text="")
        self._current_courses.heading("ID", text="ID", anchor=constants.CENTER)
        self._current_courses.heading(
            "Course Name", text="Course Name")
        self._current_courses.heading(
            "Credits", text="Credits", anchor=constants.CENTER)
        self._current_courses.heading(
            "Grade", text="Grade", anchor=constants.CENTER)
        self._current_courses.heading(
            "Status", text="Status", anchor=constants.CENTER)
        self._current_courses.heading(
            "Owner", text="Owner", anchor=constants.CENTER)
        self._current_courses.heading(
            "URL", text="URL", anchor=constants.CENTER)

        # Lisätään treeview:n kurssit grid -näkymään
        self._current_courses.grid(row=2, column=0, columnspan=4,
                                   sticky=(constants.EW), padx=5, pady=5)

    def _initialize_course_info(self):
        """ Alustaa kurssitietojen lisäämiseen liittyvät syötekentät ja otsikot

        """

        # Kurssi tietojen esittäminen LabelFrame:ssa
        self._course_info_labels = ttk.LabelFrame(
            master=self._frame, text="Course information")

        course_id_label = ttk.Label(
            master=self._course_info_labels, text="ID")
        self._course_id_entry = ttk.Entry(
            master=self._course_info_labels, state=constants.DISABLED, textvariable=self._course_id)

        course_name_label = ttk.Label(
            master=self._course_info_labels, text="Name")
        self._course_name_entry = ttk.Entry(master=self._course_info_labels)

        course_credit_label = ttk.Label(
            master=self._course_info_labels, text="Credits (0-10)")
        self._course_credit_entry = ttk.Entry(master=self._course_info_labels)

        course_grade_label = ttk.Label(
            master=self._course_info_labels, text="Grade (0-5)")
        self._course_grade_entry = ttk.Entry(master=self._course_info_labels)

        self._course_status.set(OPTIONS[0])

        course_status_label = ttk.Label(
            master=self._course_info_labels, text="Status")
        self._course_status_entry = ttk.OptionMenu(
            self._course_info_labels, self._course_status, *OPTIONS, command=self.callback)

        course_url_label = ttk.Label(
            master=self._course_info_labels, text="URL")
        self._course_url_entry = ttk.Entry(master=self._course_info_labels)

        # Course info -labels
        course_id_label.grid(row=0, column=0, padx=5, pady=2)
        course_name_label.grid(
            row=0, column=1, padx=5, pady=2)
        course_credit_label.grid(
            row=0, column=2, padx=5, pady=2)
        course_grade_label.grid(
            row=0, column=3, padx=5, pady=2)
        course_status_label.grid(
            row=0, column=4, padx=5, pady=2)
        course_url_label.grid(
            row=0, column=5, padx=5, pady=2)

        # Course info -entries
        self._course_id_entry.grid(row=1, column=0, padx=5, pady=2)
        self._course_name_entry.grid(
            row=1, column=1, sticky=(constants.W), padx=5, pady=2)
        self._course_credit_entry.grid(
            row=1, column=2, sticky=(constants.EW), padx=5, pady=2)

        self._course_grade_entry.grid(
            row=1, column=3, sticky=(constants.EW), padx=5, pady=2)
        self._course_status_entry.grid(
            row=1, column=4, sticky=(constants.EW), padx=5, pady=2)

        self._course_url_entry.grid(
            row=1, column=5, sticky=(constants.E), padx=5, pady=2)

        # Lisätään kurssitiedot grid näkymään
        self._course_info_labels.grid(row=3, column=0, columnspan=5,
                                      sticky=(constants.EW), padx=5, pady=5)

    def _initilize_buttons(self):
        """ Alustaa sovelluksen toiminnallisuuksia mahdollistavat painikkeet.

        """

        # Kurssien ja näkymän muokkamispainikkeet
        self._update_course_buttons = ttk.LabelFrame(
            master=self._frame, text="Commands")

        # Style määrittely Button-oliolle
        style = ttk.Style()
        style.configure("REDBUTTON.TButton", foreground="red")

        update_course_button = ttk.Button(
            master=self._update_course_buttons, text="Update course", command=self._update_course_info)

        create_new_course_button = ttk.Button(
            master=self._update_course_buttons, text="Add new course", command=self._create_new_course)

        remove_one_course_button = ttk.Button(
            master=self._update_course_buttons, text="Remove course", command=self._remove_one_course)

        remove_all_courses_button = ttk.Button(
            master=self._update_course_buttons, text="Remove all courses", command=self._remove_all_courses)

        clear_entry_button = ttk.Button(
            master=self._update_course_buttons, text="Clear entry inputs", command=self._clear_entry_input)

        delete_user_button = ttk.Button(
            master=self._update_course_buttons, text="Delete User", style="REDBUTTON.TButton", command=self._delete_user)

        # Takaisin Login-näkymään painike
        back_to_login_view_button = ttk.Button(
            master=self._frame, text="Back to Login", command=self._show_login_view)

        # Tietojen muokkaamisen mahdollistavat painikkeet
        update_course_button.grid(
            row=0, column=0, sticky=(constants.EW), padx=5, pady=5)

        create_new_course_button.grid(
            row=0, column=1, sticky=(constants.EW), padx=5, pady=5)

        remove_one_course_button.grid(
            row=0, column=2, sticky=(constants.EW), padx=5, pady=5)

        remove_all_courses_button.grid(
            row=0, column=3, sticky=(constants.EW), padx=5, pady=5)

        clear_entry_button.grid(
            row=0, column=4, sticky=(constants.E), padx=5, pady=5)

        delete_user_button.grid(
            row=0, column=5, sticky=(constants.E), padx=5, pady=5)

        # Uloskirjautumis painikkeen lisääminen gridiin
        back_to_login_view_button.grid(
            row=6, column=0, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        # lisätään painikkeet grid -näkymään
        self._update_course_buttons.grid(row=4, column=0, columnspan=4,
                                         sticky=(constants.EW), padx=5, pady=5)

    def _initilize_statistics_info(self):
        """ Alustaa käyttäjän suorittamien kurssien statistiikkaan liittyvän esityksen.

        """

        # Statistics tietojen lisääminen
        self._course_statistics_labels = ttk.LabelFrame(
            master=self._frame, text="Course Statistics for 'Completed' courses:")

        self._completed_courses_label = ttk.Label(
            master=self._course_statistics_labels, text="Completed courses: - ", font="bold")

        self._completed_credits_label = ttk.Label(
            master=self._course_statistics_labels, text="Completed credits: - ", font="bold")

        self._average_gpa_label = ttk.Label(
            master=self._course_statistics_labels, text="Weighted GPA: - ", font="bold")

        # Course stats -labels
        self._completed_courses_label.grid(
            row=0, column=0, sticky=(constants.EW), padx=5, pady=5)

        self._completed_credits_label.grid(
            row=0, column=1, sticky=(constants.EW), padx=5, pady=5)

        self._average_gpa_label.grid(
            row=0, column=2, sticky=(constants.E), padx=5, pady=5)

        # Lisätään statistiikka grid -näkymään
        self._course_statistics_labels.grid(
            row=5, column=0, columnspan=3, sticky=(constants.EW), padx=5, pady=5)

    def _initialize(self):
        """ Luo näkymän Frame -olion ja kutsuu siihen liitettävien komponenttien luomiseen käytettävät metodit.

        """

        self._frame = ttk.Frame(master=self._root)

        self._initialize_heading()

        self._initialize_treeview()

        self._initialize_course_info()

        self._initilize_buttons()

        self._initilize_statistics_info()

        # Sarakkeet ottavat kaiken jäljelle jäävän tilan, kun ikkunan kokoa muutetaan
        # yhdessä elementtien sticky-parametrien kanssa
        self._frame.columnconfigure(1, weight=1, minsize=400)
        self._frame.columnconfigure(0, weight=1)

        self._current_courses.bind("<ButtonRelease-1>", self._select_course)
        self._current_courses.bind("<Double-1>", self.link_tree)
