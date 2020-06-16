from PIL import Image
from .des_cipher import des_cipher


def hide(pillow_image, message, key):
	pixel_cells = pillow_image.load()
	width = pillow_image.size[0]
	height = pillow_image.size[1]
	bits = des_cipher.des_control(message, key, 1)
	# SE AGREGAN DOS BYTES QUE INDICAN QUE TERMINA EL MENSAJE
	bits += '11111111'
	bits += '00000000'

	i = 0
	bit_size = len(bits)
	for x in range(width):
		for y in range(height):
			if i < bit_size:
				pixels = pixel_cells[x, y]

				new_pixel = []
				for j in range(3):
					if i < bit_size:
						new_color = change_last_bit(pixels[j], bits[i])
						new_pixel.append(new_color)
						i += 1
					else:
						new_pixel.append(pixels[j])
				pixel_cells[x, y] = (new_pixel[0], new_pixel[1], new_pixel[2])
			else:
				break
		else:
			continue
		break
	image_file = 'C:/Users/loera/Pictures/imagen_sin_secretos.png'
	pillow_image.save(image_file)
	return image_file

def change_last_bit(byte, bit):
	color_bits = bin(byte)[2:].zfill(8)
	new_color_bits = color_bits[:-1] + str(bit)
	return int(new_color_bits, 2)