# Almacena todas las cuentas activas en la aplicacion (tempDB)
cuentas = {}

# Creacion de la clase cuenta
class Cuenta:
    siguientenumerocuenta = 1

    # Constuctor de los objetos de la clase cuenta
    def __init__(self, balance_inicial: int = -1):
        if balance_inicial < 100:
            raise Error("No puede abrir una cuenta con saldo menor a 1.00")

        self.numero = Cuenta.siguientenumerocuenta
        Cuenta.siguientenumerocuenta += 1

        self.balance = balance_inicial

    # Devuelve le informacion del objeto de forma legible
    def __str__(self):
        b = "{:0>3}".format(self.balance)
        return "Cuenta(numero={:0>4}, balance={}.{})".format(self.numero, b[:-2], b[-2:])

    # Metodo que aumenta el balance de la cuenta
    def depositar(self, monto: int):
        self.balance += monto

    # Metodo que disminuye el balance de la cuenta
    def retirar(self, monto: int):
        self.balance -= monto

    # Metodo que transfiere el monto de una cuenta a otra
    def transferir_a(self, otra, monto: int):
        self.retirar(monto)
        otra.depositar(monto)

# Formatea el mensaje para que incluya '!!!' al inicio de un error
def print_err(*m):
    print("!!!", *m)

# Formatea el mensaje para que incluya '>' al inicio
def print_info(*m):
    print(">  ", *m)

# Formatea el mensaje para que incluya ':' al inicio de un titulo
def print_title(*m):
    print(":", *m)

# Funcion que recibe un texto que se va a mostrar en la terminal, captura el monto escrito por el cliente y devuelve el resultado.
def input_monto(p: str):
    while True:
        try:
            # Imprime en la terminal el mensaje recibido como parametro y se mantiene escuchando para capturar el teclado
            s = input(p + ": ").strip()
            # Probamos que el número sea interpretable. No hace falta más del número
            float(s)

            # Se quita el punto decimal para trabajarlo como un entero
            partes = s.split(".")

            # Se verifica que el numero ingresado no contiene decimales
            if len(partes) == 1:
                return int(partes[0] + "00")
            
            # Se retorna el numero que paso de decimal a entero
            return int(partes[0] + "{:0>2}".format(partes[1]))
        
        except ValueError:
            # Gestion de error en caso que no sea valor numerico
            print_err(s, "no es un valor numérico")

# Funcion que recibe un texto que se va a mostrar en la terminal, captura un numero del cliente y devuelve el resultado.
def input_int(p: str):
    while True:
        try:
            # Imprime en la terminal el mensaje recibido como parametro y se mantiene escuchando para capturar el teclado
            s = input(p + ": ").strip()
            
            # Retorna el entero recibido
            return int(s)
        except ValueError:
            # Gestion de error en caso que no sea valor numerico
            return -1

# Funcion que recibe un texto que se va a mostrar en la terminal, captura el numero de cuenta escrito por el cliente y devuelve el resultado.
def input_cuenta(p: str):
    while True:
        try:
            # Imprime en la terminal el mensaje recibido como parametro y se mantiene escuchando para capturar el teclado
            s = input(p + ": ").strip()
            
            # Asigna el numero recibido a la variable nrocuenta
            nrocuenta = int(s)

            # Verifica que el numero de cuenta exista en la tempDB
            if nrocuenta in cuentas:
                return cuentas[nrocuenta]

            # Arroja el error de 'Cuenta no registrada' si no la consigue en la tem db
            print_err("La cuenta", nrocuenta, "no está registrada")
        except ValueError:
            # Gestion de error en caso que no sea valor numerico
            print_err(s, "no es un valor numérico")

# Callback de la opcion 1, que recibe los datos del monto con el que se va a aperturar la cuenta.
def abrircuenta():
    # Captura el monto que se desea depositar en la apertura de la cuenta.
    balance = input_monto("Indique el balance inicial de la cuenta")

    # Crea un nuevo objeto de la clase Cuenta con el balence inicial capturado anteriormente
    c = Cuenta(balance)

    # Se agrega la cuenta a la tempDB
    cuentas[c.numero] = c

    # Detalla el estado de la operacion y el balance de la cuenta relacionada.
    print_info("Nueva cuenta creada:", c)

    return c

