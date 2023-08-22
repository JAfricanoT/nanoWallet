# nanoWallet

Es un proyecto de prueba con objetivo de manipular valores numericos con alta presicion.

> Desaroollado por:
> - Joséfrancisco Africano | [@JAfricanoT](https://github.com/JAfricanoT)
> - Gustavo López | [@gusaln](https://github.com/gusaln)
> - Claudia Medina 
> - Manuel Arenas 

## Usos

La nanoWallet cuenta con un menu con las siguientes operaciones:
 0. Mostrar la cuentas en el sistema
 1. Aperutar una cuenta
 2. Realizar un depósito
 3. Realizar un retiro
 4. Realizar una transferencia entre cuentas

Para operar es tan sencillo como escribir el numero de la opción que desea ejecutar.

### Mostrar la cuentas en el sistema

Se listan todas las cuentas activas en el sistema visualizandose junte a ellas su identificardor unico y el balance.

### Aperutar una cuenta

Solicita el monto inicial de la cuenta que se desea aperturar.

### Realizar un depósito

Solicita el numero de cuenta del receptor y el monto que se desea depositar.

### Realizar un retiro

Solicita el numero de cuenta del remitente y el monto que se desea retirar.

### Realizar una transferencia entre cuentas

Solicita el numero de cuenta del remitente, el monto que se desa depositar y el numero de cuenta del receptor.

## Diseño 

### Integridad

Se utiliza la programacion orientada a objetos para poder conservar la integridad de los datos por medio del encapsulamiento de las cuentas.

### Gestion de Datos

La manipulacion de datos se realizo llevando los decimales a cantidades enteras de centavos para evitar errores de redondeo.

### Transacciones

Cada una de las operaciones que puede realizar el usuario esta encapsulada en una fucion que perte que se simplifique el flujo de la informacion y facilita el refactoring del codigo.