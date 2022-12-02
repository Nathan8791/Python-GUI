from tkinter import *
from tkinter import ttk


class Preferences(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("Preferences")
        self.preferences_frame = ttk.Frame(self.root, padding="1 1 12 12", takefocus=True)
        self.name = ""
        self.language = ""
        self.save_time = ""

    def quit(self):
        self.root.destroy()

    def print_to_file(self):
        with open(f"preferences_{self.name}.txt", "w+") as write_obj:
            write_obj.write(f"Name: {self.name}\n"
                            f"Language: {self.language}\n"
                            f"Auto Save Every: {self.save_time} Minutes")

    def validate_data(self, name: StringVar, language: StringVar, time: StringVar):
        self.name = name.get()
        self.language = language.get()
        self.save_time = time.get()
        flag = True

        if not self.name:
            # displaying apt messages
            ttk.Label(self.preferences_frame, text=" Required").grid(column=2, row=1, padx=10, pady=10)
        else:
            # blank label
            ttk.Label(self.preferences_frame, text="").grid(column=2, row=1, padx=10, pady=10)

        if self.name.isdigit():
            # displaying apt messages
            ttk.Label(self.preferences_frame, text=" Must be a non numeric value").grid(column=2, row=1, padx=10,
                                                                                        pady=10)
        else:
            # blank label
            ttk.Label(self.preferences_frame, text="").grid(column=2, row=1, padx=10, pady=10)

        if self.language and self.language.isdigit():
            # displaying apt messages
            ttk.Label(self.preferences_frame, text=" Must be a non numeric value").grid(column=2, row=2, padx=10,
                                                                                        pady=10)
        else:
            # blank label
            ttk.Label(self.preferences_frame, text="").grid(column=2, row=2, padx=10, pady=10)

        if self.save_time and self.save_time.isalpha():
            # displaying apt messages
            ttk.Label(self.preferences_frame, text=" Must be a valid integer value").grid(column=2, row=3, padx=10,
                                                                                          pady=10)
        else:
            ttk.Label(self.preferences_frame, text="").grid(column=2, row=3, padx=10, pady=10)

        if flag:
            # printing contents to file
            self.print_to_file()

    def draw_gui(self):
        name = StringVar()
        language = StringVar()
        save_time = StringVar()

        # name area
        # name label
        ttk.Label(self.preferences_frame, text="Name: ").grid(column=0, row=1, padx=10, pady=10)

        # name entry widget
        ttk.Entry(self.preferences_frame, width=30, textvariable=name).grid(column=1, row=1, padx=10, pady=10)

        # Language area
        # Language label
        ttk.Label(self.preferences_frame, text="Language: ").grid(column=0, row=2, padx=10, pady=10)
        language_entry_widget = ttk.Entry(self.preferences_frame, width=30, textvariable=language)

        # Language entry widget
        language_entry_widget.insert(END, "English")
        language_entry_widget.grid(column=1, row=2, padx=10, pady=10)

        # minutes area
        # minutes label
        ttk.Label(self.preferences_frame, text="Auto Save Every X Minutes: ").grid(column=0, row=3, padx=10, pady=10)

        # minutes entry widget
        ttk.Entry(self.preferences_frame, width=30, textvariable=save_time).grid(column=1, row=3, padx=10, pady=10)

        # buttons
        ttk.Button(self.preferences_frame, text="Save", command=lambda: self.validate_data(name=name,
                                                                                           language=language,
                                                                                           time=save_time)).grid(row=4,
                                                                                                                 column=0,
                                                                                                                 padx=30,
                                                                                                                 pady=5)

        ttk.Button(self.preferences_frame, text="Cancel", command=self.quit).grid(row=4, column=1, padx=30, pady=5)

        for child in self.root.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.root.mainloop()


if __name__ == "__main__":
    Preferences().draw_gui()