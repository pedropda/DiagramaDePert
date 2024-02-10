# Definición de actividades, tiempos y precedentes
actividades = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
tiempos = {'a': 3, 'b': 2, 'c': 5, 'd': 2, 'e': 4, 'f': 6, 'g': 5}
precedentes = {'a': [], 'b': ['a'], 'c': [], 'd': ['b', 'c'], 'e': ['a'], 'f': ['b', 'c'], 'g': ['e', 'd']}

# Cálculo de ES y EF
ES_EF = {actividad: (0, 0) for actividad in actividades}  # Inicialización de ES y EF para cada actividad

for actividad in actividades:
    if not precedentes[actividad]:  # Si la actividad no tiene precedentes
        ES = 0
        EF = tiempos[actividad]
    else:
        ES = max([ES_EF[prec][1] for prec in precedentes[actividad]])  # ES es el máximo EF de los precedentes
        EF = ES + tiempos[actividad]
    ES_EF[actividad] = (ES, EF)

# Cálculo de LF y LS (requiere un enfoque desde el final hacia el inicio)
LF_LS = {actividad: (0, 0) for actividad in actividades}  # Inicialización de LF y LS
LF_final = max(ES_EF.values(), key=lambda x: x[1])[1]  # El LF final es el máximo EF de todas las actividades

for actividad in reversed(actividades):
    sucesores = [act for act in actividades if actividad in precedentes[act]]
    if not sucesores:  # Si no tiene sucesores
        LF = ES_EF[actividad][1]  # Usa el EF de la actividad como LF
    else:
        LF = min([LF_LS[suc][0] for suc in sucesores])  # Busca el LS mínimo de los sucesores
    LS = LF - tiempos[actividad]
    LF_LS[actividad] = (LS, LF)

# Cálculo del camino crítico
camino_critico = []
for actividad in actividades:
    ES, EF = ES_EF[actividad]
    LS, LF = LF_LS[actividad]
    if ES == LS and EF == LF:  # Si ES=LS y EF=LF, la actividad es crítica
        camino_critico.append(actividad)

# Tiempo total del proyecto
tiempo_total = LF_final

ES_EF, LF_LS, camino_critico, tiempo_total
