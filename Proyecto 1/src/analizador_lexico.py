from tokens import Tokens
from error import Error
from diagrama import Diagrama
import math
from operacion import Operacion

contador_nodos = 0
lista_operaciones = []
nivel = 0
numero_operacion = 0


def analizador_lexico(entrada):
    tokens = []
    errores = []  # Lista para almacenar errores
    i = 0  # Índice para recorrer la cadena de entrada
    fila = 1
    columna = 1

    while i < len(entrada):
        char = entrada[i]

        # Reconocer espacios en blanco
        if char == ' ':
            columna += 1
            i += 1
            continue

        if char == '\t':
            columna += 1
            i += 1
            continue

        # Reconocer saltos de línea
        if char == '\n':
            fila += 1
            columna = 1
            i += 1
            continue

        # Reconocer cadenas (strings)
        if char == '"':
            i += 1
            inicio = i
            while i < len(entrada) and entrada[i] != '"':
                if not es_letra(entrada[i]):  # Validación de caracteres no válidos en la cadena
                    errores.append(Error("Error lexico", fila, columna + i - inicio, entrada[i]))
                i += 1
            if i >= len(entrada):
                errores.append(Error("No se cerraron comillas", fila, columna, entrada[inicio - 1]))
                columna += i - inicio + 1
            else:
                cadena = entrada[inicio:i].lower()
                token = Tokens("cadena", cadena)
                tokens.append(token)
                columna += i - inicio + 2
            i += 1
            continue

        # Reconocer números
        if char.isdigit() or (char == '-' and i + 1 < len(entrada) and entrada[i + 1].isdigit()):
            inicio = i
            i += 1
            while i < len(entrada) and (entrada[i].isdigit() or entrada[i] == '.'):
                i += 1
            token = Tokens("numero", entrada[inicio:i])
            tokens.append(token)
            columna += i - inicio
            continue

        if char == '{':
            token = Tokens("llave_abierta", char)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == '}':
            token = Tokens("llave_cerrada", char)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == '[':
            token = Tokens("corchete_abierto", char)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == ']':
            token = Tokens("corchete_cerrado", char)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == ':':
            token = Tokens("dos_puntos", char)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        if char == ',':
            token = Tokens("coma", char)
            tokens.append(token)
            i += 1
            columna += 1
            continue

        # Registrar errores de tokens no reconocidos
        errores.append(Error("Error lexico", fila, columna, char))
        i += 1
        columna += 1

    return tokens, errores

def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z' or (caracter >= '1' and caracter <= '2') or caracter == ' '

def buscar_configuraciones(tokens):
    i = 0
    configuraciones = []

    while i < len(tokens):
        token = tokens[i]

        if token.tipo == "cadena":
            if token.valor == "configuraciones":
                i += 4  # Saltamos cuatro tokens para obtener el tipo de configuración
                configuracion_tipo = tokens[i].valor
                if configuracion_tipo == "texto":
                    i+=2
                    configuracion_texto = tokens[i].valor
                    configuraciones.append(configuracion_texto)
                    i+=2
                    configuracion_tipo = tokens[i].valor

                if configuracion_tipo == "fondo":
                    i+=2
                    configuracio_fondo = tokens[i].valor
                    configuraciones.append(configuracio_fondo)
                    i+=2
                    configuracion_tipo = tokens[i].valor

                if configuracion_tipo == "fuente":
                    i+=2
                    configuracion_fuente = tokens[i].valor
                    configuraciones.append(configuracion_fuente)
                    i+=2
                    configuracion_tipo = tokens[i].valor

                if configuracion_tipo == "forma":
                    i+=2
                    configuracio_fondo = tokens[i].valor
                    configuraciones.append(configuracio_fondo)
                    i+=2
                    configuracion_tipo = tokens[i].valor
                
                i+=1
        i+=1
                    
    return configuraciones

