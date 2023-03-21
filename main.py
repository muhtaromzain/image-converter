from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from converter import converter

# global variable
gui = Tk()
gui.geometry("400x60")
gui.title("Image converter")

folderPathFrom = StringVar()
folderPathTo   = StringVar()

class mainWindow():
    def getFolderPath(self, isFrom = True):
        folder_selected = filedialog.askdirectory()
        if (isFrom):
            folderPathFrom.set(folder_selected)
        else:
            folderPathTo.set(folder_selected)

    def getFolderPathFrom(self):
        self.getFolderPath()

    def getFolderPathTo(self):
        self.getFolderPath(False)

    def process(self):
        folderFrom = folderPathFrom.get()
        folderTo   = folderPathTo.get()

        if (folderFrom == "" and folderTo == ""):
            print("Please select your from directory and destination directory")
        elif (folderFrom == ""):
            print("Please select your from directory")
        elif (folderTo == ""):
            print("Please select your destination directory")
        else:
            print("Convert image from", folderFrom, " to ", folderTo)
            converter(folderFrom, folderTo).run()
    
    def view(self):
        # label from path
        labelFrom = Label(gui , text="From path")
        labelFrom.grid(row=0, column=0)
        # form directory from path
        destinationPath = Entry(gui, textvariable=folderPathFrom, state='disabled')
        destinationPath.grid(row=0, column=1)
        
        # label destination path
        formPathFrom = Label(gui , text="Destination path")
        formPathFrom.grid(row=1, column=0)
        # form directory destination path
        formPathDestination = Entry(gui, textvariable=folderPathTo, state='disabled')
        formPathDestination.grid(row=1, column=1)

        # button browse dir from path
        btnBrowseFrom = ttk.Button(gui, text="Browse Folder", command=self.getFolderPathFrom)
        btnBrowseFrom.grid(row=0, column=2)
        # button browse dir destination path
        btnBrowseDestination = ttk.Button(gui, text="Browse Folder", command=self.getFolderPathTo)
        btnBrowseDestination.grid(row=1, column=2)

        # button start convert
        btnStart = ttk.Button(gui , text="Start", command=self.process)
        btnStart.grid(row=0, column=3, rowspan=3, columnspan=3, ipady=10, ipadx=10)


if __name__ == "__main__":
    # converter().run()
    window = mainWindow()

    # load view
    window.view()

    # start apps
    gui.resizable(0,0)
    gui.mainloop()