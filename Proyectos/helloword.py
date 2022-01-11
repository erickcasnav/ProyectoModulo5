a,b=0,1
print("Secuencia de Fibonacci por Erick Castro")

limite=input("Escriba el limite")
while True:
    print (str(a)+" ",end="")
    a,b=b,a+b
    if a>int(limite):
        break
