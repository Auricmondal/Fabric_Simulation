import ctypes

def dpiawareness():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except:
        ctypes.windll.user32.SetProcessDPIAware()

def get_screen_resolution():
    dpiawareness()
    dpi = ctypes.c_uint()
    monitor = ctypes.windll.user32.MonitorFromWindow(0, 1)  # Get the primary monitor
    ctypes.windll.shcore.GetDpiForMonitor(monitor, 0, ctypes.byref(dpi), ctypes.byref(dpi))
    print(dpi.value)
    return  dpi.value