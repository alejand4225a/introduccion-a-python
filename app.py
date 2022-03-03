#variables
from array import array


nombrepersona = "ALEJANDRO" #string
edad = 21 #int
numerodecimal = 10.14 #float
esmayoredad = True #false boolean 

#Debug
print(nombrepersona) #ALEJANDRO

#Array arreglo listas []

diasemana = ['lunes','martes','miercoles','jueves', 'viernes']

print(diasemana[2]) #miercoles

arrayMultiple = [1, 'hola', [5,6,[7,8]]]
print(arrayMultiple[2][1]) #8

#objetos JSON DICCIONARIO {}

persona = {
    'nombre' : 'ALEJANDRO',
    'apellido' : 'MORA',
    'edad': '21',
    'lenguajes':['python','javascript'],
}

print(persona['nombre']) #ALEJANDRO
print(persona['lenguajes'][1]) #javascript

#lista de diccionarios
personas = [
    {
        'nombre' : 'ALEJANDRO',
    'apellido' : 'MORA',
    'edad': '21',
    'lenguajes':['python','javascript'],
    },

    {
        'nombre' : 'poncho',
    'apellido' : 'renteria',
    'edad': '21',
    'lenguajes':['python','net'],
    },

    {
        'nombre' : 'diego',
    'apellido' : 'aldana',
    'edad': '21',
    'lenguajes':['python','go'],
    }
]

print(personas[1]['lenguajes'][1])

#condiciones
if esmayoredad == True:
    print('es mayor de edad ')
else:
    print('no es mayor de edad')

print('terminado')
    