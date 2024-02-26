# Practica1

def main():

    # Pedir 5 datos de una persona    
    name = input("Por favor, ingrese su nombre: ")
    age = int(input("Por favor, ingrese su edad: "))
    city = input("Por favor, ingrese el nombre de la ciudad donde vive: ")
    job = input("Por favor, ingrese su cargo laboral: ")
    hobby = input("Por favor, ingrese su pasatiempo favorito: ")

    # Mostrar los 5 datos de la persona
    print("\nAquí están los datos que ingresó:")
    print("Nombre: " + name)
    print("Edad: " + str(age))
    print("Ciudad: " + city)
    print("Cargo laboral: " + job)
    print("Pasatiempo favorito: " + hobby)

if __name__ == "__main__":
    main()