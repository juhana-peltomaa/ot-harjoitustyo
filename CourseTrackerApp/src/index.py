from tkinter import Tk, ttk
from entities.user import User
from entities.course import Course
from ui.ui import UI


def main():
    kayttaja_1 = User("Juhana", "salasana")
    kurssi_1 = Course("Ohjelmistotekniikka", 5)

    window = Tk()
    window.title("Course Tracker practicing")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()
