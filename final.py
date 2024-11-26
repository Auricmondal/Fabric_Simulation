from fabric import yarn_info,get_fault_location
from core import get_screen_info


import numpy as np
import matplotlib.pyplot as plt
import random
import tkinter as tk
import math

def get_random_value(start_range=None, end_range=None):
    if start_range and end_range:
        return random.randint(start_range, end_range)
    return random.random()

if __name__ == "__main__":

    print("Generating a fabric of 1m x 1m ")
    print("Enter Fabric Details")
    yarn_dia = yarn_info.input_yarn_dia_info()
    ep_mm = int(int(input("Enter EPI: "))/25.4) #warp
    pp_mm= int(int(input("Enter PPI: "))/25.4 )#weft


    #total yarn length in mm = lenght of warp or weft * EPMM or PPMM * length of weft or warp
    # as if there are EPMM yarns in 1 mm then there will be 1000 * EPMM yarns in 1m
    # and as we need a fabric of dimension 1 m x 1 m so we each yarn needs to be 1000 mm long
    # so total yarn length = 1000 * 1000 * EPMM or PPMM

    total_length_yarn_warp = int(1000 * 1000 * ep_mm)
    total_length_yarn_weft = int(1000 * 1000 * pp_mm)

    # Okay so after every 1000mm we will move to the next x or y coordinate
    # so again we will have faults there
    faults = get_fault_location.get_fault_location_list(total_length_yarn_weft, total_length_yarn_warp)
    fault_arr_thick = faults.get("thick")
    fault_arr_thin = faults.get("thin")
    fault_arr_neps = faults.get("neps")
    fault_arr = faults.get("total_weft")
    fault_arr_thick_warp = faults.get("thick_warp")
    fault_arr_thin_warp = faults.get("thin_warp")
    fault_arr_neps_warp = faults.get("neps_warp")
    fault_arr_warp = faults.get("total_warp")
    

    screen_width = get_screen_info.get_screen_resolution()[0]
    screen_height = get_screen_info.get_screen_resolution()[1]


    thick_position = []
    thin_position = []
    neps_position = []

    # Create a figure with the screen size
    fig = plt.figure(figsize=(screen_width / 100, screen_height / 100), dpi=100)
    count_warp = 0
    count_weft = 0
    

    for i in range(0, 1000*pp_mm):
        
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
                    plt.plot([i/pp_mm, i/pp_mm], [fault_position, fault_position + 24], color='red', linewidth=yarn_dia*fault_width)
                elif fault_arr_thin[i] > 0:
                    count += 1
                    fault_width = max(yarn_dia, 1 - get_random_value(0, 50) / 100)  # Ensure the width isn't negative

                    fault_position = get_random_value() * 1000
                    thin_position.append({
                        "x": i,
                        "y": fault_position
                    })
                    plt.plot([i/pp_mm, i/pp_mm], [fault_position, fault_position + 24], color='blue', linewidth=yarn_dia*fault_width)
                elif fault_arr_neps[i] > 0:
                    count += 1
                    fault_width = int(1 + get_random_value(50, 500) / 200)
                    fault_position = get_random_value() * 1000
                    neps_position.append({
                        "x": i,
                        "y": fault_position
                    })
                    circle = plt.Circle((fault_position, i/pp_mm), yarn_dia/2 * fault_width, color='green', fill=True)
                    plt.gca().add_patch(circle) 
                else:
                    count = fault_arr[i]  # Exit the loop if no fault found
        # else:

    for i in range(0, 1000*ep_mm):
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
                    plt.plot([fault_position, fault_position + 24], [i/ep_mm, i/ep_mm], color='red', linewidth=yarn_dia*fault_width)
                elif fault_arr_thin_warp[i] > 0:
                    count += 1
                    fault_width = max(0.5, 1 - get_random_value(0, 50) / 100)
                    fault_position = get_random_value() * 1000
                    thin_position.append({
                        "x": fault_position,
                        "y": i
                    })
                    plt.plot([fault_position, fault_position + 24], [i/ep_mm, i/ep_mm], color='blue', linewidth=yarn_dia*fault_width)
                elif fault_arr_neps_warp[i] > 0:
                    count += 1
                    fault_width = int(1 + get_random_value(50, 500) / 200)
                    fault_position = get_random_value() * 1000
                    neps_position.append({
                        "x": fault_position,
                        "y": i
                    })
                    circle = plt.Circle((i/ep_mm, fault_position), yarn_dia/2 * fault_width, color='green', fill=True) 
                    plt.gca().add_patch(circle) 
                else:
                    count = fault_arr_warp[i]  # Exit the loop if no fault found
        # else:

    for i in range(0, 1000*pp_mm):
        count_weft = count_weft+1
        plt.plot([i/pp_mm, i/pp_mm], [0, 1000], color='yellow', linewidth=yarn_dia)
    for i in range(0, 1000*ep_mm):
       
        count_warp = count_warp+1
        plt.plot([0, 1000], [i/ep_mm, i/ep_mm], color='yellow', linewidth=yarn_dia)

    print(count_warp,count_weft)

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

    plt.xlabel('1 meter - (1000mm)')
    plt.ylabel('1 meter - (1000mm)')

    #hide the axis
    plt.axis('off')

    # Set full screen mode
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()

    # Display the plot
    plt.show()
