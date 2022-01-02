import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk  
global bmi1
curr_ideal=0
bmi1=0
actual_fat=0

metre_height=["1.42","1.45","1.47","1.50","1.52","1.55","1.57","1.60","1.63","1.65","1.68","1.70","1.73","1.75","1.78","1.80","1.83","1.85","1.88","1.91","1.93","1.96","1.98","2.01","2.03","2.06","2.08","2.11","2.13"]
feet_height=['4.8', '4.9', '4.10', '4.11', '5', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '5.9', '5.10', '5.11', '6', '6.1', '6.2', '6.3', '6.4', '6.5', '6.6', '6.7', '6.8', '6.9', '6.10', '6.11','7.0']
ideal_weight_male_lbs=[111,114,117,121,124,127,130,133,136,139,142,145,148,152,155,158,161,164,167,170,173,176,179,183,186,189,192,195,198]
ideal_weight_female_lbs=[105,108,111,114,117,120,123,126,129,132,135,138,141,144,147,150,153,156,159,162,165,168,171,174,177,180,183,186,189]
metre_to_feet_dict=dict(zip(metre_height,feet_height))
feet_to_ideal_weight_male=dict(zip(feet_height,ideal_weight_male_lbs))
feet_to_ideal_weight_female=dict(zip(feet_height,ideal_weight_female_lbs))
def find_color_and_text(val):
    color=""
    stat=""
    msg=""
    if val<16:
        color="red"
        stat="Very Severely UnderWeight"
    elif val>=16 and val<17:
        color="orange"
        stat="Severely UnerWeight"
    elif val>=17 and val<18.5:
        color="yellow"
        stat="UnderWeight"
    elif val>=18.5 and val<25:
        color="green"
        stat="Normal"
    elif val>25 and val<30:
        color="yellow"
        stat="OverWeight"
    elif val>=30 and val<35:
        color="orange"
        stat="Obese Class I"
    elif val>=35 and val<40 :
        color="red"
        stat="Obese Class II"
    else: #val>40:
        color="red"
        stat="Obese Class III"
    if val<18.5:
        msg="Time to Grab a Bite"
    elif val>=18.5 and val<=25:
        msg="Great Shape"
    else:
        msg="Time for a Run"
    return stat,color,msg
        
def calc():
    curr_ideal=0
    bmi1=0
    actual_fat=0
    
    bmi_color=""
    fat_color=""
    
    pres_h=float(height_entry.get())
    pres_w=float(weight_entry.get())
    height_fin=0
    weight_fin=0
    gender=gender_choice.get()
    age=int(age_entry.get())
    
    
    
    if height_chosen.get()=="Feet and Inches":
        temp_h=str(pres_h).split(".")
        height_fin=float(temp_h[0])*0.3048+float(temp_h[1])*0.0254
        if gender=="Male":
            curr_ideal=feet_to_ideal_weight_male[str(pres_h)]
        if gender=="Female":
            curr_ideal=feet_to_ideal_weight_female[str(pres_h)]
            
    if height_chosen.get()=="Centimetres":
        temp_h=str(pres_h).split(".")
        height_fin=float(temp_h[0])*0.01+float(temp_h[1])*0.001
        temp_h1=(pres_h*0.0328084)
        temp_h1=round(temp_h1,1)
        if gender=="Male":
            curr_ideal=feet_to_ideal_weight_male[str(temp_h1)]
        if gender=="Female":
            curr_ideal=feet_to_ideal_weight_female[str(temp_h1)]
            
    if weight_chosen.get()=="lbs":
        weight_fin=pres_w*0.4535
        curr_ideal=str(curr_ideal)+" lbs"
    if weight_chosen.get()=="Kg":
        weight_fin=pres_w
        curr_ideal*=0.453592
        curr_ideal=round(curr_ideal,1)
        curr_ideal=str(curr_ideal)+" kg"

    bmi1=float(weight_fin)/float(height_fin*height_fin)
    bmi1=round(bmi1,2)
    
    stat,color,msg=find_color_and_text(int(bmi1))
    
    if gender=="Male":
        actual_fat= 1.20*bmi1 + (0.23 * age) - 16.2
    else:
        actual_fat= 1.20*bmi1 + (0.23 * age) - 5.4
        
    ideal_label=tk.Label(text="Ideal Weight",font=('Times New Roman',10, 'bold'))
    bmi_label=tk.Label(text="BMI",font=('Times New Roman',10, 'bold'))
    fat_percent=tk.Label(text="Fat %",font=('Times New Roman',10, 'bold'))

    ideal_weight=tk.Label(text=str(curr_ideal),fg="green",bg="black",font=("times new roman",10,"bold"))
    bmi_actual=tk.Label(text=str(bmi1),fg=color,bg="black",font=("times new roman",10,"bold"))
    fat_percent_actual=tk.Label(text=str(actual_fat),fg=color,bg="black",font=("times new roman",10,"bold"))
    
    ideal_label.grid(row=7,column=0)
    bmi_label.grid(row=7,column=1)
    fat_percent.grid(row=7,column=2)

    ideal_weight.grid(row=8,column=0)
    bmi_actual.grid(row=8,column=1)
    fat_percent_actual.grid(row=8,column=2)
    
    status_bmi=tk.Label(text=stat,fg=color,bg="black").grid(row=9,column=1)
    
    msg_label=tk.Label(text=msg,fg=color,font=("times new roman",18,"bold")).grid(row=10,column=1)
    #res=messagebox.showinfo("BMI","Your BMI is "+str(bmi))

top=tk.Tk()
top.title("BMI Calculator",)
top.geometry("400x400")

age_label=tk.Label(text="Enter Your Age")
age_entry=tk.Entry(top)

gender_label=tk.Label(text="Select Your Gender")
gender_chosen=StringVar(top)
gender_chosen.set("Select")
gender_choice=ttk.Combobox(top,width=17,textvariable=gender_chosen)
gender_choice['values']=("Male","Female")

height_label=tk.Label(text="Enter your Height")
height_chosen=StringVar(top)
height_chosen.set("Select")
height_entry=Entry(top)
height_options=ttk.Combobox(top,width=10,textvariable=height_chosen)
height_options['values']=("Feet and Inches","Centimeters")

weight_label=tk.Label(text="Enter your Weight")
weight_chosen=StringVar(top)
weight_chosen.set("Select")
weight_entry=Entry(top)
weight_options=ttk.Combobox(top,width=10,textvariable=weight_chosen)
weight_options["values"]=("lbs","Kg")

calculate_button=Button(text="Calculate",command=calc)


age_label.grid(row=0,column=0)
age_entry.grid(row=0,column=1)
gender_label.grid(row=1,column=0)
gender_choice.grid(row=1,column=1)

height_label.grid(row=2,column=0)
height_entry.grid(row=2,column=1)
height_options.grid(row=2,column=2)
weight_label.grid(row=3,column=0)
weight_entry.grid(row=3,column=1)
weight_options.grid(row=3,column=2)

calculate_button.grid(row=6,column=1)


#top.configure(bg="white")

top.mainloop()
