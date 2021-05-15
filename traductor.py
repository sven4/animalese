# Salvador Vásquez
import animalese

"""
    esUnaMalaPalabra: string -> boolean
    Busca de manera recursiva si alguna de las palabras en la lista de malas palabras, coincide con la 
    palabra entregada.
    ej: esUnaMalaPalabra('feo') = True
        esUnaMalaPalabra('computin') = False 
"""


def esUnaMalaPalabra(palabra, indice=0):
    if palabra == animalese.palabraEnPosicion(indice):
        return True
    # Caso base, se revisaron todas las palabras de la lista
    if indice == animalese.palabrasProhibidas() - 1:
        return False
    return esUnaMalaPalabra(palabra, indice + 1)


assert esUnaMalaPalabra('feo')
assert not esUnaMalaPalabra('computin')

"""
    reemplazarPalabrasProhibidas: string (int) (string) (string)-> string
    Reemplaza las palabras prohibidas en "oraciones" por asteriscos
    ej: reemplazarPalabrasProhibidas('Mi amigo es muy malo') = 'Mi ***** es muy ****'
"""


def reemplazarPalabrasProhibidas(oracion, indice=0, palabraActual=''):
    # Revisamos siempre si la palabra actual es una mala palabra
    if esUnaMalaPalabra(animalese.aMinusculas(palabraActual)):
        palabraActual = '*' * animalese.largo(palabraActual)
        oracion = animalese.reemplazarExtracto(oracion, palabraActual, indice - animalese.largo(palabraActual),
                                               indice-1)

    # Caso base, indice es igual al largo de la oracion
    if indice == animalese.largo(oracion):
        return oracion

    # Hay que verificar si la letra actual es un espacio, en caso de serlo, palabraActual se "reiniciara"
    if animalese.existeEnOracion(' ', oracion) and animalese.obtenerLetraEnPosicion(oracion, indice) == ' ':
        return reemplazarPalabrasProhibidas(oracion, indice + 1, '')

    palabraActual += animalese.obtenerLetraEnPosicion(oracion, indice)
    return reemplazarPalabrasProhibidas(oracion, indice + 1, palabraActual)


assert reemplazarPalabrasProhibidas('maloa') == '****a'
assert reemplazarPalabrasProhibidas('malo') == '****'
assert reemplazarPalabrasProhibidas('Mi amigo es muy malo') == 'Mi amigo es muy ****'
assert reemplazarPalabrasProhibidas('MALO MALO MALO') == '**** **** ****'
assert reemplazarPalabrasProhibidas('MALO MALO MALO ') == '**** **** **** '
assert reemplazarPalabrasProhibidas('feo MALO tonto') == '*** **** tonto'
assert reemplazarPalabrasProhibidas(' . . . . ') == ' . . . . '

"""
    reemplazarParentesis: str (int) -> str
    Reemplaza los pensamientos (todo lo escrito entre parentesis) por asteriscos
    ej: reemplazarParentesis('Me gusta jugar (a veces) con mi amigo') = 'Me gusta jugar ********* con mi amigo'
"""


def reemplazarParentesis(oracion, indice=0):
    # Caso base, no quedan más parentesis en la oracion
    if not animalese.existeEnOracion('(', oracion):
        return oracion
    indiceAbrirParentesis = animalese.posicionCaracter(oracion, '(')
    indiceCerrarParentesis = animalese.posicionCaracter(oracion, ')')

    oracion = animalese.reemplazarExtracto(oracion, "*" * (1 + indiceCerrarParentesis - indiceAbrirParentesis),
                                           indiceAbrirParentesis, indiceCerrarParentesis)
    return reemplazarParentesis(oracion, indice + 1)


assert reemplazarParentesis('(pienso mucho)') == '**************'
assert reemplazarParentesis('Me gusta jugar (a veces) con mi amigo') == 'Me gusta jugar ********* con mi amigo'
assert reemplazarParentesis('Me agrada el rojo, el azul, el negro, (y el lila),'
                            ' pero destesto el turquesa (mentira)') == 'Me agrada el rojo, el azul, el negro,' \
                                                                       ' ***********, pero destesto el turquesa ' \
                                                                       '*********'

"""
    construirAudio: str Sonido -> Sonido
    Retorna el audio correspondiende a la oracion que se le pase
"""


def construirAudio(oracion, audio, indice=0):
    if indice == animalese.largo(oracion):
        return audio

    # Instancie las variables para que no quede demasiado largo el codigo
    letraActual = animalese.aMinusculas(animalese.obtenerLetraEnPosicion(oracion, indice))
    if indice + 1 != animalese.largo(oracion):
        posibleDigrafo = animalese.aMinusculas(letraActual + animalese.obtenerLetraEnPosicion(oracion, indice + 1))
        if animalese.esDigrafo(posibleDigrafo):
            return construirAudio(oracion, audio + animalese.obtenerSonido(posibleDigrafo), indice + 2)

    if animalese.esLetra(letraActual):
        return construirAudio(oracion, audio + animalese.obtenerSonido(letraActual), indice + 1)

    if animalese.esPuntuacion(letraActual):
        return construirAudio(oracion, audio + animalese.obtenerSonido('bebebese'), indice + 1)

    return construirAudio(oracion, audio, indice + 1)


"""
    procesarTexto: str -> Sonido
    Procesa el texto 'oracion', eliminando palabras prohibidas y pensamientos (palabras entre parentesis) 
    y devuelve un audio
"""


def procesarTexto(oracion):
    oracion = reemplazarPalabrasProhibidas(reemplazarParentesis(oracion))
    print(oracion)
    audio = construirAudio(oracion, animalese.nuevoAudio())
    return animalese.cambiarVelocidadSonido(audio, 2)
