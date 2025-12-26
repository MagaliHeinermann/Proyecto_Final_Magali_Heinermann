# Diccionario para almacenar los usuarios (clave: usuario, valor: contraseña)
usuarios = {}

# Función para registrar y guardar usuarios
def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")
    usuario = input("Ingrese su nombre de usuario: ")

    # Verificar si el usuario ya existe
    if usuario in usuarios:
        print("El nombre de usuario ya está registrado.")
    else:
        contraseña = input("Ingrese su contraseña: ")
        usuarios[usuario] = contraseña
        print(f"Usuario '{usuario}' registrado correctamente.")

# Función para mostrar los usuarios registrados
def mostrar_usuarios():
    print("\n=== LISTA DE USUARIOS REGISTRADOS ===")

    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for nombre in usuarios:
            print(f"- {nombre}")

# Función para iniciar sesión (login)
def login_usuario():
    print("\n=== INICIO DE SESIÓN ===")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    # Validación de los datos
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"Bienvenido/a, {usuario}!")
    elif usuario in usuarios:
        print("Contraseña incorrecta.")
    else:
        print("El usuario no existe. Primero debe registrarse.")

# Función principal del programa
def menu_principal():
    while True:
        print("""
==========================
        MENÚ LOGIN
==========================
1. Registrar usuario
2. Iniciar sesión
3. Mostrar usuarios registrados
4. Salir
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login_usuario()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecución del programa
menu_principal()
