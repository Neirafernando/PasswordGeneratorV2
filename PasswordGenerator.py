from cryptography.fernet import Fernet
import string
import random

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for i in range(longitud))
    return contraseña

def validar_fortaleza_contraseña(contraseña):
    longitud_minima = 8
    tiene_mayusculas = any(c.isupper() for c in contraseña)
    tiene_minusculas = any(c.islower() for c in contraseña)
    tiene_numeros = any(c.isdigit() for c in contraseña)
    tiene_especiales = any(c in string.punctuation for c in contraseña)
    no_contiene_patron = not (contraseña.lower() in ["123456", "password", "qwerty","jajaja123","111111","abc123"])
    
    puntaje = 0
    if len(contraseña) >= longitud_minima:
        puntaje += 1
    if tiene_mayusculas:
        puntaje += 1
    if tiene_minusculas:
        puntaje += 1
    if tiene_numeros:
        puntaje += 1
    if tiene_especiales:
        puntaje += 1
    if no_contiene_patron:
        puntaje += 1
    
    if puntaje >= 4:
        return "Fuerte"
    elif puntaje >= 3:
        return "Moderada"
    else:
        return "Débil"
    
# Genera una clave de cifrado
def generar_clave_cifrado():
    return Fernet.generate_key()

# Cifra una contraseña utilizando la clave de cifrado
def cifrar_contraseña(contraseña, clave_cifrado):
    fernet = Fernet(clave_cifrado)
    contraseña_cifrada = fernet.encrypt(contraseña.encode())
    return contraseña_cifrada

# Descifra una contraseña utilizando la clave de cifrado
def descifrar_contraseña(contraseña_cifrada, clave_cifrado):
    fernet = Fernet(clave_cifrado)
    contraseña_descifrada = fernet.decrypt(contraseña_cifrada).decode()
    return contraseña_descifrada

# Guarda la contraseña cifrada en un archivo
def guardar_contraseña_en_archivo(contraseña_cifrada, nombre_archivo):
    with open(nombre_archivo, "wb") as archivo:
        archivo.write(contraseña_cifrada)

# Carga la contraseña cifrada desde un archivo
def cargar_contraseña_desde_archivo(nombre_archivo):
    with open(nombre_archivo, "rb") as archivo:
        contraseña_cifrada = archivo.read()
    return contraseña_cifrada

contraseña = None
clave_cifrado=None

# MENU #
while True:
    print("Menú de Opciones:")
    print("1. Generar Contraseña")
    print("2. Verificar Fortaleza")
    print("3. Cifrar y guardar contraseña")
    print("4. Decifrar contraseña")

    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        contraseña = generar_contraseña(longitud)
        print("La contraseña generada es: " + contraseña)
    elif opcion == "2":
        if contraseña is not None:  # Verifica si se ha generado una contraseña antes
            fortaleza = validar_fortaleza_contraseña(contraseña)
            print(f"La fortaleza de la contraseña es: {fortaleza}")
    elif opcion == "3":
        if contraseña is not None:
            if clave_cifrado is None:
                clave_cifrado = generar_clave_cifrado()
            contraseña_cifrada = cifrar_contraseña(contraseña, clave_cifrado)
            nombre_archivo = input("Ingrese el nombre del archivo para guardar la contraseña cifrada: ")
            guardar_contraseña_en_archivo(contraseña_cifrada, nombre_archivo)
            print("Contraseña cifrada y guardada correctamente.")
        else:
            print("Primero debe generar una contraseña.")
        
    elif opcion == "4":
        if clave_cifrado is None:
            print("Primero debe cifrar y guardar una contraseña.")
        else:
            nombre_archivo = input("Ingrese el nombre del archivo con la contraseña cifrada: ")
            contraseña_cifrada = cargar_contraseña_desde_archivo(nombre_archivo)
            contraseña_descifrada = descifrar_contraseña(contraseña_cifrada, clave_cifrado)
            print(f"La contraseña descifrada es: {contraseña_descifrada}")
    
    elif opcion=="5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")



