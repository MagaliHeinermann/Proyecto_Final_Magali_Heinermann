from Clientes.Cliente import Cliente

clientes_registrados = {}

def registrar_cliente():
    print("\n=== CREAR CLIENTE (POO) ===")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    saldo = float(input("Saldo inicial: "))

    nuevo = Cliente (nombre, apellido, email, saldo)
    clientes_registrados[email] = nuevo
    print(f"Cliente creado: {nuevo}")

def mostrar_clientes():
    print("\n=== CLIENTES ===")
    if not clientes_registrados:
        print("No hay clientes.")
    else:
        for cliente in clientes_registrados.values():
            print(cliente)
            print(f"Saldo: ${cliente.saldo}")
            print("--------------------------------")
            
def login_usuario():
    print("\n=== INICIAR SESIÓN DE CLIENTE ===")
    
    email_ingresado = input("Ingrese su Email: ")
    
    if email_ingresado in clientes_registrados:
        
        cliente_actual = clientes_registrados[email_ingresado]
        print(f"\n¡Bienvenido, {cliente_actual.nombre} {cliente_actual.apellido}!")
        print(f"Su saldo actual es: ${cliente_actual.saldo}")
        
    else:
        print("\n❌ Error: Email no encontrado. Regístrese primero.")
    
def menu():
    while True:
        print("""
===========================
        MENÚ PRINCIPAL
===========================
1. Registrar Cliente
2. Iniciar sesión de Cliente
3. Mostrar Clientes Registrados
4. Salir
""")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            login_usuario()
        elif opcion == "3":
            mostrar_clientes()
        elif opcion == "4":
            print("Saliendo...¡Hasta luego4")
            break
        else:
            print("Opción inválida.")

menu()