edad = int(input("Bienvenid@!! \nPor favor, ingresa tu edad: "))

if edad < 0:
    print("Woah! Una edad negativa es imposible! (A menos que sigas al interior de tu mama \'*v*\') \nIntenta denuevo!")
    
else:
    print("\n\n====Calculado rango de edad====")
    
    if edad < 12:
        print("\n\n Eres un/a Niño/a!!")
    elif 12 <= edad <= 17:
        print("\n\n Eres un/a Adolescente!!")
    elif 18 <= edad <= 64:
        print("\n\n Eres un/a Adulto/a!!")
    else:
        print("\n\n Eres un/a Adulto/a Mayor!!")
