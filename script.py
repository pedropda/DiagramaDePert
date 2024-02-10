# Revisamos y corregimos el cálculo de LF y LS con un enfoque correcto

# Inicializamos LF al máximo EF de la actividad final para todas las actividades
for actividad in actividades:
    LF_LS[actividad] = (0, LF_final)

# Actualizamos el cálculo de LS y LF de manera adecuada
for actividad in reversed(actividades):
    if actividad in ['d', 'g']:  # Actividades que conducen directamente al final
        LF_LS[actividad] = (LF_LS[actividad][0], LF_final)
        LS = LF_LS[actividad][1] - tiempos[actividad]
        LF_LS[actividad] = (LS, LF_final)
    else:
        sucesores = [act for act in actividades if actividad in precedentes.get(act, [])]
        if sucesores:
            LF = min([LF_LS[suc][0] for suc in sucesores])  # El LF es el mínimo LS de los sucesores
            LS = LF - tiempos[actividad]
            LF_LS[actividad] = (LS, LF)
        else:  # Si no tiene sucesores, se calcula directamente
            LF = LF_LS[actividad][1]
            LS = LF - tiempos[actividad]
            LF_LS[actividad] = (LS, LF)

# Corregimos el cálculo de camino crítico
camino_critico_corregido = []
for actividad in actividades:
    ES, EF = ES_EF[actividad]
    LS, LF = LF_LS[actividad]
    if ES == LS:  # Revisamos si ES=LS para identificar actividades críticas
        camino_critico_corregido.append(actividad)

# Tiempo total del proyecto corregido
tiempo_total_corregido = LF_final

ES_EF, LF_LS, camino_critico_corregido, tiempo_total_corregido
