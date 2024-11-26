from PIL import Image


def draw_canvas (width, height):
    image = Image.new('RGB', (width, height), 'white')
    image.save("finalImage_fabric.png")
