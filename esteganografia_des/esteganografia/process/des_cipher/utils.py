# HACE USO DE UNA LISTA PARA INTERCAMBIAR POSICIONES DE BITS
# Y EXPANDIR O ACORTAR EL TAMANO
def transpose(key_bits, table):
    new_key_bits = ''
    for bit_pos in table:
        new_key_bits += key_bits[bit_pos-1]
    return new_key_bits

# RECIBE UNA CADENA Y REGRESA LOS BITS REPRESENTANTES
def stob(string):
    key_bits = ''
    for c in string:
        bits = bin(ord(c))[2:].zfill(8)
        key_bits += bits
    return key_bits

# RECIBE UNA CADENA DE HEXADECIMALES Y REGRESA LOS BITS REPRESENTANTES
def htob(string):
    bits = ''
    for i in range(int(len(string)/2)):
        tmp = string[i*2:(i+1)*2]
        bits += bin(int(tmp, 16))[2:].zfill(8)
    return bits

# SEPARA Y CONVIERTE BITS A ASCII
def btoh(bits):
    return hex(int(bits, 2))[2:]

# SEPARA Y CONVIERTE BITS A ASCII
def btos(bits):
    string = ''
    for i in range(int(len(bits)/8)):
        tmp = bits[i*8:(i+1)*8]
        string += chr(int(tmp, 2))
    return string
