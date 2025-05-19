# Walkthrough everything!

## About the challenge

This is a CTF challenge that uses LSB steganography and web exploitation. The challenge consists of hiding a link in the photo given. The LSBs of pixels of the photo were modified to store the link. The link directs us to the web page which is to be exploited for the flag. The flag is of the format `flag{...}`.

## Solution

To solve the CTF, we first need to decode the `.png` file given to us.
<br>
<br>
To decode the photo, we will use the following script:-
```python
from PIL import Image

def decode_lsb(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    binary_data = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]  # Get RGB values (ignoring alpha if present)
            binary_data.append(r & 1)  # Extract LSB from Red
            binary_data.append(g & 1)  # Extract LSB from Green
            binary_data.append(b & 1)  # Extract LSB from Blue

    # Here we will convert the binary lists into bytes.
    message = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) < 8:
            break  # Incomplete byte
        char = int(''.join(map(str, byte)), 2)
        if char == 0:  # Null terminator (optional)
            break
        message.append(chr(char))

    return ''.join(message)

image_path = "city_of_OZ.png"
hidden_message = decode_lsb(image_path)
print("Hidden Message:", hidden_message)
```

<br>

This will lead us with the message "aHR0cDovL2xvY2FsaG9zdDo1MDAw" which can be easily recognised as a base64 code. When converted, we get "http://localhost:5000". This is the link for the web that is to be exploited.
