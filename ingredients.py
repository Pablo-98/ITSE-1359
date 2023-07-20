#48 cooks = 1.5s, 1b, 2.75f


print("how many cookies you want");


amountWanted = int(input("enter number of cookies wanted"));

sugarForOne = 1.5/48;

butterForOne = 1/48;

flourForOne = 2.75/48


finalSugar = amountWanted * sugarForOne;

finalButter = amountWanted * butterForOne;

finalFlour = amountWanted * flourForOne;

print("if you want ", amountWanted , "  cookies " + "you will need: " ,finalSugar, " of sugar ", finalButter, " of butter ", finalFlour, " of flour"); 
