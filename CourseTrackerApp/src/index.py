from tkinter import Tk, ttk
from entities.user import User
from entities.course import Course
from ui.ui import UI

from initialize_database import initialize_database


def main():
    # alustetaan database tässä - tod.näk vaihdetaan vielä pois ja eriytetään sovelluslogiikkaan
    initialize_database()
    

    window = Tk()
    window.title("Course Tracker Application")

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == '__main__':
    main()
