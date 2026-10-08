'''
Una compañía eléctrica cobra el consumo mensual con tres tarifas: $1.00 por kWh hasta
150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh.
Se necesita calcular el importe del recibo a partir del consumo del mes.
'''

# PROBLEMA
# Calcular el importe del recibo de luz a partir del consumo mensual en kWh.

# ENTRADAS
# consumo : float, kWh, mayor o igual a 0.

# SALIDAS
# pago : float, pesos, mostrado con dos decimales.

# REGLAS Y SUPUESTOS
# - De 0 a 150 kWh se cobra $1.00 por kWh.
# - De 151 a 280 kWh se cobra $1.50 por kWh.
# - Arriba de 280 kWh se cobra $3.00 por kWh.
# - Se interpreta que las tarifas son progresivas: cada bloque de consumo se cobra con su tarifa correspondiente.
# - El importe se muestra con dos decimales.
# - El límite de 150 kWh pertenece a la primera tarifa.
# - El límite de 280 kWh pertenece a la segunda tarifa.

# ALGORITMO
# 1. Leer consumo.
# 2. Si consumo <= 150:
#       pago = consumo * 1.00
# 3. En caso contrario, si consumo <= 280:
#       pago = (150 * 1.00) + ((consumo - 150) * 1.50)
# 4. En caso contrario:
#       pago = (150 * 1.00) + (130 * 1.50) + ((consumo - 280) * 3.00)
# 5. Mostrar pago.

# CASOS DE PRUEBA
# 100 kWh -> $100.00
# 150 kWh -> $150.00
# 151 kWh -> $151.50
# 200 kWh -> $225.00
# 280 kWh -> $345.00
# 281 kWh -> $348.00
# 300 kWh -> $405.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerConsumo() -> consumo : pide y devuelve el consumo mensual en kWh.
# calcularPago(consumo) -> pago : calcula y devuelve el importe del recibo.
# mostrarRecibo(pago) -> ninguna : muestra el importe del recibo.