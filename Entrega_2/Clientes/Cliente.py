class Cliente:
    total_clientes = 0

    def __init__(self, nombre, apellido, email, saldo=0):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.saldo = saldo

        Cliente.total_clientes += 1

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"

    def agregar_saldo(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se agregaron ${monto}. Saldo actual: ${self.saldo}")
        else:
            print("El monto debe ser mayor a cero.")

    def realizar_compra(self, monto):
        if monto <= 0:
            print("La compra debe ser mayor a 0.")
        elif monto > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= monto
            print(f"Compra de ${monto} realizada. Saldo restante: ${self.saldo}")
