from .keys_generator import generate

from . import utils
from . import tables

# CONTROLADOR DEL ALGORITMO.
# SI choice ES 1 SE CIFRA
# SI choice ES 0 SE DESCIFRA
def des_control(message, key, choice):
    # OBTIENE LAS LLAVES PARA CADA UNA DE LAS 16 RONDAS
    keys = generate(key)
    # CONVIERTE EL MENSAJE A BINARIO
    if choice == 1:
        message = utils.stob(message)

    # ROMPE EL MENSAJE EN BLOQUES DE 64 BITS
    message_blocks = break_message(message)
    output = ''

    # ITERA Y CIFRA CADA UNO DE LOS BLOQUES
    for block in message_blocks:
        cipher_message = des_cipher(block, keys, choice)
        if choice == 0:
            output += utils.btos(cipher_message)
        elif choice == 1:
            output += cipher_message
    return output

def break_message(message):
    message_blocks = []
    message_length = len(message)
    if message_length % 64 != 0:
        difference = 64 - (message_length % 64)
        message += "0"*difference
        message_length = len(message)

    for i in range(0, int(message_length / 64)):
        tmp_message = message[i*64:(i+1)*64]
        message_blocks.append(tmp_message)
    return message_blocks

def des_cipher(block, keys, choice):
    # APLICA LA PERMUTACION INICIAL Y RECIBE DOS MITADES
    result = initial_perm(block)
    prev_left = ''
    prev_right = ''
    
    # SE ITERAN LAS 16 RONDAS APLICANDO FEISTEL A CADA UNA
    next_left = result[0]
    next_right = result[1]
    for i in range(16):
        prev_left = next_left
        prev_right = next_right
        next_left = prev_right
        if choice == 0:
            next_right = xor(prev_left, feistel(prev_right, keys[15-i]))
        elif choice == 1:
            next_right = xor(prev_left, feistel(prev_right, keys[i]))

    final_res = utils.transpose(next_right+next_left, tables.pI)
    return final_res

def initial_perm(block):
    # APLICA LA TABLA DE LA PRIMERA ITERACION PARA
    # INTERCAMBIAR POSICIONES DE LOS BITS
    new_block = utils.transpose(block, tables.ip)
    # DIVIDE EL BLOQUE EN 2 MITADES DE 32 BITS
    left_block = new_block[0:32]
    right_block = new_block[32:64]
    return [left_block, right_block]

def feistel(right_block, key):
    # APLICA LA TABLA e
    tmp_block = utils.transpose(right_block, tables.e)
    # APLICA XOR CON EL BLOQUE Y LA LLAVE
    xor_result = xor(tmp_block, key)

    # SE ROMPE EL BLOQUE DE 48 BITS EN 8 GRUPOS DE 6 BITS
    six_packs = feistel_break(xor_result)
    # ITERA CADA GRUPO DE 6 BITS PARA RESULTAR CON 4 BITS Y ASI
    # TERMINAR CON UN BLOQUE DE 32 BITS
    new_block = ''
    for i in range(len(six_packs)):
        new_block += s_search(six_packs[i], 's_{table_number}'.format(table_number=i+1))
    new_block = utils.transpose(new_block, tables.p)
    return new_block

# REMPLAZA EL SIX_PACK POR 4 BITS
def s_search(six_pack, table):
    row = int(six_pack[0] + six_pack[-1], 2)
    col = int(six_pack[1:-1], 2)

    return bin(tables.s_tables[table][row][col])[2:].zfill(4)

# ROMPE UN BLOQUE DE 48 BITS EN 8 GRUPOS DE 6 BITS
def feistel_break(block):
    broken_block = []
    for i in range(8):
        tmp_block = block[i*6:(i+1)*6]
        broken_block.append(tmp_block)
    return broken_block

# APLICA XOR A DOS CADENAS DE BITS
def xor(a, b):
    result = int(a, 2) ^ int(b, 2)
    return '{0:0{1}b}'.format(result, len(a))