def analizar_json(entrada, diagrama):
    tokens, errores = analizador_lexico(entrada)  # Utilizamos el analizador léxico
    global lista_operaciones, nivel, numero_operacion

    if errores:
        # Manejar errores léxicos si los hubiera
        for error in errores:
            print(f"Error léxico: {error.tipo} en fila {error.fila}, columna {error.columna}, caracter {error.caracter}")

    if tokens:
        # Identificar operaciones en los tokens
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.tipo == "llave_abierta":
                # Comienza una estructura
                i += 1
                estructura_tipo = tokens[i].valor

                if estructura_tipo == "operaciones":

                    i += 1  # Avanzamos para entrar a la lista de operaciones
                    while i < len(tokens):
                        # Procesar las operaciones dentro de la lista
                        if tokens[i].tipo == "llave_abierta":
                            i += 1  # Avanzamos para obtener el tipo de operación

                            operacion_tipo = None
                            valor1 = None
                            valor2 = None

                            while i < len(tokens) and not (tokens[i].tipo == "llave_cerrada" and tokens[i].valor == "}"):
                                # Procesar los elementos dentro de una operación
                                if tokens[i].tipo == "cadena":
                                    if tokens[i].valor == "operacion":
                                        # Obtener el tipo de operación
                                        i += 2  # Saltamos dos tokens para obtener el tipo de operación
                                        operacion_tipo = tokens[i].valor
                                    elif tokens[i].valor == "valor1":
                                        # Obtener el valor1 de la operación
                                        i += 2  # Saltamos dos tokens para obtener el valor1
                                        valor1 = obtener_valor(tokens[i:], diagrama, "valor1")
                                        i += valor1[1]
                                    elif tokens[i].valor == "valor2":
                                        # Obtener el valor2 de la operación
                                        i += 2  # Saltamos dos tokens para obtener el valor2
                                        valor2 = obtener_valor(tokens[i:], diagrama, "valor2")
                                        i += valor2[1]
                                    else: 
                                        i += 1

                                else:
                                    i += 1

                            # Realizar la operación
                            if operacion_tipo and valor1 is not None and valor2 is not None:
                                resultado = realizar_operacion(operacion_tipo, valor1[0], valor2[0], diagrama)
                                print(f"Resultado de {operacion_tipo}: {resultado}")
                                operacion_nueva = Operacion(operacion_tipo, valor1[0], valor1[2], valor2[0], valor2[2], resultado, numero_operacion)
                                lista_operaciones.append(operacion_nueva)
                                generarDiagrama(diagrama, lista_operaciones)
                                lista_operaciones = []
                                numero_operacion += 1
                                nivel = 0
                                

                        i += 1  # Avanzamos al siguiente token

            i += 1


"""def generarDiagrama(diagrama, lista_operaciones):
    print("Generando diagrama...")
    operacion_anterior_anidada = False
    resultado_anterior = None
    for operacion in lista_operaciones:
        print(operacion.tipo_operacion, operacion.valor1, operacion.valor2, operacion.resultado, operacion.anidada, operacion.nivel)
        if operacion.nivel == 0:
            if operacion.valor2 == None:
                diagrama.agregar_nodo(str(operacion.valor1))
                diagrama.agregar_nodo (operacion.tipo_operacion + str(operacion.resultado))
                diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                resultado_anterior = operacion.resultado
            else:
                diagrama.agregar_nodo(str(operacion.valor1))
                diagrama.agregar_nodo(str(operacion.valor2))
                diagrama.agregar_nodo (operacion.tipo_operacion + str(operacion.resultado))
                diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                resultado_anterior = operacion.resultado

            operacion_anterior_anidada = operacion.anidada
        else:
            if operacion_anterior_anidada:
                if operacion.valor2 == None:
                    diagrama.agregar_nodo(operacion.tipo_operacion + str(operacion.resultado))
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.ultimo_nodo())
                    resultado_anterior = operacion.resultado
                else:
                    if operacion.valor1 == resultado_anterior:
                        diagrama.agregar_nodo(str(operacion.valor2))
                        diagrama.agregar_nodo(operacion.tipo_operacion + str(operacion.resultado))
                        diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                        diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                        resultado_anterior = operacion.resultado
                    else:
                        diagrama.agregar_nodo(str(operacion.valor1))
                        diagrama.agregar_nodo(operacion.tipo_operacion + str(operacion.resultado))
                        diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                        diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                        resultado_anterior = operacion.resultado
            else:
                if operacion.valor2 != None:
                    diagrama.agregar_nodo(str(operacion.valor1))
                    diagrama.agregar_nodo(str(operacion.valor2))
                    diagrama.agregar_nodo(operacion.tipo_operacion + str(operacion.resultado))
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                    resultado_anterior = operacion.resultado
                else:
                    diagrama.agregar_nodo(str(operacion.valor1))
                    diagrama.agregar_nodo(operacion.tipo_operacion + str(operacion.resultado))
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                    resultado_anterior = operacion.resultado

"""

