month = int( input("enter a month in integer form: ") )
day = int( input("enter a day in int form: ") )
year = int( input("enter a year: "))

print ("your date is: ", month, "/",day,"/",year)

if month * day == year:
	print("this is a magic date!!!!!")
else:
	print("not a magic day :( ")
