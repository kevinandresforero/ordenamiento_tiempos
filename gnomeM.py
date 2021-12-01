class gnomeM():

    def __init__(self, vector):
        self.i = 0
        self.n = len(vector)
        self.vector = 0

        while self.i<self.n:
            if self.i == 0 or vector[self.i] >= vector[self.i-1]:
                self.i = self.i+1
            else:
                temp = vector[self.i-1]
                vector[self.i-1] = vector[self.i]
                vector[self.i] = temp
                self.i = self.i-1
        self.vector = vector

    def get(self):
        return self.vector

"""lista = [4,110,1,2,6,3,77,456,33,992]
resultado = gnomeM(lista)
print(resultado.get())"""
