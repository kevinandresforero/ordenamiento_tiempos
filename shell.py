class shell():

    def __init__(self, lista):

        self.listag = 0
        inc=1
        tam=len(lista)
        for inc in range(1,tam,inc*3+1):
            while inc>0:
                for i in range(inc,tam):
                    j=i
                    temp=lista[i]
                    while j>=inc and lista[j-inc]>temp:
                        lista[j]=lista[j-inc]
                        j=j-inc
                    lista[j]=temp
                inc=inc//2
        self.listag=lista

    def get(self):
        return self.listag


'''lista = [4,110,1,2,6,3,77,456,33,992]
r = shell(lista)
print(r.get())'''
















'''vector = [50,2,5,10,9,11,1,25,19]
N = len(vector)
n = N
i = 0

while(N-n >= 0):
    n = n//2
    try:
        if vector[i] < vector[n]:
            print(vector[i],i," es menor que ",vector[n],n)
            i = i+1
            n = n+1
        else:
            if(i+n <= N):
                print(vector[i],i," es MAYOR que ",vector[n], n)
                aux = vector[i]
                vector[i] = vector[n]
                vector[n] = aux
                print(vector)
            #   recursiva
            i = i+1
            n = n+1
    except:
        break

print(vector)
'''
