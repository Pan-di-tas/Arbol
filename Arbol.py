class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz is None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar(nodo_actual.derecha, valor)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo_actual, valor):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._buscar(nodo_actual.izquierda, valor)
        else:
            return self._buscar(nodo_actual.derecha, valor)

    def preOrden(self, nodo_actual):
        if nodo_actual:
            print(nodo_actual.valor, end=' ')
            self.preOrden(nodo_actual.izquierda)
            self.preOrden(nodo_actual.derecha)

    def inOrden(self, nodo_actual):
        if nodo_actual:
            self.inOrden(nodo_actual.izquierda)
            print(nodo_actual.valor, end=' ')
            self.inOrden(nodo_actual.derecha)

    def postOrden(self, nodo_actual):
        if nodo_actual:
            self.postOrden(nodo_actual.izquierda)
            self.postOrden(nodo_actual.derecha)
            print(nodo_actual.valor, end=' ')

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo_actual, valor):
        if nodo_actual is None:
            return nodo_actual

        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminar(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, valor)
        else:
            # Caso 1: nodo sin hijos
            if nodo_actual.izquierda is None and nodo_actual.derecha is None:
                return None
            # Caso 2: nodo con un hijo
            elif nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            # Caso 3: nodo con dos hijos
            else:
                sucesor = self._minimo(nodo_actual.derecha)
                nodo_actual.valor = sucesor.valor
                nodo_actual.derecha = self._eliminar(nodo_actual.derecha, sucesor.valor)
        return nodo_actual

    def _minimo(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo

    def altura(self, nodo_actual):
        if nodo_actual is None:
            return -1
        else:
            altura_izq = self.altura(nodo_actual.izquierda)
            altura_der = self.altura(nodo_actual.derecha)
            return max(altura_izq, altura_der) + 1

    def contarHojas(self, nodo_actual):
        if nodo_actual is None:
            return 0
        if nodo_actual.izquierda is None and nodo_actual.derecha is None:
            return 1
        return self.contarHojas(nodo_actual.izquierda) + self.contarHojas(nodo_actual.derecha)

    def contarNodos(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + self.contarNodos(nodo_actual.izquierda) + self.contarNodos(nodo_actual.derecha)

    def recorrerNiveles(self):
        if self.raiz is None:
            return
        cola = [self.raiz]
        while cola:
            nodo_actual = cola.pop(0)
            print(nodo_actual.valor, end=' ')
            if nodo_actual.izquierda:
                cola.append(nodo_actual.izquierda)
            if nodo_actual.derecha:
                cola.append(nodo_actual.derecha)

    def eliminarArbol(self):
        self.raiz = None

# Ejemplo de uso:
if __name__ == "__main__":
    arbol = Arbol()
    valores = [50, 30, 70, 20, 40, 60, 80]
    print (f"La lista de los valores es: {valores}")

    # Insertar elementos
    for valor in valores:
        arbol.insertar(valor)

    # Recorridos
    print("Recorrido en PreOrden:")
    arbol.preOrden(arbol.raiz)
    print("\nRecorrido en InOrden:")
    arbol.inOrden(arbol.raiz)
    print("\nRecorrido en PostOrden:")
    arbol.postOrden(arbol.raiz)
    
    print("\nRecorrido por Niveles:")
    arbol.recorrerNiveles()

    # Altura
    print(f"\nAltura del árbol: {arbol.altura(arbol.raiz)}")

    # Eliminar un nodo
    arbol.eliminar(70)
    print("\nInOrden después de eliminar 70:")
    arbol.inOrden(arbol.raiz)
