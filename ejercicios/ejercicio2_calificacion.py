'''
La calificación final de una materia se obtiene de tres parciales que valen 30%, 30% y
40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la materia.
Se necesita mostrar la calificación final y si el alumno aprobó.
'''

# PROBLEMA
# Calcular la calificación final y determinar si el alumno aprobó la materia.

# ENTRADAS
# parcial1 : float, puntos, de 0 a 100.
# parcial2 : float, puntos, de 0 a 100.
# parcial3 : float, puntos, de 0 a 100.

# SALIDAS
# calificacion_final : float, puntos, mostrada con dos decimales.
# estado : texto, "Aprobado" o "Reprobado".

# REGLAS Y SUPUESTOS
# - El primer parcial vale 30%.
# - El segundo parcial vale 30%.
# - El tercer parcial vale 40%.
# - La materia se aprueba con una calificación final mayor o igual a 70.
# - Un parcial menor a 50 reprueba la materia, sin importar la calificación final.
# - Un parcial exactamente igual a 50 no reprueba por esta regla.
# - La calificación final se calcula antes de determinar el estado.
# - La calificación final se muestra con dos decimales.

# ALGORITMO
# 1. Leer parcial1, parcial2 y parcial3.
# 2. calificacion_final = (parcial1 * 0.30) + (parcial2 * 0.30) + (parcial3 * 0.40)
# 3. Si parcial1 < 50 o parcial2 < 50 o parcial3 < 50:
#       estado = "Reprobado"
# 4. En caso contrario, si calificacion_final >= 70:
#       estado = "Aprobado"
# 5. En caso contrario:
#       estado = "Reprobado"
# 6. Mostrar calificacion_final y estado.

# CASOS DE PRUEBA
# (80, 70, 90) -> 81.00, Aprobado
# (70, 70, 70) -> 70.00, Aprobado
# (100, 100, 40) -> 76.00, Reprobado
# (69, 70, 70) -> 69.70, Reprobado
# (50, 70, 70) -> 64.00, Reprobado
# (70, 70, 50) -> 62.00, Reprobado

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerParciales() -> parcial1, parcial2, parcial3 : pide y devuelve las tres calificaciones.
# calcularFinal(parcial1, parcial2, parcial3) -> calificacion_final : calcula y devuelve la calificación final.
# determinarEstado(parcial1, parcial2, parcial3, calificacion_final) -> estado : determina y devuelve si el alumno aprobó o reprobó.
# mostrarResultado(calificacion_final, estado) -> ninguna : muestra la calificación final y el estado.