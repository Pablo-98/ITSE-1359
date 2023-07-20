num = int (input ("enter a number: ") )

sum = 0
numInts = 0
maxValue = 0

while num:
	numInts+=1
	sum = sum + num
	if num > maxValue:
		maxValue = num
	if num <0:
		break
	elif num > 0:
		num = int (input("enter another number") )

print("sum: ",sum);
print("average: ", sum/numInts);
print("max value: ",maxValue);
