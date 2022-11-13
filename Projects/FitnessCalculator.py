from tkinter import *

color_list = ['#5C246A', '#33334d']
win = Tk()
win.geometry("1920x1080")
win.config(bg="#33334d")

def extracting_values():
    lst=[]

    lst.append(ent_name.get())
    lst.append(ent_age.get())

    #bmi
    a=int(ent_weight.get())
    b=int(ent_height.get())
    h=b/100
    try:
        cbmi=a/(h**2)
        res='{:.2f}'.format(cbmi)
        lst.append(res)
    except:
        pass

    systolic=int(ent_high.get())
    diastolic=int(ent_low.get())

    if systolic<=90 and diastolic<=60:
        cbp='Low'
        lst.append(cbp)
    elif 100<=systolic<=120 and 70<=diastolic<=80:
        cbp='Medium'
        lst.append(cbp)
    else:
        cbp='High'
        lst.append(cbp)

    
    plsrate=int(ent_pulse.get())

    if plsrate<=60:
        cplsrate='Low'
        lst.append(cplsrate)
    elif 61<=plsrate<=99:
        cplsrate='Medium'
        lst.append(cplsrate)
    else:
        cplsrate='High'
        lst.append(cplsrate)

    rbccount=float(ent_rbc.get())

    if rbccount<5.4:
        crbc='Low'
        lst.append(crbc)
    elif 5.5<=rbccount<=5.8:
        crbc='Medium'
        lst.append(crbc)
    else:
        crbc='High'
        lst.append(crbc)

    wbccount=float(ent_wbc.get())
    if wbccount<4.5:
        cwbc='Low'
        lst.append(cwbc)
    elif 4.6<=wbccount<=10.9:
        cwbc='Medium'
        lst.append(cwbc)
    else:
        cwbc='High'
        lst.append(cwbc)

    pltcount=int(ent_plate.get())

    if pltcount<150:
        cplt='Low'
        lst.append(cplt)
    elif 151<=pltcount<=399:
        cplt='Medium'
        lst.append(cplt)
    else:
        cplt='High'
        lst.append(cplt)


    hb=float(ent_hp.get())

    if hb<12.0:
        chb='Low'
        lst.append(chb)

    elif 12.1<=hb<=15.5:
        chb='Medium'
        lst.append(chb)
    else :
        chb='High'
        lst.append(chb)

    uric=float(ent_acid.get())
    
    if uric<3.5:
        curic='Low'
        lst.append(curic)
    elif 3.6<=uric<=7.2:
        curic='Medium'
        lst.append(curic)
    else:
        chb='High'
        lst.append(curic)
    
    chol=int(ent_col.get())

    if chol<=170:
        cchol='Low'
        lst.append(cchol)
    elif 171<=chol<=239:
        cchol='Medium'
        lst.append(cchol)
    else:
        cchol='High'
        lst.append(cchol)
    return lst

def clear():
    ent_name.delete(0, END)
    ent_age.delete(0, END)
    weightvalue.set(0)
    heightvalue.set(0)
    bplowvalue.set(0)
    bphighvalue.set(0)
    pulseratevalue.set(0)
    rbccountvalue.set(0)
    wbccountvalue.set(0)
    platelatevalue.set(0)
    hpvalue.set(0)
    uricacidvalue.set(0)
    cholesterolvalue.set(0)


