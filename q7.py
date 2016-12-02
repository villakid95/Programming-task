def Prime(x):
    return test (x, x-1)

def test(n, d):
    if n%d == 0:
        return False
    elif d == 2:
        return True
    else:
        return test(n,d-1)

#FUNCTION PRIME (X)
#   RETURN test (X, X-1)
#
#FUNCTION TEST (Y, Z)
#   ELSE y  MODULUS z = ZERO
#        RETURN False
#    ELSE IF z = 2
#        RETURN True
#    ELSE
#        RETURN test(y,z-1)
        
    