"""def generarDiagrama(diagrama, lista_operaciones):
    lista_operaciones.reverse()
    print("Generando diagrama...")
    i=0
    for operacion in lista_operaciones:
        print(operacion.tipo_operacion, operacion.valor1, operacion.valor2, operacion.resultado, operacion.anidada, operacion.nivel)
        if i+1 < len(lista_operaciones):
            operacion_siguiente = lista_operaciones[i+1]
        else:
            operacion_siguiente = None
        if operacion_siguiente != None:
            if i == 0:
                diagrama.agregar_nodo(operacion.tipo_operacion + "\n" + str(operacion.resultado))
                
                if  operacion_siguiente.anidada:
                    if operacion.valor2 != None:
                        if operacion_siguiente.resultado == operacion.valor1:
                            diagrama.agregar_nodo(operacion_siguiente.tipo_operacion + "\n" + str(operacion_siguiente.resultado))
                            diagrama.agregar_nodo(str(operacion.valor2))
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 2)
                        else:
                            diagrama.agregar_nodo(str(operacion.valor1))
                            diagrama.agregar_nodo(operacion_siguiente.tipo_operacion + "\n" + str(operacion_siguiente.resultado))
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 2)
                    else:
                        if operacion_siguiente.resultado == operacion.valor1:
                            diagrama.agregar_nodo(operacion_siguiente.tipo_operacion + "\n" + str(operacion_siguiente.resultado))
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 3)
                        else:
                            diagrama.agregar_nodo(str(operacion.valor1))
                            diagrama.agregar_nodo(operacion_siguiente.tipo_operacion + "\n" + str(operacion_siguiente.resultado))
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 3)
                    i+=1    
                else:
                    diagrama.agregar_nodo(str(operacion.valor1))
                    diagrama.agregar_nodo(str(operacion.valor2))
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                    i+=1

            else:
                if operacion.valor2 != None:
                    if  operacion_siguiente.anidada:
                        if operacion_siguiente.resultado == operacion.valor1:
                            diagrama.agregar_nodo(operacion_siguiente.tipo_operacion + "\n" + str(operacion_siguiente.resultado))
                            diagrama.agregar_nodo(str(operacion.valor2))
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 2)
                        else:
                            diagrama.agregar_nodo(str(operacion.valor1))
                            diagrama.agregar_nodo(operacion_siguiente.tipo_operacion + "\n" + str(operacion_siguiente.resultado))
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 2)
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                    else:
                        if operacion_siguiente.resultado == operacion.valor1:
                            diagrama.agregar_nodo(str(operacion.valor2))
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                        else:
                            diagrama.agregar_nodo(str(operacion.valor1))
                            diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                    i+=1
                else:
                    diagrama.agregar_nodo(str(operacion.valor1))
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                    i+=1
        else:
        # para la ultima operacion
            if operacion.valor2 != None:
                diagrama.agregar_nodo(str(operacion.valor1))
                diagrama.agregar_nodo(str(operacion.valor2))
                diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 2)
                diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                i+=1
            else:
                diagrama.agregar_nodo(str(operacion.valor1))
                diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                        
            """

