import string 
import random 

tamano =  int(input("Introduce el tamano de la contraseña: "))
caracteres = string.ascii_letters + string.digits + string.punctuation

contrasena = ("".join(random.choice(caracteres)for i in range(tamano))) 

if input("deseas ver tu contrasena?") == "si":
	print("tu contrasena es: " + contrasena)
else:
	input("deseas ver tu contrasena?") == "no"
	print("esta bien")


