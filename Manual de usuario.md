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
Bienvenido al Manual de Usuario de la Aplicación de Análisis Léxico. Esta aplicación escrita en Python está diseñada para analizar y ejecutar operaciones matemáticas definidas en un formato específico de archivo JSON. Con esta aplicación, podrás realizar cálculos matemáticos, incluyendo operaciones anidadas y configurar visualmente las salidas de los resultados. Antes de comenzar, asegúrate de tener instalada una versión de Python compatible en tu sistema.

## Objetivos
* Objetivo General
    *  El objetivo general de este manual es proporcionar a los usuarios una guía completa y comprensible para utilizar la aplicación de Análisis Léxico en Python de manera efectiva, permitiéndoles realizar operaciones matemáticas y personalizar la presentación de resultados a través de un archivo JSON de entrada.
* Objetivos Específicos
    * Proporcionar instrucciones detalladas sobre cómo cargar un archivo JSON de entrada.
    * Explicar cómo utilizar funciones matemáticas especiales y anidar múltiples operaciones.
    * Ayudar a los usuarios a personalizar la apariencia de los resultados generados por la aplicación.


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

La interfaz gráfica de nuestra aplicación es la ventana principal donde los usuarios pueden interactuar con facilidad. Está diseñada de manera intuitiva para facilitar la edición de archivos JSON y la realización de análisis léxicos. A continuación, describiremos los componentes clave de la interfaz:

![Imagen 1](https://i.ibb.co/3hcFGC6/Interfaz-1.png)

1. Barra de Menú:

    En la parte superior de la ventana, encontrarás una barra de menú que ofrece acceso a diversas funciones.
    Puedes abrir, guardar o guardar como archivos JSON utilizando las opciones en el menú "Archivo".
    En el menú "Herramientas", puedes realizar análisis léxicos, verificar errores y generar las imagenes con los resultados de las operaciones obtenidas del archivo JSON.
    
2. Área de Edición de Texto:

    El área principal de la interfaz es una caja de texto con un fondo oscuro y texto blanco.
    Aquí puedes editar y visualizar el contenido del archivo JSON.
    La caja de texto admite desplazamiento horizontal mediante el deslizador ubicado en la parte inferior.

3. Indicador de Línea y Columna:

    En la parte inferior derecha de la ventana, encontrarás una etiqueta que muestra la posición actual del cursor.
    Muestra la línea y la columna en la que te encuentras mientras editas el archivo.
    
4. Funcionalidades Principales:

    Puedes abrir archivos JSON existentes utilizando la opción "Abrir" del menú "Archivo". Esto carga el contenido del archivo en el área de edición de texto.
    La opción "Guardar" permite guardar los cambios en el archivo actual.
    Si deseas guardar el archivo con un nuevo nombre, puedes utilizar la opción "Guardar como".
    
    ![Imagen 2](https://i.ibb.co/9WJLVyk/Interfaz-2.png)
    
    La opción "Analizar" inicia el proceso de análisis léxico del contenido JSON en la caja de texto.
    "Errores" te permite verificar y guardar un informe de errores si se encuentran problemas en el análisis.
    "Reporte" genera y guarda un diagrama con el resultado y procedimiento de todas las operaciones encontradas en el archivo JSON durante el análisis.
    
    ![Imagen 2](https://i.ibb.co/gRspzx8/Interfaz-3.png)
    
    
5. Actualización en Tiempo Real:

    El indicador de línea y columna se actualiza automáticamente mientras editas el contenido.
    Los resultados del análisis léxico se muestran en ventanas emergentes, informando si se encontraron errores o si la operación se completó con éxito.


#### Estructura del archivo JSON

Para que la aplicación funcione sin problemas, es importante que el archivo JSON de entrada siga una estructura específica que la aplicación pueda comprender y procesar correctamente. A continuación, se describe la estructura necesaria para el archivo JSON:

```sh
{
  "operaciones": [
    {
      "operacion": "nombre_operacion",
      "valor1": valor,
      "valor2": valor_o_lista_de_operaciones
    },
    {
      "operacion": "nombre_operacion",
      "valor1": valor,
      "valor2": valor_o_lista_de_operaciones
    },
    ...
  ],
  "configuraciones": [
    {
      "texto": "texto_descriptivo",
      "fondo": "color_de_fondo",
      "fuente": "color_de_fuente",
      "forma": "forma_geometrica"
    }
  ]
}
```

#### Guía de uso
En esta sección, te proporcionaremos una guía paso a paso sobre cómo utilizar nuestra aplicación de análisis léxico en Python. Siga estos pasos para aprovechar al máximo la funcionalidad de la aplicación:

* Paso 1: Abrir un Archivo JSON

    * Haga clic en "Archivo" en la barra de menú.
    * Seleccione "Abrir" para cargar un archivo JSON existente.
    * Navegue y elija el archivo JSON que desea analizar y editar.
    * Haga clic en "Abrir" para cargar el contenido del archivo en el área de     edición de texto.
    
* Paso 2: Realizar Operaciones Matemáticas

    * En el área de edición de texto, verá el contenido del archivo JSON.
    Asegúrese de que el contenido siga la estructura adecuada con operaciones matemáticas y configuraciones.
    * Utilice las operaciones matemáticas definidas en el archivo según sus necesidades.
    * Puede anidar operaciones y utilizar funciones matemáticas especiales según lo requiera.
    
* Paso 3: Personalizar la Salida (Opcional)

    * Si desea personalizar la apariencia de la salida de resultados, agregué la sección de configuraciones tal como se muestra en la estructura del archivo JSON, coloque los datos que desee
    
* Paso 4: Realizar el Análisis Léxico

    * Vaya al menú "Herramientas" y seleccione "Analizar" para iniciar el análisis léxico.
    * El análisis se completará y se mostrará un mensaje emergente con los resultados.
    * Si se encuentran errores, se mostrará un informe que puede guardar.
    * Si no se encuentran errores, se mostrará un mensaje de éxito.
    
* Paso 5: Guardar el reporte de resultados
    
    * Si el análisis se completó con exito, presione el boton "Reporte" del menú "Herramientas" para visualizar los resultados de las operaciones matemáticas reconocidas en el archivo JSON.
    
     ![Imagen 5](https://i.ibb.co/b5Tt4yL/RESULTADOS-202200349.png) 

* Paso 6: Guardar el reporte de errores
    
    * Si el análisis no se completó con exito, presione el boton "Errores" del menú "Herramientas" para visualizar un archivo JSON con todos los errores encontrados durante el análisis
    
    ![Imagen 5](https://i.ibb.co/1sZYBNc/Errores.png) 

* Paso 7: Guardar el Archivo (Opcional)

    * Para guardar los cambios realizados en el archivo, vaya al menú "Archivo".
    Seleccione "Guardar" para sobrescribir el archivo actual o "Guardar como" para guardar con un nuevo nombre.
    
* Paso 8: Cerrar la Aplicación

    * Cuando haya terminado, vaya al menú "Archivo" y seleccione "Salir" para cerrar la aplicación.

Siga estos pasos para una experiencia fluida al utilizar la aplicación. Si necesita ayuda adicional o encuentra problemas, pongase en contacto al número 1777