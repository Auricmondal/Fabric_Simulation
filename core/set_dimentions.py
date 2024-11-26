#Sets the dimentions of the canvas
from core.get_screen_info import get_screen_resolution



def set_dimentions(required_width_mm,required_height_mm):
    dpi_x,dpi_y = get_screen_resolution()
    width= dpi_x*required_width_mm//25.4
    height= dpi_y*required_height_mm// 25.4

    return width,height
    
