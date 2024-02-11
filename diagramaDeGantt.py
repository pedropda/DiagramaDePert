import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Fechas de inicio del proyecto
start_date = datetime(2024, 2, 11)

# Definición de actividades, tiempos de inicio y duraciones
actividades = [
    {"Actividad": "Preparación del Proyecto", "Inicio": 0, "Duración": 15, "Responsable": "Equipo de Proyecto"},
    {"Actividad": "Diseño de la Expansión y Nuevos Productos", "Inicio": 15, "Duración": 30, "Responsable": "Departamento de Ingeniería"},
    {"Actividad": "Adquisición de Materiales y Equipos", "Inicio": 45, "Duración": 30, "Responsable": "Departamento de Compras"},
    {"Actividad": "Construcción y Ampliación", "Inicio": 75, "Duración": 45, "Responsable": "Contratista General"},
    {"Actividad": "Desarrollo de Productos y Pruebas", "Inicio": 120, "Duración": 15, "Responsable": "Departamento de I+D"},
    {"Actividad": "Puesta en Marcha y Capacitación", "Inicio": 135, "Duración": 15, "Responsable": "Departamento de Operaciones"},
]

# Convertir a DataFrame
df = pd.DataFrame(actividades)

# Calcular fechas de inicio y fin
df["Fecha de inicio"] = df["Inicio"].apply(lambda x: start_date + timedelta(days=x))
df["Fecha de fin"] = df.apply(lambda x: x["Fecha de inicio"] + timedelta(days=x["Duración"]), axis=1)

# Preparar gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Colores por responsables (para simplificar)
colores = {
    "Equipo de Proyecto": "tab:blue",
    "Departamento de Ingeniería": "tab:orange",
    "Departamento de Compras": "tab:green",
    "Contratista General": "tab:red",
    "Departamento de I+D": "tab:purple",
    "Departamento de Operaciones": "tab:brown",
}

# Agregar barras para cada actividad
for i, actividad in df.iterrows():
    inicio = mdates.date2num(actividad["Fecha de inicio"])
    fin = mdates.date2num(actividad["Fecha de fin"])
    ax.barh(actividad["Actividad"], fin - inicio, left=inicio, color=colores[actividad["Responsable"]])

# Formatear el gráfico
ax.set_xlabel("Fecha")
ax.set_ylabel("Actividades")
ax.set_title("Diagrama de Gantt para la Ampliación de la Planta de Loop Mask")
ax.xaxis_date()  # interpretar el eje x como fechas
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar gráfico
plt.show()
