# -*- coding: utf-8 -*-
from Tkinter import *
from datetime import date
from dateutil.relativedelta import relativedelta

root = Tk()
root.title("Escalafon - Calculadora")

canvas = Canvas(root, width=500, height=600)
canvas.grid(columnspan=7, rowspan=35)

date1_label = Label(root, text="Fec nombramiento ", anchor='e')
date1_label.grid(column=1, row=1, sticky=W+E)
date1_display = Entry(root)
date1_display.grid(column=2, row=1, sticky=W+E)
date1_display.focus()

date_fall_label = Label(root, text="Fec fallecimiento ", anchor='e')
date_fall_label.grid(column=3, row=1, sticky=W+E)
date_fall_display = Entry(root)
date_fall_display.grid(column=4, row=1, sticky=W+E)

penality_label = Label(root, text="Sanciones: ")
penality_label.grid(column=1, row=2, sticky=W+E)
penality_display = Entry(root)
penality_display.grid(column=2, row=2, sticky=W+E)
penality_label2 = Label(root, text="(DD/MM/YY)", anchor='w')
penality_label2.grid(column=3, row=2, sticky=W+E)

p1_label = Label(root, text="1.- Fecha Inicio ", anchor='e')
p1_label.grid(column=1, row=3, sticky=W+E)
p1_display = Entry(root)
p1_display.grid(column=2, row=3, sticky=W+E)

p2_label = Label(root, text="Fecha Fin ", anchor='e')
p2_label.grid(column=3, row=3, sticky=W+E)
p2_display = Entry(root)
p2_display.grid(column=4, row=3, sticky=W+E)

p3_label = Label(root, text="2.- Fecha Inicio ", anchor='e')
p3_label.grid(column=1, row=4, sticky=W+E)
p3_display = Entry(root)
p3_display.grid(column=2, row=4, sticky=W+E)

p4_label = Label(root, text="Fecha Fin ", anchor='e')
p4_label.grid(column=3, row=4, sticky=W+E)
p4_display = Entry(root)
p4_display.grid(column=4, row=4, sticky=W+E)

p5_label = Label(root, text="3.- Fecha Inicio ", anchor='e')
p5_label.grid(column=1, row=5, sticky=W+E)
p5_display = Entry(root)
p5_display.grid(column=2, row=5, sticky=W+E)

p6_label = Label(root, text="Fecha Fin ", anchor='e')
p6_label.grid(column=3, row=5, sticky=W+E)
p6_display = Entry(root)
p6_display.grid(column=4, row=5, sticky=W+E)

p7_label = Label(root, text="4.- Fecha Inicio ", anchor='e')
p7_label.grid(column=1, row=6, sticky=W+E)
p7_display = Entry(root)
p7_display.grid(column=2, row=6, sticky=W+E)

p8_label = Label(root, text="Fecha Fin ", anchor='e')
p8_label.grid(column=3, row=6, sticky=W+E)
p8_display = Entry(root)
p8_display.grid(column=4, row=6, sticky=W+E)

p9_label = Label(root, text="5.- Fecha Inicio ", anchor='e')
p9_label.grid(column=1, row=7, sticky=W+E)
p9_display = Entry(root)
p9_display.grid(column=2, row=7, sticky=W+E)

p10_label = Label(root, text="Fecha Fin ", anchor='e')
p10_label.grid(column=3, row=7, sticky=W+E)
p10_display = Entry(root)
p10_display.grid(column=4, row=7, sticky=W+E)

# CONTRATOS

contracts_label = Label(root, text="Contratos:")
contracts_label.grid(column=1, row=8, sticky=W+E)
contracts_display = Entry(root)
contracts_display.grid(column=2, row=8, sticky=W+E)
contracts_label2 = Label(root, text="(DD/MM/YY)", anchor='w')
contracts_label2.grid(column=3, row=8, sticky=W+E)

c1_label = Label(root, text="1.- Fecha Inicio ", anchor='e')
c1_label.grid(column=1, row=9, sticky=W+E)
c1_display = Entry(root)
c1_display.grid(column=2, row=9, sticky=W+E)

