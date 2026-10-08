'''
Una tienda aplica 10% de descuento en compras de $1,000 o más y 20% en compras de
$5,000 o más. A la compra se le agrega el 16% de IVA. Se necesita mostrar el ticket
con subtotal, descuento, IVA y total.
'''

# PROBLEMA
# Calcular el descuento, IVA y total de una compra.

# ENTRADAS
# subtotal : float, pesos, mayor o igual a 0.

# SALIDAS
# descuento : float, pesos, mostrado con dos decimales.
# iva : float, pesos, mostrado con dos decimales.
# total : float, pesos, mostrado con dos decimales.

# REGLAS Y SUPUESTOS
# - Las compras menores a $1,000 no tienen descuento.
# - Las compras de $1,000 o más tienen 10% de descuento.
# - Las compras de $5,000 o más tienen 20% de descuento.
# - El límite de $1,000 pertenece al descuento del 10%.
# - El límite de $5,000 pertenece al descuento del 20%.
# - El IVA es del 16%.
# - El IVA se calcula después de aplicar el descuento.
# - El total se calcula sumando el subtotal después del descuento y el IVA.
# - Los importes se muestran con dos decimales.

# ALGORITMO
# 1. Leer subtotal.
# 2. Si subtotal >= 5000:
#       descuento = subtotal * 0.20
# 3. En caso contrario, si subtotal >= 1000:
#       descuento = subtotal * 0.10
# 4. En caso contrario:
#       descuento = 0
# 5. calcularIVA = (subtotal - descuento) * 0.16
# 6. calcularTotal = (subtotal - descuento) + calcularIVA
# 7. Mostrar subtotal, descuento, IVA y total.

# CASOS DE PRUEBA
# $500 -> descuento $0.00, IVA $80.00, total $580.00
# $900 -> descuento $0.00, IVA $144.00, total $1,044.00
# $999 -> descuento $0.00, IVA $159.84, total $1,158.84
# $1,000 -> descuento $100.00, IVA $144.00, total $1,044.00
# $1,001 -> descuento $100.10, IVA $144.14, total $1,045.04
# $4,999 -> descuento $499.90, IVA $719.86, total $5,218.96
# $5,000 -> descuento $1,000.00, IVA $640.00, total $4,640.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerSubtotal() -> subtotal : pide y devuelve el subtotal de la compra.
# calcularDescuento(subtotal) -> descuento : calcula y devuelve el descuento.
# calcularIVA(subtotal, descuento) -> iva : calcula y devuelve el IVA.
# calcularTotal(subtotal, descuento, iva) -> total : calcula y devuelve el total.
# mostrarTicket(subtotal, descuento, iva, total) -> ninguna : muestra el ticket con los importes.