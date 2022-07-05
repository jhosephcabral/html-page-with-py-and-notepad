from multiprocessing.connection import wait
from struct import pack
from webbrowser import open_new


letra = ""

with open("music.txt", "r") as arq:
    for linha in arq:
        letra += linha + "<br>"

with open("musicweb.html", "w") as arq:
    arq.write("<html>")
    arq.write("<head><title>What country is this?</title></head>")
    arq.write("<body>")

    arq.write(letra)

    arq.write("</body")
    arq.write("</html>") 