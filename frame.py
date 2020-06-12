# **********Note for everyone working on this file***********
# This file has the main purpose of synthesizing the FRONT END
# for our program for SGS. This is super rough, but it gets
# the idea out there, so that we have a running model to look
# at and base the rest of the project on.
# -----------------------------------------------------------
# >> '__init__()' gives us the main buttons on top
# >> 'host_survey' gives the front end of hosting surveys live.
#    **Corresponds with 'surveyhost.py' in order to
#    work with the backend.
# >> 'upload_data()' allows the user to browse for the .csv or
#    .xls file, with SGS's survey data.
#    **Corresponds with 'dataupload.py' in order to
#    work with the backend.
# >> 'report_options()' encompasses the options for what type of
#    report SGS wants to export given the input data.
#    **Corresponds with 'options.py' in order to
#    work with the backend.
# >> 'report_preview()' gives the user a preview of what the
#    report will look like and *maybe* give them the option
#    of changing the appearance to what they want it to look
#    like.
#    **Corresponds with 'previewreport.py' in order to
#    work with the backend.
# >> 'download_report()' allows the user to download the
#    report to anywhere they want
#    **Corresponds with 'download.py' in order to
#    work with the backend.
# -----------------------------------------------------------
# >> 'runner()' goes to 'main.py' in order to run the program
# >> 'clear()' clears the BOTTOM FRAME in order to move
#    between the different interfaces.
# -----------------------------------------------------------
#    **CLARIFICATION**
#    There is a bottom frame and an upper frame. All the
#    objects and widgets within __init__() have been placed
#    in the UPPER FRAME. *DON'T TOUCH THIS UNLESS YOU'RE
#    TRYING TO MAKE IT LOOK PRETTIER. (thanks:))*
#    Put everything else in the BOTTOM FRAME.

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import surveyhost as sh
import dataupload as du

# SGS Color Hex Codes
SGS_orange = '#FF8F1C'
SGS_coolgray = '#BBBCBC'
SGS_tealblue = '#05C3DE'
SGS_yellow = '#FBD872'
SGS_green = '#7AE1BF'
SGS_purple = '#8E3A80'
black = '#FFFFFF'


