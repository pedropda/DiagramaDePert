# Diagrama De Pert

Este código realiza la planificación de un proyecto utilizando la técnica de gestión de proyectos conocida como el Método de la Ruta Crítica (Critical Path Method, CPM). El objetivo es calcular los tiempos de inicio y fin más tempranos y más tardíos para cada actividad dentro de un proyecto, identificar el camino crítico, y determinar la duración total del proyecto. Aquí explico cada sección del código:

1. **Definición de actividades, tiempos y precedentes**:
   - `actividades`: Lista de todas las actividades del proyecto, identificadas por letras.
   - `tiempos`: Diccionario que asigna a cada actividad su duración.
   - `precedentes`: Diccionario que para cada actividad lista sus actividades precedentes, es decir, aquellas que deben completarse antes de que la actividad en cuestión pueda comenzar.

2. **Cálculo de ES (Earliest Start) y EF (Earliest Finish)**:
   - Se inicializa el diccionario `ES_EF` para almacenar los tiempos de inicio más temprano (ES) y de finalización más temprana (EF) para cada actividad.
   - Se itera sobre cada actividad para calcular su ES y EF. Si la actividad no tiene precedentes, su ES es 0 y su EF es igual a su tiempo de duración. Si tiene precedentes, su ES es el máximo EF de todas sus actividades precedentes, y su EF es su ES más su tiempo de duración.

3. **Cálculo de LF (Latest Finish) y LS (Latest Start)**:
   - Se inicializa el diccionario `LF_LS` para almacenar los tiempos de finalización más tardía (LF) y de inicio más tardío (LS) para cada actividad.
   - El LF final del proyecto es el máximo EF entre todas las actividades. Este valor se utiliza para calcular hacia atrás los LF y LS de cada actividad.
   - Se itera sobre las actividades en orden inverso para calcular su LF y LS. Para la última actividad (en este caso, 'g'), LF es igual al LF final del proyecto, y LS se calcula restando su tiempo de duración a su LF. Para las demás actividades, LF es el mínimo LF entre todas sus actividades sucesoras, y LS se calcula restando su tiempo de duración a su LF.

4. **Cálculo del camino crítico**:
   - Se inicializa una lista vacía `camino_critico`.
   - Se itera sobre todas las actividades para identificar aquellas que son críticas, es decir, aquellas cuyos tiempos de inicio y fin más tempranos coinciden con sus tiempos de inicio y fin más tardíos. Estas actividades se agregan al camino crítico.

5. **Tiempo total del proyecto**:
   - El tiempo total del proyecto es el LF final, es decir, el tiempo de finalización más tardío entre todas las actividades.

Al final, el código devuelve los diccionarios `ES_EF` y `LF_LS` con los tiempos calculados para cada actividad, la lista del camino crítico, y el tiempo total del proyecto. Esto permite visualizar cómo se planifica el proyecto, identificar las actividades críticas que directamente afectan la duración total del proyecto, y gestionar de manera efectiva los recursos y los tiempos.
