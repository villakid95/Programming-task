def trailingZeros (number):
    amountOfFives= 0
    for factorialNumber in range (2,number +1) :
        while factorialNumber > 0:	 	
            if factorialNumber % 5 == 0:		
                amountOfFives +=1		
                factorialNumber = factorialNumber/5	
            else:			
                break                 

    return amountOfFives

number = 50
print(trailingZeros(number))

#Run time Bound = 0(n^2)
