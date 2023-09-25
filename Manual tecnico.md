# Lenguajes formales y de programación
## Proyecto 1
### 4to Semestre
```js
Universidad San Carlos de Guatemala
Programador: Irving Fernando Alvarado Asensio
Carne: 202200349
Correo: 3291590461103@ingenieria.usac.edu.gt
```
---
## Descripción
El Manual Técnico de la Aplicación Analizador Léxico en Python proporciona una guía detallada para comprender, instalar y utilizar esta aplicación diseñada para procesar archivos JSON que contienen instrucciones para realizar operaciones matemáticas. El manual está estructurado de manera lógica y organizada en varias secciones para ayudar a los usuarios a obtener el máximo provecho de la aplicación.

## Objetivos
* Objetivo General
    *  Proporcionar a los usuarios una guía completa y detallada para comprender, instalar y utilizar la aplicación Analizador Léxico en Python, permitiéndoles procesar archivos JSON que contienen instrucciones para operaciones matemáticas de manera efectiva y eficiente.
* Objetivos Específicos
    * Proporcionar una introducción clara y accesible que ayude a los usuarios a comprender la funcionalidad y el propósito de la aplicación, así como sus ventajas y beneficios en el procesamiento de operaciones matemáticas.
    * Suministrar instrucciones paso a paso para instalar y utilizar la aplicación, incluyendo la estructura del código fuente, lo que permitirá a los usuarios aprovechar al máximo todas las características y funcionalidades de la aplicación.
    * Ayudar a los usuarios a personalizar la aplicación según sus necesidades mediante la explicación detallada de las configuraciones disponibles. Además, proporcionar soluciones y consejos para abordar problemas comunes que puedan surgir durante el uso de la aplicación, lo que contribuirá a una experiencia de usuario más fluida y satisfactoria.


---
## Descripción del proyecto
La Aplicación de Analizador Léxico en Python es un proyecto informático que ofrece una solución efectiva para procesar archivos JSON que contienen instrucciones para realizar operaciones matemáticas. Esta aplicación fue creada con el objetivo de facilitar la interpretación y ejecución de operaciones matemáticas de manera sencilla y flexible. El analizador léxico es una parte esencial en la interpretación de expresiones matemáticas, y esta aplicación lo hace accesible y utilizable tanto para usuarios educativos como para aquellos que necesitan realizar cálculos avanzados.

#### Requisitos del sistema
Antes de comenzar a utilizar la Aplicación de Analizador Léxico en Python, es importante asegurarse de que su sistema cumpla con los requisitos mínimos. Esto garantizará una experiencia de uso fluida y sin problemas. A continuación, se detallan los requisitos del sistema:

* Requisitos de Hardware

    Para ejecutar la aplicación de manera eficiente, se recomienda un equipo con las siguientes especificaciones mínimas:

    * Procesador de al menos 1 GHz.
    * 1 GB de memoria RAM.
    * 10 MB de espacio en disco duro para la aplicación y archivos relacionados.
    * Conexión a Internet (para instalar bibliotecas adicionales, si es necesario).
    
