import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Simulación de registros de accesos
data = {
    "usuario": ["user1"] * 5 + ["user2"] * 3 + ["user3"] * 4 + ["user4"] * 6,
    "ip": ["181.45.12.34", "181.45.12.34", "45.67.89.10", "102.54.32.11", "181.45.12.34",
           "190.23.45.12", "190.23.45.12", "45.67.89.10",
           "170.33.56.78", "170.33.56.78", "203.45.12.89", "10.0.0.1",
           "201.34.56.23", "10.10.10.10", "99.99.99.99", "45.67.89.10", "55.66.77.88", "45.67.89.10"],
    "ubicacion": ["Argentina", "Argentina", "EE.UU.", "Rusia", "Argentina",
                  "Brasil", "Brasil", "EE.UU.",
                  "España", "España", "China", "Argentina",
                  "México", "Argentina", "Nigeria", "EE.UU.", "Argentina", "EE.UU."],
    "exitoso": [True, True, False, False, True, True, False, False, True, False, False, True, True, True, False, False, True, False]
}

df = pd.DataFrame(data)

# Filtramos intentos fallidos
intentos_fallidos = df[df["exitoso"] == False]

# Conteo de intentos fallidos por ubicación
conteo_por_ubicacion = intentos_fallidos["ubicacion"].value_counts()

# Visualización
plt.figure(figsize=(10, 5))
sns.barplot(x=conteo_por_ubicacion.index, y=conteo_por_ubicacion.values, palette="Reds")
plt.xlabel("Ubicación de Intento Fallido")
plt.ylabel("Cantidad de Intentos")
plt.title("Intentos de Acceso Fallidos por Ubicación")
plt.xticks(rotation=45)
plt.show()

# Detección de actividad sospechosa
print("\n Posibles accesos sospechosos detectados:")
for index, row in intentos_fallidos.iterrows():
    print(f"Usuario: {row['usuario']} - Ubicación: {row['ubicacion']} - IP: {row['ip']} ")
