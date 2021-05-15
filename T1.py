# Salvador Vásquez
import traductor
import animalese
from playsound import playsound

"""
    agregarPalabraProhibidaRecursiva: None -> None
    Pide al usuario que agregue una palabra prohibida a la lista de malas palabras recursivamente. Si el usuario escribe
     'fin' la recursividad termina
"""


def agregarPalabraProhibidaRecursiva():
    nuevaPalabraProhibida = animalese.aMinusculas(str(input()))
    if nuevaPalabraProhibida == 'fin':
        return
    animalese.agregarPalabraProhibida(nuevaPalabraProhibida)
    print('Palabra agregada!')
    agregarPalabraProhibidaRecursiva()


print("########################Bienvenidos, verdaderos creyentes y nuevos tambien########################")

print("A continuacion ingrese las palabras prohibidas en su Aldea, o 'fin' para terminar: ")

print("Ingrese palabra prohibida: ")

agregarPalabraProhibidaRecursiva()

print("Ingrese mensaje a traducir: ")

mensajeTraducir = str(input())

audio = traductor.procesarTexto(mensajeTraducir)

print("Ingrese nombre de archivo: ")

nombreArchivo = str(input())

animalese.generarArchivoAudio(audio, nombreArchivo)

playsound(nombreArchivo + ".wav")
