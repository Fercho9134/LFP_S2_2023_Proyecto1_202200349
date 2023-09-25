from graphviz import Digraph

class Diagrama:
    def __init__(self, nombre, fondo, fuente, forma):
        self.dot = Digraph(comment=nombre, format='png')
        self.cantidad_nodos = 0
        self.fondo = fondo
        self.fuente = fuente
        self.forma = forma

    def agregar_nodo(self, informacion):
        self.dot.node(str(self.cantidad_nodos), informacion, style = "filled", fillcolor = self.fondo, fontcolor = self.fuente, shape = self.forma)
        self.cantidad_nodos += 1
        
    def agregar_arista(self, nodo1, nodo2):
          self.dot.edge(str(nodo1), str(nodo2))

    def guardar(self):
        self.dot.render("RESULTADOS_202200349", view=True)

    def ultimo_nodo(self):
        return f"nodo{self.cantidad_nodos - 1}"