from cgitb import text
from genericpath import exists
from sys import displayhook
from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox
import os
import tkinter as tk
import json
import time
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from turtle import bgcolor, width
import tkinter.ttk
import tkinter.font as font
from click import command

def guardar():
        pacientes = {}
        pacientes = []

        pacientes.append(
                    {
                    "Nombre y Apellido": nombre.get(),
                    "Enf. Respiratorias" : f"{agreementa.get()}, {enfrespiratorias.get()}",
                    "Enf. Cardiacas" : f"{agreementb.get()}, {enfcardiacas.get()}",
                    "Enf. Alergicas" : f"{agreementc.get()}, {enfalegicas.get()}",
                    "Enf. Autoinmunes" : f"{agreementd.get()}, {enfautoinmunes.get()}",
                    "Enf. Renales" : f"{agreemente.get()}, {enfrenales.get()}",
                    "Cirugias Previas" : f"{agreementf.get()}, {cirugiasprevias.get()}",
                    "Motivo de Consulta" : f"{motivoc.get()}",
                    "18" :f"Palatino: {e18p.get()}, Vestibular: {e18v.get()}, Oclusal: {e18o.get()}. Mesial: {e18m.get()}, Distal: {e18d.get()}"
        
                    }
        )
        verificar = os.path.exists('./grupopacientes')
        if verificar == True:
            fileName = f"C:/Users/diego/Desktop/ProgrmacionPhyton/consultorio/pacientes/grupopacientes/{nombre.get()}.json"
            isarchivo = os.path.isfile(fileName)
            if isarchivo == True:
                with open(f'grupopacientes/{nombre.get()}.json','w') as document:
                        json.dump(pacientes, document, indent=3)
                        messagebox.showinfo("Informacion","Se ha actualizado el paciente correctamente")
            else:
                with open(f'grupopacientes/{nombre.get()}.json','w') as document:
                        json.dump(pacientes, document, indent=3)
                        messagebox.showinfo("Informacion","Se ha añadido el paciente correctamente")

        else:
            directorio = "grupopacientes"
  
            # Parent Directory path
            parent_dir = "C:/Users/diego/Desktop/ProgrmacionPhyton/consultorio/pacientes"
            
            # Path
            path = os.path.join(parent_dir, directorio)
            
            # Create the directory
            # 'GeeksForGeeks' in
            # '/home / User / Documents'
            os.mkdir(path)
            messagebox.showinfo("Informacion","La Carpeta no existia, se ha creado y se ha añadido el Paciente")
            with open(f'grupopacientes/{nombre.get()}.json','w') as document:
                    json.dump(pacientes, document, indent=3)
                    messagebox.showinfo("Informacion","Se ha añadido el paciente correctamente")

def back_to_main():
        global current_frame
        current_frame.pack_forget()
        inicio.pack()
        current_frame = inicio             
    
def show_datos_filiatorios():  
        global current_frame
        current_frame.pack_forget()
        datosfiliatorios_frame.pack()
        current_frame = datosfiliatorios_frame

def show_motivo_consulta():
        global current_frame
        current_frame.pack_forget()
        motivoconsulta_frame.pack()
        current_frame = motivoconsulta_frame

def show_antecedentes_patologicos():  
        global current_frame
        current_frame.pack_forget()
        antecedentes_patologicos_frame.pack()
        current_frame = antecedentes_patologicos_frame

def show_odontograma():
        global current_frame
        current_frame.pack_forget()
        odontograma_frame.pack()
        current_frame = odontograma_frame

