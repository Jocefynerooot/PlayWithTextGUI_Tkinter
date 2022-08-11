from tkinter import *

class PlayWithText:
    def capitalizeEachWord(self, text):
        textr = text.split(" ")
        returnText = ""
        for word in textr:
            returnText += word.capitalize() + " "
        return returnText

    def newFile(self):
        pass

    def openFile(self):
        pass

    def saveFile(self):
        pass

    def cut(self):
        pass

    def copy(self):
        pass

    def paste(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass

    def help(self):
        pass

    def click(self, event):
        pass

    # Functions For Themes
    def shiftMode(self, event):
        pass

    def theme(self,
              bgColo="white",
              textColor="black",
              titleColor="#3b2664",
              textAreaColor="black"):
        pass

    def lightTheme(self):
        pass

    def darkTheme(self):
        pass

    def redTheme(self):
        pass

    def purpleTheme(self):
        pass


if __name__ == "__main__":
    # Gui Starts Here
    root = Tk()
    root.title("PlayWithText - Jocefyneroot")
    root.geometry("830x700")
    root.minsize(500, 400)

    heading = Label(root,
                    text="Welcome to Play With Text",
                    font="sans 15 bold",
                    fg="#3e1d7e")
    heading.pack(pady=5)

    modeBtnsFrame = Frame(root)
    modeBtnsFrame.pack()

    screensFame = Frame(root)
    screensFame.pack()

    buttonsFrame = Frame(root)
    buttonsFrame.pack()

    # Text Areas Here
    userText = Text(screensFame, font="lucida 14", width=35, height=15)
    userText.pack(padx=10, side=LEFT)

    userTextResult = Text(screensFame, font="lucida 14", width=35, height=15)
    userTextResult.pack(padx=10, side=LEFT)

    modeBtns = ["Enable Relax Mode", "Enable Light Mode"]
    for btn in modeBtns:
        btnColor = "#656572"
        modeBtn = Button(modeBtnsFrame,
                         text=f"{btn}",
                         font="lucida 10 bold",
                         bg=f"{btnColor}",
                         fg="white")
        modeBtn.pack(pady=15, padx=10, side=LEFT)

    allBtns = [
        "Capitalize", "Upper Case", "Lower Case", "Cap Each Word", "Copy",
        "Cut", "Paste", "Save", "Open", "Delete"
    ]
    for btn in allBtns:
        btnColor = "#656572"
        modeBtn = Button(buttonsFrame,
                         text=f"{btn}",
                         font="lucida 10 bold",
                         bg=f"{btnColor}",
                         fg="white")
        modeBtn.pack(pady=15, padx=10, side=LEFT)

    # Menu Bar
    menuBar = Menu(root)
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New")
    fileMenu.add_command(label="Open")
    fileMenu.add_command(label="Save")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit")

    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Copy")
    editMenu.add_command(label="Cut")
    editMenu.add_command(label="Paste")
    editMenu.add_separator()
    editMenu.add_command(label="Undo")
    editMenu.add_command(label="Redo")

    themeMenu = Menu(menuBar, tearoff=0)
    themeMenu.add_command(label="Light Theme")
    themeMenu.add_command(label="Dark Theme")
    themeMenu.add_command(label="Red Theme")
    themeMenu.add_command(label="Purple Theme")

    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="How To Use")

    menuBar.add_cascade(label="File", menu=fileMenu)
    menuBar.add_cascade(label="Edit", menu=editMenu)
    menuBar.add_cascade(label="Theme", menu=themeMenu)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menuBar)

    root.mainloop()