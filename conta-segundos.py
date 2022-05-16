segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos // 86400
segSobraDias = segundos % 86400
horas = segSobraDias // 3600
segSobraHoras = segSobraDias % 3600
minutos = segSobraHoras // 60
segFinal = segSobraHoras % 60
print (dias,"dias,",horas,"horas,",minutos, "minutos e",segFinal,"segundos.")
