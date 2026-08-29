# sistema de facturacion fase 1
# datos del negocio
nombre_negocio = "Papeleria El Lapiz Feliz"
nit = "1088737737"
numero_factura = 1
tarifa_iva=0.19
print("Bienvenido a la Papeleria El Lapiz Feliz")

# sistema de facturacion fase 1
# datos del negocio
nombre_negocio = "Papeleria El Lapiz Feliz"
nit = "1088737737"
numero_factura = 1
tarifa_iva=0.19
print("Bienvenido a la Papeleria El Lapiz Feliz")

# sistema de facturacion fase 3
# conversion de tipos
cantidad = int(cantidad)
valor_unitario = float(valor_unitario)
total_competencia=float(total_competencia)
type(valor_unitario)

# sistema de facturacion fase 4
# proceso
subtotal = cantidad*valor_unitario
iva=subtotal*tarifa_iva
total=subtotal+iva
ahorro=total_competencia-total

# sistema de facturacion fase 5
print(nombre_negocio)
print("===================")
print(nit)
print(numero_factura)
print(cliente, producto, cantidad)
print(subtotal)
print(iva)
print(total)
print(ahorro)

# sistema de facturacion fase 6
#cierre caja
venta_1=input("venta_1: ")
venta_2=input("venta_2: ")
venta_1=float(venta_1)
venta_2 = float(venta_2)
total_dia = total+venta_1+venta_2
promedio_dia = total_dia/3
print("resumen del dia  ", total_dia)

