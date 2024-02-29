# FIFO (cola)
# LIFO (pila)

class Pila:
    def __init__(self):
        # Inicializa una pila vacía
        self.items = []
    def is_empty(self):
        return self.items == []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            print("La pila está vacía")
            return
        return self.items.pop()
    
    def reset(self):
        self.items = []
        
    def items_show(self):
        print(self.items)


pila = Pila()

pila.items_show()
pila.add(3)
pila.items_show()
pila.add('Sergio Casas')
pila.items_show()
pila.add('mario bros')
pila.items_show()
pila.remove()
pila.items_show()
pila.remove()
pila.items_show()
pila.remove()
pila.items_show()
pila.remove()
pila.items_show()