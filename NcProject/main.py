import tkinter as tk
import tkinter.font as tkFont
import Home


class App:
    def __init__(self, root):
        #setting title
        root.title("Authentication")
        root["bg"] = "#2F2F2B"
        #setting window size
        width=1034
        height=562
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_776=tk.Label(root)
        ft = tkFont.Font(family='Agency FB', size=45, weight='bold')
        GLabel_776["font"] = ft
        GLabel_776["text"] = "Login"
        GLabel_776["bg"] = "#2F2F2B"
        GLabel_776["fg"] = "#FF7129"
        GLabel_776["relief"] = "flat"
        GLabel_776.place(x=480, y=120, )


        GLabel_775=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI', size=20)
        GLabel_775["font"] = ft
        GLabel_775["bg"] = "#2F2F2B"
        GLabel_775["fg"] = "#FF7129"
        GLabel_775["justify"] = "center"
        GLabel_775["text"] = "ID"
        GLabel_775.place(x=450, y=220, anchor="e")

        GLineEdit_466 = tk.Entry(root)
        ft = tkFont.Font(family='Segoe UI', size=13)
        GLineEdit_466["font"] = ft
        GLineEdit_466["justify"] = "left"
        GLineEdit_466["relief"] = "flat"
        GLineEdit_466.place(x=480, y=210, width=170, height=25)

        GLabel_335=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI',size=20)
        GLabel_335["font"] = ft
        GLabel_335["bg"] = "#2F2F2B"
        GLabel_335["fg"] = "#FF7129"
        GLabel_335["justify"] = "center"
        GLabel_335["text"] = "Password"
        GLabel_335.place(x=450,y=257, anchor="e")

        GLineEdit_481=tk.Entry(root)
        ft = tkFont.Font(family='Segoe UI',size=13)
        GLineEdit_481["font"] = ft
        GLineEdit_481["justify"] = "left"
        GLineEdit_481["relief"] = "flat"
        GLineEdit_481.place(x=480,y=250,width=170,height=25)

        GButton_88=tk.Button(root)
        GButton_88["bg"] = "#FF7129"
        ft = tkFont.Font(family='Century Gothic',size=14)
        GButton_88["font"] = ft
        GButton_88["fg"] = "#2F2F2B"
        GButton_88["justify"] = "center"
        GButton_88["text"] = "SIGN IN"
        GButton_88["relief"] = "flat"
        GButton_88.place(x=490,y=360,width=140,height=35)
        GButton_88["command"] = self.goTo_Home

    def goTo_Home(self):
        root.withdraw()
        toplevel = tk.Toplevel(root)
        Home.Home(toplevel)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
