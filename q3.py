def perfectSquare(number):
    number1 = number
    while True:
        if number1**2 <= number:
            return number1**2 
        else:
            number1 -= 1

#Pseudocode

#FUNCTION sqrRoot (x)
#    integer -> x
#    WHILE TRUE
#       IF integer POWER OF 2 >-> x
#           RETURN integer POWER OF 2
#       ELSE
#           x --> 1
#       END IF
#    END WHILE
    
