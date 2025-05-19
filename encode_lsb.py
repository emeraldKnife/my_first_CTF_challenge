from PIL import Image

def encode_lsb(image_path, secret_message, output_path):
    img = Image.open(image_path).convert("RGB")  # Force convert to RGB mode
    binary_secret = ''.join(format(ord(c), '08b') for c in secret_message)
    binary_secret += '00000000'  # Null terminator
    
    if len(binary_secret) > img.width * img.height * 3:
        raise ValueError("Secret message too large for the image!")
    
    pixels = list(img.getdata())
    secret_index = 0
    new_pixels = []
    
    for pixel in pixels:
        # Extract RGB values (ignore alpha if present)
        r, g, b = pixel[0], pixel[1], pixel[2]
        
        if secret_index < len(binary_secret):
            # Modify LSB of each RGB component
            r = (r & 0xFE) | int(binary_secret[secret_index])
            secret_index += 1
            if secret_index < len(binary_secret):
                g = (g & 0xFE) | int(binary_secret[secret_index])
                secret_index += 1
            if secret_index < len(binary_secret):
                b = (b & 0xFE) | int(binary_secret[secret_index])
                secret_index += 1
        new_pixels.append((r, g, b))
    
    new_img = Image.new('RGB', img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path)
    print(f"Secret embedded into {output_path}!")

encode_lsb("original.png", "aHR0cDovL2xvY2FsaG9zdDo1MDAw", "hidden_portal.png")