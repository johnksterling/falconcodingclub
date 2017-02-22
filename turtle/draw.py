import turtle
import tkinter


def run_draw():
    root = tkinter.Tk()
    root.title("Draw!")
    cv = tkinter.Canvas(root, width=600, height=600)
    cv.pack(side=tkinter.LEFT)

    t = turtle.RawTurtle(cv)
    screen = t.getscreen()
    screen.setworldcoordinates(0, 0, 600, 600)
    screen.bgcolor("white")

    button_frame = tkinter.Frame(root)
    button_frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

    pointLabel = tkinter.Label(button_frame, text="Width")
    pointLabel.pack()

    pointSize = tkinter.StringVar()
    pointEntry = tkinter.Entry(button_frame, textvariable=pointSize)
    pointEntry.pack()
    pointSize.set(str(1))

    def quitHandler():
        root.destroy()
        root.quit()
    quitButton = tkinter.Button(button_frame, text="Quit", command=quitHandler)
    quitButton.pack()

    def clickHandler(x, y):
        t.width(int(pointSize.get()))
        t.goto(x, y)
    screen.onclick(clickHandler)
    tkinter.mainloop()

if __name__ == "__main__":
    run_draw()
