import numpy as np
import matplotlib.pyplot as plt
import random
import tkinter as tk
import math

def get_random_value(start_range=None, end_range=None):
    if start_range and end_range:
        return random.randint(start_range, end_range)
    return random.random()

total_length_yarn_warp = 1000 * 3 *1000
total_length_yarn_weft = 1000 *3 *1000

# Okay so after every 1000mm we will move to the next x or y coordinate
# so again we will have faults there

fault_arr_thick = np.random.poisson(0.02, total_length_yarn_weft)
fault_arr_thin = np.random.poisson(0.02, total_length_yarn_weft)
fault_arr_neps = np.random.poisson(0.02, total_length_yarn_weft)
fault_arr = fault_arr_thick + fault_arr_thin + fault_arr_neps
fault_arr_thick_warp = np.random.poisson(0.02, total_length_yarn_warp)
fault_arr_thin_warp = np.random.poisson(0.02, total_length_yarn_warp)
fault_arr_neps_warp = np.random.poisson(0.02, total_length_yarn_warp)
fault_arr_warp = fault_arr_thick_warp + fault_arr_thin_warp + fault_arr_neps_warp

# Create a Tkinter root window to get screen size
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.withdraw()  # Hide the Tkinter root window

thick_position = []
thin_position = []
neps_position = []

# Create a figure with the screen size
fig = plt.figure(figsize=(screen_width / 100, screen_height / 100), dpi=100)

for i in range(0, 3*1000):
    plt.plot([i, i], [0, 1000], color='black', linewidth=0.5)
    plt.plot([0, 1000], [i, i], color='black', linewidth=0.5)

for i in range(0, 3*1000):
    if fault_arr[i] > 0:
        count = 0
        while count < fault_arr[i]:
            if fault_arr_thick[i] > 0:
                count += 1
                fault_width = 1 + get_random_value(0, 50) / 100
                fault_position = get_random_value() * 1000
                thick_position.append({
                    "x": i,
                    "y": fault_position
                })
                plt.plot([i, i], [fault_position, fault_position + 24], color='red', linewidth=0.5*fault_width)
            elif fault_arr_thin[i] > 0:
                count += 1
                fault_width = max(0.5, 1 - get_random_value(0, 50) / 100)  # Ensure the width isn't negative

                fault_position = get_random_value() * 1000
                thin_position.append({
                    "x": i,
                    "y": fault_position
                })
                plt.plot([i, i], [fault_position, fault_position + 24], color='blue', linewidth=0.5*fault_width)
            elif fault_arr_neps[i] > 0:
                count += 1
                fault_width = int(1 + get_random_value(50, 500) / 200)
                fault_position = get_random_value() * 1000
                neps_position.append({
                    "x": i,
                    "y": fault_position
                })
                circle = plt.Circle((fault_position, i), 0.5/2 * fault_width, color='green', fill=True)
                plt.gca().add_patch(circle) 
            else:
                count = fault_arr[i]  # Exit the loop if no fault found
    # else:
    

    if fault_arr_warp[i] > 0:
        count = 0
        while count < fault_arr_warp[i]:
            if fault_arr_thick_warp[i] > 0:
                count += 1
                fault_width = int(1 + get_random_value(0, 50) / 100)
                fault_position = get_random_value() * 1000
                thick_position.append({
                    "x": fault_position,
                    "y": i
                })
                plt.plot([fault_position, fault_position + 24], [i, i], color='red', linewidth=0.5*fault_width)
            elif fault_arr_thin_warp[i] > 0:
                count += 1
                fault_width = max(0.5, 1 - get_random_value(0, 50) / 100)
                fault_position = get_random_value() * 1000
                thin_position.append({
                    "x": fault_position,
                    "y": i
                })
                plt.plot([fault_position, fault_position + 24], [i, i], color='blue', linewidth=0.5*fault_width)
            elif fault_arr_neps_warp[i] > 0:
                count += 1
                fault_width = int(1 + get_random_value(50, 500) / 200)
                fault_position = get_random_value() * 1000
                neps_position.append({
                    "x": fault_position,
                    "y": i
                })
                circle = plt.Circle((i, fault_position), 0.5 * fault_width, color='green', fill=True) 
                plt.gca().add_patch(circle) 
            else:
                count = fault_arr_warp[i]  # Exit the loop if no fault found
    # else:
        

        #P(TH,TH)	P(TH,TN)	P(TH,N)	P(TN,TH)	P(TN,TN)	P(TN,N)	P(N,TH)	P(N,TN)	P(N,N)

# print("Thick Position", thick_position)
# print("Thin Position", thin_position)
# print("Neps Position", neps_position)

fault_closeness_probability = {
    "TH,TH": 0, #
    "TH,TN": 0, #
    "TH,N": 0, #
    # "TN,TH": 0,
    "TN,TN": 0, #
    "TN,N": 0, #
    # "N,TH": 0,
    # "N,TN": 0,
    "N,N": 0,
}

# Calculate closeness for each pair within 24-unit distance

# Thick-Thick
for i, thick in enumerate(thick_position):
    # print(i)
    # print( thick.get("x"), thick.get("y"))
    x1 = thick.get("x")
    y1 = thick.get("y")
    for j in range(i + 1, len(thick_position)):
        # thick_x = i
        # other_thick_x = j
        x2 = thick_position[j].get("x")
        y2 = thick_position[j].get("y")
        # print(thick_position[j].get("x"), thick_position[j].get("y"))
        
        if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= 24:
            fault_closeness_probability["TH,TH"] += 1
    
# Thick-Thin
for thick in thick_position:
    x1 = thick.get("x")
    y1 = thick.get("y")
    for thin in thin_position:
        x2 = thin.get("x")
        y2 = thin.get("y")
        if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= 24:
            fault_closeness_probability["TH,TN"] += 1


