import tkinter
from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)

def revisar_check():
    x = 0
    for c in cuadro_comida:
        if variable_comida[x].get() == 1:
            cuadro_comida[x].config(state=NORMAL)
            if cuadro_comida[x].get() == '0':
                cuadro_comida[x].delete(0,END)
            cuadro_comida[x].focus()
        else:
            cuadro_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1
    x = 0
    for c in cuadro_bebidas:
        if variable_bebidas[x].get() == 1:
            cuadro_bebidas[x].config(state=NORMAL)
            if cuadro_bebidas[x].get() == '0':
                cuadro_bebidas[x].delete(0,END)
            cuadro_bebidas[x].focus()
        else:
            cuadro_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1
    x = 0
    for c in cuadro_postres:
        if variable_postres[x].get() == 1:
            cuadro_postres[x].config(state=NORMAL)
            if cuadro_postres[x].get() == '0':
                cuadro_postres[x].delete(0,END)
            cuadro_postres[x].focus()
        else:
            cuadro_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


def total():
    sum_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sum_total_comida = sum_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
    print((sum_total_comida))

    sum_total_bebidas= 0
    p = 0
    for cantidad in texto_bebidas:
        sum_total_bebidas = sum_total_bebidas + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    print((sum_total_bebidas))

    sum_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sum_total_postres = sum_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1
    print((sum_total_postres))

    sub_total = sum_total_comida + sum_total_bebidas + sum_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sum_total_comida,2)}')
    var_costo_bebida.set(f'$ {round(sum_total_bebidas,2)}')
    var_costo_postre.set(f'$ {round(sum_total_postres,2)}')
    var_subtotal.set(f'$ {round(sub_total,2)}')
    var_impuesto.set(f'$ {round(impuestos,2)}')
    var_total.set(f'$ {round(total,2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year}'
    texto_recibo.insert(END, f'DATOS: \t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*'*47+'\n')
    texto_recibo.insert(END, 'Items\tCant\tCosto item\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comida[x]}\t\t{comida.get()}\t\t'
                                     f'${int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t\t'
                                     f'${int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t\t'
                                     f'${int(postre.get()) * precios_postres[x]}\n')
        x += 1
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuesto: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f' TOTAL: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('informacion','ashakjdhaksdh')


def resetear():
    texto_recibo.delete(0.1, END)
    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')
    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postres:
        cuadro.config(state=DISABLED)

    for v in variable_comida:
        v.set(0)
    for v in variable_bebidas:
        v.set(0)
    for v in variable_postres:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')
     




# Iniciar Tkinter

aplicacion = Tk()



# tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# Evitar maxim
aplicacion.resizable(0, 0)

# Titulo de la ventana
aplicacion.title("Restobar - Facturacion")

# Color de Fondo
aplicacion.config(bg='burlywood')

# Panel Superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiquerta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4', font=('Dosis', 58), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)


# Panel Izqueirro
panel_izquiero = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquiero.pack(side=LEFT)

# Panel Costos
panel_costo = Frame(panel_izquiero, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costo.pack(side=BOTTOM)

# Panel Comidas
panel_comidas = LabelFrame(panel_izquiero, text='Comida', font=('Dosis', 19), bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquiero, text='Bebidas', font=('Dosis', 19), bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# PAnel Postres
panel_postres = LabelFrame(panel_izquiero, text='Postres', font=('Dosis', 19), bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)


# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel Calculadora
panel_Calculador = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_Calculador.pack()

# Panel Recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel Botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

#Lsita de productos
lista_comida = ['pollo', 'pollo2', 'pollo3', 'pollo4',"tiramiso", 'flan', 'coca', 'fernet']
lista_bebidas = ['cerveza', ' agua', 'coca', 'fernet', 'pollo2', 'pollo3', 'pollo4', "tiramiso"]
lista_postres = ["tiramiso", 'flan', ' agua', 'coca', 'fernet', 'pollo2', 'pollo3', 'pollo4']

#generar items comida
variable_comida= []
cuadro_comida = []
texto_comida = []
contador = 0

for comida in lista_comida:

    # Crear Check button
    variable_comida.append('')
    variable_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadro_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadro_comida[contador] = Entry(panel_comidas,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador])
    cuadro_comida[contador].grid(row=contador,
                                 column=1)

    contador += 1

#generar items bebidas
variable_bebidas= []
cuadro_bebidas = []
texto_bebidas = []
contador = 0

for bebidas in lista_bebidas:

    # Crear Check button
    variable_bebidas.append('')
    variable_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas,
                          text=bebidas.title(),
                          font=('Dosis', 19),
                          onvalue=1,
                          offvalue=0,
                          variable=variable_bebidas[contador],
                          command=revisar_check)
    bebidas.grid(row=contador,
                 column=0,
                 sticky=W)

    # crear los cuadros de entrada
    cuadro_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadro_bebidas[contador] = Entry(panel_bebidas,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_bebidas[contador])
    cuadro_bebidas[contador].grid(row=contador,
                                 column=1)

    contador += 1


#generar items postres
variable_postres= []
cuadro_postres = []
texto_postres = []
contador = 0

for postres in lista_postres:

    # Crear Check button
    variable_postres.append('')
    variable_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=('Dosis', 19),
                          onvalue=1,
                          offvalue=0,
                          variable=variable_postres[contador],
                          command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # crear los cuadros de entrada
    cuadro_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadro_postres[contador] = Entry(panel_postres,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_postres[contador])
    cuadro_postres[contador].grid(row=contador,
                                 column=1)

    contador += 1

# Variable
var_costo_comida= StringVar()
var_costo_bebida= StringVar()
var_costo_postre= StringVar()
var_subtotal= StringVar()
var_impuesto= StringVar()
var_total= StringVar()


# etiquetas costo de las comidas y campos de entrada

etiqueta_costo_comida = Label(panel_costo,
                              text= 'costo comida',
                              font= ('dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costo,
                           font= ('dosis', 12, 'bold'),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_costo_comida)
texto_costo_comida.grid(row= 0, column= 1, padx=41)



# etiquetas costo de las comidabebidapos de entrada

etiqueta_costo_bebida = Label(panel_costo,
                              text= 'costo bebida',
                              font= ('dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costo,
                           font= ('dosis', 12, 'bold'),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_costo_bebida)
texto_costo_bebida.grid(row= 1, column= 1, padx=41)



# etiquetas costo de las postre campos de entrada

etiqueta_costo_postre = Label(panel_costo,
                              text= 'costo postre',
                              font= ('dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costo,
                           font= ('dosis', 12, 'bold'),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_costo_postre)
texto_costo_postre.grid(row= 2, column= 1, padx=41)

# etiquetas subtotal

etiqueta_subtotal = Label(panel_costo,
                              text= 'subtotal',
                              font= ('dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costo,
                           font= ('dosis', 12, 'bold'),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_subtotal)
texto_subtotal.grid(row= 0, column= 3, padx=41)

# etiquetas impuesto

etiqueta_impuesto = Label(panel_costo,
                              text= 'impuesto',
                              font= ('dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costo,
                           font= ('dosis', 12, 'bold'),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_impuesto)
texto_impuesto.grid(row= 1, column= 3, padx=41)

# etiquetas total

etiqueta_total = Label(panel_costo,
                              text= 'total',
                              font= ('dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costo,
                           font= ('dosis', 12, 'bold'),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_total)
texto_total.grid(row= 2, column= 3, padx=41)


# ARmar Botones
botones =['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columna = 0
for boton in botones:
    boton = Button(panel_botones,
                   text= boton.title(),
                   font= ('dosis', 14, 'bold'),
                   fg= 'white',
                   bg='azure4',
                   bd=1,
                   width=9)

    botones_creados.append((boton))
    boton.grid(row=0,
               column = columna)
    columna += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)





# Area REcibo
texto_recibo = Text(panel_recibo,
                    font= ('dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column = 0)


# Calculadora
visor_calculadora = Entry(panel_Calculador,
                          font= ('dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column = 0,
                       columnspan=4)

botones_calculadora = [ '7','8','9','+','4','5','6','-','3','2','1','x','R','B','0','/']

botones_guardados = []


fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_Calculador,
                   text=boton.title(),
                   font= ('dosis', 14, 'bold'),
                   bd=1,
                   fg='white',
                   bg='azure4',
                   width=9)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('3'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('1'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))
botones_guardados[13].config(command=borrar)
botones_guardados[12].config(command=obtener_resultado)






























# Evitar que se cierre
aplicacion.mainloop()