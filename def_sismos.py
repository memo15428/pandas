from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#Inicio
def inicio():
    print()
    print("=========ZONAS SISMORRESISTENTES=========")

#Menu Principal:
def menu():
    print("""
    MENU PRINCIPAL
    1) ZONAS SISMORRESISTENTE.
    2) PERFILES DE SUELO.
    3) ZONAS SISMICAS.
    4) SALIR""")
    print()

    while True:
        escoger = input("Ingrese la opcion: ")

        try:
            escoger = int(escoger)

            if escoger == 1:
                sismorresistente()

            elif escoger == 2:
                perfiles_suelos()

            elif escoger == 3:
                z_sismica()

            elif escoger == 4:
                exit()

        except ValueError:
            print()
            print("Escriba valores numericos para las opciones.")
            print()


#ZONAS SISMORRESISTENTES:
def sismorresistente():
    print()
    print("=========ZONAS SISMORRESISTENTES=========")
    print("""   OPCIONES:
    1) ZONA 01
    2) ZONA 02
    3) ZONA 03
    4) ZONA 04
    5) TABLA DE ZONA SISMICA
    6) VOLVER AL MENU ANTERIOR""")

    # Variables y valores de zonas sismoresistente:
    zona_1 = 0.45
    zona_2 = 0.35
    zona_3 = 0.25
    zona_4 = 0.10

    while True:
        print()
        opcion_sismo = input("Ingrese el número de la opción: ")

        try:
            opcion_sismo = int(opcion_sismo)

            if opcion_sismo == 1:
                print()
                print ("El factor de zona 1 es: ", str(zona_1), ".")

            elif opcion_sismo == 2:
                print()
                print ("El factor de zona 2 es: ", str(zona_2), ".")

            elif opcion_sismo == 3:
                print()
                print("El factor de zona 3 es: ", str(zona_3), ".")

            elif opcion_sismo == 4:
                print()
                print ("El factor de zona 4 es: ", str(zona_4),".")

            elif opcion_sismo == 5:
                im = Image.open("C:/Users/Miguel Mogollòn/Desktop/proyectos_python/zona_sism/archivo_sismo/zona_sismica.jpg")
                im.show()

            elif opcion_sismo == 6:
                menu()

            else:
                print()
                print("Ingresa la zona correcta.")

        except ValueError:
            print()
            print("Escriba valores numericos.")
            print()

    sismorresistente()

#PERFILES DE SUELOS:

def perfiles_suelos():
    print()
    print("=========PERFILES DE SUELOS=========")
    print("""   OPCIONES:
       1) INGRESAR VELOCIDADES DE CORTE (Vs)
       2) VER TABLA DE CLASIFICACION DE PERFILES DE SUELOS
       3) VOLVER AL MENU ANTERIOR""")

    print()
    opciones = input("Ingrese la opción: ")

    try:

        opciones = int(opciones)

        if opciones == 1:

            while True:
                print()
                opcion_perf = input("Ingrese la Velocidad de Corte Vs (m/s): ")

                try:
                    opcion_perf = float(opcion_perf)

                    if opcion_perf > 1500:
                        print()
                        print("Perfil tipo S0: Roca Dura.")

                    elif opcion_perf > 500 and opcion_perf <= 1500:
                        print()
                        print("Perfil tipo S1: Roca y Suelos muy rigidos.")

                    elif opcion_perf > 180 and opcion_perf <= 500:
                        print()
                        print("Perfil tipo S2: Suelos Intermedios.")

                    elif opcion_perf <= 180:
                        print()
                        print("Perfil tipo S3: Suelos Blandos.")
                    break

                except ValueError:
                    print()
                    print("Escriba valores numericos")
                    print()

        elif opciones == 2:
            im = Image.open("C:/Users/Miguel Mogollòn/Desktop/proyectos_python/zona_sism/archivo_sismo/tabla_perf.jpg")
            im.show()

        elif opciones == 3:
            menu()

    except ValueError:
        print()
        print("Ingrese valores numéricos.")

    perfiles_suelos()

#ZONA SISMICA
def z_sismica():

    print()
    print("""ZONAS SISMICA
    1) INGRESAR DISTRITO
    2) ABRIR NORMA TECNICA E.030
    3) VOLVER AL MENU ANTERIOR
    """)

    datos = pd.read_csv("distri_sism_1.csv", encoding="latin9", sep=";")
    df = pd.DataFrame(datos)

    opcion_z_sismica = input("Ingrese la opcion: ")

    try:

        opcion_z_sismica = int(opcion_z_sismica)

        if opcion_z_sismica == 1:

            while True:

                ingreso = str.upper(input("Ingresa el distrito: "))

                for idx in df.index:
                    #ingreso = input("Ingresa: ")
                    if df.DISTRITO[idx] == ingreso:
                        print (f"La zona sismica de '{ingreso}' es: {df.ZONA_SISMICA[idx]}")
                        z_sismica()
                        break
                else:
                    print("Ingrese el distrito correcto.")

        elif opcion_z_sismica == 2:
            os.popen("norma_tecnica_e_030.pdf")

        elif opcion_z_sismica == 3:
            menu()

    except ValueError:
        print()
        print("Ingrese un valor numerico.")

    z_sismica()

inicio()
menu()