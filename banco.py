cuentas = {}

class Cuenta:
    siguientenumerocuenta = 1

    def __init__(self, balance_inicial: int = -1):
        if balance_inicial < 100:
            raise Error("No puede abrir una cuenta con saldo menor a 1.00")

        self.numero = Cuenta.siguientenumerocuenta
        Cuenta.siguientenumerocuenta += 1

        self.balance = balance_inicial

    def __str__(self):
        b = "{:0>3}".format(self.balance)
        return "Cuenta(numero={:0>4}, balance={}.{})".format(self.numero, b[:-2], b[-2:])

    def depositar(self, monto: int):
        self.balance += monto

    def retirar(self, monto: int):
        self.balance -= monto

    def transferir_a(self, otra, monto: int):
        self.retirar(monto)
        otra.depositar(monto)


def print_err(*m):
    print("!!!", *m)

def print_info(*m):
    print(">  ", *m)

def print_title(*m):
    print(":", *m)

def input_monto(p: str):
    while True:
        try:
            s = input(p + ": ").strip()
            # Probamos que el número sea interpretable. No hace falta más del número
            float(s)

            partes = s.split(".")

            if len(partes) == 1:
                return int(partes[0] + "00")
            
            return int(partes[0] + "{:0>2}".format(partes[1]))
        
        except ValueError:
            print_err(s, "no es un valor numérico")

def input_int(p: str):
    while True:
        try:
            s = input(p + ": ").strip()
            
            return int(s)
        
        except ValueError:
            return -1

def input_cuenta(p: str):
    while True:
        try:
            s = input(p + ": ").strip()
            
            nrocuenta = int(s)

            if nrocuenta in cuentas:
                return cuentas[nrocuenta]

            print_err("La cuenta", nrocuenta, "no está registrada")
        except ValueError:
            print_err(s, "no es un valor numérico")

def abrircuenta():
    balance = input_monto("Indique el balance inicial de la cuenta")
    c = Cuenta(balance)
    cuentas[c.numero] = c

    print_info("Nueva cuenta creada:", c)

    return c


def retirar():
    cuenta = input_cuenta("Indique el número de la cuenta de la que desea realizar el retiro")
    print_info(cuenta)
    
    monto = input_monto("Indique el monto a retirar")

    if monto > cuenta.balance:
        print_err("El monto es mayor al balance actual de la cuenta")
        return

    cuenta.retirar(monto)

    print_info("Operacion realizada con éxito")
    print_info(cuenta)


def depositar():
    cuenta = input_cuenta("Indique el número de la cuenta en la que desea realizar depositar")
    print_info(cuenta)
    
    monto = input_monto("Indique el monto a depositar")
    cuenta.depositar(monto)

    print_info("Operacion realizada con éxito")
    print_info(cuenta)


def transferir():
    remitente = input_cuenta("Indique el número de la cuenta de la que saldrá el dinero")
    print_info(remitente)

    monto = input_monto("Indique el monto a transferir")
    
    if monto > remitente.balance:
        print_err("El monto es mayor al valance actual de la cuenta")
        return

    receptor = input_cuenta("Indique el número de la cuenta que recibirá el dinero")
    print_info(receptor)
    
    remitente.transferir_a(receptor, monto)

    print_info("Operacion realizada con éxito")
    print_info("Remitente", remitente)
    print_info("Receptor", receptor)


def listarcuentas():
    for nro, c in cuentas.items():
        print_info(c)


c = Cuenta(100000)
cuentas[c.numero] = c

c = Cuenta(25000)
cuentas[c.numero] = c

if __name__ == '__main__':
    opciones = [
        ["Mostrar la cuentas en el sistema", listarcuentas],
        ["Aperutar una cuenta", abrircuenta],
        ["Realizar un depósito", depositar],
        ["Realizar un retiro", retirar],
        ["Realizar una transferencia entre cuentas", transferir],
    ]

    while True:
        print_title("Menú")

        for i, par in enumerate(opciones):
            texto, callback = par
            print("   [{}]".format(i), texto)

        opcion = input_int("Seleccione una opción")
        
        if opcion > -1 and opcion < len(opciones):
            texto, callback = opciones[opcion]

            callback()
        else:
            print_err(opcion, "no está en el menú")
        print()

