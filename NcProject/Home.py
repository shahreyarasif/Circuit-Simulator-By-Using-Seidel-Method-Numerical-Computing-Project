import tkinter as tk
import tkinter.font as tkFont
import numpy as np
from PIL import ImageTk, Image

from Calc import Calc



class Home:
    def __init__(self, root):
        #setting title
        root.title("Get_Info")
        root["bg"] = "#2F2F2B"
        #setting window size
        width=1035
        height=563
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_633=tk.Label(root)
        ft = tkFont.Font(family='Agency FB', size=33)
        GLabel_633["font"] = ft
        GLabel_633["bg"] = "#2F2F2B"
        GLabel_633["fg"] = "#FF7129"
        GLabel_633["justify"] = "center"
        GLabel_633["text"] = "STEP 1"
        GLabel_633.place(x=30, y=20, width=176, height=62)

        GLabel_615=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLabel_615["font"] = ft
        GLabel_615["bg"] = "#2F2F2B"
        GLabel_615["fg"] = "#FF7129"
        GLabel_615["justify"] = "center"
        GLabel_615["text"] = "R1"
        GLabel_615.place(x=50, y=120, width=72, height=37)

        GLineEdit_191=tk.Entry(root)
        GLineEdit_191["borderwidth"] = "1px"
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLineEdit_191["font"] = ft
        GLineEdit_191["fg"] = "#333333"
        GLineEdit_191["justify"] = "left"
        GLineEdit_191["text"] = ""
        GLineEdit_191.place(x=120, y=120, width=120, height=33)

        GLabel_663=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLabel_663["font"] = ft
        GLabel_663["bg"] = "#2F2F2B"
        GLabel_663["fg"] = "#FF7129"
        GLabel_663["justify"] = "center"
        GLabel_663["text"] = "R2"
        GLabel_663.place(x=50, y=160, width=72, height=37)

        GLineEdit_490=tk.Entry(root)
        GLineEdit_490["borderwidth"] = "1px"
        ft = tkFont.Font(family='Segoe UI',size=16)
        GLineEdit_490["font"] = ft
        GLineEdit_490["fg"] = "#333333"
        GLineEdit_490["justify"] = "left"
        GLineEdit_490["text"] = ""
        GLineEdit_490.place(x=120, y=160, width=120, height=33)

        GLabel_727=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLabel_727["font"] = ft
        GLabel_727["bg"] = "#2F2F2B"
        GLabel_727["fg"] = "#FF7129"
        GLabel_727["justify"] = "center"
        GLabel_727["text"] = "R3"
        GLabel_727.place(x=50, y=200, width=72, height=37)

        GLabel_384=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLabel_384["font"] = ft
        GLabel_384["bg"] = "#2F2F2B"
        GLabel_384["fg"] = "#FF7129"
        GLabel_384["justify"] = "center"
        GLabel_384["text"] = "R4"
        GLabel_384.place(x=50, y=240, width=72, height=37)

        GLabel_928=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLabel_928["font"] = ft
        GLabel_928["bg"] = "#2F2F2B"
        GLabel_928["fg"] = "#FF7129"
        GLabel_928["justify"] = "center"
        GLabel_928["text"] = "V Source"
        GLabel_928.place(x=270, y=240, width=82, height=36)

        GLabel_792=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI',size=16)
        GLabel_792["font"] = ft
        GLabel_792["bg"] = "#2F2F2B"
        GLabel_792["fg"] = "#FF7129"
        GLabel_792["justify"] = "center"
        GLabel_792["text"] = "R7"
        GLabel_792.place(x=290, y=200, width=72, height=37)

        GLabel_416=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLabel_416["font"] = ft
        GLabel_416["bg"] = "#2F2F2B"
        GLabel_416["fg"] = "#FF7129"
        GLabel_416["justify"] = "center"
        GLabel_416["text"] = "R6"
        GLabel_416.place(x=290, y=160, width=72, height=37)

        GLabel_969=tk.Label(root)
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLabel_969["font"] = ft
        GLabel_969["bg"] = "#2F2F2B"
        GLabel_969["fg"] = "#FF7129"
        GLabel_969["justify"] = "center"
        GLabel_969["text"] = "R5"
        GLabel_969.place(x=290, y=120, width=72, height=37)

        GLineEdit_338=tk.Entry(root)
        GLineEdit_338["borderwidth"] = "1px"
        ft = tkFont.Font(family='Segoe UI',size=16)
        GLineEdit_338["font"] = ft
        GLineEdit_338["fg"] = "#333333"
        GLineEdit_338["justify"] = "left"
        GLineEdit_338["text"] = ""
        GLineEdit_338.place(x=120, y=200, width=120, height=33)

        GLineEdit_864=tk.Entry(root)
        GLineEdit_864["borderwidth"] = "1px"
        ft = tkFont.Font(family='Segoe UI',size=16)
        GLineEdit_864["font"] = ft
        GLineEdit_864["fg"] = "#333333"
        GLineEdit_864["justify"] = "left"
        GLineEdit_864["text"] = ""
        GLineEdit_864.place(x=120, y=240, width=120, height=33)

        GLineEdit_560=tk.Entry(root)
        GLineEdit_560["borderwidth"] = "1px"
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLineEdit_560["font"] = ft
        GLineEdit_560["fg"] = "#333333"
        GLineEdit_560["justify"] = "left"
        GLineEdit_560["text"] = ""
        GLineEdit_560.place(x=360, y=120, width=120, height=33)

        GLineEdit_344=tk.Entry(root)
        GLineEdit_344["borderwidth"] = "1px"
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLineEdit_344["font"] = ft
        GLineEdit_344["fg"] = "#333333"
        GLineEdit_344["justify"] = "left"
        GLineEdit_344["text"] = ""
        GLineEdit_344.place(x=360, y=160, width=120, height=33)

        GLineEdit_848=tk.Entry(root)
        GLineEdit_848["borderwidth"] = "1px"
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLineEdit_848["font"] = ft
        GLineEdit_848["fg"] = "#333333"
        GLineEdit_848["justify"] = "left"
        GLineEdit_848["text"] = ""
        GLineEdit_848.place(x=360, y=200, width=120, height=33)

        GLineEdit_104=tk.Entry(root)
        GLineEdit_104["borderwidth"] = "1px"
        ft = tkFont.Font(family='Segoe UI', size=16)
        GLineEdit_104["font"] = ft
        GLineEdit_104["fg"] = "#333333"
        GLineEdit_104["justify"] = "left"
        GLineEdit_104["text"] = ""
        GLineEdit_104.place(x=360, y=240, width=120, height=33)

        GButton_735=tk.Button(root)
        ft = tkFont.Font(family='Century Gothic', size=20, weight="bold")
        GButton_735["font"] = ft
        GButton_735["bg"] = "#FF7129"
        GButton_735["fg"] = "#2F2F2B"
        GButton_735["justify"] = "center"
        GButton_735["text"] = "SIMULATE"
        GButton_735["relief"] = "flat"
        GButton_735.place(x=430, y=400, width=155, height=40)
        GButton_735["command"] =lambda : self.Pre_Simulation(root, GLineEdit_191,
                                                             GLineEdit_490,
                                                             GLineEdit_338,
                                                             GLineEdit_864,
                                                             GLineEdit_560,
                                                             GLineEdit_344,
                                                             GLineEdit_848,
                                                             GLineEdit_104,)

        load = Image.open("T.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(root, image=render)
        img.image = render
        img.place(x=570, y=50, width=450, height=304)

    def Results(self, root, vlst, clst, vt):
        root.withdraw()
        new = tk.Toplevel(root)
        Calc(new, vlst, clst, vt)

    def Pre_Simulation(self, root, res1, res2, res3, res4, res5, res6, res7, vs):
        r1 = int(res1.get())
        r2 = int(res2.get())
        r3 = int(res3.get())
        r4 = float(res4.get())
        r5 = int(res5.get())
        r6 = int(res6.get())
        r7 = int(res7.get())
        vSource = int(vs.get())


        # Node2Data:

        #I1=I2 + I3
        # v1/r1 =v2/r2 +v3/r3
       #( 10-vn2

        # Node2Data:
        constn2 = (r2 * r3 * vSource)
        Vn2 = -(-(r2 * r3) - (r1 * r3) - (r1 * r2))
        Vn3 = -(r1 * r3)
        Vn4 = -(r1 * r2)
        Vn5 = 0
        CoffOfNode2 = [Vn2, Vn3, Vn4, Vn5, constn2]
        print(CoffOfNode2)

        # Node3Data:
        Vn2 = (r4 * r5)
        Vn3 = (-(r2 * r4) - (r4 * r5) - (r2 * r5))
        Vn4 = (r2 * r5)
        Vn5 = (r2 * r4)
        constn3 = 0

        CoffOfNode3 = [Vn2, Vn3, Vn4, Vn5, constn3]
        print(CoffOfNode3)

        # Node4Data:
        Vn2 = (r4 * r6)
        Vn3 = (r3 * r6)
        Vn4 = -((r3 * r6) + (r4 * r6) + (r3 * r4))
        Vn5 = (r3 * r4)
        constn4 = 0
        CoffOfNode4 = [Vn2, Vn3, Vn4, Vn5, constn4]
        print(CoffOfNode4)

        # Node5Data:
        Vn2 = 0
        Vn3 = (r6 * r7)
        Vn4 = (r5 * r7)
        Vn5 = -(r6 * r7) - (r5 * r7) - (r5 * r6)
        constn5 = 0
        CoffOfNode5 = [Vn2, Vn3, Vn4, Vn5, constn5]
        print(CoffOfNode5)

        print(CoffOfNode2[0], "Vn2", CoffOfNode2[1], "Vn3", CoffOfNode2[2], "Vn4", CoffOfNode2[3], "Vn5", "=", constn2)
        print(CoffOfNode3[0], "Vn2", CoffOfNode3[1], "Vn3", CoffOfNode3[2], "Vn4", CoffOfNode3[3], "Vn5", "=", constn3)
        print(CoffOfNode4[0], "Vn2", CoffOfNode4[1], "Vn3", CoffOfNode4[2], "Vn4", CoffOfNode4[3], "Vn5", "=", constn4)
        print(CoffOfNode5[0], "Vn2", CoffOfNode5[1], "Vn3", CoffOfNode5[2], "Vn4", CoffOfNode5[3], "Vn5", "=", constn5)

        c = np.array([CoffOfNode2, CoffOfNode3, CoffOfNode4, CoffOfNode5])
        # Seidel
        x = np.zeros(len(c))
        for k in range(0, 20):
            for i in range(0, len(c)):
                y = 0
                for j in range(0, len(c)):
                    if i != j:
                        y = y + (c[i][j] * x[j])
                y = c[i][len(c)] - y
                x[i] = y / c[i][i]

        print(x)

        Vn = x
        Vn2 = Vn[0]
        Vn3 = Vn[1]
        Vn4 = Vn[2]
        Vn5 = Vn[3]

        v1 = vSource - Vn2
        v2 = Vn2 - Vn3
        v3 = Vn2 - Vn4
        v4 = Vn4 - Vn3
        v5 = Vn3 - Vn5
        v6 = Vn4 - Vn5
        v7 = Vn5

        Vollist = list()
        Vollist.append(round(v1, 3))
        Vollist.append(round(v2, 3))
        Vollist.append(round(v3, 3))
        Vollist.append(round(v4, 3))
        Vollist.append(round(v5, 3))
        Vollist.append(round(v6, 3))
        Vollist.append(round(v7, 3))

        Currlist = list()
        Currlist.append((round((v1 / r1), 4)))
        Currlist.append((round((v2 / r2), 4)))
        Currlist.append((round((v3 / r3), 4)))
        Currlist.append((round((v4 / r4), 4)))
        Currlist.append((round((v5 / r5), 4)))
        Currlist.append((round((v6 / r6), 4)))
        Currlist.append((round((v7 / r7), 4)))


        print("The Voltage Of r1 is ", v1, "and current is ", round((v1 / r1), 4))
        print("The Voltage Of r2 is ", v2, "and current is ", round((v2 / r2), 4))
        print("The Voltage Of r3 is ", v3, "and current is ", round((v3 / r3), 4))
        print("The Voltage Of r4 is ", v4, "and current is ", round((v4 / r4), 4))
        print("The Voltage Of r5 is ", v5, "and current is ", round((v5 / r5), 4))
        print("The Voltage Of r6 is ", v6, "and current is ", round((v6 / r6), 4))
        print("The Voltage Of r7 is ", v7, "and current is ", round((v7 / r7), 4))

        self.Results(root, Vollist, Currlist, vSource)

