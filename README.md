# nanoWallet

Es un proyecto de prueba con objetivo de manipular valores numéricos con alta precisión.

## Autores
Los autores y colaboradores se encuentran en [AUTHORS.md](https://github.com/JAfricanoT/nanoWallet/blob/main/AUTHORS.md)

Para contribuir en el proyecto es importante leer el archivo [AUTHORS.md](https://github.com/JAfricanoT/nanoWallet/blob/main/CONTRIBUTING.md)

## Usos

La nanoWallet permite la administracion de cuentas, por defecto se puede operara entre las cuentas usando la modalidad ***"Invitado"***, donde se solicitará todos los valores necesarios para cada operacion. Sin embargo, se puede iniciar sesion y entrar en la modalidad ***"Usuario"***, la cual permite crear una sesion y facilita operar entre la cuenta solicitando solo la minima informacion necesaria.

### Invitado

El menú general contiene las siguientes operaciones:

 0. Mostrar la cuentas en el sistema
 1. Aperturar una cuenta
 2. Realizar un depósito
 3. Realizar un retiro
 4. Realizar una transferencia entre cuentas
 5. Comenzar una sesión

#### Mostrar la cuentas en el sistema

Se listan todas las cuentas activas en el sistema visualizándose junte a ellas su identificador único y el balance.

#### Aperturar una cuenta

Solicita el monto inicial de la cuenta que se desea aperturar.

Para ello se solicitaran los siguientes valores:
- Cedula: Solo se admiten números.
- Nombre: Propietario de la cuenta.
- Clave especial: Debe contener al menos 8 caracteres.
- Balance inicial: Debe ser mayor a 1.

#### Realizar un depósito

Solicita el numero de cuenta del receptor y el monto que se desea depositar.

Para realizar un deposito debe contar con:
- No. Cuenta: Cuenta a donde se va a depositar.
- Monto: Debe ser un numero positivo y no puede ser 0

#### Realizar un retiro

Solicita el numero de cuenta del remitente y el monto que se desea retirar.

Para realizar un retiro debe contar con:
- No. Cuenta: Cuenta a donde se va a depositar.
- Monto: Debe ser un numero positivo y no puede ser 0

#### Realizar una transferencia entre cuentas

Solicita el numero de cuenta del remitente, el monto que se desea depositar y el numero de cuenta del receptor.

> :warning: **Advertencia**: Solo se puede hacer transferencias entre cuentas previamente creadas.

#### Comenzar sesión

Permite agilizar el proceso al momento de realizar operaciones con una misma cuenta.

Al momento de iniciar sesión se deben completar las siguiente solicitudes:
- No. Cuenta: Cuenta a la cual se va a iniciar.
- Clave especial: Se debe ingresar la clave especial previamente registrada.

> :warning: **Advertencia**: Cuando se inicia sesion las operaciones se realizaran al rededor de la cuenta iniciada.

### Usuario

El menú de sesión contiene las siguientes operaciones:

 0. Realizar un depósito
 1. Realizar un retiro
 2. Realizar una transferencia entre cuentas
 3. Cerrar sesión

Para operar es tan sencillo como escribir el numero de la opción que desea ejecutar.