# Callback de la opcion 2, que recibe los datos del receptor y monto para realizar un deposito en la cuenta.
def depositar():
    # Captura el numero que se desea como receptor y devuelve el objeto de la cuenta.
    cuenta = input_cuenta("Indique el número de la cuenta en la que desea realizar depositar")
    print_info(cuenta)
    
    # Captura el monto que se desea retirar.
    monto = input_monto("Indique el monto a depositar")

    # Llamada al metodo que realiza el deposito de la cuenta
    cuenta.depositar(monto)

    # Detalla el estado de la operacion y el balance de la cuenta relacionada.
    print_info("Operacion realizada con éxito")
    print_info(cuenta)

# Callback de la opcion 3, que recibe los datos del remitente y monto para realizar el retiro de la cuenta.
def retirar():
    # Captura el numero que se desea como remitente y devuelve el objeto de la cuenta.
    cuenta = input_cuenta("Indique el número de la cuenta de la que desea realizar el retiro")
    print_info(cuenta)
    
    # Captura el monto que se desea retirar.
    monto = input_monto("Indique el monto a retirar")

    # Verifica que el monto que se desea retirar esta disponible en el balance del remitente
    if monto > cuenta.balance:
        print_err("El monto es mayor al balance actual de la cuenta")
        return

    # Llamada al metodo que realiza el retiro de la cuenta
    cuenta.retirar(monto)

    # Detalla el estado de la operacion y el balance de la cuenta relacionada.
    print_info("Operacion realizada con éxito")
    print_info(cuenta)

# Callback de la opcion 4, que recibe los datos de remitente, receptor y monto para realizar una transferencia entre cuenta.
def transferir():
    # Captura el numero que se desea como remitente y devuelve el objeto de la cuenta.
    remitente = input_cuenta("Indique el número de la cuenta de la que saldrá el dinero")
    print_info(remitente)

    # Captura el monto que se desea transferir.
    monto = input_monto("Indique el monto a transferir")
    
    # Verifica que el monto que se desea transferir esta disponible en el balance del remitente
    if monto > remitente.balance:
        print_err("El monto es mayor al valance actual de la cuenta")
        return

    # Captura el numero que se desea como receptor y devuelve el objeto de la cuenta.
    receptor = input_cuenta("Indique el número de la cuenta que recibirá el dinero")
    print_info(receptor)
    
    # Llamada al metodo que realiza la transferencia entre las cuentas
    remitente.transferir_a(receptor, monto)

    # Detalla el estado de la operacion y el balance de las cuentas relacionadas.
    print_info("Operacion realizada con éxito")
    print_info("Remitente", remitente)
    print_info("Receptor", receptor)

# Funcion que lista todas las cuentas
def listarcuentas():
    for nro, c in cuentas.items():
        print_info(c)

# Cuentas predeterminadas
c = Cuenta(100000)
cuentas[c.numero] = c

c = Cuenta(25000)
cuentas[c.numero] = c

# Menu
if __name__ == '__main__':
    # Lista de opciones del menu junto al callback de cada opcion
    opciones = [
        ["Mostrar la cuentas en el sistema", listarcuentas],
        ["Aperutar una cuenta", abrircuenta],
        ["Realizar un depósito", depositar],
        ["Realizar un retiro", retirar],
        ["Realizar una transferencia entre cuentas", transferir],
    ]

    # Ciclo que activa el menu.
    while True:
        print_title("Menú")

        #Imprime en la consola las opciones
        for i, par in enumerate(opciones):
            texto, callback = par
            print("   [{}]".format(i), texto)

        # Captura la opcion escrita por el cliente
        opcion = input_int("Seleccione una opción")
        
        # Selecciona la opcion escogida por el cliente
        if opcion > -1 and opcion < len(opciones):
            texto, callback = opciones[opcion]
            callback()
        # Arroja el error en caso que se escriba una opcion que no esta disponoble
        else:
            print_err(opcion, "no está en el menú")
        print()