def create_datos_filiatorios():
        global nombre
        nombre = StringVar()
        global edad
        edad = StringVar()
        global direccion
        direccion = StringVar()
        global ocupacion
        ocupacion = StringVar()
        global obrasocial
        obrasocial = StringVar()

        datos_filiatorios = ttk.Button(datosfiliatorios_frame, text="Datos Filiatorios")
        datos_filiatorios.grid(row=0, column=1, pady=5)
        
        label_base_input = ttk.Label(datosfiliatorios_frame,text=" Nombre y Apellido")
        label_base_input.grid(row=1, column=1,sticky=W, pady=5)

        entry_base_input = ttk.Entry(datosfiliatorios_frame,textvariable=nombre, width= 21)
        entry_base_input.grid(row=2, column=1,sticky=N,pady=5, padx= 3)

        edadL = ttk.Label(datosfiliatorios_frame,text=" Edad")
        edadL.grid(row=3, column=1,sticky=W, pady=5)

        edadE = ttk.Entry(datosfiliatorios_frame,textvariable=edad, width= 21)
        edadE.grid(row=4, column=1,sticky=N,pady=5, padx= 3)

        direccionL = ttk.Label(datosfiliatorios_frame,text=" Direccion")
        direccionL.grid(row=5, column=1,sticky=W, pady=5)

        direccionE = ttk.Entry(datosfiliatorios_frame,textvariable=direccion, width= 21)
        direccionE.grid(row=6, column=1,sticky=N,pady=5, padx= 3)

        ocupacionL = ttk.Label(datosfiliatorios_frame,text=" Ocupacion")
        ocupacionL.grid(row=7, column=1,sticky=W, pady=5)

        ocupacionE = ttk.Entry(datosfiliatorios_frame,textvariable=ocupacion, width= 21)
        ocupacionE.grid(row=8, column=1,sticky=N,pady=5, padx= 3)

        obrasocialL = ttk.Label(datosfiliatorios_frame,text=" Obra Social")
        obrasocialL.grid(row=9, column=1,sticky=W, pady=5)

        obrasocialE = ttk.Entry(datosfiliatorios_frame,textvariable=obrasocial, width= 21)
        obrasocialE.grid(row=10, column=1,sticky=N,pady=5, padx= 3)

        ttk.Button(datosfiliatorios_frame, text="Back", command=back_to_main).grid(row=11,column=1,sticky=N,pady=5, padx= 3)

        return nombre

def create_motivo_consulta():
            #Motivo de Consulta
        global motivoc
        motivoc = StringVar()

        motivo_de_consultaTitle = ttk.Button(motivoconsulta_frame, text="---------------------")
        motivo_de_consultaTitle.grid(row=0, column=3, sticky=W, pady=5)

        motivo_de_consultaL = ttk.Label(motivoconsulta_frame, text="Motivo de consulta")
        motivo_de_consultaL.grid(row=1, column=3, sticky=W, pady=5)

        motivo_de_consultaE = ttk.Entry(motivoconsulta_frame,textvariable=motivoc, width= 21,)
        motivo_de_consultaE.grid(row=2, column=3,sticky=N,pady=5, padx= 3)

        ttk.Button(motivoconsulta_frame, text="Back", command=back_to_main).grid(row=11,column=3,sticky=S,pady=5, padx= 3)


