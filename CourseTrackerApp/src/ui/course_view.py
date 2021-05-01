from tkinter import ttk, constants, messagebox, StringVar
from services.course_service import course_service, ExistingCourseError, CourseEntryError, CourseUpdateError, CourseValueError, InvalidUrlError


OPTIONS = ["          ", "Registered", "On-going", "Completed"]


class CourseView:
    def __init__(self, root, show_login_view):
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
        self._course_url_entry = " "

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
        course_name = self._course_name_entry.get()

        if course_service.remove_one_course(course_name) is True:
            self._course_id.set(OPTIONS[0])
            self._display_all_courses()
            self._display_statistics()

    def _remove_all_courses(self):
        if course_service.remove_all_courses() is True:
            self._course_id.set(OPTIONS[0])
            self._display_all_courses()
            self._display_statistics()

    def callback(self, selection):
        self._course_status.set(selection)
        return selection

    def _select_course(self, e):
        # tyhjennetään entry-laatikot
        self._course_id.set(OPTIONS[0])
        self._course_name_entry.delete(0, constants.END)
        self._course_credit_entry.delete(0, constants.END)
        self._course_grade_entry.delete(0, constants.END)
        self._course_status.set(OPTIONS[0])
        self._course_url_entry.delete(0, constants.END)

        # haetaan valitun rivin arvot
        select = self._current_courses.focus()

        values = self._current_courses.item(select, "values")

        # sisällytetään valitun rivin arvot
        self._course_id.set(values[0])
        self._course_name_entry.insert(0, values[1])
        self._course_credit_entry.insert(0, values[2])
        self._course_grade_entry.insert(0, values[3])
        self._course_status.set(values[4])
        self._course_url_entry.insert(0, values[6])

    def link_tree(self, event):
        select = self._current_courses.focus()
        values = self._current_courses.item(select, "values")

        url = values[6]

        import webbrowser
        webbrowser.open('{}'.format(url))

    def _clear_entry_input(self):
        self._course_id.set(OPTIONS[0])
        self._course_name_entry.delete(0, constants.END)
        self._course_credit_entry.delete(0, constants.END)
        self._course_grade_entry.delete(0, constants.END)
        self._course_status.set(OPTIONS[0])
        self._course_url_entry.delete(0, constants.END)

        self._course_grade_entry.insert(0, "")
        self._course_url_entry.insert(0, " ")

    def _display_all_courses(self):
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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Heading label, joka kertoo mitä tällä sivulla tehdään
        heading_label = ttk.Label(
            master=self._frame, text="Add new courses and view all of your existing courses!")

        current_user_label = ttk.Label(
            master=self._frame, text=f"Logged in as: {self._user}")

        # Kurssit lisätään treeview-näkymään
        current_courses_tree = ttk.Treeview(master=self._frame)
        self._current_courses = current_courses_tree

        # Treeview:n muotoilua
        current_courses_tree["columns"] = (
            "ID", "Course Name", "Credits", "Grade", "Status", "Owner", "URL")
        current_courses_tree.column("#0", width=0, stretch=constants.NO)
        current_courses_tree.column("ID", width=30, stretch=constants.NO)
        current_courses_tree.column(
            "Course Name", width=50, stretch=constants.YES)
        current_courses_tree.column(
            "Credits", anchor=constants.CENTER, width=30, stretch=constants.YES)
        current_courses_tree.column(
            "Grade", anchor=constants.CENTER, width=10, stretch=constants.YES)
        current_courses_tree.column(
            "Status", anchor=constants.CENTER, width=40, stretch=constants.YES)
        current_courses_tree.column(
            "Owner", anchor=constants.CENTER, width=50, stretch=constants.YES)
        current_courses_tree.column(
            "URL", anchor=constants.CENTER, minwidth=200, stretch=constants.YES)

        current_courses_tree.heading("#0", text="")
        current_courses_tree.heading("ID", text="ID", anchor=constants.CENTER)
        current_courses_tree.heading(
            "Course Name", text="Course Name")
        current_courses_tree.heading(
            "Credits", text="Credits", anchor=constants.CENTER)
        current_courses_tree.heading(
            "Grade", text="Grade", anchor=constants.CENTER)
        current_courses_tree.heading(
            "Status", text="Status", anchor=constants.CENTER)
        current_courses_tree.heading(
            "Owner", text="Owner", anchor=constants.CENTER)
        current_courses_tree.heading(
            "URL", text="URL", anchor=constants.CENTER)

        # Kurssi tiedoille oma LabelFrame
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

        # Kurssien ja näkymän muokkamispainikkeet

        self._update_course_buttons = ttk.LabelFrame(
            master=self._frame, text="Commands")

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

        # Takaisin Login-näkymään
        back_to_login_view_button = ttk.Button(
            master=self._frame, text="Back to Login", command=self._show_login_view)

        # Statistics framein lisääminen
        self._course_statistics_labels = ttk.LabelFrame(
            master=self._frame, text="Course Statistics for 'Completed' courses:")

        self._completed_courses_label = ttk.Label(
            master=self._course_statistics_labels, text="Completed courses: - ", font="bold")

        self._completed_credits_label = ttk.Label(
            master=self._course_statistics_labels, text="Completed credits: - ", font="bold")

        self._average_gpa_label = ttk.Label(
            master=self._course_statistics_labels, text="Weighted GPA: - ", font="bold")

        # Gridin luominen

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=(constants.W), padx=5, pady=5)

        current_user_label.grid(row=1, column=0, columnspan=2,
                                sticky=(constants.W), padx=5, pady=5)

        current_courses_tree.grid(row=2, column=0, columnspan=4,
                                  sticky=(constants.EW), padx=5, pady=5)

        self._course_info_labels.grid(row=3, column=0, columnspan=5,
                                      sticky=(constants.EW), padx=5, pady=5)

        self._update_course_buttons.grid(row=4, column=0, columnspan=4,
                                         sticky=(constants.EW), padx=5, pady=5)

        self._course_statistics_labels.grid(
            row=5, column=0, columnspan=3, sticky=(constants.EW), padx=5, pady=5)

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

        # Course update -buttons
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

        # Course stats -labels
        self._completed_courses_label.grid(
            row=0, column=0, sticky=(constants.EW), padx=5, pady=5)

        self._completed_credits_label.grid(
            row=0, column=1, sticky=(constants.EW), padx=5, pady=5)

        self._average_gpa_label.grid(
            row=0, column=2, sticky=(constants.E), padx=5, pady=5)

        # Uloskirjautuminen
        back_to_login_view_button.grid(
            row=6, column=0, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        # Sarakkeet ottavat kaiken jäljelle jäävän tilan, kun ikkunan kokoa muutetaan
        # yhdessä elementtien sticky-parametrien kanssa
        self._frame.columnconfigure(1, weight=1, minsize=400)
        self._frame.columnconfigure(0, weight=1)

        self._current_courses.bind("<ButtonRelease-1>", self._select_course)
        self._current_courses.bind("<Double-1>", self.link_tree)
