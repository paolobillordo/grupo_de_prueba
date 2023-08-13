class Stack:
    def __init__(self):
        self._data = []
     
    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self.is_empty():
            return self._data.pop()
        else:
            raise IndexError('La pila esta vacia')
    
    def top(self):
        if not self.is_empty():
            return self._data[-1]
        else:
            raise IndexError('La pila esta vacia')
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def display(self):
        print("La pila tiene los siguientes elementos:")
        return [ print(i) for i in reversed(self._data) ]