c2_label = Label(root, text="Fecha Fin ", anchor='e')
c2_label.grid(column=3, row=9, sticky=W+E)
c2_display = Entry(root)
c2_display.grid(column=4, row=9, sticky=W+E)

c3_label = Label(root, text="2.- Fecha Inicio ", anchor='e')
c3_label.grid(column=1, row=10, sticky=W+E)
c3_display = Entry(root)
c3_display.grid(column=2, row=10, sticky=W+E)

c4_label = Label(root, text="Fecha Fin ", anchor='e')
c4_label.grid(column=3, row=10, sticky=W+E)
c4_display = Entry(root)
c4_display.grid(column=4, row=10, sticky=W+E)

c5_label = Label(root, text="3.- Fecha Inicio ", anchor='e')
c5_label.grid(column=1, row=11, sticky=W+E)
c5_display = Entry(root)
c5_display.grid(column=2, row=11, sticky=W+E)

c6_label = Label(root, text="Fecha Fin ", anchor='e')
c6_label.grid(column=3, row=11, sticky=W+E)
c6_display = Entry(root)
c6_display.grid(column=4, row=11, sticky=W+E)

c7_label = Label(root, text="4.- Fecha Inicio ", anchor='e')
c7_label.grid(column=1, row=12, sticky=W+E)
c7_display = Entry(root)
c7_display.grid(column=2, row=12, sticky=W+E)

c8_label = Label(root, text="Fecha Fin ", anchor='e')
c8_label.grid(column=3, row=12, sticky=W+E)
c8_display = Entry(root)
c8_display.grid(column=4, row=12, sticky=W+E)

c9_label = Label(root, text="5.- Fecha Inicio ", anchor='e')
c9_label.grid(column=1, row=13, sticky=W+E)
c9_display = Entry(root)
c9_display.grid(column=2, row=13, sticky=W+E)

c10_label = Label(root, text="Fecha Fin ", anchor='e')
c10_label.grid(column=3, row=13, sticky=W+E)
c10_display = Entry(root)
c10_display.grid(column=4, row=13, sticky=W+E)

# LICENCIAS

license_label = Label(root, text="Licencias:")
license_label.grid(column=1, row=15, sticky=W+E)
license_display = Entry(root)
license_display.grid(column=2, row=15, sticky=W+E)
license_label2 = Label(root, text="(DD/MM/YY)", anchor='w')
license_label2.grid(column=3, row=15, sticky=W+E)

l1_label = Label(root, text="1.- Fecha Inicio ", anchor='e')
l1_label.grid(column=1, row=16, sticky=W+E)
l1_display = Entry(root)
l1_display.grid(column=2, row=16, sticky=W+E)

l2_label = Label(root, text="Fecha Fin ", anchor='e')
l2_label.grid(column=3, row=16, sticky=W+E)
l2_display = Entry(root)
l2_display.grid(column=4, row=16, sticky=W+E)

l3_label = Label(root, text="2.- Fecha Inicio ", anchor='e')
l3_label.grid(column=1, row=17, sticky=W+E)
l3_display = Entry(root)
l3_display.grid(column=2, row=17, sticky=W+E)

l4_label = Label(root, text="Fecha Fin ", anchor='e')
l4_label.grid(column=3, row=17, sticky=W+E)
l4_display = Entry(root)
l4_display.grid(column=4, row=17, sticky=W+E)

l5_label = Label(root, text="3.- Fecha Inicio ", anchor='e')
l5_label.grid(column=1, row=18, sticky=W+E)
l5_display = Entry(root)
l5_display.grid(column=2, row=18, sticky=W+E)

l6_label = Label(root, text="Fecha Fin ", anchor='e')
l6_label.grid(column=3, row=18, sticky=W+E)
l6_display = Entry(root)
l6_display.grid(column=4, row=18, sticky=W+E)

l7_label = Label(root, text="4.- Fecha Inicio ", anchor='e')
l7_label.grid(column=1, row=19, sticky=W+E)
l7_display = Entry(root)
l7_display.grid(column=2, row=19, sticky=W+E)

l8_label = Label(root, text="Fecha Fin ", anchor='e')
l8_label.grid(column=3, row=19, sticky=W+E)
l8_display = Entry(root)
l8_display.grid(column=4, row=19, sticky=W+E)

