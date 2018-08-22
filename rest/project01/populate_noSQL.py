import csv
from cooking.models import Usuario
from django.utils.dateparse import parse_date

with open('todosmisservicios.csv','r') as csv_file:
	csv_reader=csv.reader(csv_file, delimiter=";")
	#Cesar Gracia Saavedra;CNEL;Esmeraldas;2018-06-24;703;
	for l in csv_reader:					
		#print(line)
		u=Usuario(nombre=l[0],servicio=l[1] , ciudad=l[2],fecha=parse_date(l[3]))
		u.save()