def generarDiagrama(diagrama, lista_operaciones):
    lista_operaciones.reverse()
    i=0
    contador=0
    valor1_siguiente_un_nodo = False
    valor1_anidado = False
    doble_anidado = False
    
    for operacion in lista_operaciones:
        print(operacion.tipo_operacion, operacion.valor1, operacion.valor1_aninado, operacion.valor2, operacion.valor2_aninado, operacion.resultado, operacion.numero_operacion, operacion.valor1_aninado, operacion.valor2_aninado)
        
        #Nodo raiz

        if contador+1 < len(lista_operaciones):
            operacion_siguiente = lista_operaciones[contador+1]
        else:
            operacion_siguiente = None
        
        if contador+2 < len(lista_operaciones):
            operacion_siguiente2 = lista_operaciones[contador+2]
        else:
            operacion_siguiente2 = None


        #Se ejecutara mientras no sea la ultima operacion
        if i == 0:
            diagrama.agregar_nodo(operacion.tipo_operacion + "\n" + str(operacion.resultado))
            

        if operacion_siguiente != None:
            
            #Para operaciones con dos valores
            if operacion.valor2 != None:
                
                #Si el valor1 de la operacion es resultado de la operacion anterior
                if operacion.valor1_aninado and operacion.valor2_aninado == False:
                    diagrama.agregar_nodo(operacion_siguiente.tipo_operacion + "\n" + str(operacion_siguiente.resultado))
                    
                    if operacion_siguiente.valor2==None:
                        valor1_siguiente_un_nodo = True
                    

                    diagrama.agregar_nodo(str(operacion.valor2))
                    if valor1_anidado == False:    
                        diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                        diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 2)
                    else:
                        diagrama.agregar_arista(diagrama.cantidad_nodos - 4, diagrama.cantidad_nodos - 1)
                        diagrama.agregar_arista(diagrama.cantidad_nodos - 4, diagrama.cantidad_nodos - 2)
                        valor1_anidado = False

                    valor1_anidado = True

                    i+=1
                    contador+=1
                #Si el valor2 de la operacion es resultado de la operacion anterior
                elif operacion.valor2_aninado and operacion.valor1_aninado == False:
                    diagrama.agregar_nodo(str(operacion.valor1))
                    diagrama.agregar_nodo(operacion_siguiente.tipo_operacion + "\n" + str(operacion_siguiente.resultado))
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 2)
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                    i+=1
                    contador+=1
                
                #Si ambos valores de la operacion son resultado de operaciones anteriores
                elif operacion.valor1_aninado and operacion.valor2_aninado:
                    diagrama.agregar_nodo(operacion_siguiente.tipo_operacion + "\n" + str(operacion_siguiente.resultado))
                    diagrama.agregar_nodo(operacion_siguiente2.tipo_operacion + "\n" + str(operacion_siguiente2.resultado))
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 2)
                    doble_anidado = True
                    valor1_anidado = True
                    i+=1
                    contador+=2
            
            #Para operaciones con un solo valor
            else:

                #Si el valor1 de la operacion es resultado de la operacion anterior
                if operacion.valor1_aninado:
                    diagrama.agregar_nodo(operacion_siguiente.tipo_operacion + "\n" + str(operacion_siguiente.resultado))
                    if valor1_siguiente_un_nodo == False:
                        diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                    else:
                        diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                        valor1_siguiente_un_nodo = False
                    i+=1
                    contador+=1


                
        #Si ninguno de los valores de la operacion son resultado de operaciones anteriores quiere decir que es la ultima operacion
        else:
            #Si es solo un valor
            if operacion.valor2 == None:
                diagrama.agregar_nodo(str(operacion.valor1))
                if valor1_siguiente_un_nodo == False:
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 2, diagrama.cantidad_nodos - 1)
                else:
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                    valor1_siguiente_un_nodo = False
                i=0
                contador+=1
            #Si son dos valores
            else:

                diagrama.agregar_nodo(str(operacion.valor1))
                diagrama.agregar_nodo(str(operacion.valor2))

                if valor1_anidado == False:
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 1)
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 3, diagrama.cantidad_nodos - 2)
                else:
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 4, diagrama.cantidad_nodos - 1)
                    diagrama.agregar_arista(diagrama.cantidad_nodos - 4, diagrama.cantidad_nodos - 2)
                    valor1_anidado = False
                i=0
                contador+=1



