stack = []
def push(item,capacity):
    if not isFull(capacity):
        stack.append(item)
        return "Elemento apilado..."
    return "Pila llena..."

def isFull(capacity):
    return len(stack) == capacity 

def peek():
    if not isEmpty():
        return stack[-1]
    return "Pila vacía..."

def pop():
    if not isEmpty():
        return stack.pop()
    return "Pila vacía..."

def isEmpty():
    return not len(stack)

def show():
    message = ""
    for item in reversed(stack):
        message += f"=={item :>6}   == \n"
        message += f"=============\n"
    return message

while True:
    print("Elija la opcion: \n1. Apilar caja \n2. Desapilar \n3.Consultar tope \n4.Mostrar pila \n5.Salir")
    opcion = int(input())
    if opcion == 1:
        capacity = int(input("Dime el tamaño de la pila: "))
        while True:
            item = input("Dime un valor:")
            print(push(item, capacity))
            answer = input("Desea ingresar otro valor [S | N]: ")
            if answer.lower() == "n":
                break 
    elif opcion == 2:
        while True:
            answer = input("Desea desapilar [S | N]: ")
            if answer.lower() == "si":
               print(pop())
            elif answer.lower() == "n":
                break
            else:
                 print("Opcion invalida")
    elif opcion == 3:
        print("Mostrar tope\n", peek())
    elif opcion == 4:
        print(show())
    elif opcion == 5:
        break
    else: 
        print("Opcion invalida")