# thin - thin
for i, thin in enumerate(thin_position):
    x1 = thin.get("x")
    y1 = thin.get("y")
    for j in range(i + 1, len(thin_position)):
        x2 = thin_position[j].get("x")
        y2 = thin_position[j].get("y")
        if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= 24:
            fault_closeness_probability["TN,TN"] += 1

#  thin - neps
for thin in thin_position:
    x1 = thin.get("x")
    y1 = thin.get("y")
    for neps in neps_position:
        x2 = neps.get("x")
        y2 = neps.get("y")
        if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= 24:
            fault_closeness_probability["TN,N"] += 1

#thick - neps
for thick in thick_position:
    x1 = thick.get("x")
    y1 = thick.get("y")
    for neps in neps_position:
        x2 = neps.get("x")
        y2 = neps.get("y")
        if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= 24:
            fault_closeness_probability["TH,N"] += 1



# neps - neps
for i, neps in enumerate(neps_position):
    x1 = neps.get("x")
    y1 = neps.get("y")
    for j in range(i + 1, len(neps_position)):
        x2 = neps_position[j].get("x")
        y2 = neps_position[j].get("y")
        if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= 24:
            fault_closeness_probability["N,N"] += 1


print("Probability of closeness of faults", "Count")
for key, value in fault_closeness_probability.items():
    print(key, value)



print("Done")

# Set the scale for x and y axes to cover the entire screen dimensions
plt.xlim(0, 1000)
plt.ylim(0, 1000)

# Set full screen mode
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

# Display the plot
plt.show()




# import math
# from itertools import combinations

# # Helper function to calculate distance between two points
# def calculate_distance(point1, point2):
#     return math.sqrt((point1.get("x") - point2.get("x")) ** 2 + (point1.get("y") - point2.get("y")) ** 2)

# # Update fault closeness counts
# def update_fault_closeness_count(fault_closeness_probability, positions, label, max_distance):
#     # Two-element combinations
#     for point1, point2 in combinations(positions, 2):
#         if calculate_distance(point1, point2) <= max_distance:
#             fault_closeness_probability[label] += 1

#     # Three-element combinations
#     for point1, point2, point3 in combinations(positions, 3):
#         if (calculate_distance(point1, point2) <= max_distance and
#             calculate_distance(point1, point3) <= max_distance and
#             calculate_distance(point2, point3) <= max_distance):
#             fault_closeness_probability[f"{label},{label},{label}"] += 1

#     # Four-element combinations
#     for point1, point2, point3, point4 in combinations(positions, 4):
#         if (calculate_distance(point1, point2) <= max_distance and
#             calculate_distance(point1, point3) <= max_distance and
#             calculate_distance(point1, point4) <= max_distance and
#             calculate_distance(point2, point3) <= max_distance and
#             calculate_distance(point2, point4) <= max_distance and
#             calculate_distance(point3, point4) <= max_distance):
#             fault_closeness_probability[f"{label},{label},{label},{label}"] += 1

# # Initialize data
# fault_closeness_probability = {
#     "TH,TH": 0, "TH,TN": 0, "TH,N": 0, "TN,TN": 0, "TN,N": 0, "N,N": 0,
#     "TH,TH,TH": 0, "TH,TH,TN": 0, "TH,TH,N": 0, "TH,TN,TN": 0, "TH,TN,N": 0,
#     "TH,N,N": 0, "TN,TN,TN": 0, "TN,TN,N": 0, "TN,N,N": 0, "N,N,N": 0,
#     "TH,TH,TH,TH": 0, "TH,TH,TH,TN": 0, "TH,TH,TH,N": 0, "TH,TH,TN,TN": 0,
#     "TH,TH,TN,N": 0, "TH,TH,N,N": 0, "TH,TN,TN,TN": 0, "TH,TN,TN,N": 0,
#     "TH,TN,N,N": 0, "TH,N,N,N": 0, "TN,TN,TN,TN": 0, "TN,TN,TN,N": 0,
#     "TN,TN,N,N": 0, "TN,N,N,N": 0, "N,N,N,N": 0
# }

# # Positions (example lists of dictionaries with x, y coordinates)
# thick_position = [{"x": 1, "y": 2}, {"x": 3, "y": 4}, {"x": 5, "y": 6}]  # Add actual data
# thin_position = [{"x": 2, "y": 3}, {"x": 4, "y": 5}, {"x": 6, "y": 7}]   # Add actual data
# neps_position = [{"x": 1, "y": 1}, {"x": 3, "y": 3}, {"x": 5, "y": 5}]   # Add actual data

# max_distance = 24  # Threshold distance

# # Calculate fault closeness probabilities
# update_fault_closeness_count(fault_closeness_probability, thick_position, "TH", max_distance)
# update_fault_closeness_count(fault_closeness_probability, thin_position, "TN", max_distance)
# update_fault_closeness_count(fault_closeness_probability, neps_position, "N", max_distance)

# # Thick-Thin combinations
# for thick in thick_position:
#     for thin in thin_position:
#         if calculate_distance(thick, thin) <= max_distance:
#             fault_closeness_probability["TH,TN"] += 1

# # Thick-Neps combinations
# for thick in thick_position:
#     for neps in neps_position:
#         if calculate_distance(thick, neps) <= max_distance:
#             fault_closeness_probability["TH,N"] += 1

# # Thin-Neps combinations
# for thin in thin_position:
#     for neps in neps_position:
#         if calculate_distance(thin, neps) <= max_distance:
#             fault_closeness_probability["TN,N"] += 1

# # Print results
# print(fault_closeness_probability)
