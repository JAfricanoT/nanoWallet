# nanoWallet

Es un proyecto de prueba con objetivo de manipular valores numéricos con alta precisión.

## Usos

La nanoWallet cuenta diferentes operaciones dependiendo que dependen de si el usuario ha iniciado una sesión o no.
El menú general contiene las siguientes operaciones:

 0. Mostrar la cuentas en el sistema
 1. Aperturar una cuenta
 2. Realizar un depósito
 3. Realizar un retiro
 4. Realizar una transferencia entre cuentas
 5. Comenzar una sesión

El menú de sesión contiene las siguientes operaciones:

 0. Realizar un depósito
 1. Realizar un retiro
 2. Realizar una transferencia entre cuentas
 3. Cerrar sesión

Para operar es tan sencillo como escribir el numero de la opción que desea ejecutar.

### Mostrar la cuentas en el sistema

Se listan todas las cuentas activas en el sistema visualizándose junte a ellas su identificador único y el balance.

### Aperturar una cuenta

Solicita el monto inicial de la cuenta que se desea aperturar.

### Realizar un depósito

Solicita el numero de cuenta del receptor y el monto que se desea depositar.

### Realizar un retiro

Solicita el numero de cuenta del remitente y el monto que se desea retirar.

### Realizar una transferencia entre cuentas

Solicita el numero de cuenta del remitente, el monto que se desea depositar y el numero de cuenta del receptor.

## Diseño

### Integridad

Se utiliza la programación orientada a objetos para poder conservar la integridad de los datos por medio del encapsulamiento de las cuentas.

### Gestión de Datos

La manipulación de datos se realizo llevando los decimales a cantidades enteras de centavos para evitar errores de redondeo.

### Transacciones

Cada una de las operaciones que puede realizar el usuario esta encapsulada en una función que se simplifique el flujo de la información y facilita el refactoring del código.
