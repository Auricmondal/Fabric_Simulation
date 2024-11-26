import numpy as np

def get_fault_location_list(total_length_yarn_weft, total_length_yarn_warp):
    fault_arr_thick = np.random.poisson(0.0034, total_length_yarn_weft)
    fault_arr_thin = np.random.poisson(0.0034, total_length_yarn_weft)
    fault_arr_neps = np.random.poisson(0.00034, total_length_yarn_weft)
    fault_arr = fault_arr_thick + fault_arr_thin + fault_arr_neps
    fault_arr_thick_warp = np.random.poisson(0.0034, total_length_yarn_warp)
    fault_arr_thin_warp = np.random.poisson(0.0034, total_length_yarn_warp)
    fault_arr_neps_warp = np.random.poisson(0.0034, total_length_yarn_warp)
    fault_arr_warp = fault_arr_thick_warp + fault_arr_thin_warp + fault_arr_neps_warp

    return {
        "thick": fault_arr_thick,
        "thin": fault_arr_thin,
        "neps": fault_arr_neps,
        "thick_warp": fault_arr_thick_warp,
        "thin_warp": fault_arr_thin_warp,
        "neps_warp": fault_arr_neps_warp,
        "total_weft": fault_arr,
        "total_warp": fault_arr_warp
    }