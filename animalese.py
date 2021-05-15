import warnings
warnings.filterwarnings("ignore")
import wave, os, math, sys, random, string, re
from pydub import AudioSegment
from pydub.playback import play

TEMP_FILE_NAME = "temp.wav"
letter_graphs = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z"
]

digraphs = [
    "ch", "sh", "ph", "th", "wh"
]

bebebese = "bebebese"

swear_words = ["feo", "asco", "malo"]


#largo: str -> int
#Entrega el largo de la palabra incluyendo caracteres especiales
#Ej: largo("Hola, que tal?") -> 14
def largo(palabra):
    return len(palabra)

assert largo("Hola, que tal?") == 14

#nuevoAudio: None -> Sonido
#Retorna un Sonido vacio.
def nuevoAudio():
    return AudioSegment.empty()

#obtenerLetraEnPosicion: str int -> str
#Entrega el caracter del string 'oracion' en la posicion 'indice', comenzando con 0
#Ej: obtenerLetraEnPosicion("hola", 2) -> "l"
def obtenerLetraEnPosicion(oracion, indice):
    return oracion[indice]

assert obtenerLetraEnPosicion("hola", 2) == "l"

#esLetra: str -> bool
#Indica si el string en 'letra' está en la lista de sonidos.
#Ej: esLetra("l") -> True
#Ej: esLetra(";") -> False
def esLetra(letra):
    return letra in letter_graphs

assert esLetra("l")
assert not esLetra(";")

#esDigrafo: str -> bool
#Indica si el string en 'digrafo' está en la lista de sonidos.
#Ej: esDigrafo("sh") -> True
#Ej: esDigrafo("al") -> False
def esDigrafo(digrafo):
    return digrafo in digraphs

assert esDigrafo("sh")
assert not esDigrafo("al")

#esPuntuacion: str -> bool
#Indica si el string en 'letra' es un signo de puntuacion.
#Ej: esPuntuacion(":") -> True
#Ej: esPuntuacion("a") -> False
def esPuntuacion(letra):
    return letra in string.punctuation

assert esPuntuacion(":")
assert not esPuntuacion("a")

#obtenerSonido: str -> Sonido
#Entrega el sonido asociado al string 'letra'
def obtenerSonido(letra):
    return AudioSegment.from_wav("letters/{}.wav".format(letra))

#reemplazarPalabra: str str str -> str
#Reemplaza el string 'palabra' por 'nueva' en 'oracion'
#Ej: reemplazarPalabra("Hola, vamos a jugar", "jugar", "dormir") -> "Hola, vamos a dormir"
def reemplazarPalabra(oracion, palabra, nueva):
    return oracion.replace(palabra, nueva)

assert reemplazarPalabra("Hola, vamos a jugar", "jugar", "dormir") == "Hola, vamos a dormir"

#palabrasProhibidas: None -> int
#Entrega la cantidad de palabras prohibidas
def palabrasProhibidas():
    return len(swear_words)

#palabraEnPosicion: int -> str
#Entrega la palabra prohibida en la posicion 'i'
def palabraEnPosicion(i):
    return swear_words[i]

#posicionCaracter: str str -> int
#Entrega la posicion del caracter 'letra' en 'oracion'
#Ej: posicionCaracter("hola", "l") -> 2
def posicionCaracter(oracion,letra):
    return oracion.index(letra)

assert posicionCaracter("hola", "l") == 2

#existeEnOracion: str str -> bool
#Indica si el string en 'letra' está en el string 'oracion'
#Ej: existeEnOracion("l", "hola") -> True
def existeEnOracion(letra, oracion):
    return letra in oracion

assert existeEnOracion("l", "hola")

#reemplazarExtracto: str str int int -> str
#Inserta el string 'reemplazo' en 'oracion' entre las posiciones 'inicio' y 'fin'
#Ej: reemplazarExtracto("Vamos a jugar al parque?", "alla", 14, 22) -> "Vamos a jugar alla?"
def reemplazarExtracto(oracion, reemplazo, inicio, fin):
    return oracion[:inicio] + reemplazo + oracion[fin+1:]

assert reemplazarExtracto("Vamos a jugar al parque?", "alla", 14, 22) == "Vamos a jugar alla?"

#aMinusculas: str -> str
#Pasa el string 'oracion' a minusculas
#Ej: aMinusculas("necesito el trabajo ASAP") -> "necesito el trabajo asap"
def aMinusculas(oracion):
    return oracion.lower()

assert aMinusculas("necesito el trabajo ASAP") == "necesito el trabajo asap"

#cambiarVelocidadSonido: Sonido int -> Sonido
#Cambia la velocidad del sonido afectando el tono del mismo, segun 'velocidad'
def cambiarVelocidadSonido(sound, velocidad):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * velocidad)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

#agregarPalabraProhibida: str -> None
#Agrega el string 'palabra' a la lista de palabras prohibidas
def agregarPalabraProhibida(palabra):
    swear_words.append(palabra)

#generarArchivoAudio: Sonido str -> None
#Genera el archivo .wav a partir del parametro audio, cuyo nombre será el ingresado en 'nombre'
def generarArchivoAudio(audio, nombre):
    return audio.export(nombre + ".wav", format="wav")
