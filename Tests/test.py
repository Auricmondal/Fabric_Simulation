# from PIL import Image, ImageDraw, ImageTk
# import random
# import tkinter as tk
# import math

# def get_random_value(start_range=None,end_range=None):
#     if start_range and end_range:
#         return random.randint(start_range,end_range)
#     return random.random()

# def create_yarn_image_with_faults(yarn_dia,width, height,screen_height,screen_width):
#     image = Image.new('RGB', (width, height), 'white')
#     draw = ImageDraw.Draw(image)
#     # Draw the yarn as a simple line
#     draw.line((0, height // 2, width, height // 2), fill='black', width=yarn_dia)

#     for i in range(0,14):
#         fault_width = int(yarn_dia + get_random_value(50,500)/100)
#         fault_position = get_random_value()
#         draw.line((screen_width*fault_position, screen_height , screen_width*fault_position+24, screen_height), fill='red', width=fault_width)

#     image.show()
#     image.save("finalImage.png")

# # def add_faults(image, faults):
    
# #     for fault in faults:
# #         x, y, fault_type,thickQuant= fault
# #         for i in range(0,thickQuant):
# #             if fault_type == 'thick':
# #                 fault_width = int(1 + get_random_value(50,500)/100)
# #                 fault_position = get_random_value()
# #                 draw.line((x*fault_position, y , x*fault_position+3, y), fill='red', width=fault_width)
# #         # elif fault_type == 'thin':
# #         #     draw.line((x, y - 2, x, y + 2), fill='blue', width=1)
# #         # elif fault_type == 'neps':
# #         #     draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill='green')
    
# #     return image


# def get_screen_resolution():
#     root = tk.Tk()
#     width = root.winfo_screenwidth()
#     height = root.winfo_screenheight()
#     root.destroy()
#     return width, height

# def take_input_from_user():
#     print("Choose Method to Generate Image")
#     print("1. Yarn Diameter /n 2. Yarn Count")
#     choice = int(input())
#     if choice == 1:
#         yarn_dia = int(input("Enter Yarn Diameter in mm: ")*10)
#         return yarn_dia
#     elif choice == 2:
#         yarn_count = int(input("Enter Yarn Count: "))
#         yarn_dia =int( 0.9071428571428/math.sqrt(yarn_count) *10)
#         return yarn_dia
    

# if __name__ == "__main__":
#     screen_width, screen_height = get_screen_resolution()
#     print("Screen Resolution: ", screen_width, screen_height)

#     width = int(10000000 *120//25.4)
#     height = int(10000000 * 120//25.4)

#     # take input from user
#     yarn_dia = take_input_from_user()
#     print(yarn_dia)

    
#     yarn_image = create_yarn_image_with_faults(yarn_dia,width, height,screen_height//2,width)
    
    
# import matplotlib.pyplot as plt

# # Dimensions in millimeters
# length_m = 1000
# width_mm = 1

# # Create a figure with the specified dimensions
# fig, ax = plt.subplots(figsize=(length_m / 25.4, width_mm / 25.4))

# # Draw the line
# ax.plot([0, length_m], [width_mm / 2, width_mm / 2], linewidth=width_mm / 25.4, color='black', fill='black')

# # Remove axes
# ax.axis('off')

# plt.show()


import numpy as np
import matplotlib.pyplot as plt
import random
import tkinter as tk

def get_random_value(start_range=None, end_range=None):
    if start_range and end_range:
        return random.randint(start_range, end_range)
    return random.random()

total_length_yarn_warp = 1000 * 1000 / 1000
total_length_yarn_weft = 1000 * 1000 / 1000

# Okay so after every 1000mm we will move to the next x or y coordinate
# so again we will have faults there

fault_arr_thick = np.random.poisson(0.02, 1000)
fault_arr_thin = np.random.poisson(0.02, 1000)
fault_arr_neps = np.random.poisson(0.02, 1000)
fault_arr = fault_arr_thick + fault_arr_thin + fault_arr_neps
fault_arr_thick_warp = np.random.poisson(0.02, 1000)
fault_arr_thin_warp = np.random.poisson(0.02, 1000)
fault_arr_neps_warp = np.random.poisson(0.02, 1000)
fault_arr_warp = fault_arr_thick_warp + fault_arr_thin_warp + fault_arr_neps_warp

# Create a Tkinter root window to get screen size
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.withdraw()  # Hide the Tkinter root window

# Create a figure with the screen size
fig = plt.figure(figsize=(screen_width / 100, screen_height / 100), dpi=100)

for i in range(0, 1000):
    print(i)
    if fault_arr[i] > 0:
        count = 0
        while count < fault_arr[i]:
            if fault_arr_thick[i] > 0:
                count += 1
                fault_width = int(1 + get_random_value(50, 500) / 100)
                fault_position = get_random_value() * 1000
                plt.plot([i, i], [fault_position, fault_position + 24], color='red', linewidth=fault_width)
            elif fault_arr_thin[i] > 0:
                count += 1
                fault_width = max(0.5, 1 - get_random_value(0, 50) / 100)  # Ensure the width isn't negative
                fault_position = get_random_value() * 1000
                plt.plot([i, i], [fault_position, fault_position + 24], color='blue', linewidth=fault_width)
            elif fault_arr_neps[i] > 0:
                count += 1
                fault_width = int(1 + get_random_value(50, 500) / 100)
                fault_position = get_random_value() * 1000
                circle = plt.Circle((fault_position, i), 12 * fault_width, color='green', fill=True)
                plt.gca().add_patch(circle) 
            else:
                count = fault_arr[i]  # Exit the loop if no fault found
    # else:
        # plt.plot([i, i], [0, 1000], color='black', linewidth=1)

    if fault_arr_warp[i] > 0:
        count = 0
        while count < fault_arr_warp[i]:
            if fault_arr_thick_warp[i] > 0:
                count += 1
                fault_width = int(1 + get_random_value(50, 500) / 100)
                fault_position = get_random_value() * 1000
                plt.plot([fault_position, fault_position + 24], [i, i], color='red', linewidth=fault_width)
            elif fault_arr_thin_warp[i] > 0:
                count += 1
                fault_width = max(0.5, 1 - get_random_value(0, 50) / 100)
                fault_position = get_random_value() * 1000
                plt.plot([fault_position, fault_position + 24], [i, i], color='blue', linewidth=fault_width)
            elif fault_arr_neps_warp[i] > 0:
                count += 1
                fault_width = int(1 + get_random_value(50, 500) / 100)
                fault_position = get_random_value() * 1000
                circle = plt.Circle((i, fault_position), 12 * fault_width, color='green', fill=True) 
                plt.gca().add_patch(circle) 
            else:
                count = fault_arr_warp[i]  # Exit the loop if no fault found
    # else:
        # plt.plot([0, 1000], [i, i], color='black', linewidth=0.5)

print("Done")
# Set the scale for x and y axes to cover the entire screen dimensions
plt.xlim(0, 1000)
plt.ylim(0, 1000)

# Set full screen mode
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

# Display the plot
plt.show()
