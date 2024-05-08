#Super Tienda
codigo_producto = int(input("Ingresa código: "))
nombre_producto = str(input("Nombre producto: "))
cantidad_compra = int(input("Cantidad: "))
valor_unitario = float(input("Cuanto cuesta: "))
iva_porcentaje = 19/100


valor_producto = cantidad_compra * valor_unitario
valor_iva = iva_porcentaje * valor_producto
valor_final = valor_producto + valor_iva

print("\n Codigo de compra:",codigo_producto)
print("Cantidad adquirida: ",cantidad_compra)
print("Producto adquirido: ",nombre_producto)
print("valor sin iva: ",valor_producto)
print(" El valor total de su compra es: ",valor_final)