def create_antecedentes_patologicos():
        global agreementa
        agreementa = tk.StringVar()
        agreementa.set('No')
        global agreementb
        agreementb = tk.StringVar()
        agreementb.set('No')
        global agreementc
        agreementc = tk.StringVar()
        agreementc.set('No')
        global agreementd
        agreementd = tk.StringVar()
        agreementd.set('No')
        global agreemente
        agreemente = tk.StringVar()
        agreemente.set('No')
        global agreementf
        agreementf = tk.StringVar()
        agreementf.set('No')

        enfermedades = ttk.Button(antecedentes_patologicos_frame, text="Enfermedades Previas")
        enfermedades.grid(row=0, column=4, pady=5)

        global enfrespiratorias
        global enfcardiacas
        global enfautoinmunes
        global enfrenales
        global enfalegicas
        global cirugiasprevias    

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Enf. Respiratorias")
        label_base_input.grid(row=1, column=4,sticky=W,pady=10)
        a = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreementa,
                        variable=agreementa,
                        onvalue='Si',
                        offvalue='No',
                         ).grid(row=1, column=5,sticky=W)

        enfrespiratorias = StringVar()
        addEntrya = ttk.Entry(antecedentes_patologicos_frame,textvariable=enfrespiratorias, width= 21)
        addEntrya.grid(row=2, column=4,sticky=S, pady=5, padx= 3)

        #Añadir Enf. Cardiacas

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Enf. Cardiacas")
        label_base_input.grid(row=3, column=4,sticky=W,pady=10)
        b = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreementb,
                        variable=agreementb,
                        onvalue='Si',
                        offvalue='No',
                        ).grid(row=3, column=5,sticky=W)
        enfcardiacas = StringVar()
        addEntryb = ttk.Entry(antecedentes_patologicos_frame,textvariable=enfcardiacas, width= 21)
        addEntryb.grid(row=4, column=4,sticky=S, pady=5, padx= 3)

        #Añadir Enf. Alergicas

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Enf. Alergicas")
        label_base_input.grid(row=5, column=4,sticky=W,pady=5)
        c = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreementc,
                        variable=agreementc,
                        onvalue='Si',
                        offvalue='No',
                         ).grid(row=5, column=5,sticky=W)
        enfalegicas = StringVar()
        addEntryc = ttk.Entry(antecedentes_patologicos_frame,textvariable=enfalegicas, width= 21)
        addEntryc.grid(row=6, column=4,sticky=S, pady=5, padx= 3)

        #Añadir Enf. Autoinmunes 

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Enf. Autoinmunes")
        label_base_input.grid(row=7, column=4,sticky=W, pady=10)
        d = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreementd,
                        variable=agreementd,
                        onvalue='Si',
                        offvalue='No',
                         ).grid(row=7, column=5,sticky=W)
        enfautoinmunes = StringVar()
        addEntryd = ttk.Entry(antecedentes_patologicos_frame,textvariable=enfautoinmunes, width= 21)
        addEntryd.grid(row=8, column=4,sticky=S, pady=5, padx= 3)

        #Añadir Enf. Renales

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Enf. Renales")
        label_base_input.grid(row=9, column=4,sticky=W, pady=10)
        e = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreemente,
                        variable=agreemente,
                        onvalue='Si',
                        offvalue='No',
                         ).grid(row=9, column=5,sticky=W)
        
        enfrenales = StringVar()
        addEntrye = ttk.Entry(antecedentes_patologicos_frame,textvariable=enfrenales, width= 21)
        addEntrye.grid(row=10, column=4,sticky=S, pady=5, padx= 3)

        #Añadir Cirugias Previas

        label_base_input = ttk.Label(antecedentes_patologicos_frame,text=" Cirugias Previas")
        label_base_input.grid(row=11, column=4,sticky=W, pady=10)
        f = ttk.Checkbutton(antecedentes_patologicos_frame,
                        command=agreementf,
                        variable=agreementf,
                        onvalue='Si',
                        offvalue='No',
                         ).grid(row=11, column=5,sticky=W)
        
        cirugiasprevias = StringVar()
        addEntryf = ttk.Entry(antecedentes_patologicos_frame,textvariable=cirugiasprevias, width= 21)
        addEntryf.grid(row=12, column=4,sticky=S, pady=5, padx= 3)    

        ttk.Button(antecedentes_patologicos_frame, text="Back", command=back_to_main).grid(row=13,column=4,sticky=N,pady=5, padx= 3)



