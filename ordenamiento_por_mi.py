#metodo de ordenamiento hecho a base de logica y lo que se

tam_array=int(input("Ingresa el tamaño del array a ordenar: "))#pido el tamaño del array
array=[]#creo el array
for i in range (tam_array):#este for es para rellenar el array
    numerito=float(input("Ingresa el numero en la pocicion " + str((i+1))+": "))
    array.append(numerito)

print("Numero ingresados")#confirmacion de que se rellenaron
print("\n-----------")
print("El array desordenado es: ",array)#imprimo el array desordenado para que se vea la diferencia

#ordenamiento por logica
def Ordenar(array,tam):
    #llamo a una ves al metodo que hará las operaiciones y el return que tiene es un array que almaceno en un arreglo
    arreglo=metodo(array)
    #con este for es para mandar a llamar al metodo de las operaciones las veces necesarias segun el tamaño del array para que se ordene y vaya actualizando el valor de arreglo
    for i in range(tam):
        arreglo=metodo(arreglo)
    #presento el array ordenado
    print("\n-----------")
    print("El array ordenado es: ", arreglo)

#cerebro de la operacion
def metodo(array):#entra como parametro el array
    numerito=array[0]#variable que se le almacena el primer valor del array par compararlo con los demas y ver si es mayor o no
    #para organizar el array
    for i in range(len(array)):#i hasta la longitud del array
        try:#este try catch es para que no explote el programa, o de error
            if numerito>array[i+1]:#si numerito es mayor a lo que hay en el array en el numero de la vuelta +1
                array[i]=array[i+1]#al array en la pocion de la vuelta le asigna el valor que esta una casilla delante de el, el que sigue en otrass palabras
                array[1+i]=numerito#al siguiente numero se le asigna el valor de numerito que es el que se esta comparando
            else:
                numerito=array[i+1]#este es en caso de que el primer numero sea menor al siguiente numero, de esta manera asigno el valor del siguente numero a numerito
                #para poder ordenar desde ese punto
        #como llega un momento en el que i+1 supera la longitud del array daria error, entoces para compensarlo meti este trycatch, donde intenta lo de arriba
        #si lo logro sin erroes sigue el ciclo, si da un errro pasa al catch donde pasa al ciclo sin dar error
        except:
            pass
    #regreso el array
    return array
   
#mando a llamar los metodos
Ordenar(array,tam_array)