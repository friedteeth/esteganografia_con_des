from . import utils
from . import tables


def generate(key_string):
    # VERIFICA QUE EL LONGITUD DE LA LLAVE SEA DE 64 BITS
    key_string = adjust_key(key_string)
    # CONVIERTE LA LLAVE A UNA LISTA DE BITS
    key_bits = utils.stob(key_string)
    # APLICA LA TABLA pc1 PARA COMPRIMIR LA LLAVE A 56 BITS
    key_bits = utils.transpose(key_bits, tables.pc1)
    # DIVIDE LA LLAVE DE 56 BITS EN DOS PARTES IGUALES
    key_bits_left = key_bits[0:28]
    key_bits_right = key_bits[28:56]

    round_keys = []
    # GENERA LAS LLAVES DE LAS 16 RONDAS
    for i in range(1, 17):
        key_bits_left = shift_left(key_bits_left, i)
        key_bits_right = shift_left(key_bits_right, i)

        round_keys.append(utils.transpose(key_bits_left+key_bits_right, tables.pc2))
    return round_keys

# AJUSTA LA LLAVE A UNA LONGITUD DE 64 BITS
# REPITE LA LLAVE SI FALTAN Y CORTA LA LLAVE
# SI SE PASA
def adjust_key(key_string):
    if len(key_string) == 8:
        return key_string
    else:
        if len(key_string) > 8:
            return key_string[0:8]
        else:
            new_key = key_string
            while len(new_key) < 8:
                for c in key_string:
                    new_key += c
                    if len(new_key) == 8:
                        return new_key

# ROTA UNA LISTA HACIA LA IZQUIERDA POR 1 O 2 BITS
# DEPENDIENDO DE LA RONDA QUE SE ENCUENTRE
def shift_left(bits, round):
    new_bits = bits
    shifts = 1 if round in tables.one_bit_shift else 2
    for i in range(0, shifts):
        tmp_char = new_bits[0]
        new_bits = new_bits[1:] + tmp_char
    return new_bits
