# Contribuir en nanoWallet

## Tecnologias 
Pyhton v3.11
Git v2.30

## Git
La estructura para los commits sigue el sistema de [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/).



## Diseño

### Integridad

Se utiliza la programación orientada a objetos para poder conservar la integridad de los datos por medio del encapsulamiento de las cuentas.

### Gestión de Datos

La manipulación de datos se realizo llevando los decimales a cantidades enteras de centavos para evitar errores de redondeo.

### Transacciones

Cada una de las operaciones que puede realizar el usuario esta encapsulada en una función que se simplifique el flujo de la información y facilita el refactoring del código.