* Requisitos de Software

    Asegúrese de tener los siguientes componentes de software instalados en su sistema:

    * Python 3.x: La aplicación está escrita en Python y requiere una versión de Python 3.x. Puede descargar Python desde el sitio web oficial (https://www.python.org/downloads/) e instalarlo siguiendo las instrucciones proporcionadas en la documentación.
    
* Bibliotecas Adicionales

    * Graphviz (Biblioteca adicional): Para visualizar un grafo de las operaciones realizadas, la aplicación utiliza la biblioteca Graphviz. Puede descargar e instalar Graphviz desde el sitio web oficial (https://www.graphviz.org/download/) siguiendo las instrucciones específicas para su sistema operativo. Asegúrese de que la instalación de Graphviz esté correctamente configurada y sea accesible desde la línea de comandos.
    * Tkinter (Biblioteca adicional): Para visualizar la interfaz gráfica


#### Interfaz gráfica

La apariencia de la interfaz de la aplicación se muestra a continuación

![Imagen1](https://i.ibb.co/yYq7G88/interfaz.png)

La Interfaz Gráfica de Usuario (GUI) de la Aplicación de Analizador Léxico en Python ofrece una experiencia interactiva y amigable para los usuarios que desean interactuar con la aplicación de manera efectiva y eficiente. Esta interfaz ha sido diseñada para simplificar la carga, edición y análisis de archivos JSON que contienen instrucciones para operaciones matemáticas, proporcionando herramientas intuitivas y opciones funcionales. El codigo usado para las funciones descritas anteriormente es este:

A continuación, se presenta una descripción general de los componentes clave de la interfaz:

* Barra de Herramientas (Menú): La barra de herramientas en la parte superior de la ventana brinda acceso a diversas funcionalidades, incluyendo la gestión de archivos, análisis léxico, manejo de errores y generación de informes visuales.

* Área de Texto Principal: El área central de la interfaz actúa como un editor de texto donde los usuarios pueden ingresar o cargar archivos JSON. La apariencia de la caja de texto se ha personalizado para una mejor legibilidad.

* Deslizador Horizontal: Un deslizador horizontal facilita la navegación a través del contenido de la caja de texto cuando el contenido es más amplio que la ventana visible.

* Indicador de Línea y Columna: En la parte inferior derecha, un indicador proporciona información sobre la ubicación actual del cursor en términos de línea y columna dentro del editor de texto.

La interfaz permite a los usuarios realizar acciones esenciales, como abrir y guardar archivos, analizar el contenido JSON, gestionar errores y generar informes gráficos de las operaciones realizadas. Proporciona una experiencia de usuario completa para aprovechar al máximo la funcionalidad de la aplicación.

El código utilizado para las fuciones abrir, guardar, guardar como y salir es el siguiente:

```sh
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
```

Al seleccionar "Analizar" desde el menú de herramientas, la aplicación realiza un análisis léxico del contenido JSON en el área de texto, con ayuda de la funcion analizar_json(entrada_diagrama) que se describirá posteriormente y muestra información sobre los tokens reconocidos. También puede detectar errores y generar un informe de errores en formato JSON si se encuentran errores de análisis. Además, puedes generar un reporte gráfico de las operaciones utilizando la biblioteca Graphviz.

A lo largo de este manual técnico, se explorarán en detalle las diferentes funcionalidades y procedimientos que la interfaz ofrece, brindando a los usuarios una comprensión completa de cómo utilizar eficazmente la Aplicación de Analizador Léxico en Python.

#### Analizador léxico

Su principal función es analizar una cadena de entrada, que generalmente es un archivo JSON, y dividirla en unidades más pequeñas llamadas "tokens". Cada token representa un componente léxico, como números, cadenas, corchetes, comas y otros símbolos que son parte de la estructura del archivo JSON.

A continuación, se describen las partes más destacadas del código:

* Función analizador_lexico(entrada): Esta función recibe una cadena de entrada y la analiza carácter por carácter para identificar y clasificar los tokens. Los tokens reconocidos se almacenan en una lista, mientras que los errores léxicos se registran en otra lista. Los tipos de tokens reconocidos incluyen cadenas (strings), números, corchetes, llaves, comas y dos puntos.

* Función es_letra(caracter): Esta función auxiliar verifica si un carácter es una letra válida dentro de una cadena. Se utiliza para validar caracteres en cadenas (strings).

* Función buscar_configuraciones(tokens): Esta función busca configuraciones específicas en la lista de tokens. Estas configuraciones servirán para darle estilo al grafo generado por graphviz

* Función analizar_json(entrada, diagrama): Esta función utiliza la función analizador_lexico para obtener una lista de tokens a partir de la cadena de entrada. Luego, busca y procesa las operaciones definidas en el archivo JSON, realizando cálculos matemáticos y generando un diagrama para representar las operaciones.

* Función obtener_valor(tokens, diagrama, tipo): Esta función se encarga de extraer y evaluar valores numéricos o expresiones dentro del contexto de las operaciones definidas en el archivo JSON. Recibe tres parámetros:
    * tokens: La lista de tokens que contiene la información léxica de la cadena de entrada.
    * diagrama: El objeto que representa el diagrama en el que se representan las operaciones.
    * tipo: Un indicador que especifica si se está buscando un valor para "valor1" o "valor2" en una operación.

    La función recorre la lista de tokens y busca el valor correspondiente a tipo siguiendo reglas específicas:

    Si encuentra un número, lo convierte en un valor numérico y lo devuelve.
    Si encuentra un corchete abierto [, asume que se trata de una operación anidada y continúa buscando el valor dentro de esa operación anidada. Esto puede involucrar recursión.
    Cuando encuentra el valor, ya sea un número o el resultado de una operación anidada, lo devuelve junto con la posición actual en la lista de tokens.
    Esta función es crucial para la ejecución de las operaciones, ya que permite evaluar expresiones matemáticas complejas dentro de los archivos JSON. También se encarga de rastrear si el valor obtenido proviene de una operación anidada para su representación en el diagrama.

    En resumen, obtener_valor es una función clave para el análisis y evaluación de expresiones matemáticas en el contexto de la aplicación.

* Función generarDiagrama(diagrama, lista_operaciones): Esta función se encarga de generar un diagrama que representa visualmente las operaciones matemáticas realizadas. Utiliza una estructura de nodos y aristas para crear el diagrama. Cada operación se representa como un nodo en el diagrama, y las aristas conectan los nodos según la secuencia de las operaciones.

El código completo de esta implementación, debido a su extensión, no se presenta en este contexto, pero se encuentra disponible en el repositorio público de GitHub en el siguiente enlace: https://github.com/Fercho9134/LFP_S2_2023_Proyecto1_202200349 Los interesados pueden acceder al repositorio para obtener el código fuente completo y explorar su funcionamiento en detalle.

#### Errores

La función errores() es una parte crucial de la aplicación, diseñada para realizar un análisis léxico del contenido ingresado por el usuario en una caja de texto. Su principal objetivo es detectar errores léxicos en el código ingresado y generar un archivo JSON que registra los detalles de los errores encontrados. Esta función se utiliza para facilitar la identificación y corrección de problemas en el código fuente.

La función errores() utiliza la funcion analizador_lexico(entrada) que se describió anteriormente, para analizar el contenido de la caja de texto y obtener los errores de esta si es que los contiene.

* Comportamiento
    * Inicia el análisis léxico del contenido presente en la caja de texto.
    * Si no se detectan errores léxicos durante el análisis, muestra un mensaje informativo indicando que no se encontraron errores.
    * Si se encuentran errores léxicos, procede a crear un archivo JSON que almacena información detallada sobre cada error encontrado.


* Cada entrada en la lista "errores" representa un error y contiene los siguientes campos:

    "No.": Un número de identificación único para cada error.
    "descripcion": Un diccionario que proporciona detalles sobre el error, que incluye:
    "lexema": El lexema que causó el error.
    "tipo": El tipo de error, que generalmente es "Error léxico".
    "columna": La columna en la que se encontró el error.
    "fila": La fila en la que se encontró el error.

El código es el sguiente:

```sh
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
```

Se ejecuta cada vez que el usuario presiona el boton "errores" del menú