l9_label = Label(root, text="5.- Fecha Inicio ", anchor='e')
l9_label.grid(column=1, row=20, sticky=W+E)
l9_display = Entry(root)
l9_display.grid(column=2, row=20, sticky=W+E)

l10_label = Label(root, text="Fecha Fin ", anchor='e')
l10_label.grid(column=3, row=20, sticky=W+E)
l10_display = Entry(root)
l10_display.grid(column=4, row=20, sticky=W+E)

message_result = StringVar()
message_result_label = Label(root, textvariable=message_result, anchor='w')
message_result_label.grid(row=21, column=1, sticky=W+E, columnspan=4)

message_result2 = StringVar()
message_result2_label = Label(root, textvariable=message_result2, anchor='w')
message_result2_label.grid(row=22, column=1, sticky=W+E, columnspan=4)

message_result3 = StringVar()
message_result3_label = Label(root, textvariable=message_result3, anchor='w')
message_result3_label.grid(row=23, column=1, sticky=W+E, columnspan=4)

message_result4 = StringVar()
message_result4_label = Label(root, textvariable=message_result4, anchor='w')
message_result4_label.grid(row=24, column=1, sticky=W+E, columnspan=4)

message_result5 = StringVar()
message_result5_label = Label(root, textvariable=message_result5, anchor='w')
message_result5_label.grid(row=25, column=1, sticky=W+E, columnspan=4)

message_result6 = StringVar()
message_result6_label = Label(root, textvariable=message_result6, anchor='w')
message_result6_label.grid(row=26, column=1, sticky=W+E, columnspan=4)

message_result7 = StringVar()
message_result7_label = Label(root, textvariable=message_result7, anchor='w')
message_result7_label.grid(row=27, column=1, sticky=W+E, columnspan=4)

message_p1_days = StringVar()
message_p1_label = Label(root, textvariable=message_p1_days, anchor='w')
message_p1_label.grid(row=3, column=6, sticky=W+E)

message_p2_days = StringVar()
message_p2_label = Label(root, textvariable=message_p2_days, anchor='w')
message_p2_label.grid(row=4, column=6, sticky=W+E)

message_p3_days = StringVar()
message_p3_label = Label(root, textvariable=message_p3_days, anchor='w')
message_p3_label.grid(row=5, column=6, sticky=W+E)

message_p4_days = StringVar()
message_p4_label = Label(root, textvariable=message_p4_days, anchor='w')
message_p4_label.grid(row=6, column=6, sticky=W+E)

message_p5_days = StringVar()
message_p5_label = Label(root, textvariable=message_p5_days, anchor='w')
message_p5_label.grid(row=7, column=6, sticky=W+E)

message_c1_days = StringVar()
message_c1_label = Label(root, textvariable=message_c1_days, anchor='w')
message_c1_label.grid(row=9, column=6, sticky=W+E)

message_c2_days = StringVar()
message_c2_label = Label(root, textvariable=message_c2_days, anchor='w')
message_c2_label.grid(row=10, column=6, sticky=W+E)

message_c3_days = StringVar()
message_c3_label = Label(root, textvariable=message_c3_days, anchor='w')
message_c3_label.grid(row=11, column=6, sticky=W+E)

message_c4_days = StringVar()
message_c4_label = Label(root, textvariable=message_c4_days, anchor='w')
message_c4_label.grid(row=12, column=6, sticky=W+E)

message_c5_days = StringVar()
message_c5_label = Label(root, textvariable=message_c5_days, anchor='w')
message_c5_label.grid(row=13, column=6, sticky=W+E)

message_l1_days = StringVar()
message_l1_label = Label(root, textvariable=message_l1_days, anchor='w')
message_l1_label.grid(row=16, column=6, sticky=W+E)

message_l2_days = StringVar()
message_l2_label = Label(root, textvariable=message_l2_days, anchor='w')
message_l2_label.grid(row=17, column=6, sticky=W+E)

message_l3_days = StringVar()
message_l3_label = Label(root, textvariable=message_l3_days, anchor='w')
message_l3_label.grid(row=18, column=6, sticky=W+E)

message_l4_days = StringVar()
message_l4_label = Label(root, textvariable=message_l4_days, anchor='w')
message_l4_label.grid(row=19, column=6, sticky=W+E)

