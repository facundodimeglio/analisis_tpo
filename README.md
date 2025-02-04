# 📌 Santander - Análisis y Validación de Seguridad

## 🛠 Santander_Analisis.py

### ✨ Características del script:
- Simula intentos de acceso, algunos exitosos y otros fallidos.
- Filtra intentos fallidos y cuenta cuántos provienen de ubicaciones inusuales.
- Genera un gráfico de barras para visualizar los intentos fallidos.
- Muestra un listado de intentos sospechosos detectados en consola.

### 📊 Resultado del análisis:

#### 📷 **Gráfico generado:**
![image](https://github.com/user-attachments/assets/1e3f55b3-39e1-45fa-b37d-6d5d8b54f2c6)

Este gráfico representa la cantidad de intentos de acceso fallidos por ubicación.

### 🔍 Análisis de los datos:
- **EE.UU.** tiene la mayor cantidad de intentos fallidos (4 intentos), lo que podría indicar actividad inusual desde esta región.
- **Rusia, Brasil, España, China y Nigeria** presentan cada uno 1 intento fallido.
- Se utiliza un gradiente de colores en rojo para indicar la intensidad del problema; los tonos más oscuros representan ubicaciones más críticas.

### 📌 Conclusiones y posibles interpretaciones:
- **Actividad sospechosa desde EE.UU.:** Podría tratarse de intentos automatizados o repetidos desde una misma zona.
- **Ubicaciones internacionales diversas:** Si el banco opera en una región específica (ej. Latinoamérica) y aparecen intentos desde países inusuales, se podría considerar una alerta.
- **Patrones de intentos:** Si los intentos fallidos aumentan en ciertos países, sería recomendable reforzar medidas de seguridad como la autenticación multifactor (MFA).

---

## 🛠 Validacion_Inputs.py

### ✨ Características del script:
- Define funciones para validar usuario y contraseña según las normas del Banco Santander.
- Usa inputs para que el usuario pueda probar diferentes combinaciones en tiempo real.
- Incluye pruebas automáticas con datos ficticios.

### 🚀 Cómo usarlo:
1. **Pruebas automáticas:** Se ejecutan validaciones con datos ficticios.
2. **Prueba manual:** Permite ingresar un usuario y una contraseña para validar en tiempo real.

### 📌 Ejemplo de Output:

```
🔹 Resultados de validación automática:
Usuario 'usuario1': Usuario válido.
Usuario 'ClienteVIP2024': Usuario válido.
Usuario '123456': Error: El usuario debe tener entre 8 y 20 caracteres.
Usuario 'Us3rInv@lido!': Error: El usuario solo puede contener letras y números.
Usuario 'BancoSantander23': Usuario válido.

Contraseña 'Abc123!': Error: La contraseña debe incluir al menos un carácter especial (!@#$%^&...).
Contraseña 'segura123': Error: La contraseña debe incluir al menos una letra mayúscula.
Contraseña 'PASSWORD': Error: La contraseña debe incluir al menos una letra minúscula y un número.
Contraseña 'Santander2024!': Contraseña segura.
Contraseña 'abcdEFGH123$': Contraseña segura.

🔹 Prueba manual (ingresa datos para validar en tiempo real):
Ingrese un usuario: JuanPerez2023
Usuario válido.
Ingrese una contraseña: MiClaveSegura2024!
Contraseña segura.
```

---


- **Santander_Analisis.py** ayuda a detectar patrones sospechosos en intentos de acceso.
- **Validacion_Inputs.py** permite verificar si un usuario y contraseña cumplen con las políticas de seguridad del banco.
- Estos scripts pueden utilizarse como base para pruebas de seguridad en sistemas de autenticación.

