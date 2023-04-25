from Clase import Email
import csv
from collections import Counter


def test():
    print("E3 TESTEO\n")
    print("\nDatos correctos: \n[]informatica.fcefn@gmail.com \n[]wicc2019@unsj-cuim.edu \n[]juanLiendro1957@yahoo.com")
    tester = Email()
    print('informatica.fcefn@gmail.com')
    tester.crearCuenta('informatica.fcefn@gmail.com','contrasena1')
    
    print('wicc2019@unsj-cuim.edu')
    tester.crearCuenta('wicc2019@unsj-cuim.edu','contrasena2')
    
    print('juanLiendro1957@yahoo.com')
    tester.crearCuenta('juanLiendro1957@yahoo.com','contrasena2')
    
    print("\nDatos Incorrectos: \n[]informatica.fcefn@gmailcom \n[]wicc2019unsj-cuim.edu")
    
    print('informatica.fcefn@gmailcom')
    tester.crearCuenta('informatica.fcefn@gmailcom','contrasena1')
    
    print('wicc2019unsj-cuim.edu')
    tester.crearCuenta('wicc2019unsj-cuim.edu','contrasena2')

if __name__ == '__main__':
    Mail=Email()
    
    print("E1\n")
    nom = input("Ingresa el nombre: ")
    correo = input("Ingresa el correo:")
    contra=input("Ingresa la contraseña: ")
    Mail.crearCuenta(correo,contra)
    
    print("E2\n")
    Mail.modificaContra()
    
    test()
    
    print("E4\n")
    cont = 0
    path_archivo='./Correos.csv'
    archivo = open(path_archivo,"r")
    reader = csv.reader(archivo,delimiter=',')
    id=input('Ingrese identificador a buscar: ')
    for fila in reader:
       if fila[1] == id:
           cont += 1
    print("La cantidad de personas con el identificador '{}' es: {}".format(id,cont))
    if cont > 1:
       print("El identificador se repite")
    else:
       print("El identificador no se repite")
    archivo.close()

    