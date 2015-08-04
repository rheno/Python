import csv
import sys
with open(sys.argv[1]) as csvfile:
	reader = csv.DictReader(csvfile)
	
	try :
		f = open(sys.argv[2], 'w')
		for row in reader:
			s = str(row) + '\n'
			f.write(s)
		f.close()
	except Exception as e :
		print e.message