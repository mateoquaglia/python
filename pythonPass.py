import string 
import random 

def generar_contrasena(tamano):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(caracteres)for i in range(tamano))


def main():
    try:
        tamano = int(input("ingresa el tamano de la contrasena: "))
        if tamano <= 0:
              print("el tamano debe ser mayor a 0 si o si")
              return
        
        contrasena = generar_contrasena(tamano)


        if input("deseas ver tu contrasena? (si/no):").strip().lower() == "si":
            print("tu contrasena es: " + contrasena)
        else:
         print("esta bien")
              
    
    except ValueError:
          print("solo pudes responder si o no")

if __name__ == "__main__":
      main()

