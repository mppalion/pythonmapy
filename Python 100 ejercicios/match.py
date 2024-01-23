auto= "Diablo"

match auto:
    case "208":
        print("Peugeot")
    case "Twingo":
        print("Renault")
    case "3008":
        print("Peugeot")
    case "Diablo":
        print("Lamborguini")
    case _:
        print("No existe marca para ese modelo")