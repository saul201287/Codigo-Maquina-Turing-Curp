import tkinter as tk
from tkinter import messagebox
import random
import string

def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def validar_fecha(año, mes, dia):
    if mes == 2: 
        if es_bisiesto(año):
            return dia <= 29
        else:
            return dia <= 28
    elif mes in [4, 6, 9, 11]:
        return dia <= 30
    else:  
        return dia <= 31

def validar_curp(curp):
    print(len(curp))
    if len(curp) != 18:
        return False

    año = int(curp[4:6])
    mes = int(curp[6:8])
    dia = int(curp[8:10])
    
    año += 1900 if año > 20 else 2000

    return validar_fecha(año, mes, dia)

def generar_vocal_interna(apellido):
    for letra in apellido[1:]:  
        if letra in 'AEIOU':
            return letra
    return ''  

def generar_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado):
    primer_apellido = apellido_paterno.strip().upper()
    segundo_apellido = apellido_materno.strip().upper()
    nombres = nombre.strip().upper()

    letra1 = primer_apellido[0] 
    letra2 = generar_vocal_interna(primer_apellido)
    letra3 = segundo_apellido[0]  
    letra4 = nombres[0]  
    año = fecha_nacimiento[:4]
    mes = fecha_nacimiento[5:7]
    dia = fecha_nacimiento[8:10]

    penultimo_digito_año = año[-2]  
    ultimo_digito_año = año[-1]    

    lugar_nacimiento = estado[:2].upper()  
    caracteres_aleatorios = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    curp = (
        letra1 +
        letra2 +
        letra3 +
        letra4 +
        penultimo_digito_año +
        ultimo_digito_año +
        mes +
        dia +
        sexo +
        lugar_nacimiento +
        caracteres_aleatorios
    )

    return curp

def validar_y_generar_curp():
    nombre = entry_nombre.get()
    apellido_paterno = entry_apellido_paterno.get()
    apellido_materno = entry_apellido_materno.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    sexo = entry_sexo.get().upper()
    estado = entry_estado.get().upper()

    try:
        año = int(fecha_nacimiento[:4])
        mes = int(fecha_nacimiento[5:7])
        dia = int(fecha_nacimiento[8:10])
    except ValueError:
        messagebox.showerror("Error", "Fecha de nacimiento inválida. Formato debe ser AAAA-MM-DD.")
        return

    if not validar_fecha(año, mes, dia):
        messagebox.showerror("Error", "Fecha de nacimiento no válida.")
        return

    curp = generar_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado)
    
    if validar_curp(curp):
        messagebox.showinfo("CURP Generada", f"La CURP generada es: {curp}")
    else:
        messagebox.showerror("Error", "CURP no válida.")

ventana = tk.Tk()
ventana.title("Generador y Validador de CURP")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Apellido Paterno:").grid(row=1, column=0)
entry_apellido_paterno = tk.Entry(ventana)
entry_apellido_paterno.grid(row=1, column=1)

tk.Label(ventana, text="Apellido Materno:").grid(row=2, column=0)
entry_apellido_materno = tk.Entry(ventana)
entry_apellido_materno.grid(row=2, column=1)

tk.Label(ventana, text="Fecha de Nacimiento (AAAA-MM-DD):").grid(row=3, column=0)
entry_fecha_nacimiento = tk.Entry(ventana)
entry_fecha_nacimiento.grid(row=3, column=1)

tk.Label(ventana, text="Sexo (H/M):").grid(row=4, column=0)
entry_sexo = tk.Entry(ventana)
entry_sexo.grid(row=4, column=1)

tk.Label(ventana, text="Estado (clave de 2 letras):").grid(row=5, column=0)
entry_estado = tk.Entry(ventana)
entry_estado.grid(row=5, column=1)

boton_validar = tk.Button(ventana, text="Generar y Validar CURP", command=validar_y_generar_curp)
boton_validar.grid(row=6, columnspan=2)

ventana.mainloop()
