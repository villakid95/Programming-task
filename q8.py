def vowel(text):
    banned = "aeiou"   
    if len(text)==0:  
        return text
    elif text[0] in banned: 
        return vowel(text[1:]) 
    else:   
        return text[0] + vowel(text[1:])

#FUNCTION VOWEL (TEXT)
#    Var = "aeiou"
#    IF LENGTH(TEXT)=ZERO
#        RETURN Text
#    ELSE IF text[ZERO] in Var
#        RETURN VOWEL(Text[1:])
#    ELSE
#        RETURN text[ZERO] ADD VOWEL (Text[1:])
                                     
