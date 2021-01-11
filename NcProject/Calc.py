import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import Home

class Calc:
    def __init__(self, root, vlst, clst,vt):
        #setting title
        root.title("Result")
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
        ft = tkFont.Font(family='Agency FB',size=43, weight="bold")
        GLabel_633["font"] = ft
        GLabel_633["fg"] = "#FF7129"
        GLabel_633["bg"] = "#2F2F2B"
        GLabel_633["justify"] = "center"
        GLabel_633["text"] = "RESULT"
        GLabel_633.place(x=430, y=0)

        GLabel_928 = tk.Label(root)
        ft = tkFont.Font(family='Agency FB', size=30)
        GLabel_928["font"] = ft
        GLabel_928["bg"] = "#2F2F2B"
        GLabel_928["fg"] = "#FF7129"
        GLabel_928["justify"] = "center"
        GLabel_928["text"] = "Voltage Drops"
        GLabel_928.place(x=140, y=80)

        GLabel_615=tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_615["font"] = ft
        GLabel_615["bg"] = "#2F2F2B"
        GLabel_615["fg"] = "#FF7129"
        GLabel_615["justify"] = "center"
        GLabel_615["text"] = "VR1"
        GLabel_615.place(x=50,y=140)

        GLabel_616 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_616["font"] = ft
        GLabel_616["bg"] = "#2F2F2B"
        GLabel_616["fg"] = "#FF7129"
        GLabel_616["justify"] = "center"
        GLabel_616["text"] = vlst[0]
        GLabel_616.place(x=120, y=140)

        GLabel_663=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_663["font"] = ft
        GLabel_663["bg"] = "#2F2F2B"
        GLabel_663["fg"] = "#FF7129"
        GLabel_663["justify"] = "center"
        GLabel_663["text"] = "VR2"
        GLabel_663.place(x=50,y=170)

        GLabel_664 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_664["font"] = ft
        GLabel_664["bg"] = "#2F2F2B"
        GLabel_664["fg"] = "#FF7129"
        GLabel_664["justify"] = "center"
        GLabel_664["text"] = vlst[1]
        GLabel_664.place(x=120, y=170)

        GLabel_727=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_727["font"] = ft
        GLabel_727["bg"] = "#2F2F2B"
        GLabel_727["fg"] = "#FF7129"
        GLabel_727["justify"] = "center"
        GLabel_727["text"] = "VR3"
        GLabel_727.place(x=50,y=200)

        GLabel_728 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_728["font"] = ft
        GLabel_728["bg"] = "#2F2F2B"
        GLabel_728["fg"] = "#FF7129"
        GLabel_728["justify"] = "center"
        GLabel_728["text"] = vlst[2]
        GLabel_728.place(x=120, y=200)

        GLabel_384=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_384["font"] = ft
        GLabel_384["bg"] = "#2F2F2B"
        GLabel_384["fg"] = "#FF7129"
        GLabel_384["justify"] = "center"
        GLabel_384["text"] = "VR4"
        GLabel_384.place(x=50,y=230,width=72,height=37)

        GLabel_385 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_385["font"] = ft
        GLabel_385["bg"] = "#2F2F2B"
        GLabel_385["fg"] = "#FF7129"
        GLabel_385["justify"] = "center"
        GLabel_385["text"] = vlst[3]
        GLabel_385.place(x=120, y=230, width=72, height=37)

        GLabel_969=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_969["font"] = ft
        GLabel_969["bg"] = "#2F2F2B"
        GLabel_969["fg"] = "#FF7129"
        GLabel_969["justify"] = "center"
        GLabel_969["text"] = "VR5"
        GLabel_969.place(x=230,y=140,width=72,height=37)

        GLabel_970 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_970["font"] = ft
        GLabel_970["bg"] = "#2F2F2B"
        GLabel_970["fg"] = "#FF7129"
        GLabel_970["justify"] = "center"
        GLabel_970["text"] = vlst[4]
        GLabel_970.place(x=300, y=140, width=72, height=37)

        GLabel_416 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_416["font"] = ft
        GLabel_416["bg"] = "#2F2F2B"
        GLabel_416["fg"] = "#FF7129"
        GLabel_416["justify"] = "center"
        GLabel_416["text"] = "VR6"
        GLabel_416.place(x=230, y=170, width=72, height=37)

        GLabel_417 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_417["font"] = ft
        GLabel_417["bg"] = "#2F2F2B"
        GLabel_417["fg"] = "#FF7129"
        GLabel_417["justify"] = "center"
        GLabel_417["text"] = vlst[5]
        GLabel_417.place(x=300, y=170, width=72, height=37)


        GLabel_792 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_792["font"] = ft
        GLabel_792["bg"] = "#2F2F2B"
        GLabel_792["fg"] = "#FF7129"
        GLabel_792["justify"] = "center"
        GLabel_792["text"] = "VR7"
        GLabel_792.place(x=230, y=200, width=72, height=37)

        GLabel_793 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_793["font"] = ft
        GLabel_793["bg"] = "#2F2F2B"
        GLabel_793["fg"] = "#FF7129"
        GLabel_793["justify"] = "center"
        GLabel_793["text"] = vlst[6]
        GLabel_793.place(x=300, y=200, width=72, height=37)


        #CURRRENTTSSSS
        GLabel_546 = tk.Label(root)
        ft = tkFont.Font(family='Agency FB', size=23)
        GLabel_546["font"] = ft
        GLabel_546["bg"] = "#2F2F2B"
        GLabel_546["fg"] = "#FF7129"
        GLabel_546["justify"] = "center"
        GLabel_546["text"] = "Current Flow"
        GLabel_546.place(x=140, y=290, width=183, height=30)

        GLabel_426=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_426["font"] = ft
        GLabel_426["bg"] = "#2F2F2B"
        GLabel_426["fg"] = "#FF7129"
        GLabel_426["justify"] = "center"
        GLabel_426["text"] = "IR1"
        GLabel_426.place(x=60,y=330,width=70,height=25)

        GLabel_427 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_427["font"] = ft
        GLabel_427["bg"] = "#2F2F2B"
        GLabel_427["fg"] = "#FF7129"
        GLabel_427["justify"] = "center"
        GLabel_427["text"] = clst[0]
        GLabel_427.place(x=130, y=330, width=70, height=25)


        GLabel_9=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_9["font"] = ft
        GLabel_9["bg"] = "#2F2F2B"
        GLabel_9["fg"] = "#FF7129"
        GLabel_9["justify"] = "center"
        GLabel_9["text"] = "IR2"
        GLabel_9.place(x=60,y=360,width=70,height=25)

        GLabel_10 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_10["font"] = ft
        GLabel_10["bg"] = "#2F2F2B"
        GLabel_10["fg"] = "#FF7129"
        GLabel_10["justify"] = "center"
        GLabel_10["text"] = clst[1]
        GLabel_10.place(x=130, y=360, width=70, height=25)

        GLabel_194=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_194["font"] = ft
        GLabel_194["bg"] = "#2F2F2B"
        GLabel_194["fg"] = "#FF7129"
        GLabel_194["justify"] = "center"
        GLabel_194["text"] = "IR3"
        GLabel_194.place(x=60,y=390,width=70,height=25)

        GLabel_195 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_195["font"] = ft
        GLabel_195["bg"] = "#2F2F2B"
        GLabel_195["fg"] = "#FF7129"
        GLabel_195["justify"] = "center"
        GLabel_195["text"] = clst[2]
        GLabel_195.place(x=130, y=390, width=70, height=25)

        GLabel_282=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_282["font"] = ft
        GLabel_282["bg"] = "#2F2F2B"
        GLabel_282["fg"] = "#FF7129"
        GLabel_282["justify"] = "center"
        GLabel_282["text"] = "IR4"
        GLabel_282.place(x=60,y=420,width=70,height=25)

        GLabel_283 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_283["font"] = ft
        GLabel_283["bg"] = "#2F2F2B"
        GLabel_283["fg"] = "#FF7129"
        GLabel_283["justify"] = "center"
        GLabel_283["text"] = clst[3]
        GLabel_283.place(x=130, y=420, width=70, height=25)

        GLabel_154 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_154["font"] = ft
        GLabel_154["bg"] = "#2F2F2B"
        GLabel_154["fg"] = "#FF7129"
        GLabel_154["justify"] = "center"
        GLabel_154["text"] = "IR5"
        GLabel_154.place(x=250, y=330, width=70, height=25)

        GLabel_155 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_155["font"] = ft
        GLabel_155["bg"] = "#2F2F2B"
        GLabel_155["fg"] = "#FF7129"
        GLabel_155["justify"] = "center"
        GLabel_155["text"] = clst[4]
        GLabel_155.place(x=320, y=330, width=70, height=25)

        GLabel_123 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_123["font"] = ft
        GLabel_123["bg"] = "#2F2F2B"
        GLabel_123["fg"] = "#FF7129"
        GLabel_123["justify"] = "center"
        GLabel_123["text"] = "IR6"
        GLabel_123.place(x=250, y=360, width=70, height=25)

        GLabel_124 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_124["font"] = ft
        GLabel_124["bg"] = "#2F2F2B"
        GLabel_124["fg"] = "#FF7129"
        GLabel_124["justify"] = "center"
        GLabel_124["text"] = clst[5]
        GLabel_124.place(x=320, y=360, width=70, height=25)

        GLabel_802=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_802["font"] = ft
        GLabel_802["bg"] = "#2F2F2B"
        GLabel_802["fg"] = "#FF7129"
        GLabel_802["justify"] = "center"
        GLabel_802["text"] = "IR7"
        GLabel_802.place(x=250,y=390,width=70,height=25)

        GLabel_803 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_803["font"] = ft
        GLabel_803["bg"] = "#2F2F2B"
        GLabel_803["fg"] = "#FF7129"
        GLabel_803["justify"] = "center"
        GLabel_803["text"] = clst[6]
        GLabel_803.place(x=320, y=390, width=70, height=25)



        GLabel_364=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_364["font"] = ft
        GLabel_364["bg"] = "#2F2F2B"
        GLabel_364["fg"] = "#FF7129"
        GLabel_364["justify"] = "center"
        GLabel_364["text"] = "Total Current"
        GLabel_364.place(x=70,y=470)

        GLabel_365 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_365["font"] = ft
        GLabel_365["bg"] = "#2F2F2B"
        GLabel_365["fg"] = "#FF7129"
        GLabel_365["justify"] = "center"
        GLabel_365["text"] = round((clst[1] + clst[2]),4)
        GLabel_365.place(x=200, y=470)

        GLabel_108=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_108["font"] = ft
        GLabel_108["bg"] = "#2F2F2B"
        GLabel_108["fg"] = "#FF7129"
        GLabel_108["justify"] = "center"
        GLabel_108["text"] = "Total Voltage"
        GLabel_108.place(x=410,y=470)

        GLabel_109 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_109["font"] = ft
        GLabel_109["bg"] = "#2F2F2B"
        GLabel_109["fg"] = "#FF7129"
        GLabel_109["justify"] = "center"
        GLabel_109["text"] = vt
        GLabel_109.place(x=540, y=470)

        GLabel_914=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_914["font"] = ft
        GLabel_914["bg"] = "#2F2F2B"
        GLabel_914["fg"] = "#FF7129"
        GLabel_914["justify"] = "center"
        GLabel_914["text"] = "Total Resistance"
        GLabel_914.place(x=730,y=470)

        GLabel_915 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_915["font"] = ft
        GLabel_915["bg"] = "#2F2F2B"
        GLabel_915["fg"] = "#FF7129"
        GLabel_915["justify"] = "center"
        GLabel_915["text"] = round((vt/(clst[1] + clst[2])),3)
        GLabel_915.place(x=880, y=470)

        ret_BUTTON = tk.Button(root)
        ft = tkFont.Font(family='Century Gothic', size=20, weight="bold")
        ret_BUTTON["font"] = ft
        ret_BUTTON["bg"] = "#FF7129"
        ret_BUTTON["fg"] = "#2F2F2B"
        ret_BUTTON["justify"] = "center"
        ret_BUTTON["text"] = "RETURN"
        ret_BUTTON["relief"] = "flat"
        ret_BUTTON.place(x=430, y=500, width=155, height=40)
        ret_BUTTON["command"] = lambda: goTo_Home(root)

        load = Image.open("T.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(root, image=render)
        img.image = render
        img.place(x=510,y=90,width=439,height=328)

        def goTo_Home(self):
            root.withdraw()
            toplevel = tk.Toplevel(root)
            Home.Home(toplevel)