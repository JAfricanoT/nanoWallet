from hashlib import sha1

# Almacena todas las cuentas activas en la aplicación (tempDB)
cuentas = {}

# Cuentas en sesión. Se usa un dict + SESION_ID para evitar tener que lidiar con el keyword global
SESION_ID = 0
sesiones = {SESION_ID: None}


def esta_ci_registrada(ci: int):
    """
    Verifica si una C.I. está registrada.

    :param ci: La C.I. a buscar.
    """

    for c in cuentas.values():
        if c.cedula == ci:
            return True
    return False


def format_centavos(monto: int) -> str:
    """
    Formatea el monto ingresado de centavos a enteros.
    
    :param monto: El monto en centavos.
    """

    b = "{:0>3}".format(monto)

    return "{}.{}".format(b[:-2], b[-2:])


def hash_clave(clave: str):
    """
    Facilita crear el hash de una clave especial.
    
    :param clave: Clave en texto plano.
    """
    return sha1(clave.strip().encode()).hexdigest()


def print_err(*m):
    """
    Imprime los mensajes de error formateados.

    :param *m: Valores a mostrar
    """
    print("!!!", *m)


def print_info(*m):
    """
    Imprime los mensajes informativos formateados.

    :param *m: Valores a mostrar
    """
    print(">  ", *m)


def print_title(*m):
    """
    Imprime los títulos formateados.

    :param *m: Valores a mostrar
    """
    print(":", *m)


class Cuenta:
    """
    Encapsula la información y las operaciones de cada cuenta.
    
    Cada cuenta tiene una clave especial que le permite al propietario validar operaciones.
    Esta clave se almacena en forma de hash, tal que no quede registro de la clave original en texto plano.

    Nótese ninguna de la operaciones realiza validación directamente, sino que se deja de parte del programador.
    """
    siguiente_numero_cuenta = 1

    def __init__(self,
                 nombre: str,
                 cedula: int,
                 clave_especial: str,
                 balance_inicial: int = -1
                 ):
        """
        Construye los objetos de la clase Cuenta.
        
        :param nombre: Nombre del propietario de la :class:`Cuenta`
        :param cedula: C.I. del propietario :class:`Cuenta`
        :param clave_especial: La clave que se usará para autorizar operaciones
        :param balance_inicial: El balance inicial de la cuenta en centavos
        :raises ValueError: cuando el balance inicial es menor a 1.00
        """
        if balance_inicial < 100:
            raise ValueError("No puede abrir una cuenta con saldo menor a 1.00")

        self.numero = Cuenta.siguiente_numero_cuenta
        Cuenta.siguiente_numero_cuenta += 1

        self.nombre = nombre
        self.cedula = cedula
        self.clave_especial = hash_clave(clave_especial)
        self.balance = balance_inicial

    def __str__(self):
        """Devuelve le información del objeto de forma legible""" 
        return "Cuenta(numero={:0>4}, nombre={}, ci={}, balance={})".format(self.numero, self.nombre, self.cedula, format_centavos(self.balance))

    def validar_clave(self, clave: str):
        """Método que indica si una clave especial es válida""" 
        return self.clave_especial == hash_clave(clave)
    
    def cambiar_clave(self, clave: str):
        """Método que cambia la clave especial""" 
        
        self.clave_especial == hash_clave(clave)

        return 

    def depositar(self, monto: int):
        """Método que aumenta el balance de la cuenta""" 
        self.balance += monto

    def retirar(self, monto: int):
        """Método que disminuye el balance de la cuenta""" 
        self.balance -= monto

    def transferir_a(self, otra, monto: int):
        """Método que transfiere el monto de una cuenta a otra""" 
        self.retirar(monto)
        otra.depositar(monto)


def input_str(p: str):
    """
    Función que recibe un texto que se va a mostrar en la terminal.
    

    Esta función es trivial, pero garantiza una TUI consistente.
    """
    return input(p + ": ").strip()


