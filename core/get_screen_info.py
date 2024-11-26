import ctypes

def set_dpi_awareness():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Windows 8.1 or later
    except Exception as e:
        try:
            ctypes.windll.user32.SetProcessDPIAware()  # Windows Vista or 7
        except Exception as e:
            pass



def get_screen_resolution():
    set_dpi_awareness()
    dpi_x = ctypes.c_uint()
    dpi_y = ctypes.c_uint()
    monitor = ctypes.windll.user32.MonitorFromWindow(0, 1)  # Get the primary monitor
    ctypes.windll.shcore.GetDpiForMonitor(monitor, 0, ctypes.byref(dpi_x), ctypes.byref(dpi_y))
    return  dpi_x.value, dpi_y.value