message_l5_days = StringVar()
message_l5_label = Label(root, textvariable=message_l5_days, anchor='w')
message_l5_label.grid(row=20, column=6, sticky=W+E)

def clear_all():
    date1_display.delete(0, 'end')
    date_fall_display.delete(0, 'end')

    penality_display.delete(0, 'end')
    p1_display.delete(0, 'end')
    p2_display.delete(0, 'end')
    p3_display.delete(0, 'end')
    p4_display.delete(0, 'end')
    p5_display.delete(0, 'end')
    p6_display.delete(0, 'end')
    p7_display.delete(0, 'end')
    p8_display.delete(0, 'end')
    p9_display.delete(0, 'end')
    p10_display.delete(0, 'end')

    contracts_display.delete(0, 'end')
    c1_display.delete(0, 'end')
    c2_display.delete(0, 'end')
    c3_display.delete(0, 'end')
    c4_display.delete(0, 'end')
    c5_display.delete(0, 'end')
    c6_display.delete(0, 'end')
    c7_display.delete(0, 'end')
    c8_display.delete(0, 'end')
    c9_display.delete(0, 'end')
    c10_display.delete(0, 'end')

    license_display.delete(0, 'end')
    l1_display.delete(0, 'end')
    l2_display.delete(0, 'end')
    l3_display.delete(0, 'end')
    l4_display.delete(0, 'end')
    l5_display.delete(0, 'end')
    l6_display.delete(0, 'end')
    l7_display.delete(0, 'end')
    l8_display.delete(0, 'end')
    l9_display.delete(0, 'end')
    l10_display.delete(0, 'end')


def formarter_date(input_date):
    if input_date:
        array_date = [int(x) for x in input_date.split('/')]
        return array_date # [dd, mm, yy]
    else: 
        return [0,0,0]

def calculate_time_of_service(date_today, date_user, date_fall):
    date_user = date_user - relativedelta(days=+1)
    if date_fall != [0,0,0]:
        difference = relativedelta(date_fall, date_user) 
    else:
        difference = relativedelta(date_today, date_user)

    return difference

def update_to_date(arr):
    try:
        date_format = date(arr[2], arr[1], arr[0])
        return date_format
    except:
        return [0,0,0]

def calculate_difference(date_begin, date_end):
    # Se empieza contando desde el dia indicado, sin embargo cuando se trata de meses se cuentan los meses   
    arr = [0,0,0]
    try:
        if date_begin.day == date_end.day:
            difference = relativedelta(date_end, date_begin)
            arr[0] = difference.days
            arr[1] = difference.months
            arr[2] = difference.years
        else:
            difference = relativedelta(date_end, date_begin)
            arr[0] = difference.days + 1
            arr[1] = difference.months
            arr[2] = difference.years
        return arr
    except:
        return arr

def calculate_difference_days(date_begin, date_end):
    try:
        date_diff = date_end - date_begin
        date_diff = int(date_diff.days) + 1
        return date_diff
    except:
        date_diff = 0
        return date_diff

def from_days_to_legix(days):
    arr = [0,0,0]
    years = int(days/365)
    tmp = days % 365
    months = int(tmp/30)
    days = tmp % 30
    arr = [days,months,years]

    return arr

def from_arr_to_days(arr):
    arr[2] = arr[2]*365
    arr[1] = arr[1]*30
    arr[0] = arr[0]*1

    total_days = arr[2] + arr[1] + arr[0]
    
    return total_days