def input_monto(p: str):
    """Función que recibe un texto que se va a mostrar en la terminal, captura el monto escrito por el cliente y devuelve el resultado"""
    while True:
        try:
            # Imprime en la terminal el mensaje recibido como parámetro y se mantiene escuchando para capturar el teclado
            s = input_str(p)
            # Probamos que el número sea interpretable. No hace falta más del número
            float(s)

            # Se quita el punto decimal para trabajarlo como un entero
            entera, _, decimales = s.partition(".")

            # Se retorna el numero que paso de decimal a entero
            return int(entera + "{:0<2}".format(decimales[:2]))
        
        except ValueError:
            # Gestión de error en caso que no sea valor numérico
            print_err(s, "no es un valor numérico")


def input_int(p: str):
    """Función que recibe un texto que se va a mostrar en la terminal, captura un numero del cliente y devuelve el resultado"""
    while True:
        try:
            # Imprime en la terminal el mensaje recibido como parámetro y se mantiene escuchando para capturar el teclado
            s = input_str(p)
            
            # Retorna el entero recibido
            return int(s)
        except ValueError:
            # Gestión de error en caso que no sea valor numérico
            return -1


def input_cuenta(p: str) -> Cuenta:
    """Función que recibe un texto que se va a mostrar en la terminal, captura el numero de cuenta escrito por el cliente y devuelve el resultado"""
    while True:
        try:
            # Imprime en la terminal el mensaje recibido como parámetro y se mantiene escuchando para capturar el teclado
            s = input_str(p)
            
            # Asigna el numero recibido a la variable nrocuenta
            nrocuenta = int(s)

            # Verifica que el numero de cuenta exista en la tempDB
            if nrocuenta in cuentas:
                return cuentas[nrocuenta]

            # Arroja el error de 'Cuenta no registrada' si no la consigue en la tem db
            print_err("La cuenta", nrocuenta, "no está registrada")
        except ValueError:
            # Gestión de error en caso que no sea valor numérico
            print_err(s, "no es un valor numérico")


def input_nuevaclave():
    while True:
        clave = input_str("Indique la clave especial (debe tener al menos 8 caracteres, sin empezar ni terminar en espacios)")
        if len(clave) < 8:
            print_err("La clave especial debe tener al menos 8 caracteres y no empezar ni terminar en espacios")
            continue
        
        if clave == input("Por favor repita su clave especial: ").strip():
            return clave
        else: 
            print_err("Las dos versiones de la clave especial no coinciden")

def empezar_sesion():
    """Empieza una sesión"""
    c = input_cuenta("Seleccione un cuenta para empezar su sesión")

    clave = input_str("Indique su clave especial")
    if c.validar_clave(clave):
        sesiones[SESION_ID] = c 
        print_info("Sesión iniciada para", c)
    else:
        print_err("Clave inválida")


def cerrar_sesion():
    """Cierra una sesión"""
    sesiones[SESION_ID] = None
    print_info("Sesión cerrada")


def abrircuenta():
    """Recibe los datos del monto con el que se va a aperturar la cuenta"""
    
    ci = input_int("Indique la C.I. del propietario o la propietaria")
    if esta_ci_registrada(ci):
        print_err("Ya hay una cuenta con esta C.I. registrada")
        return

    nombre = input("Indique el nombre del propietario o la propietaria de la cuenta: ").strip()
    clave = input_nuevaclave()

    # Captura el monto que se desea depositar en la apertura de la cuenta.
    balance = input_monto("Indique el balance inicial de la cuenta")

    # Crea un nuevo objeto de la clase Cuenta con el balance inicial capturado anteriormente
    c = Cuenta(nombre, ci, clave, balance)

    # Se agrega la cuenta a la tempDB
    cuentas[c.numero] = c

    # Detalla el estado de la operación y el balance de la cuenta relacionada.
    print_info("Nueva cuenta creada:", c)

    return c


def depositar():
    """Recibe los datos del receptor y monto para realizar un deposito en la cuenta"""

    cuenta = sesiones[SESION_ID]
    if cuenta == None:
        # Captura el numero que se desea como receptor y devuelve el objeto de la cuenta.
        cuenta = input_cuenta("Indique el número de la cuenta en la que desea realizar depositar")
    print_info(cuenta)
    
    # Captura el monto que se desea retirar.
    monto = input_monto("Indique el monto a depositar")

    # Llamada al método que realiza el deposito de la cuenta
    cuenta.depositar(monto)

    # Detalla el estado de la operación y el balance de la cuenta relacionada.
    print_info("Operación realizada con éxito")
    print_info(cuenta)