def secwin():
    root = Tk()
    root.title(' REPORT ')
    root.geometry('900x900')
    root.resizable(0, 0)
    root.configure(bg='grey')

    a=extracting_values()
    
    zerolabel = Label(root, text='R E S U L T', bg='GREEN', fg='BLACK', width=30, font=('Courier', 15))
    zerolabel.grid(row=0, column=0, padx=10, pady=20)
    zeroreslabel = Label(root, text='', bg='grey', font=('Arial', 10), width=25, fg='black')
    zeroreslabel.grid(row=0, column=1, padx=10, pady=0)

    bmilabel = Label(root, text='BMI (Body Mass Index):', bg='black', fg='white', width=30, font=('Arial', 13))
    bmilabel.grid(row=1, column=0, padx=50, pady=3)
    bmireslabel = Label(root, text=a[2], bg='white', font=('Arial', 10), width=25, fg='black')
    bmireslabel.grid(row=1, column=1, padx=10, pady=3)

    bplabel = Label(root, text='BP (High/Medium/Low):', bg='black', fg='white', width=30, font=('Arial', 13))
    bplabel.grid(row=2, column=0, padx=10, pady=3)
    bpreslabel = Label(root, text=a[3], bg='white', font=('Arial', 10), width=25, fg='black')
    bpreslabel.grid(row=2, column=1, padx=10, pady=0)

    prlabel = Label(root, text='Pulse Rate(High/Medium/Low):', bg='black', fg='white', width=30, font=('Arial', 13))
    prlabel.grid(row=3, column=0, padx=10, pady=3)
    prreslabel = Label(root, text=a[4], bg='white', font=('Arial', 10), width=25, fg='black')
    prreslabel.grid(row=3, column=1, padx=10, pady=0)

    rbclabel = Label(root, text='RBC Count(High/Medium/Low):', bg='black', fg='white', width=30, font=('Arial', 13))
    rbclabel.grid(row=4, column=0, padx=10, pady=3)
    rbcreslabel = Label(root, text=a[5], bg='white', font=('Arial', 10), width=25, fg='black')
    rbcreslabel.grid(row=4, column=1, padx=10, pady=0)

    wbclabel = Label(root, text='WBC Count(High/Medium/Low):', bg='black', fg='white', width=30, font=('Arial', 13))
    wbclabel.grid(row=5, column=0, padx=20, pady=3)
    wbcreslabel = Label(root, text=a[6], bg='white', font=('Arial', 10), width=25, fg='black')
    wbcreslabel.grid(row=5, column=1, padx=10, pady=2)

    plateletslabel = Label(root, text='Platelets(High/Medium/Low):', bg='black', fg='white', width=30,font=('Arial', 13))
    plateletslabel.grid(row=6, column=0, padx=10, pady=3)
    plateletsreslabel = Label(root, text=a[7], bg='white', font=('Arial', 10), width=25, fg='black')
    plateletsreslabel.grid(row=6, column=1, padx=10, pady=0)

    hblabel = Label(root, text='HB(High/Medium/Low):', bg='black', fg='white', width=30, font=('Arial', 13))
    hblabel.grid(row=7, column=0, padx=10, pady=3)
    hbreslabel = Label(root, text=a[8], bg='white', font=('Arial', 10), width=25, fg='black')
    hbreslabel.grid(row=7, column=1, padx=10, pady=0)

    uriclabel = Label(root, text='Uric Acid(High/Medium/Low):', bg='black', fg='white', width=30, font=('Arial', 13))
    uriclabel.grid(row=8, column=0, padx=10, pady=3)
    uricreslabel = Label(root, text=a[9], bg='white', font=('Arial', 10), width=25, fg='black')
    uricreslabel.grid(row=8, column=1, padx=10, pady=0)

    cholesterollabel = Label(root, text='Cholesterol(High/Medium/Low):', bg='black', fg='white', width=30,font=('Arial', 13))
    cholesterollabel.grid(row=9, column=0, padx=10, pady=3)
    cholesterolreslabel = Label(root, text=a[10], bg='white', font=('Arial', 10), width=25, fg='black')
    cholesterolreslabel.grid(row=9, column=1, padx=10, pady=0)    

    root.mainloop()

namevalue= StringVar()
agevalue= IntVar()
gendervalue=IntVar()
weightvalue=IntVar()
weightvalue.set(0)
heightvalue=IntVar()
heightvalue.set(0)
bplowvalue=IntVar()
bplowvalue.set(0)
bphighvalue=IntVar()
bphighvalue.set(0)
pulseratevalue=IntVar()
pulseratevalue.set(0)
rbccountvalue=DoubleVar()
rbccountvalue.set(0)
wbccountvalue=DoubleVar()
wbccountvalue.set(0)
platelatevalue=IntVar()
platelatevalue.set(0)
hpvalue=DoubleVar()
hpvalue.set(0)
uricacidvalue=DoubleVar()
uricacidvalue.set(0)
cholesterolvalue=IntVar()
cholesterolvalue.set(0)
genbutvalue=IntVar()
clearbutvalue=IntVar()

frame2 = Frame(win, bg=color_list[1])
frame2.pack(fill='both', expand=True)

