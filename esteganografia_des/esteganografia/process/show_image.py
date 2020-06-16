from PIL import Image
from .des_cipher import des_cipher


def show(pillow_image, key):
	pixel_cells = pillow_image.load()
	width = pillow_image.size[0]
	height = pillow_image.size[1]
	
	message_bits = ''
	byte = ''
	last_byte = ''
	end = False

	for x in range(width):
		for y in range(height):
			pixels = pixel_cells[x, y]
			for j in range(3):
				byte += get_last_bit(pixels[j])
				if len(byte) >= 8:
					if byte == '00000000' and last_byte == '11111111':
						message_bits = message_bits[:-8]
						break
					message_bits += byte
					last_byte = byte
					byte = ''
			else:
				continue
			break
		else:
			continue
		break
	return des_cipher.des_control(message_bits, key, 0)

def get_last_bit(byte):
	color_bits = bin(byte)[2:].zfill(8)
	return color_bits[-1]
