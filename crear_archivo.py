

def name_file():
    names = []
    # convertir nombres en listas
    with open("./names_file.txt", "r", encoding="utf-8") as file:
        for line in file:
            # .rstrip('\n') sirve para elimunar saltos de linea 
            names.append(line.rstrip('\n'))
    # recorrer lista y generaar archivo 
    for line in  names:
        file =  open(line, "w", encoding="utf-8")
        file.write("# language: es\n") 
        file.write("@Cucumber\n") 
        file.write("  Escenario:\n")
        file.write("    Dado El usuario ingresa a carga de trayectos\n")
        file.write("    Cuando El usuario va a cargar un archivo de Excel\n")
        file.write("    Entonces El archivo se carga al sistema\n")
    




def run():
    name_file()

if __name__ == "__main__":
    run()


