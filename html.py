# Programa 9.7 Criação de uma página inicial em Python

with open("página.html", "w", encoding="utf-8") as página:
    página.write("<!DOCTYPE html>\n")
    página.write("<html lang=\"pt-BR\">\n")
    página.write("<head>\n")
    página.write("<meta charset=\"utf-8\">\n")
    página.write("<title>Título da Página</title>\n")
    página.write("</head>\n")
    página.write("<body>\n")
    página.write("Olá!")
    for l in range(10):
        página.write(f" <p>{l}</p>\n")
    página.write("</body>\n")
    página.write("</html>\n")
