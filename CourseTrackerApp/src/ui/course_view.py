from tkinter import ttk, constants, messagebox
from repositories.course_repo import CourseRepo
from ui.login_view import LoginView
from entities.course import Course
from services.course_service import course_service, ExistingCourseError, CourseEntryError


class CourseView:
    def __init__(self, root, show_login_view):
        self._root = root
        self._frame = None

        self._current_courses = None

        self._course_name_entry = None
        self._course_credit_entry = None

        self._show_login_view = show_login_view

        self._user = course_service.current_user()
        self._initialize()
        self._display_all_courses()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _create_new_course(self):
        course_name = self._course_name_entry.get()
        course_credit = self._course_credit_entry.get()

        try:
            new_course = course_service.create_new_course(
                course_name, course_credit)

            if new_course:
                if self._display_all_courses() is not None:
                    messagebox.showinfo("Course registration",
                                        f"Course {course_name} successfully added!")
            else:
                messagebox.showinfo("Course registration",
                                    f"Something went wrong in adding course {course_name}!")

        except ExistingCourseError:
            messagebox.showinfo("Course registration",
                                f"Course {course_name} has already been added!")

        except CourseEntryError:
            messagebox.showinfo("Course registration",
                                "Course registration failed. Enter both course name and credits!")

    def _update_course_name(self):
        pass

    def _update_course_credits(self):
        pass

    def _update_course_grade(self):
        pass

    def _update_course_status(self):
        pass

    def _display_all_courses(self):
        # tyhjennetään treeview ennen kurssien näyttämistä
        for course in self._current_courses.get_children():
            self._current_courses.delete(course)

        courses = course_service.display_all_courses()

        if courses is not None:
            for row in courses:
                self._current_courses.insert(parent="", index="end", text="", values=(
                    row[0], row[1], row[2], row[3], row[4]))
        return None

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
            "Course Name", "Credits", "Grade", "Status", "Owner")
        current_courses_tree.column("#0", width=0, stretch=constants.NO)
        current_courses_tree.column("Course Name", width=140)
        current_courses_tree.column(
            "Credits", anchor=constants.CENTER, width=70)
        current_courses_tree.column(
            "Grade", anchor=constants.CENTER, width=70)
        current_courses_tree.column(
            "Status", anchor=constants.CENTER, width=100)
        current_courses_tree.column(
            "Owner", anchor=constants.CENTER, width=100)

        current_courses_tree.heading("#0", text="")
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

        # Testataan käyttäjänimen kirjaamista UI:hin
        course_name_label = ttk.Label(
            master=self._frame, text="Name")
        self._course_name_entry = ttk.Entry(master=self._frame)

        # Testataan salasanan kirjaamista UI:hin
        course_credit_label = ttk.Label(
            master=self._frame, text="Credits")
        self._course_credit_entry = ttk.Entry(master=self._frame)

        course_grade_label = ttk.Label(
            master=self._frame, text="Grade")
        course_grade_entry = ttk.Entry(master=self._frame)

        course_status_label = ttk.Label(
            master=self._frame, text="Status")
        course_status_entry = ttk.Entry(master=self._frame)

        # Kurssitietojen päivittämistä

        # update_course_name_label = ttk.Label(
        #     master=self._frame, text=" ")
        # update_course_name_entry = ttk.Entry(master=self._frame)

        # update_course_credits_label = ttk.Label(
        #     master=self._frame, text=" ")
        # update_course_credits_entry = ttk.Entry(master=self._frame)

        # update_course_grade_label = ttk.Label(
        #     master=self._frame, text=" ")
        # update_course_grade_entry = ttk.Entry(master=self._frame)

        # update_course_status_label = ttk.Label(
        #     master=self._frame, text=" ")
        # update_course_status_entry = ttk.Entry(master=self._frame)

        # update_course_name_button = ttk.Button(
        #     master=self._frame, text="Update course name", command=self._update_course_name)
        # update_course_credits_button = ttk.Button(
        #     master=self._frame, text="Update course credits", command=self._update_course_credits)
        # update_course_grade = ttk.Button(
        #     master=self._frame, text="Update course grade", command=self._update_course_grade)
        # update_course_status = ttk.Button(
        #     master=self._frame, text="Update course status", command=self._update_course_status)

        # Uuden kurssin lisääminen
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

        current_courses_tree.grid(row=2, column=0, columnspan=2,
                                  sticky=(constants.EW), padx=5, pady=5)

        # Kurssin lisäämisen painikkeet
        course_name_label.grid(row=3, column=0, padx=5, pady=5)
        course_credit_label.grid(row=3, column=1, padx=5, pady=5)
        course_grade_label.grid(row=3, column=2, padx=5, pady=5)
        course_status_label.grid(row=3, column=3, padx=5, pady=5)

        self._course_name_entry.grid(row=4, column=0, padx=5, pady=5)
        self._course_credit_entry.grid(row=4, column=1, padx=5, pady=5)
        course_grade_entry.grid(row=4, column=2, padx=5, pady=5)
        course_status_entry.grid(row=4, column=3, padx=5, pady=5)

        create_new_course_button.grid(
            row=5, column=1, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        # Kurssitietojen muokkaamisen painikkeet

        # update_course_name_label.grid(row=5, column=0, padx=5, pady=5)
        # update_course_name_entry.grid(row=5, column=1, sticky=(
        #     constants.E, constants.W), padx=5, pady=5)

        # update_course_credits_label.grid(row=6, column=0, padx=5, pady=5)
        # update_course_credits_entry.grid(row=6, column=1, sticky=(
        #     constants.E, constants.W), padx=5, pady=5)

        # update_course_grade_label.grid(row=7, column=0, padx=5, pady=5)
        # update_course_grade_entry.grid(row=7, column=1, sticky=(
        #     constants.E, constants.W), padx=5, pady=5)

        # update_course_status_label.grid(row=8, column=0, padx=5, pady=5)
        # update_course_status_entry.grid(row=8, column=1, sticky=(
        #     constants.E, constants.W), padx=5, pady=5)

        # Uloskirjautuminen
        back_to_login_view_button.grid(
            row=9, column=1, columnspan=1, sticky=constants.EW, padx=5, pady=5)

        # Sarakkeet ottavat kaiken jäljelle jäävän tilan, kun ikkunan kokoa muutetaan
        # yhdessä elementtien sticky-parametrien kanssa
        self._frame.columnconfigure(1, weight=1, minsize=400)
