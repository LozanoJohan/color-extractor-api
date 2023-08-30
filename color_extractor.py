from PIL import Image
from config import MAX_WIDTH, MAX_HEIGHT, UPLOAD_DIR
from image import ImageResponse




def extract(file_name: str):
    colors = []

    imagen = Image.open(UPLOAD_DIR + '/' + file_name) 
    width, height = imagen.size

    if width > MAX_WIDTH or height > MAX_HEIGHT:
        # Resize the image to 72x72 pixels
        imagen = imagen.resize((MAX_WIDTH, MAX_HEIGHT), Image.ADAPTIVE)
        width, height = MAX_WIDTH, MAX_HEIGHT

    for y in range(height):
        for x in range(width):
            color_pixel = imagen.getpixel((x, y))
            color_hex = "#{:02X}{:02X}{:02X}".format(color_pixel[0], color_pixel[1], color_pixel[2])

            colors.append(color_hex)
    
    img = ImageResponse(name=file_name.split('.')[0], ext=file_name.split('.')[1], width=width, height=height, colors=colors)
    
    return img
        
