from PIL import Image
import numpy as np
import random
import os
import itertools

def bits(byte):
    """Yield the bits of a byte, from least significant to most significant."""
    for i in range(8):
        yield byte & 1
        byte >>= 1

def new_pixel_value(value, bit):
    """Return the new pixel value with the least significant bit set to the given bit."""
    value_bit = value & 1
    if value_bit == bit:
        return value
    return value - 1 if bit == 0 else value + 1

def file_to_image(file_path, image_input, image_output, seed, EOT_max=5):
    """Encode a file into an image."""
    img = Image.open(image_input).convert('RGB')
    img_array = np.array(img)
    height, width, channels = img_array.shape
    maximum_bits = height * width * 3

    total_bits = (os.stat(file_path).st_size + EOT_max) * 8
    if total_bits > maximum_bits:
        raise ValueError(
            f'Maximum number of bits supported for this image is {maximum_bits}. '
            f'Your file is {total_bits} bits ({total_bits / maximum_bits * 100:.2f}% bigger).'
        )

    img_array = img_array.reshape((height * width, channels))
    order = list(range(height * width))
    random.Random(seed).shuffle(order)

    end_of_file = b'\x04' * EOT_max

    with open(file_path, 'rb') as file:
        i = 0
        j = 0
        for byte in itertools.chain(file.read(), end_of_file):
            for bit in bits(byte):
                idx = order[i]
                pixel = img_array[idx]
                pixel[j] = new_pixel_value(pixel[j], bit)
                if j == 2:
                    j = 0
                    i += 1
                else:
                    j += 1

    img_array = img_array.reshape((height, width, channels))
    img = Image.fromarray(img_array, 'RGB')
    img.save(image_output)

def image_to_file(image_input, file_output, seed, EOT_max=5):
    """Decode a file from an image."""
    img = Image.open(image_input).convert('RGB')
    img_array = np.array(img)
    height, width, channels = img_array.shape
    img_array = img_array.reshape((height * width, channels))

    order = list(range(height * width))
    random.Random(seed).shuffle(order)

    file_bytes = bytearray()
    byte_int = 0
    i = 0
    j = 0
    EOT_count = 0

    while True:
        bit = 1
        for k in range(8):
            idx = order[i]
            pixel = img_array[idx]
            pixel_bit = pixel[j] & 1
            if pixel_bit:
                byte_int += bit
            bit <<= 1
            if j == 2:
                j = 0
                i += 1
            else:
                j += 1

        if byte_int == 4:
            EOT_count += 1
        else:
            EOT_count = 0

        if EOT_count == EOT_max:
            break

        file_bytes.append(byte_int)
        byte_int = 0

    with open(file_output, 'wb') as file:
        file.write(file_bytes[:-EOT_count + 1])
