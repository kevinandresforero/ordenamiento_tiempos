import time as t
from gnomeM import gnomeM
from shell import shell

arr = input("Ingrese el arreglo que quiere ordenar: \n")
arr = arr.split()

i = 0
for v in arr:
    arr[i] = int(v)
    i = i + 1

i_g = t.time()
resultado_gnome = gnomeM(arr)
f_g = t.time()
t_gnome = f_g - i_g

i_s = t.time()
resultado_shell = shell(arr)
f_s = t.time()
t_shell = f_s - i_s


print("\nGnome",resultado_gnome.get(), " tiempo: " , t_gnome)
print("\nShell",resultado_shell.get(), " tiempo: " , t_shell)


'''
110 22 55 44 990 99
'''