def calculate_ats(button_years):
    try:
        today = date.today()

        ######Nombramiento y fallecimiento
        date_formated = formarter_date(date1_display.get())
        user_date = date(date_formated[2], date_formated[1], date_formated[0])

        date_fall_formated = formarter_date(date_fall_display.get())
        fall_date = update_to_date(date_fall_formated)
        ######END-Nombramiento y fallecimiento

        ######sanciones
        penal_formt = formarter_date(penality_display.get())
        
        #sancion1
        p1_formt = formarter_date(p1_display.get())
        p1_date = update_to_date(p1_formt)

        p2_formt = formarter_date(p2_display.get())
        p2_date = update_to_date(p2_formt)

        #sancion2
        p3_formt = formarter_date(p3_display.get())
        p3_date = update_to_date(p3_formt)

        p4_formt = formarter_date(p4_display.get())
        p4_date = update_to_date(p4_formt)

        #sancion3
        p5_formt = formarter_date(p5_display.get())
        p5_date = update_to_date(p5_formt)

        p6_formt = formarter_date(p6_display.get())
        p6_date = update_to_date(p6_formt)

        #sancion4
        p7_formt = formarter_date(p7_display.get())
        p7_date = update_to_date(p7_formt)

        p8_formt = formarter_date(p8_display.get())
        p8_date = update_to_date(p8_formt)

        #sancion5
        p9_formt = formarter_date(p9_display.get())
        p9_date = update_to_date(p9_formt)

        p10_formt = formarter_date(p10_display.get())
        p10_date = update_to_date(p10_formt)

        #calcular la diferencia de tiempo entre las fechas de SANCION
        g1 = calculate_difference(p1_date, p2_date)
        d_pen_days1 = calculate_difference_days(p1_date, p2_date)

        g2 = calculate_difference(p3_date, p4_date)
        d_pen_days2 = calculate_difference_days(p3_date, p4_date)

        g3 = calculate_difference(p5_date, p6_date)
        d_pen_days3 = calculate_difference_days(p5_date, p6_date)

        g4 = calculate_difference(p7_date, p8_date)
        d_pen_days4 = calculate_difference_days(p7_date, p8_date)

        g5 = calculate_difference(p9_date, p10_date)
        d_pen_days5 = calculate_difference_days(p9_date, p10_date)

        total_penal = [0,0,0]
        dif_total_pen_days = 0

        #Acumular por años, meses, dias
        total_penal[0] = g1[0] + g2[0] + g3[0] + g4[0] + g5[0] + penal_formt[0]
        total_penal[1] = g1[1] + g2[1] + g3[1] + g4[1] + g5[1] + penal_formt[1]
        total_penal[2] = g1[2] + g2[2] + g3[2] + g4[2] + g5[2] + penal_formt[2]

        #calcular todo a dias
        pen_input_count = from_arr_to_days(penal_formt)
        dif_total_pen_days = d_pen_days1 + d_pen_days2 + d_pen_days3 + d_pen_days4 + d_pen_days5 + pen_input_count
        pen_legix = from_days_to_legix(dif_total_pen_days)
        #######END-sanciones

        #######contratos
        contract_formt = formarter_date(contracts_display.get())
        
        #contrato1
        c1_formt = formarter_date(c1_display.get())
        c1_date = update_to_date(c1_formt)

        c2_formt = formarter_date(c2_display.get())
        c2_date = update_to_date(c2_formt)

        #contrato2
        c3_formt = formarter_date(c3_display.get())
        c3_date = update_to_date(c3_formt)

        c4_formt = formarter_date(c4_display.get())
        c4_date = update_to_date(c4_formt)

        #contrato3
        c5_formt = formarter_date(c5_display.get())
        c5_date = update_to_date(c5_formt)

        c6_formt = formarter_date(c6_display.get())
        c6_date = update_to_date(c6_formt)

        #contrato4
        c7_formt = formarter_date(c7_display.get())
        c7_date = update_to_date(c7_formt)

        c8_formt = formarter_date(c8_display.get())
        c8_date = update_to_date(c8_formt)

        #contrato5
        c9_formt = formarter_date(c9_display.get())
        c9_date = update_to_date(c9_formt)

        c10_formt = formarter_date(c10_display.get())
        c10_date = update_to_date(c10_formt)

        #calcular la diferencia de tiempo entre las fechas de CONTRATO
        f1 = calculate_difference(c1_date, c2_date)
        f_con_days1 = calculate_difference_days(c1_date, c2_date)

        f2 = calculate_difference(c3_date, c4_date)
        f_con_days2 = calculate_difference_days(c3_date, c4_date)
 
        f3 = calculate_difference(c5_date, c6_date)
        f_con_days3 = calculate_difference_days(c5_date, c6_date)

        f4 = calculate_difference(c7_date, c8_date)
        f_con_days4 = calculate_difference_days(c7_date, c8_date)

        f5 = calculate_difference(c9_date, c10_date)
        f_con_days5 = calculate_difference_days(c9_date, c10_date)

        f_total_con = [0,0,0]
        dif_total_con_days = 0

        #Acumular por años, meses, dias
        f_total_con[0] = f1[0] + f2[0] + f3[0] + f4[0] + f5[0] + contract_formt[0]
        f_total_con[1] = f1[1] + f2[1] + f3[1] + f4[1] + f5[1] + contract_formt[1]
        f_total_con[2] = f1[2] + f2[2] + f3[2] + f4[2] + f5[2] + contract_formt[2]

        #Calcular todo a dias
        con_input_count = from_arr_to_days(contract_formt)
        dif_total_con_days = f_con_days1 + f_con_days2 + f_con_days3 + f_con_days4 + f_con_days5 + con_input_count
        con_legix = from_days_to_legix(dif_total_con_days)
        ######END-contratos
        
        ######licencias
        license_formt = formarter_date(license_display.get())

        #licencia1
        l1_formt = formarter_date(l1_display.get())
        l1_date = update_to_date(l1_formt)

        l2_formt = formarter_date(l2_display.get())
        l2_date = update_to_date(l2_formt)

        #licencia2
        l3_formt = formarter_date(l3_display.get())
        l3_date = update_to_date(l3_formt)

        l4_formt = formarter_date(l4_display.get())
        l4_date = update_to_date(l4_formt)

        #licencia3
        l5_formt = formarter_date(l5_display.get())
        l5_date = update_to_date(l5_formt)

        l6_formt = formarter_date(l6_display.get())
        l6_date = update_to_date(l6_formt)

        #licencia4
        l7_formt = formarter_date(l7_display.get())
        l7_date = update_to_date(l7_formt)

        l8_formt = formarter_date(l8_display.get())
        l8_date = update_to_date(l8_formt)

        #licencia5
        l9_formt = formarter_date(l9_display.get())
        l9_date = update_to_date(l9_formt)

        l10_formt = formarter_date(l10_display.get())
        l10_date = update_to_date(l10_formt)

        #calcular la diferencia de tiempo entre las fechas de LICENCIA
        d1 = calculate_difference(l1_date, l2_date)
        d_lic_days1 = calculate_difference_days(l1_date, l2_date)

        d2 = calculate_difference(l3_date, l4_date)
        d_lic_days2 = calculate_difference_days(l3_date, l4_date)
 
        d3 = calculate_difference(l5_date, l6_date)
        d_lic_days3 = calculate_difference_days(l5_date, l6_date)

        d4 = calculate_difference(l7_date, l8_date)
        d_lic_days4 = calculate_difference_days(l7_date, l8_date)

        d5 = calculate_difference(l9_date, l10_date)
        d_lic_days5 = calculate_difference_days(l9_date, l10_date)

        d_total_lic = [0,0,0]
        dif_total_lic_days = 0

        #Acumular por años, meses, dias
        d_total_lic[0] = d1[0] + d2[0] + d3[0] + d4[0] + d5[0] + license_formt[0]
        d_total_lic[1] = d1[1] + d2[1] + d3[1] + d4[1] + d5[1] + license_formt[1]
        d_total_lic[2] = d1[2] + d2[2] + d3[2] + d4[2] + d5[2] + license_formt[2]

        #Calcular todo a dias
        lic_input_count = from_arr_to_days(license_formt)
        dif_total_lic_days = d_lic_days1 + d_lic_days2 + d_lic_days3 + d_lic_days4 + d_lic_days5 + lic_input_count
        lic_legix = from_days_to_legix(dif_total_lic_days)
        ######END-licencias
        
        ######Calculo de ats +Sancion +Licencias
        date_wpenal = user_date + relativedelta(years=+total_penal[2], months=+total_penal[1], days=+total_penal[0])
        date_wlicen_wpenal = date_wpenal + relativedelta(years=+d_total_lic[2], months=+d_total_lic[1], days=+d_total_lic[0])
        final_date = date_wlicen_wpenal + relativedelta(years=+button_years)
        
        ######Calculo de ats -Contratos
        date_wcontrac = final_date - relativedelta(years=+f_total_con[2], months=+f_total_con[1], days=+f_total_con[0])

        ######Calculo de tiempo de servicios
        tos = calculate_time_of_service(today, user_date, fall_date)
        tos_wcontrac = tos + relativedelta(years=+f_total_con[2], months=+f_total_con[1], days=+f_total_con[0])
 
        ######Mensajes de los calculos
        message_result.set('Calculo de '+ str(button_years) + ' años(desde nombramiento): ' + str(final_date.day) + '/' + str(final_date.month) + '/' + str(final_date.year))
        message_result2.set('-- Con contratos -- : ' + str(date_wcontrac.day) + '/' + str(date_wcontrac.month) + '/' + str(date_wcontrac.year))
        
        if fall_date == [0,0,0]:
            message_result3.set('Tiempo de servicios al ' + str(today.day) + '/' + str(today.month) + '/' + str(today.year) + '(desde nombramiento): ' + str(tos.years) + ' años, ' + str(tos.months) + ' meses, ' + str(tos.days) + ' dias')
        else:
            message_result3.set('Tiempo de servicios al ' + str(fall_date.day) + '/' + str(fall_date.month) + '/' + str(fall_date.year) + '(desde nombramiento): ' + str(tos.years) + ' años, ' + str(tos.months) + ' meses, ' + str(tos.days) + ' dias')

        message_result4.set('-- Con contratos --: ' + str(tos_wcontrac.years) + ' años, ' + str(tos_wcontrac.months) + ' meses, ' + str(tos_wcontrac.days) + ' dias')
        message_result5.set('Tiempo en sanciones: ' + str(total_penal[2]) + ' años, ' + str(total_penal[1]) + ' meses, ' + str(total_penal[0]) + ' dias' + ' // legix: ' + str(pen_legix[2]) + ' años, ' + str(pen_legix[1]) + ' meses, ' + str(pen_legix[0]) + ' dias //' + ' (' + str(dif_total_pen_days) + ') dias totales')
        message_result6.set('Tiempo en contratos: ' + str(f_total_con[2]) + ' años, ' + str(f_total_con[1]) + ' meses, ' + str(f_total_con[0]) + ' dias' + ' // legix: ' + str(con_legix[2]) + ' años, ' + str(con_legix[1]) + ' meses, ' + str(con_legix[0]) + ' dias //' + ' (' + str(dif_total_con_days) + ') dias totales')
        message_result7.set('Tiempo en licencias: ' + str(d_total_lic[2]) + ' años, ' + str(d_total_lic[1]) + ' meses, ' + str(d_total_lic[0]) + ' dias' + ' // legix: ' + str(lic_legix[2]) + ' años, ' + str(lic_legix[1]) + ' meses, ' + str(lic_legix[0]) + ' dias //' + ' (' + str(dif_total_lic_days) + ') dias totales')
    
        message_p1_days.set('' + str(d_pen_days1))
        message_p2_days.set('' + str(d_pen_days2))
        message_p3_days.set('' + str(d_pen_days3))
        message_p4_days.set('' + str(d_pen_days4))
        message_p5_days.set('' + str(d_pen_days5))

        message_c1_days.set('' + str(f_con_days1))
        message_c2_days.set('' + str(f_con_days2))
        message_c3_days.set('' + str(f_con_days3))
        message_c4_days.set('' + str(f_con_days4))
        message_c5_days.set('' + str(f_con_days5))

        message_l1_days.set('' + str(d_lic_days1))
        message_l2_days.set('' + str(d_lic_days2))
        message_l3_days.set('' + str(d_lic_days3))
        message_l4_days.set('' + str(d_lic_days4))
        message_l5_days.set('' + str(d_lic_days5))

    except Exception as e:
        message_result.set('La fecha ingresada es incorrecta, por favor ingresela de nuevo')

Button(root, text="Calcular 30 años", command=lambda:calculate_ats(30)).grid(row=28, column=2, sticky=W+E, columnspan=2)
Button(root, text="Calcular 25 años", command=lambda:calculate_ats(25)).grid(row=29, column=2, sticky=W+E, columnspan=2)
Button(root, text="Limpiar", command=lambda:clear_all()).grid(row=28, column=4, columnspan=1, rowspan=2)

root.mainloop()