from PIL import Image

def encode_lsb(image_path, output_path):
    secret_password = "axpwagjt"
    binary_secret = ''.join(format(ord(c), '08b') for c in secret_password)
    binary_secret += '00000000'  # Null terminator
    
    img = Image.open(image_path).convert("RGB")
    
    if len(binary_secret) > img.width * img.height * 3:
        raise ValueError("Secret too large!")
    
    pixels = list(img.getdata())
    secret_index = 0
    new_pixels = []
    
    for pixel in pixels:
        r, g, b = pixel[0], pixel[1], pixel[2]
        if secret_index < len(binary_secret):
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
    print(f"Password embedded into {output_path}!")

# Example usage:
encode_lsb("original.png", "hidden_portal.png")