def obtener_valor(tokens, diagrama, tipo):
    global lista_operaciones, nivel, numero_operacion
    i = 0
    valor = None

    valor_anidado = False

    while i < len(tokens):
        token = tokens[i]

        if token.tipo == "numero":
            valor = float(token.valor) if token.tipo == "numero" else token.valor
            return valor, i + 1, valor_anidado

        elif token.tipo == "corchete_abierto":
            i += 4
            operacion_tipo = tokens[i].valor
            valor_anidado = True

            if operacion_tipo in ["suma", "resta", "multiplicacion", "division", "mod", "potencia", "raiz"]:
                i += 4
                valor1 = obtener_valor(tokens[i:], diagrama, "valor1")
                i += valor1[1]
                valor2 = obtener_valor(tokens[i:], diagrama, "valor2")
                i += valor2[1]
                resultado = realizar_operacion(operacion_tipo, valor1[0], valor2[0], diagrama)
                valor = resultado
                operacion_nueva = Operacion(operacion_tipo, valor1[0], valor1[2], valor2[0], valor2[2], resultado, numero_operacion)
                lista_operaciones.append(operacion_nueva)
                nivel += 1

                return valor, i + 1, valor_anidado

            elif operacion_tipo in ["seno", "coseno", "tangente", "inverso"]:
                i += 4
                valor1 = obtener_valor(tokens[i:], diagrama, "valor1")
                i += valor1[1]
                resultado = realizar_operacion_avanzada(operacion_tipo, valor1[0], diagrama)
                valor = resultado
                operacion_nueva = Operacion(operacion_tipo, valor1[0], valor1[2], None, None, resultado, numero_operacion)
                lista_operaciones.append(operacion_nueva)
                nivel += 1
                return valor, i + 1, valor_anidado
            

        i += 1

    return valor, i, valor_anidado



def realizar_operacion(operador, valor1, valor2, diagrama):
    if operador == "suma":
        return valor1 + valor2
    elif operador == "resta":
        #print("Resultado de la resta", (valor1 - valor2))
        return valor1 - valor2
    elif operador == "multiplicacion":
        #print("Resultado de la multiplicación", (valor1 * valor2))
        return valor1 * valor2
    elif operador == "potencia":
        #print("Resultado de la potencia", (valor1 ** valor2))
        return valor1 ** valor2
    
    elif operador == "raiz":
        #print("Resultado de la raiz", (valor1 ** (1/valor2)))
        return valor1 ** (1/valor2)
    
    elif operador == "division":
        if valor2 == 0:
            print("Error: División por cero")
            return None
        #print("resultado de la división", (valor1 / valor2))
        return valor1 / valor2
    elif operador == "mod":
        if valor2 == 0:
            print("Error: División por cero")
            return None
        #print("resultado del módulo", (valor1 % valor2))
        return valor1 % valor2
    
    else:
        print(f"Error: Operación no válida: {operador}")
        return None
    
def realizar_operacion_avanzada(operacion, valor1, diagrama, valor2=None):
    if operacion == "seno":
        #print("resultado del seno", math.sin(math.radians(valor1)))
        return math.sin(math.radians(valor1))
    elif operacion == "coseno":
        #print("resultado del coseno", math.cos(math.degrees(valor1)))
        return math.cos(math.radians(valor1))
    
    elif operacion == "tangente":
        #print("resultado de la tangente", math.tan(math.degrees(valor1)))
        return math.tan(math.radians(valor1))
    elif operacion == "inverso":
        #print("resultado del inverso", (1/valor1))
        return 1/valor1

    else:
        print(f"Error: Operación no válida: {operacion}")
        return None
