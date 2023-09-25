import tkinter as tk
from tkinter import Menu, Scrollbar, filedialog, messagebox
from analizador_lexico import *
from diagrama import Diagrama
import json

class InterfazGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")
        self.root.geometry("800x600")  # Tamaño inicial de la ventana
        self.ruta_archivo = None
        self.archivo_abierto = False
        self.diagrama = None


        # Barra de herramientas (menú)
        self.barra_menu = Menu(root)
        self.root.config(menu=self.barra_menu)

        self.configurar_menu()

        # Marco que contiene el área de texto
        marco = tk.Frame(root)
        marco.pack(fill="both", expand=True)

        # Caja de texto principal
        self.caja_texto = tk.Text(marco, bg="#2C3333", fg="white", insertbackground="white", font=("consolas", 12), wrap="none")
        self.caja_texto.pack(expand="true", fill="both")

        # Deslizador horizontal
        self.deslizador_horizontal = Scrollbar(marco, orient="horizontal", command=self.caja_texto.xview)
        self.caja_texto.config(xscrollcommand=self.deslizador_horizontal.set)
        self.deslizador_horizontal.pack(fill="x")

        # Etiqueta para indicar línea y columna actual
        self.etiqueta_indicador = tk.Label(root, text="Línea: 1, Columna: 1", bd=1, relief="sunken", anchor="e")
        self.etiqueta_indicador.pack(side="right", fill="both")

        # Actualizar el indicador de línea y columna al escribir y al soltar el botón del mouse
        self.caja_texto.bind("<KeyRelease>", self.actualizar_indicador)
        self.caja_texto.bind("<ButtonRelease-1>", self.actualizar_indicador)

    def configurar_menu(self):
        menu_archivo = Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Archivo", menu=menu_archivo, font=("Helvetica", 12, "bold"))
        menu_archivo.add_command(label="Abrir", command=self.abrir)
        menu_archivo.add_command(label="Guardar", command=self.guardar)
        menu_archivo.add_command(label="Guardar como", command=self.guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.salir)

        menu_herramientas = Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label="Herramientas", menu=menu_herramientas, font=("Helvetica", 12, "bold"))
        menu_herramientas.add_command(label="Analizar", command=self.analizar)
        menu_herramientas.add_command(label="Errores", command=self.errores)
        menu_herramientas.add_command(label="Reporte", command=self.reporte)

    def abrir(self):
        try:
            archivo = filedialog.askopenfilename(filetypes=[("JSON", "*.json"), ("Todos los archivos", "*.*")])
            if archivo:
                self.ruta_archivo = archivo
                with open(archivo, 'r') as archivo:
                    contenido = archivo.read()
                self.caja_texto.delete("1.0", tk.END)
                self.caja_texto.insert("1.0", contenido)
                self.archivo_abierto = True
        except Exception as e:
            print(e)

    def guardar(self):
        contenido = self.caja_texto.get("1.0", tk.END)
        if self.archivo_abierto:  # Si se abrió un archivo previamente
            with open(self.ruta_archivo, 'w') as archivo:
                archivo.write(contenido)
        else:
            self.guardar_como()

    def guardar_como(self):
        contenido = self.caja_texto.get("1.0", tk.END)
        archivo = filedialog.asksaveasfile(filetypes=[("JSON", "*.json"), ("Todos los archivos", "*.*")], defaultextension=".json")
        if archivo:
            self.ruta_archivo = archivo.name
            with open(self.ruta_archivo, 'w') as archivo:
                archivo.write(contenido)
            self.archivo_abierto = True

    def salir(self):
        self.root.destroy()

    def analizar(self):
        codigo_json = self.caja_texto.get("1.0", "end")

        token, error = analizador_lexico(codigo_json)
        
        configuraciones = buscar_configuraciones(token)
        self.diagrama = Diagrama(configuraciones[0], configuraciones[1], configuraciones[2], configuraciones[3])

        analizar_json(codigo_json, self.diagrama)

        #Mostrar motificacion popup de que se realizo el analisis, si se encontraron errores indicarlo y decir que puede que las operaciones no se realicen correctamente
        if error:
            messagebox.showinfo("Analisis", "El análisis se completó. Se encontraron errores en el analisis, puede que las operaciones no se realicen correctamente\n Genere el reporte de errores para ver los detalles")
        else:
            messagebox.showinfo("Analisis", "El análisis se completó. No se encontraron errores en el analisis")

 

    def errores(self):
        token, error = analizador_lexico(self.caja_texto.get("1.0", "end"))
        errores_json = []
        contador = 1
        if not error:
            messagebox.showinfo("Errores", "No se encontraron errores en el analisis")
        else:

            for dato_error in error:

                error_nuevo ={
                    "No.": contador,
                    "descripcion":{
                        "lexema": dato_error.caracter,
                        "tipo": dato_error.tipo,
                        "columna": dato_error.columna,
                        "fila": dato_error.fila
                    }
                }
                errores_json.append(error_nuevo)
                contador += 1

                data = {
                    "errores": errores_json
                }

            with open('RESULTADOS_202200349.json', 'w') as file:
                json.dump(data, file, indent=4)


    def reporte(self):
        self.diagrama.guardar()

    def actualizar_indicador(self, event=None):
        linea, columna = self.caja_texto.index(tk.INSERT).split(".")
        self.etiqueta_indicador.config(text=f"Línea: {linea}, Columna: {columna}")
