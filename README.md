# analisis_tpo


santander_analisis.py

-Caracteristicas del script:
  Simula intentos de acceso, algunos exitosos y otros fallidos.
  Filtra intentos fallidos y cuenta cuántos provienen de ubicaciones inusuales.
  Genera un gráfico de barras para visualizar los intentos fallidos.
  Muestra un listado de intentos sospechosos detectados en consola.


Como resultado nos arroja el siguiente grafico:
![image](https://github.com/user-attachments/assets/1e3f55b3-39e1-45fa-b37d-6d5d8b54f2c6)


Este gráfico muestra la cantidad de intentos de acceso fallidos por ubicación.

Análisis de los datos:
  EE.UU. tiene la mayor cantidad de intentos fallidos (4 intentos), lo que podría indicar actividad inusual desde esta región.
  Rusia, Brasil, España, China y Nigeria presentan cada uno 1 intento fallido.
  El uso de un gradiente de colores en rojo indica la intensidad del problema, con tonos más oscuros representando ubicaciones más críticas.
-Conclusiones y posibles interpretaciones:
  Actividad sospechosa desde EE.UU.: Podría tratarse de intentos automatizados o repetidos desde una misma zona.
  Ubicaciones internacionales diversas: Si el banco opera en una región específica (ej. Latinoamérica) y aparecen intentos desde países menos comunes, se podría considerar una alerta.
  Patrones de intentos: Si los intentos fallidos continúan aumentando en ciertos países, sería recomendable reforzar medidas de seguridad como autenticación multifactor (MFA).



____________________________________________________


validacion_inputs.py


-Características del script:
  Define funciones para validar usuario y contraseña según las normas del Banco Santander.
  Usa inputs para que el usuario pueda probar diferentes combinaciones en tiempo real
  Incluye pruebas automáticas con datos ficticios.


-Como usarlo:
  Primero se muestran pruebas automáticas con datos ficticios.
  Luego, podrás ingresar un usuario y una contraseña para validar en tiempo real.


Ejemplo de Output:

Resultados de validación automática:
Usuario 'usuario1': Usuario válido.
Usuario 'ClienteVIP2024': Usuario válido.
Usuario '123456': Error: El usuario debe tener entre 8 y 20 caracteres.
Usuario 'Us3rInv@lido!': Error: El usuario solo puede contener letras y números.
Usuario 'BancoSantander23': Usuario válido.

Contraseña 'Abc123!': Error: La contraseña debe incluir al menos un carácter especial (!@#$%^&*...).
Contraseña 'segura123*': Error: La contraseña debe incluir al menos una letra mayúscula.
Contraseña 'PASSWORD': Error: La contraseña debe incluir al menos una letra minúscula y un número.
Contraseña 'Santander2024!': Contraseña segura.
Contraseña 'abcdEFGH123$': Contraseña segura.

Prueba manual (ingresa datos para validar en tiempo real):
Ingrese un usuario: JuanPerez2023
Usuario válido.
Ingrese una contraseña: MiClaveSegura2024!
Contraseña segura.




