from tkinter import *

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

  modeBtns = ["Enable Relax Mode", "Enable Light Mode", "Text"]
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




  root.mainloop()