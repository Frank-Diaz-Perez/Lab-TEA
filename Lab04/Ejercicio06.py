def calcularsalario(horas, tarifa):
    horas_extra = int(horas) - Max_horas_semanale
    if (horas_extra > 0):
        pago = (Max_horas_semanale * tarifa) + (horas_extra * tarifa * 1.5)
    else:
        pago = horas * tarifa
    return pago
try:
    Max_horas_semanale = 40
    horas = int(input("Ingrese numero de horas: "))
    tarifa = float(input("Ingrese tarifa por hora: "))
    salario = calcularsalario(horas, tarifa)
    print(salario)
except:
    print("Error, debe ingresar números")