#Importacione
from tkinter import *
from tkinter import ttk
from inicioPAM import InicioPAM


#Constantes de colores para ser reutilizadas a posteriori
bg_color = "#e5e5e5"
fg_color = "#000000"
text_bg_color = "#e5e5e5"


#ventana principal
root = Tk()
root.title("Reglamento PAM TIID213")
root.geometry("800x700")
root.configure(bg=bg_color)

#Estilos
style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", background=bg_color, foreground=fg_color, font=("Arial", 14))
style.configure("TButton", background=bg_color, foreground=fg_color)
style.configure("TFrame", background=bg_color)
frame = ttk.Frame(root, padding="15 15 15 15")
frame.pack(fill=BOTH, expand=True)

#Texto
text_widget = Text(frame, wrap=WORD, font=("Arial", 12),
                   bg=text_bg_color, fg=fg_color,
                   insertbackground=fg_color, borderwidth=0,
                   highlightthickness=0)
text_widget.pack(fill=BOTH, expand=True, padx=10, pady=10)


"""
    IMPORTANTE
        instanciación de clases

"""
iPAM = InicioPAM()


"""
    Reglamento del curso
        se extrae de la función la información del diccionario

"""
text_widget.insert(END, "Reglamento del curso\n\n", "header")
reglamento = iPAM.reglamentoPAM()

for key, value in reglamento.items():
    text_widget.insert(END, f"{key}. {value}\n\n", "normal_text")



"""
    Fechas de Parciales
        se extrae de la función la información del diccionario

"""
text_widget.insert(END, "\nFechas de Parciales\n\n", "header")

fechas = iPAM.fechasDeParciales()
for key, value in fechas.items():
    text_widget.insert(END, f"{key.replace('_', ' ').title()}: {value}\n\n", "list_item")

"""
    Lineamientos del Classroom
        se extrae de la función la información del diccionario

"""
text_widget.insert(END, "Lineamientos de classroom\n\n", "header")
reglamento = iPAM.lineamientosClassRoom()

for key, value in reglamento.items():
    text_widget.insert(END, f"{key}. {value}\n\n", "normal_text")


"""
    Porcentajes por Parcial
        se extrae de la función la información del diccionario

"""

text_widget.insert(END, "\nPorcentajes por Parcial\n\n", "header")

porcentajes = iPAM.porcentajesPorParcial()

for partial, details in porcentajes.items():
    text_widget.insert(END, f"{partial.replace('_', ' ').title()}\n", "subheader")
    for evidence, percentage in details.items():
        text_widget.insert(END, f"  - {evidence}: {percentage}\n", "list_item")
    text_widget.insert(END, "\n") 


#FOOTER
text_widget.insert(END, "\nTrabajo realizado por:\n Mariano Martinez Escobedo\n 124049281\n", "footer")

#Estilos de los widgets de texto para el header, el footer y los textos normales
text_widget.tag_configure("footer", font=("Arial", 18, "bold"), foreground="#000814",justify='center')
text_widget.tag_configure("header", font=("Arial", 18, "bold"), foreground="#000814")
text_widget.tag_configure("normal_text", font=("Arial", 12), foreground=fg_color)
text_widget.config(state=DISABLED)


#Loop Prinicpal
root.mainloop()