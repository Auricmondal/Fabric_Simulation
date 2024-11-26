
import math

def input_yarn_dia_info(message):
    print("Choose Method Based on the Data You have")
    print("Enter details for ", message)
    print("1. Yarn Diameter \n2. Yarn Count")
    choice = int(input())
    if choice == 1:
        yarn_dia = int(input("Enter Yarn Diameter in mm: "))
        return yarn_dia
    elif choice == 2:
        yarn_count = int(input("Enter Yarn Count: "))
        yarn_dia = 0.9071428571428/math.sqrt(yarn_count)
        return yarn_dia