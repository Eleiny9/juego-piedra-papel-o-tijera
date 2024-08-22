print("Introduce tu monto inicial")
monto_inicial = float(input())

tasa_interes = 0.04
i=1

while i<=3:
  monto_inicial = monto_inicial * (tasa_interes +1)
  print("El monto final es: {:.2f} ". format( monto_inicial))
  i=i+1