def create_odontograma():
    #Odontograma
        global e18d
        global e18o
        global e18m
        global e18v
        global e18p

        patologias = ttk.Combobox(odontograma_frame)
        patologias.grid(row=10,column=37)
        patologias["values"] = ["Caries", "Endodoncia", "Exodoncia", "Corona", "Puente"]

        e18d = tk.StringVar()
        e18d.set('Sano')
        e18o = tk.StringVar()
        e18m = tk.StringVar()
        e18v = tk.StringVar()
        e18p = tk.StringVar()

        elemento18L = ttk.Label(odontograma_frame, text="18")
        elemento18L.grid(column=7, row=1)
        elemento18D = ttk.Checkbutton(odontograma_frame, width=0, variable=e18d, offvalue=f'Sano', onvalue=f'{patologias}')
        elemento18D.grid(column=6, row=3)
        elemento18O = ttk.Checkbutton(odontograma_frame, width=0,offvalue=f'Sano', onvalue=f'{e18o}')
        elemento18O.grid(column=7, row=3, padx= 1)
        elemento18M = ttk.Checkbutton(odontograma_frame, width=0,offvalue=f'Sano', onvalue=f'{e18m}')
        elemento18M.grid(column=8, row=3)
        elemento18V = ttk.Checkbutton(odontograma_frame, width=0,offvalue=f'Sano', onvalue=f'{e18v}')
        elemento18V.grid(column=7, row=2)
        elemento18P = ttk.Checkbutton(odontograma_frame, width=0,offvalue=f'Sano', onvalue=f'{e18p}')
        elemento18P.grid(column=7, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=9,row=2, rowspan=3, sticky='ns', padx= 3)

        global e17d
        global e17o
        global e17m
        global e17v
        global e17p
        
        e17d = tk.StringVar()
        e17o = tk.StringVar()
        e17m = tk.StringVar()
        e17v = tk.StringVar()
        e17p = tk.StringVar()


        elemento17L = ttk.Label(odontograma_frame, text="17")
        elemento17L.grid(column=11, row=1)

        elemento17D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento17D.grid(column=10, row=3)
        elemento17O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento17O.grid(column=11, row=3, padx= 3)
        elemento17M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento17M.grid(column=12, row=3, )
        elemento17V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento17V.grid(column=11, row=2)
        elemento17P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento17P.grid(column=11, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=13,row=2, rowspan=3, sticky='ns', padx= 3)

        global e16d
        global e16o
        global e16m
        global e16v
        global e16p
        
        e16d = tk.StringVar()
        e16o = tk.StringVar()
        e16m = tk.StringVar()
        e16v = tk.StringVar()
        e16p = tk.StringVar()

        elemento16L = ttk.Label(odontograma_frame, text="16")
        elemento16L.grid(column=15, row=1)

        elemento16D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento16D.grid(column=14, row=3)
        elemento16O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento16O.grid(column=15, row=3, padx= 3)
        elemento16M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento16M.grid(column=16, row=3)
        elemento16V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento16V.grid(column=15, row=2)
        elemento16P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento16P.grid(column=15, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=17,row=2, rowspan=3, sticky='ns', padx= 3)

        global e15d
        global e15o
        global e15m
        global e15v
        global e15p
        
        e15d = tk.StringVar()
        e15o = tk.StringVar()
        e15m = tk.StringVar()
        e15v = tk.StringVar()
        e15p = tk.StringVar()    

        elemento15L = ttk.Label(odontograma_frame, text="15")
        elemento15L.grid(column=19, row=1)

        elemento15D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento15D.grid(column=18, row=3)
        elemento15O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento15O.grid(column=19, row=3, padx= 3)
        elemento15M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento15M.grid(column=20, row=3)
        elemento15V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento15V.grid(column=19, row=2)
        elemento15P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento15P.grid(column=19, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=21,row=2, rowspan=3, sticky='ns', padx= 3)

        global e14d
        global e14o
        global e14m
        global e14v
        global e14p
        
        e14d = tk.StringVar()
        e14o = tk.StringVar()
        e14m = tk.StringVar()
        e14v = tk.StringVar()
        e14p = tk.StringVar()

        elemento14L = ttk.Label(odontograma_frame, text="14")
        elemento14L.grid(column=23, row=1)

        elemento14D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento14D.grid(column=22, row=3)
        elemento14O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento14O.grid(column=23, row=3, padx= 3)
        elemento14M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento14M.grid(column=24, row=3)
        elemento14V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento14V.grid(column=23, row=2)
        elemento14P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento14P.grid(column=23, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=25,row=2, rowspan=3, sticky='ns', padx= 3)

        global e13d
        global e13o
        global e13m
        global e13v
        global e13p
        
        e13d = tk.StringVar()
        e13o = tk.StringVar()
        e13m = tk.StringVar()
        e13v = tk.StringVar()
        e13p = tk.StringVar()

        elemento13L = ttk.Label(odontograma_frame, text="13")
        elemento13L.grid(column=27, row=1)

        elemento13D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento13D.grid(column=26, row=3)
        elemento13O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento13O.grid(column=27, row=3, padx= 3)
        elemento13M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento13M.grid(column=28, row=3)
        elemento13V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento13V.grid(column=27, row=2)
        elemento13P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento13P.grid(column=27, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=29,row=2, rowspan=3, sticky='ns', padx= 3)

        global e12d
        global e12o
        global e12m
        global e12v
        global e12p
        
        e12d = tk.StringVar()
        e12o = tk.StringVar()
        e12m = tk.StringVar()
        e12v = tk.StringVar()
        e12p = tk.StringVar()

        elemento12L = ttk.Label(odontograma_frame, text="12")
        elemento12L.grid(column=31, row=1)

        elemento12D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento12D.grid(column=30, row=3)
        elemento12O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento12O.grid(column=31, row=3, padx= 3)
        elemento12M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento12M.grid(column=32, row=3)
        elemento12V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento12V.grid(column=31, row=2)
        elemento12P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento12P.grid(column=31, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=33,row=2, rowspan=3, sticky='ns', padx= 3)

        global e11d
        global e11o
        global e11m
        global e11v
        global e11p
        
        e11d = tk.StringVar()
        e11o = tk.StringVar()
        e11m = tk.StringVar()
        e11v = tk.StringVar()
        e11p = tk.StringVar()

        elemento11L = ttk.Label(odontograma_frame, text="11")
        elemento11L.grid(column=35, row=1)

        elemento11D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento11D.grid(column=34, row=3)
        elemento11O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento11O.grid(column=35, row=3, padx= 3)
        elemento11M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento11M.grid(column=36, row=3)
        elemento11V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento11V.grid(column=35, row=2)
        elemento11P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento11P.grid(column=35, row=4)

        #Sector 2

        elemento21L = ttk.Label(odontograma_frame, text="21")
        elemento21L.grid(column=41, row=1)


        elemento21M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento21M.grid(column=40, row=3)
        elemento21O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento21O.grid(column=41, row=3, padx= 3)
        elemento21D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento21D.grid(column=42, row=3)
        elemento21V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento21V.grid(column=41, row=2)
        elemento21P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento21P.grid(column=41, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=43,row=2, rowspan=3, sticky='ns', padx= 3)

        elemento22L = ttk.Label(odontograma_frame, text="22")
        elemento22L.grid(column=45, row=1)


        elemento22M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento22M.grid(column=44, row=3)
        elemento22O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento22O.grid(column=45, row=3, padx= 3)
        elemento22D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento22D.grid(column=46, row=3)
        elemento22V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento22V.grid(column=45, row=2)
        elemento22P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento22P.grid(column=45, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=47,row=2, rowspan=3, sticky='ns', padx= 3)

        elemento23L = ttk.Label(odontograma_frame, text="23")
        elemento23L.grid(column=50, row=1)


        elemento23M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento23M.grid(column=49, row=3)
        elemento23O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento23O.grid(column=50, row=3, padx= 3)
        elemento23D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento23D.grid(column=51, row=3)
        elemento23V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento23V.grid(column=50, row=2)
        elemento23P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento23P.grid(column=50, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=52,row=2, rowspan=3, sticky='ns', padx= 3)

        elemento24L = ttk.Label(odontograma_frame, text="24")
        elemento24L.grid(column=54, row=1)


        elemento24M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento24M.grid(column=53, row=3)
        elemento24O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento24O.grid(column=54, row=3, padx= 3)
        elemento24D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento24D.grid(column=55, row=3)
        elemento24V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento24V.grid(column=54, row=2)
        elemento24P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento24P.grid(column=54, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=56,row=2, rowspan=3, sticky='ns', padx= 3)

        elemento25L = ttk.Label(odontograma_frame, text="25")
        elemento25L.grid(column=58, row=1)


        elemento25M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento25M.grid(column=57, row=3)
        elemento25O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento25O.grid(column=58, row=3, padx= 3)
        elemento25D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento25D.grid(column=59, row=3)
        elemento25V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento25V.grid(column=58, row=2)
        elemento25P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento25P.grid(column=58, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=60,row=2, rowspan=3, sticky='ns', padx= 3)

        elemento26L = ttk.Label(odontograma_frame, text="26")
        elemento26L.grid(column=62, row=1)


        elemento26M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento26M.grid(column=61, row=3)
        elemento26O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento26O.grid(column=62, row=3, padx= 3)
        elemento26D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento26D.grid(column=63, row=3)
        elemento26V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento26V.grid(column=62, row=2)
        elemento26P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento26P.grid(column=62, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=64,row=2, rowspan=3, sticky='ns', padx= 3)

        elemento27L = ttk.Label(odontograma_frame, text="27")
        elemento27L.grid(column=66, row=1)


        elemento27M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento27M.grid(column=65, row=3)
        elemento27O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento27O.grid(column=66, row=3, padx= 3)
        elemento27D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento27D.grid(column=67, row=3)
        elemento27V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento27V.grid(column=66, row=2)
        elemento27P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento27P.grid(column=66, row=4)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=68,row=2, rowspan=3, sticky='ns', padx= 3)

        elemento28L = ttk.Label(odontograma_frame, text="28")
        elemento28L.grid(column=70, row=1)


        elemento28M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento28M.grid(column=69, row=3)
        elemento28O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento28O.grid(column=70, row=3, padx= 3)
        elemento28D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento28D.grid(column=71, row=3)
        elemento28V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento28V.grid(column=70, row=2)
        elemento28P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento28P.grid(column=70, row=4)


        elemento48L = ttk.Label(odontograma_frame, text="48")
        elemento48L.grid(column=7, row=5)

        elemento48D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento48D.grid(column=6, row=7)
        elemento48O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento48O.grid(column=7, row=7, padx= 3)
        elemento48M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento48M.grid(column=8, row=7)
        elemento48V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento48V.grid(column=7, row=6)
        elemento48P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento48P.grid(column=7, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=9,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento47L = ttk.Label(odontograma_frame, text="47")
        elemento47L.grid(column=11, row=5)

        elemento47D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento47D.grid(column=10, row=7)
        elemento47O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento47O.grid(column=11, row=7, padx= 3)
        elemento47M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento47M.grid(column=12, row=7, )
        elemento47V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento47V.grid(column=11, row=6)
        elemento47P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento47P.grid(column=11, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=13,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento46L = ttk.Label(odontograma_frame, text="46")
        elemento46L.grid(column=15, row=5)

        elemento46D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento46D.grid(column=14, row=7)
        elemento46O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento46O.grid(column=15, row=7, padx= 3)
        elemento46M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento46M.grid(column=16, row=7)
        elemento46V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento46V.grid(column=15, row=6)
        elemento46P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento46P.grid(column=15, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=17,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento45L = ttk.Label(odontograma_frame, text="45")
        elemento45L.grid(column=19, row=5)

        elemento45D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento45D.grid(column=18, row=7)
        elemento45O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento45O.grid(column=19, row=7, padx= 3)
        elemento45M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento45M.grid(column=20, row=7)
        elemento45V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento45V.grid(column=19, row=6)
        elemento45P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento45P.grid(column=19, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=21,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento44L = ttk.Label(odontograma_frame, text="44")
        elemento44L.grid(column=23, row=5)

        elemento44D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento44D.grid(column=22, row=7)
        elemento44O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento44O.grid(column=23, row=7, padx= 3)
        elemento44M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento44M.grid(column=24, row=7)
        elemento44V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento44V.grid(column=23, row=6)
        elemento44P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento44P.grid(column=23, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=25,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento43L = ttk.Label(odontograma_frame, text="43")
        elemento43L.grid(column=27, row=5)

        elemento43D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento43D.grid(column=26, row=7)
        elemento43O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento43O.grid(column=27, row=7, padx= 3)
        elemento43M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento43M.grid(column=28, row=7)
        elemento43V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento43V.grid(column=27, row=6)
        elemento43P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento43P.grid(column=27, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=29,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento42L = ttk.Label(odontograma_frame, text="42")
        elemento42L.grid(column=31, row=5)

        elemento42D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento42D.grid(column=30, row=7)
        elemento42O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento42O.grid(column=31, row=7, padx= 3)
        elemento42M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento42M.grid(column=32, row=7)
        elemento42V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento42V.grid(column=31, row=6)
        elemento42P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento42P.grid(column=31, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=33,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento41L = ttk.Label(odontograma_frame, text="41")
        elemento41L.grid(column=35, row=5)

        elemento41D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento41D.grid(column=34, row=7)
        elemento41O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento41O.grid(column=35, row=7, padx= 3)
        elemento41M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento41M.grid(column=36, row=7)
        elemento41V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento41V.grid(column=35, row=6)
        elemento41P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento41P.grid(column=35, row=8)

        #Sector 2

        elemento31L = ttk.Label(odontograma_frame, text="31")
        elemento31L.grid(column=41, row=5)


        elemento31M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento31M.grid(column=40, row=7)
        elemento31O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento31O.grid(column=41, row=7, padx= 3)
        elemento31D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento31D.grid(column=42, row=7)
        elemento31V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento31V.grid(column=41, row=6)
        elemento31P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento31P.grid(column=41, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=43,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento32L = ttk.Label(odontograma_frame, text="32")
        elemento32L.grid(column=45, row=5)


        elemento32M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento32M.grid(column=44, row=7)
        elemento32O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento32O.grid(column=45, row=7, padx= 3)
        elemento32D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento32D.grid(column=46, row=7)
        elemento32V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento32V.grid(column=45, row=6)
        elemento32P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento32P.grid(column=45, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=47,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento33L = ttk.Label(odontograma_frame, text="33")
        elemento33L.grid(column=50, row=5)


        elemento33M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento33M.grid(column=49, row=7)
        elemento33O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento33O.grid(column=50, row=7, padx= 3)
        elemento33D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento33D.grid(column=51, row=7)
        elemento33V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento33V.grid(column=50, row=6)
        elemento33P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento33P.grid(column=50, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=52,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento34L = ttk.Label(odontograma_frame, text="34")
        elemento34L.grid(column=54, row=5)


        elemento34M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento34M.grid(column=53, row=7)
        elemento34O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento34O.grid(column=54, row=7, padx= 3)
        elemento34D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento34D.grid(column=55, row=7)
        elemento34V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento34V.grid(column=54, row=6)
        elemento34P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento34P.grid(column=54, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=56,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento35L = ttk.Label(odontograma_frame, text="35")
        elemento35L.grid(column=58, row=5)


        elemento35M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento35M.grid(column=57, row=7)
        elemento35O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento35O.grid(column=58, row=7, padx= 3)
        elemento35D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento35D.grid(column=59, row=7)
        elemento35V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento35V.grid(column=58, row=6)
        elemento35P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento35P.grid(column=58, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=60,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento36L = ttk.Label(odontograma_frame, text="36")
        elemento36L.grid(column=62, row=5)


        elemento36M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento36M.grid(column=61, row=7)
        elemento36O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento36O.grid(column=62, row=7, padx= 3)
        elemento36D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento36D.grid(column=63, row=7)
        elemento36V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento36V.grid(column=62, row=6)
        elemento36P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento36P.grid(column=62, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=64,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento37L = ttk.Label(odontograma_frame, text="37")
        elemento37L.grid(column=66, row=5)


        elemento37M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento37M.grid(column=65, row=7)
        elemento37O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento37O.grid(column=66, row=7, padx= 3)
        elemento37D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento37D.grid(column=67, row=7)
        elemento37V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento37V.grid(column=66, row=6)
        elemento37P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento37P.grid(column=66, row=8)

        tkinter.ttk.Separator(odontograma_frame, orient=VERTICAL).grid(column=68,row=6, rowspan=3, sticky='ns', padx= 3)

        elemento38L = ttk.Label(odontograma_frame, text="38")
        elemento38L.grid(column=70, row=5)


        elemento38M = ttk.Checkbutton(odontograma_frame, width=0)
        elemento38M.grid(column=69, row=7)
        elemento38O = ttk.Checkbutton(odontograma_frame, width=0)
        elemento38O.grid(column=70, row=7, padx= 3)
        elemento38D = ttk.Checkbutton(odontograma_frame, width=0)
        elemento38D.grid(column=71, row=7)
        elemento38V = ttk.Checkbutton(odontograma_frame, width=0)
        elemento38V.grid(column=70, row=6)
        elemento38P = ttk.Checkbutton(odontograma_frame, width=0)
        elemento38P.grid(column=70, row=8)

        
        ttk.Button(odontograma_frame, text="Guardar", command=guardar).grid(row=11,pady=5, column=37)
        ttk.Button(odontograma_frame, text="Back", command=back_to_main).grid(row=11,column=37,sticky=N,pady=5, padx= 3)


def pagina_inicial():
        ttk.Label(inicio, text="Bienvenidos a Dentalis-Ingreso de Pacientes").grid(row=0,pady=5)
        ttk.Button(inicio, text="1-Datos Filiatorios", command=show_datos_filiatorios).grid(row=2,pady=5)
        ttk.Button(inicio, text="2-Antecedentes Patologicos", command=show_antecedentes_patologicos).grid(row=4,pady=5)
        ttk.Button(inicio, text="3-Motivo de Consulta", command=show_motivo_consulta).grid(row=6,pady=5)
        ttk.Button(inicio, text="4-Odontograma", command=show_odontograma).grid(row=8,pady=5)
        ttk.Button(inicio, text="Guardar", command=guardar).grid(row=10,pady=5)
        




    




        





root = tk.Tk()
inicio = ttk.Frame(root)
root.title("Dentalist")
root.geometry('1600x800')
root.resizable(True, True)
root.iconbitmap("./image/den.ico")
inicio.pack()

datosfiliatorios_frame = ttk.Frame(root)
antecedentes_patologicos_frame = ttk.Frame(root)
odontograma_frame = ttk.Frame(root)
motivoconsulta_frame = ttk.Frame(root)
current_frame = inicio

pagina_inicial()
create_datos_filiatorios()
create_motivo_consulta()
create_antecedentes_patologicos()
create_odontograma()

root.mainloop()

