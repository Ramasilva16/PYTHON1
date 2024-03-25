dinero = int (input("Ingrese monto a retirar: "))
aux = dinero
Billetes1000 = dinero // 1000
dinero = dinero % 1000
Billetes500 = dinero // 500
dinero = dinero % 500
Billetes200 = dinero //200
dinero = dinero % 200
Billetes100 = dinero // 100
dinero = dinero % 100
print("Usted Ingreso", aux, "Por lo que el cajero le\nDebe dar ", Billetes1000, "billete/s de mil\nDebe dar ", Billetes500, "billete/s de 500\nDebe dar ", Billetes200, "billete/s de 200\nDebe dar ", Billetes100, "billete/s de 100")