# FITNESS LABEL
lab = Label(frame2, text='FITNESS CALCULATOR', font=('impact', 40), bg='#33334d', fg='white')
lab.place(x=100, y=80)

# NAME LABEL
lab_name = Label(frame2, text='Name:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_name.place(x=20, y=200)
ent_name = Entry(frame2, width=15, borderwidth=0, textvariable=namevalue)
ent_name.place(x=110, y=208)

# AGE LABEL
lab_age = Label(frame2, text='Age:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_age.place(x=270, y=200)
ent_age = Entry(frame2, width=15, borderwidth=0, textvariable=agevalue)
ent_age.place(x=340, y=208)

# GENDER
lab_gen = Label(frame2, text='Gender:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_gen.place(x=20, y=250)
button1 = Radiobutton(frame2, text='Male  ', value=1, variable=genbutvalue).place(x=140, y=256)
button2 = Radiobutton(frame2, text='Female  ', value=0, variable=genbutvalue).place(x=250, y=256)

# WEIGHT
lab_weight = Label(frame2, text='Weight:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_weight.place(x=20, y=300)
ent_weight = Entry(frame2, width=15, borderwidth=0, textvariable=weightvalue)
ent_weight.place(x=180, y=308)

# HEIGHT
lab_height = Label(frame2, text='Height:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_height.place(x=20, y=340)
ent_height = Entry(frame2, width=15, borderwidth=0, textvariable=heightvalue)
ent_height.place(x=180, y=348)

# BP LOW
lab_low = Label(frame2, text='BP Low:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_low.place(x=20, y=380)
ent_low = Entry(frame2, width=15, borderwidth=0, textvariable=bplowvalue)
ent_low.place(x=180, y=388)

# BP HIGH
lab_high = Label(frame2, text='BP High:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_high.place(x=20, y=420)
ent_high = Entry(frame2, width=15, borderwidth=0, textvariable=bphighvalue)
ent_high.place(x=180, y=428)

# PULSE RATE
lab_pulse = Label(frame2, text='Pulse Rate:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_pulse.place(x=20, y=460)
ent_pulse = Entry(frame2, width=15, borderwidth=0, textvariable=pulseratevalue)
ent_pulse.place(x=180, y=468)

# RBC COUNT
lab_rbc = Label(frame2, text='RBC Count:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_rbc.place(x=20, y=500)
ent_rbc = Entry(frame2, width=15, borderwidth=0, textvariable=rbccountvalue)
ent_rbc.place(x=180, y=508)

# WBC COUNT
lab_wbc = Label(frame2, text='WBC Count:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_wbc.place(x=20, y=540)
ent_wbc = Entry(frame2, width=15, borderwidth=0, textvariable=wbccountvalue)
ent_wbc.place(x=180, y=548)

# PLATELETS
lab_plate = Label(frame2, text='Platelets:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_plate.place(x=20, y=580)
ent_plate = Entry(frame2, width=15, borderwidth=0, textvariable=platelatevalue)
ent_plate.place(x=180, y=588)

# HP
lab_hp = Label(frame2, text='HP:', fg='white', bg='#33334d' , font=('arial', 20,'bold'))
lab_hp.place(x=20, y=620)
ent_hp = Entry(frame2, width=15, borderwidth=0, textvariable=hpvalue)
ent_hp.place(x=180, y=628)

# URIC ACID
lab_acid = Label(frame2, text='Uric Acid:', fg='white', bg='#33334d', font=('arial', 20,'bold'))
lab_acid.place(x=20, y=660)
ent_acid = Entry(frame2, width=15, borderwidth=0, textvariable=uricacidvalue)
ent_acid.place(x=180, y=668)

# CHOLESTEROL
lab_col = Label(frame2, text='Cholesterol:', fg='white', bg='#33334d', font=('arial', 20,'bold'))
lab_col.place(x=20, y=700)
ent_col = Entry(frame2, width=15, borderwidth=0, textvariable=cholesterolvalue)
ent_col.place(x=180, y=708)

button = Button(frame2, text='VIEW RESULT', command=secwin, font=("impact", 20), bg='GREEN', fg='white', bd=0)
button.place(x=510, y=650)
button = Button(frame2, text='CLEAR', command=clear, font=("impact", 20), bg='RED', fg='white', bd=0)
button.place(x=680, y=650)

win.mainloop()
