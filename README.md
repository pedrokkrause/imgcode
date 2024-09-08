# imgcode

`imgcode` is a Python module that allows you to encode and decode any type of file within images using steganography. This can be useful for hiding data within images for secure transmission or storage.

## Features

- Encode any type of file (e.g., text, binary, images, pdf) into an image.
- Decode a file from an image.
- Simple and easy-to-use API.

## Installation

To use `imgcode`, you need to have Python installed on your system. You can install the required dependencies using `pip`:

```bash
pip install pillow numpy
```

## Usage

### Encoding a File into an Image

To encode a file into an image, use the `file_to_image` function:

```python
from imgcode import file_to_image

file_path = 'path/to/your/file.ext'  # Path to the file you want to encode
image_input = 'path/to/input/image.png'  # Path to the input image
image_output = 'path/to/output/image.png'  # Path to save the output image
seed = 12345  # Password needed to decode the file from the image

file_to_image(file_path, image_input, image_output, seed)
```

### Decoding a File from an Image

To decode a file from an image, use the `image_to_file` function:

```python
from imgcode import image_to_file

image_input = 'path/to/output/image.png'  # Path to the encoded image
file_output = 'path/to/decoded/file.ext'  # Path to save the decoded file
seed = 12345  # Password needed to decode the file from the image

image_to_file(image_input, file_output, seed)
```

### End-of-Transmission (EOT) Marker

The functions have an optional argument called `EOT_max`, which specifies the number of end-of-transmission (EOT) markers used to indicate the end of the encoded file within the image. By default, `EOT_max` is set to 5. This helps ensure that the decoding process correctly identifies the end of the file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Pillow](https://python-pillow.org/) - Python Imaging Library (PIL) fork.
- [NumPy](https://numpy.org/) - Fundamental package for scientific computing with Python.
