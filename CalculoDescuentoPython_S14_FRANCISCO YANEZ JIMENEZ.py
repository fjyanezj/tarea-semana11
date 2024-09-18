def calcular_descuento(monto_total, porcentaje_descuento=10):
  descuento = monto_total * (porcentaje_descuento / 100)
  return descuento

# Primer llamada de la funcion, sando valor fijo del descuento 10%
print("""################EJERCICIO 1########################
...................................................""")
monto_total = 100
descuento1 = calcular_descuento(monto_total)
monto_final1 = monto_total - descuento1
print("Descuento (10%):", descuento1)
print("Monto final:", monto_final1)

print("""################EJERCICIO 2########################
...................................................""")
# Segunda llamada, poniendo un porcentaje de descuento diferente
monto_total2 = 200
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
monto_final2 = monto_total2 - descuento2
print("Descuento (15%):", descuento2)
print("Monto final:", monto_final2)