def retirar():
    """Recibe los datos del remitente y monto para realizar el retiro de la cuenta"""

    cuenta = sesiones[SESION_ID]
    if cuenta == None:
        # Captura el numero que se desea como remitente y devuelve el objeto de la cuenta.
        cuenta = input_cuenta("Indique el número de la cuenta de la que desea realizar el retiro")
    print_info(cuenta)

    # Captura el monto que se desea retirar.
    monto = input_monto("Indique el monto a retirar")

    # Verifica que el monto que se desea retirar esta disponible en el balance del remitente
    if monto > cuenta.balance:
        print_err("El monto es mayor al balance actual de la cuenta")
        return

    # De haber una sesión activa, validamos la clave especial
    if sesiones[SESION_ID] != None:
        clave = input_str(f"Por favor indique su clave especial para autorizar un retiro de {format_centavos(monto)}")
        if not cuenta.validar_clave(clave):
            print_err("Clave especial no coincide con la clave de la cuenta")
            return

    # Llamada al método que realiza el retiro de la cuenta
    cuenta.retirar(monto)

    # Detalla el estado de la operación y el balance de la cuenta relacionada.
    print_info("Operación realizada con éxito")
    print_info(cuenta)


def transferir():
    """Recibe los datos de remitente, receptor y monto para realizar una transferencia entre cuenta"""

    remitente = sesiones[SESION_ID]
    if remitente == None:    
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
    
    # De haber una sesión activa, validamos la clave especial
    if sesiones[SESION_ID] != None:
        clave = input_str(f"Por favor indique su clave especial para autorizar un una transferencia de {format_centavos(monto)} a la cuenta nro. {receptor.numero}")
        if not remitente.validar_clave(clave):
            print_err("Clave especial no coincide con la clave de la cuenta remitente")
            return

    # Llamada al método que realiza la transferencia entre las cuentas
    remitente.transferir_a(receptor, monto)

    # Detalla el estado de la operación y el balance de las cuentas relacionadas.
    print_info("Operación realizada con éxito")
    print_info("Remitente", remitente)
    print_info("Receptor", receptor)


def listarcuentas():
    """Función que lista todas las cuentas""" 
    for nro, c in cuentas.items():
        print_info(c)


# Cuentas predeterminadas
c = Cuenta("Gustavo Lopez", 20000001, "its over anakin", 100000)
cuentas[c.numero] = c

c = Cuenta("Josefrancisco Africano", 20000002, "i have the high ground", 100000)
cuentas[c.numero] = c

# Menu
if __name__ == '__main__':
    # Lista de opciones del menu junto al callback de cada opción
    opciones_general = [
        ["Mostrar la cuentas en el sistema", listarcuentas],
        ["Aperturar una cuenta", abrircuenta],
        ["Realizar un depósito", depositar],
        ["Realizar un retiro", retirar],
        ["Realizar una transferencia entre cuentas", transferir],
        ["Comenzar sesión", empezar_sesion],
    ]

    opciones_sesion = [
        ["Realizar un depósito", depositar],
        ["Realizar un retiro", retirar],
        ["Realizar una transferencia entre cuentas", transferir],
        ["Cerrar sesión", cerrar_sesion],
    ]

    # Ciclo que activa el menu.
    while True:
        # Para evitar tener que separa el código en varios scripts, se incluye
        if sesiones[SESION_ID] == None:
            print_title("Menú")
        else:
            print_title("Menú para:", sesiones[SESION_ID])

        opciones = opciones_general if sesiones[SESION_ID] == None else opciones_sesion

        #Imprime en la consola las opciones
        for i, par in enumerate(opciones):
            texto, callback = par
            print("   [{}]".format(i), texto)

        # Captura la opción escrita por el cliente
        opcion = input_int("Seleccione una opción")
        
        # Selecciona la opcion escogida por el cliente
        if opcion > -1 and opcion < len(opciones):
            texto, callback = opciones[opcion]
            callback()
        # Arroja el error en caso que se escriba una opcion que no esta disponible
        else:
            print_err("La opción", opcion, "no está en el menú")
        print()

