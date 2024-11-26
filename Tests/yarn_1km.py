from PIL import Image, ImageDraw, ImageTk
import random
import tkinter as tk
import math

def get_random_value(start_range=None,end_range=None):
    if start_range and end_range:
        return random.randint(start_range,end_range)
    return random.random()

def create_yarn_image_with_faults(yarn_dia,width, height,screen_height,screen_width):
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    # Draw the yarn as a simple line
    draw.line((0, height // 2, width, height // 2), fill='black', width=yarn_dia)

    for i in range(0,14):
        fault_width = int(yarn_dia + get_random_value(50,500)/100)
        fault_position = get_random_value()
        draw.line((screen_width*fault_position, screen_height , screen_width*fault_position+24, screen_height), fill='red', width=fault_width)

    image.show()
    image.save("finalImage.png")

# def add_faults(image, faults):
    
#     for fault in faults:
#         x, y, fault_type,thickQuant= fault
#         for i in range(0,thickQuant):
#             if fault_type == 'thick':
#                 fault_width = int(1 + get_random_value(50,500)/100)
#                 fault_position = get_random_value()
#                 draw.line((x*fault_position, y , x*fault_position+3, y), fill='red', width=fault_width)
#         # elif fault_type == 'thin':
#         #     draw.line((x, y - 2, x, y + 2), fill='blue', width=1)
#         # elif fault_type == 'neps':
#         #     draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill='green')
    
#     return image


def get_screen_resolution():
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height

def take_input_from_user():
    print("Choose Method to Generate Image")
    print("1. Yarn Diameter /n 2. Yarn Count")
    choice = int(input())
    if choice == 1:
        yarn_dia = int(input("Enter Yarn Diameter in mm: "))
        return yarn_dia
    elif choice == 2:
        yarn_count = int(input("Enter Yarn Count: "))
        yarn_dia = 0.9071428571428/math.sqrt(yarn_count)
        if(yarn_dia<1):
            yarn_dia = 1
        return yarn_dia
    

if __name__ == "__main__":
    screen_width, screen_height = get_screen_resolution()
    print("Screen Resolution: ", screen_width, screen_height)

    width = 100000  # 1000 meters represented as 100000 pixels (10mm = 1 pixel)
    height = screen_height  

    # take input from user
    yarn_dia = take_input_from_user()

    
    yarn_image = create_yarn_image_with_faults(yarn_dia,width, height,screen_height//2,width)
    
    
