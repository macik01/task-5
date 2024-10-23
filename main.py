import string
import keyword

#task 5/1
if smina in keyword.kwlist:
    print("False")
elif smina.isupper() or smina in string.whitespace or (smina in string.punctuation and smina != '_'):
    print("False")
elif smina.count("_") > 1:
    print ("False")
elif smina[0].isdigit():
    print("False")
else: print("True")