class AppFrame():

    # Widgets for app window are created here
    def __init__(self, master):
        self.master = master
        master.title("SGS-1")  # Name of app window
        # master.configure(bg=SGS_coolgray) #This is just for deco

        self.frame = tk.Frame(self.master)
        self.frame.grid(row=1,
                        column=0,
                        sticky="nsew")

        # Establishing bottom frame
        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.grid(row=2,
                               column=0,
                               sticky="nsew")

        load = Image.open("SGS_LOGO.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self.frame, image=render)
        img.image = render
        img.grid(column=0,
                 row=0,
                 columnspan=6)

        self.survey_button = tk.Button(self.frame, text="HOST SURVEY",
                                       command=self.host_survey,
                                       activeforeground=SGS_orange,
                                       activebackground=SGS_orange,
                                       bg=SGS_coolgray)
        self.survey_button.grid(column=0, row=1, sticky="nsew")

        self.upload_button = tk.Button(self.frame, text="UPLOAD DATA",
                                       command=self.upload_data,
                                       activeforeground=SGS_orange,
                                       activebackground=SGS_orange,
                                       bg=SGS_coolgray)
        self.upload_button.grid(column=1, row=1, sticky="nsew")

        self.options_button = tk.Button(self.frame, text="REPORT OPTIONS",
                                        command=self.report_options,
                                        activeforeground=SGS_orange,
                                        activebackground=SGS_orange,
                                        bg=SGS_coolgray)
        self.options_button.grid(column=2, row=1, sticky="nsew")

        self.preview_button = tk.Button(self.frame, text="REPORT PREVIEW",
                                        command=self.report_preview,
                                        activeforeground=SGS_orange,
                                        activebackground=SGS_orange,
                                        bg=SGS_coolgray)
        self.preview_button.grid(column=3, row=1, sticky="nsew")

        self.download_button = tk.Button(self.frame, text="DOWNLOAD REPORT",
                                         command=self.download_report,
                                         activeforeground=SGS_orange,
                                         activebackground=SGS_orange,
                                         bg=SGS_coolgray)
        self.download_button.grid(column=4, row=1, sticky="nsew")

        self.close_button = tk.Button(self.frame, text="QUIT",
                                      command=master.quit,
                                      activeforeground=SGS_orange,
                                      activebackground=SGS_orange,
                                      bg=SGS_coolgray)
        self.close_button.grid(column=5, row=1, sticky="nsew")

    # Each part of program
    def host_survey(self):
        # Clearing Previous Widgets
        self.clear()

        # Creating Checkboxes
        targets = ["Student", "Parent", "Teacher"]
        r = 2
        for demographic in targets:
            tk.Checkbutton(self.bottom_frame, text=demographic,
                           relief=tk.RIDGE).grid(row=r,
                                                 column=0,
                                                 sticky="nsew")
            r = r + 1
        host_button = tk.Button(self.bottom_frame, text="HOST",
                                bg=SGS_orange)
        host_button.grid(column=0,
                         row=r,
                         columnspan=6,
                         sticky="nsew")  # Still needs command=
        print("Host Survey")

    filename = ""

    def upload_data(self):  # DON'T TOUCH THIS CARELESSLY, BROWSE_BUTTON IS MY BRAINCHILD
        # Clear widgets
        self.clear()

        # Action Items
        filepath = tk.Entry(self.bottom_frame)
        filepath.grid(column=0,
                      row=2,
                      # columnspan=4,
                      sticky="nsew")

        browse_button = tk.Button(self.bottom_frame, text="BROWSE",
                                  bg=SGS_orange,
                                  command=lambda: [du.find_file(),
                                                   filepath.delete(first=0, last='end'),
                                                   filepath.insert(0, AppFrame.filename)])
        browse_button.grid(column=1,
                           row=2,
                           # columnspan=4,
                           sticky="nsew")

        upload_button = tk.Button(self.bottom_frame, text="UPLOAD",
                                  bg=SGS_orange,
                                  command=du.upload)
        upload_button.grid(column=2,
                           row=2,
                           sticky="nsew")  # Still needs command=

        print("Upload Data")

    def report_options(self):
        # Clear Widgets
        self.clear()

        # Options
        options = ["EDUCATION REPORT",
                   "DONOR REPORT",
                   "PARENT REPORT",
                   "STUDENT REPORT",
                   "INTERNAL REPORT",
                   "CONDENSED REPORT"]
        tk.Label(self.bottom_frame, text="CHOOSE REPORT TYPE: ").grid(column=0,
                                                                      row=2,
                                                                      sticky="nsew")

        report_type = ttk.Combobox(self.bottom_frame, values=options)
        report_type.grid(column=1,
                         row=2,
                         sticky="nsew")

        tk.Label(self.bottom_frame, text="SEND TO WEBSITE?").grid(column=0,
                                                                  row=3,
                                                                  sticky="nsew")

        send_to_website = ttk.Combobox(self.bottom_frame, values=["YES", "NO"])
        send_to_website.grid(column=1,
                             row=3,
                             sticky="nsew")

        print("Report Options")

    def report_preview(self):
        # Clear Widgets
        self.clear()
        print("Report Preview")

    def download_report(self):
        # Clear Widgets
        self.clear()
        print("Download Report")

    # Edit Window itself in this function
    def runner(self):
        root = tk.Tk()
        #root.geometry("772x720")  # SGS_LOGO.png has width 177, height 766
        root.geometry("772x400")  # Temporary size
        my_gui = AppFrame(root)
        root.mainloop()

    def clear(self):
        widgets = self.bottom_frame.grid_slaves()
        for w in widgets:
            w.destroy()
