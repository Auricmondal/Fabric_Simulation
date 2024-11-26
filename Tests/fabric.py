# Generate a fabric of 1m x 1m with the least count in x-asis as 1mm and in y-axis as 0.1mm

from core.set_dimentions import set_dimentions
from fabric import yarn_info, yarn
from canvas import draw_canvas,show_fabric


from tqdm import tqdm


if __name__ == "__main__":

    print("Generating a fabric of 1m x 1m ")
    print("Enter Fabric Details")
    yarn_dia = yarn_info.input_yarn_dia_info()
    ep_mm = int(input("Enter EPI: "))/25.4
    pp_mm= int(input("Enter PPI: "))/25.4
    fabric_width_mm = int(input("Enter Fabric Width in meter: "))*1000
    fabric_height_mm = int(input("Enter Fabric Height int meter: "))*1000

    print(fabric_height_mm)

    weft_yarn_count = int(fabric_height_mm*pp_mm)
    warp_yarn_count = int(fabric_width_mm*ep_mm)

    canvas_width,canvas_height = set_dimentions(fabric_width_mm,fabric_height_mm)
    canvas_height = int(canvas_height)
    canvas_width = int(canvas_width)
    draw_canvas.draw_canvas(canvas_width,canvas_height)

    consecutive_yarn_gap_warp = int(fabric_width_mm - warp_yarn_count*yarn_dia)
    consecutive_yarn_gap_weft = canvas_width - weft_yarn_count*yarn_dia 

    print(warp_yarn_count,weft_yarn_count)


    for _ in tqdm(range(100), desc="Drawing fabric", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
        for i in range(0,warp_yarn_count):
            image = yarn.draw_yarn(i/warp_yarn_count*canvas_height ,yarn_dia, 'warp')
        for i in range(0,weft_yarn_count):
            image = yarn.draw_yarn(i/weft_yarn_count*canvas_height ,yarn_dia, 'weft')

    
    
    show_fabric.show()