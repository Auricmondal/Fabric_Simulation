import math

def input_info(message):
    print(message)
    return input()



def get_fabric_info():
    print("Enter the Following to proceed with fabric informations")
    count = input_info("Enter count in Ne of the yarn used")
    staple_length = input_info("Enter the staple length of the yarn used")
    ep_cm = input_info("Enter the ends per cm of the fabric")
    pp_cm = input_info("Enter the picks per cm of the fabric")
    thick_places =input_info("Enter the thick places details")
    thin_places = input_info("Enter the thin places details")
    neps = input_info("Enter the neps details")
    length_of_neps = input_info("Enter the length of neps")
    print("Information Entered Successfully")
    return {
        "count": count,
        "staple_length": staple_length,
        "ep_cm": ep_cm,
        "pp_cm": pp_cm,
        "thick_places": thick_places,
        "thin_places": thin_places,
        "neps": neps,
        "length_of_neps": length_of_neps
    }


def get_unit_warp_weft_length(ep_cm, pp_cm):
    warp_length = 1 / ep_cm
    weft_length = 1 / pp_cm
    return {
        "warp_length": warp_length,
        "weft_length": weft_length
    }


def get_warp_weft_count_per_meter(ep_cm, pp_cm):
    warp_count = ep_cm*100
    weft_count = pp_cm*100
    total_length_warp_1m_1m = warp_count*100
    total_length_weft_1m_1m = weft_count*100 
    total_discrete_warp = total_length_warp_1m_1m*pp_cm
    return {
        "warp_count": warp_count,
        "weft_count": weft_count,
        "total_length_warp_1m_1m": total_length_warp_1m_1m,
        "total_length_weft_1m_1m": total_length_weft_1m_1m,
        "total_discrete_warp": total_discrete_warp
    }


def get_total_thick_len_1km_warp(staple_length, thick_places,pp_cm):
    total_thick_len_1km_warp = staple_length*thick_places*pp_cm
    total_thick_len_1cm_warp = total_thick_len_1km_warp/math.pow(10,5)
    return{
        "total_thick_len_1km_warp": total_thick_len_1km_warp,
        "total_thick_len_1cm_warp": total_thick_len_1cm_warp
    }


def get_total_thick_len_1km_weft(staple_length, thick_places,ep_cm):
    total_thick_len_1km_weft = staple_length*thick_places*ep_cm
    total_thick_len_1cm_weft = total_thick_len_1km_weft/math.pow(10,5)
    return{
        "total_thick_len_1km_weft": total_thick_len_1km_weft,
        "total_thick_len_1cm_weft": total_thick_len_1cm_weft
    }

def get_total_thin_len_1km_warp(staple_length, thin_places,pp_cm):
    total_thin_len_1km_warp = staple_length*thin_places*pp_cm
    total_thin_len_1cm_warp = total_thin_len_1km_warp/math.pow(10,5)
    return{
        "total_thin_len_1km_warp": total_thin_len_1km_warp,
        "total_thin_len_1cm_warp": total_thin_len_1cm_warp
    }

def get_total_thin_len_1km_weft(staple_length, thin_places,ep_cm):
    total_thin_len_1km_weft = staple_length*thin_places*ep_cm
    total_thin_len_1cm_weft = total_thin_len_1km_weft/math.pow(10,5)
    return{
        "total_thin_len_1km_weft": total_thin_len_1km_weft,
        "total_thin_len_1cm_weft": total_thin_len_1cm_weft
    }

def get_total_neps_len_1km_warp(length_of_neps, neps,pp_cm):
    total_neps_len_1km_warp = length_of_neps*neps*pp_cm
    total_neps_len_1cm_warp = total_neps_len_1km_warp/math.pow(10,5)
    return{
        "total_neps_len_1km_warp": total_neps_len_1km_warp,
        "total_neps_len_1cm_warp": total_neps_len_1cm_warp
    }

def get_total_neps_len_1km_weft(length_of_neps, neps,ep_cm):
    total_neps_len_1km_weft = length_of_neps*neps*ep_cm
    total_neps_len_1cm_weft = total_neps_len_1km_weft/math.pow(10,5)
    return{
        "total_neps_len_1km_weft": total_neps_len_1km_weft,
        "total_neps_len_1cm_weft": total_neps_len_1cm_weft
    }

def get_total_thick_discrete_warp_unit_1m_1m(staple_length, thick_places, pp_cm,ep_cm):
    total_thick_discrete_warp_unit_1m_1m = staple_length*thick_places*pp_cm*ep_cm /10
    return {
        "total_thick_discrete_warp_unit_1m_1m": total_thick_discrete_warp_unit_1m_1m
    }

def get_total_thick_discrete_weft_unit_1m_1m(staple_length, thick_places, pp_cm,ep_cm):
    total_thick_discrete_weft_unit_1m_1m = staple_length*thick_places*pp_cm*ep_cm /10
    return {
        "total_thick_discrete_weft_unit_1m_1m": total_thick_discrete_weft_unit_1m_1m
    }

def get_total_thin_discrete_warp_unit_1m_1m(staple_length, thin_places, pp_cm,ep_cm):
    total_thin_discrete_warp_unit_1m_1m = staple_length*thin_places*pp_cm*ep_cm /10
    return {
        "total_thin_discrete_warp_unit_1m_1m": total_thin_discrete_warp_unit_1m_1m
    }

def get_total_thin_discrete_weft_unit_1m_1m(staple_length, thin_places, pp_cm,ep_cm):
    total_thin_discrete_weft_unit_1m_1m = staple_length*thin_places*pp_cm*ep_cm /10
    return {
        "total_thin_discrete_weft_unit_1m_1m": total_thin_discrete_weft_unit_1m_1m
    }

def get_total_neps_discrete_warp_unit_1m_1m(staple_length, neps, pp_cm,ep_cm):
    total_neps_discrete_warp_unit_1m_1m = staple_length*neps*pp_cm*ep_cm /10
    return {
        "total_neps_discrete_warp_unit_1m_1m": total_neps_discrete_warp_unit_1m_1m
    }

def get_total_neps_discrete_weft_unit_1m_1m(staple_length, neps, pp_cm,ep_cm):
    total_neps_discrete_weft_unit_1m_1m = staple_length*neps*pp_cm*ep_cm /10
    return {
        "total_neps_discrete_weft_unit_1m_1m": total_neps_discrete_weft_unit_1m_1m
    }

def probability_of_thick_warp_1m_1m(total_thick_discrete_warp_unit_1m_1m,ep_cm,pp_cm):
    probability_of_thick_warp = total_thick_discrete_warp_unit_1m_1m/(ep_cm*pp_cm)
    return {
        "probability_of_thick_warp": probability_of_thick_warp
    }

def probability_of_thick_weft_1m_1m(total_thick_discrete_weft_unit_1m_1m,ep_cm,pp_cm):
    probability_of_thick_weft = total_thick_discrete_weft_unit_1m_1m/(ep_cm*pp_cm)
    return {
        "probability_of_thick_weft": probability_of_thick_weft
    }


def probability_of_thin_warp_1m_1m(total_thin_discrete_warp_unit_1m_1m,ep_cm,pp_cm):
    probability_of_thin_warp = total_thin_discrete_warp_unit_1m_1m/(ep_cm*pp_cm)
    return {
        "probability_of_thin_warp": probability_of_thin_warp
    }

def probability_of_thin_weft_1m_1m(total_thin_discrete_weft_unit_1m_1m,ep_cm,pp_cm):
    probability_of_thin_weft = total_thin_discrete_weft_unit_1m_1m/(ep_cm*pp_cm)
    return {
        "probability_of_thin_weft": probability_of_thin_weft
    }

def probability_of_neps_warp_1m_1m(total_neps_discrete_warp_unit_1m_1m,ep_cm,pp_cm):
    probability_of_neps_warp = total_neps_discrete_warp_unit_1m_1m/(ep_cm*pp_cm)
    return {
        "probability_of_neps_warp": probability_of_neps_warp
    }

def probability_of_neps_weft_1m_1m(total_neps_discrete_weft_unit_1m_1m,ep_cm,pp_cm):
    probability_of_neps_weft = total_neps_discrete_weft_unit_1m_1m/(ep_cm*pp_cm)
    return {
        "probability_of_neps_weft": probability_of_neps_weft
    }

def get_norm_places_count_warp (staple_length, thick_places, thin_places, neps, length_of_neps,pp_cm,ep_cm):
    norm_places_count = math.pow(10,5)-(staple_length*thick_places + staple_length*thin_places + staple_length*neps*length_of_neps)
    discrete_reg_warp_count = norm_places_count*pp_cm
    total_discrete_reg_warp_count = discrete_reg_warp_count*ep_cm/10
    return {
        "norm_places_count": norm_places_count,
        "discrete_reg_warp_count": discrete_reg_warp_count,
        "total_discrete_reg_warp_count": total_discrete_reg_warp_count
    }

def get_norm_places_count_weft (staple_length, thick_places, thin_places, neps, length_of_neps,pp_cm,ep_cm):
    norm_places_count = math.pow(10,5)-(staple_length*thick_places + staple_length*thin_places + staple_length*neps*length_of_neps)
    discrete_reg_weft_count = norm_places_count*ep_cm
    total_discrete_reg_weft_count = discrete_reg_weft_count*pp_cm/10
    return {
        "norm_places_count": norm_places_count,
        "discrete_reg_weft_count": discrete_reg_weft_count,
        "total_discrete_reg_weft_count": total_discrete_reg_weft_count
    }


def probability_reg_plac_1m_1m_warp(total_discrete_reg_warp_count,ep_cm,pp_cm):
    probability_reg_plac = total_discrete_reg_warp_count/(ep_cm*pp_cm*100*100)
    return {
        "probability_reg_plac": probability_reg_plac
    }

def probability_reg_plac_1m_1m_weft(total_discrete_reg_weft_count,ep_cm,pp_cm):
    probability_reg_plac = total_discrete_reg_weft_count/(ep_cm*pp_cm*100*100)
    return {
        "probability_reg_plac": probability_reg_plac
    }


def dia_yarn_places(count):
    dia_yarn = 2.54/28*math.sqrt(count)
    dia_yarn_thick = dia_yarn+ 0.50*dia_yarn
    dia_yarn_thin = dia_yarn - 0.50*dia_yarn
    dia_yarn_neps = dia_yarn + 2*dia_yarn
    return {
        "dia_yarn": dia_yarn,
        "dia_yarn_thick": dia_yarn_thick,
        "dia_yarn_thin": dia_yarn_thin,
        "dia_yarn_neps": dia_yarn_neps
    }


def total_unit_cell_count_1m_1m(ep_cm, pp_cm):
    total_unit_cell_count = math.pow(ep_cm*pp_cm*math.pow(10,4),2)
    return {
        "total_unit_cell_count": total_unit_cell_count
    }


if __name__ =="__main__":

    fabric_info = get_fabric_info()
    ep_cm = float(fabric_info["ep_cm"])
    pp_cm = float(fabric_info["pp_cm"])
    count = float(fabric_info["count"])
    staple_length = float(fabric_info["staple_length"])
    thick_places = float(fabric_info["thick_places"])
    thin_places = float(fabric_info["thin_places"])
    neps = float(fabric_info["neps"])
    length_of_neps = float(fabric_info["length_of_neps"])

    unit_warp_weft_length = get_unit_warp_weft_length(ep_cm, pp_cm)
    warp_length = unit_warp_weft_length["warp_length"]
    weft_length = unit_warp_weft_length["weft_length"]

    warp_weft_count_per_meter = get_warp_weft_count_per_meter(ep_cm, pp_cm)
    warp_count = warp_weft_count_per_meter["warp_count"]
    weft_count = warp_weft_count_per_meter["weft_count"]
    total_length_warp_1m_1m = warp_weft_count_per_meter["total_length_warp_1m_1m"]
    total_length_weft_1m_1m = warp_weft_count_per_meter["total_length_weft_1m_1m"]
    total_discrete_warp = warp_weft_count_per_meter["total_discrete_warp"]

    total_thick_len_1km_warp = get_total_thick_len_1km_warp(staple_length, thick_places,pp_cm)
    total_thick_len_1km_weft = get_total_thick_len_1km_weft(staple_length, thick_places,ep_cm)
    total_thin_len_1km_warp = get_total_thin_len_1km_warp(staple_length, thin_places,pp_cm)
    total_thin_len_1km_weft = get_total_thin_len_1km_weft(staple_length, thin_places,ep_cm)
    total_neps_len_1km_warp = get_total_neps_len_1km_warp(length_of_neps, neps,pp_cm)
    total_neps_len_1km_weft = get_total_neps_len_1km_weft(length_of_neps, neps,ep_cm)

    total_thick_discrete_warp_unit_1m_1m = get_total_thick_discrete_warp_unit_1m_1m(staple_length, thick_places, pp_cm,ep_cm)
    total_thick_discrete_weft_unit_1m_1m = get_total_thick_discrete_weft_unit_1m_1m(staple_length, thick_places, pp_cm,ep_cm)
    total_thin_discrete_warp_unit_1m_1m = get_total_thin_discrete_warp_unit_1m_1m(staple_length, thin_places, pp_cm,ep_cm)
    total_thin_discrete_weft_unit_1m_1m = get_total_thin_discrete_weft_unit_1m_1m(staple_length, thin_places, pp_cm,ep_cm)
    total_neps_discrete_warp_unit_1m_1m = get_total_neps_discrete_warp_unit_1m_1m(staple_length, neps, pp_cm,ep_cm)
    total_neps_discrete_weft_unit_1m_1m = get_total_neps_discrete_weft_unit_1m_1m(staple_length, neps, pp_cm,ep_cm)


    probability_of_thick_warp = probability_of_thick_warp_1m_1m(total_thick_discrete_warp_unit_1m_1m,ep_cm,pp_cm)
    probability_of_thick_weft = probability_of_thick_weft_1m_1m(total_thick_discrete_weft_unit_1m_1m,ep_cm,pp_cm)
    probability_of_thin_warp = probability_of_thin_warp_1m_1m(total_thin_discrete_warp_unit_1m_1m,ep_cm,pp_cm)
    probability_of_thin_weft = probability_of_thin_weft_1m_1m(total_thin_discrete_weft_unit_1m_1m,ep_cm,pp_cm)
    probability_of_neps_warp = probability_of_neps_warp_1m_1m(total_neps_discrete_warp_unit_1m_1m,ep_cm,pp_cm)
    probability_of_neps_weft = probability_of_neps_weft_1m_1m(total_neps_discrete_weft_unit_1m_1m,ep_cm,pp_cm)

    norm_places_count_warp = get_norm_places_count_warp(staple_length, thick_places, thin_places, neps, length_of_neps,pp_cm,ep_cm)
    norm_places_count_weft = get_norm_places_count_weft(staple_length, thick_places, thin_places, neps, length_of_neps,pp_cm,ep_cm)

    probability_reg_plac_1m_1m_warp = probability_reg_plac_1m_1m_warp(norm_places_count_warp["total_discrete_reg_warp_count"],ep_cm,pp_cm)
    probability_reg_plac_1m_1m_weft = probability_reg_plac_1m_1m_weft(norm_places_count_weft["total_discrete_reg_weft_count"],ep_cm,pp_cm)

    dia_yarn_places = dia_yarn_places(count)
    total_unit_cell_count_1m_1m = total_unit_cell_count_1m_1m(ep_cm, pp_cm)

    print("Fabric Information")
    print(f"Count: {count}")
    print(f"Staple Length: {staple_length}")
    print(f"Ends per cm: {ep_cm}")
    print(f"Picks per cm: {pp_cm}")
    print(f"Thick Places: {thick_places}")
    print(f"Thin Places: {thin_places}")
    print(f"Neps: {neps}")
    print(f"Length of Neps: {length_of_neps}")
    print("Unit Warp and Weft Length")
    print(f"Warp Length: {warp_length}")
    print(f"Weft Length: {weft_length}")
    print("Warp and Weft Count per Meter")
    print(f"Warp Count: {warp_count}")
    print(f"Weft Count: {weft_count}")
    print(f"Total Length Warp 1m 1m: {total_length_warp_1m_1m}")
    print(f"Total Length Weft 1m 1m: {total_length_weft_1m_1m}")
    print(f"Total Discrete Warp: {total_discrete_warp}")
    print("Total Thick Length 1km Warp")
    print(f"Total Thick Length 1km Warp: {total_thick_len_1km_warp['total_thick_len_1km_warp']}")
    print(f"Total Thick Length 1cm Warp: {total_thick_len_1km_warp['total_thick_len_1cm_warp']}")
    print("Total Thick Length 1km Weft")
    print(f"Total Thick Length 1km Weft: {total_thick_len_1km_weft['total_thick_len_1km_weft']}")
    print(f"Total Thick Length 1cm Weft: {total_thick_len_1km_weft['total_thick_len_1cm_weft']}")
    print("Total Thin Length 1km Warp")
    print(f"Total Thin Length 1km Warp: {total_thin_len_1km_warp['total_thin_len_1km_warp']}")

    print(f"Total Thin Length 1cm Warp: {total_thin_len_1km_warp['total_thin_len_1cm_warp']}")
    print("Total Thin Length 1km Weft")
    print(f"Total Thin Length 1km Weft: {total_thin_len_1km_weft['total_thin_len_1km_weft']}")
    print(f"Total Thin Length 1cm Weft: {total_thin_len_1km_weft['total_thin_len_1cm_weft']}")
    print("Total Neps Length 1km Warp")
    print(f"Total Neps Length 1km Warp: {total_neps_len_1km_warp['total_neps_len_1km_warp']}")
    print(f"Total Neps Length 1cm Warp: {total_neps_len_1km_warp['total_neps_len_1cm_warp']}")
    print("Total Neps Length 1km Weft")
    print(f"Total Neps Length 1km Weft: {total_neps_len_1km_weft['total_neps_len_1km_weft']}")
    print(f"Total Neps Length 1cm Weft: {total_neps_len_1km_weft['total_neps_len_1cm_weft']}")
    print("Total Thick Discrete Warp Unit 1m 1m")
    print(f"Total Thick Discrete Warp Unit 1m 1m: {total_thick_discrete_warp_unit_1m_1m['total_thick_discrete_warp_unit_1m_1m']}")
    print("Total Thick Discrete Weft Unit 1m 1m")
    print(f"Total Thick Discrete Weft Unit 1m 1m: {total_thick_discrete_weft_unit_1m_1m['total_thick_discrete_weft_unit_1m_1m']}")
    print("Total Thin Discrete Warp Unit 1m 1m")
    print(f"Total Thin Discrete Warp Unit 1m 1m: {total_thin_discrete_warp_unit_1m_1m['total_thin_discrete_warp_unit_1m_1m']}")
    print("Total Thin Discrete Weft Unit 1m 1m")
    print(f"Total Thin Discrete Weft Unit 1m 1m: {total_thin_discrete_weft_unit_1m_1m['total_thin_discrete_weft_unit_1m_1m']}")
    print("Total Neps Discrete Warp Unit 1m 1m")
    print(f"Total Neps Discrete Warp Unit 1m 1m: {total_neps_discrete_warp_unit_1m_1m['total_neps_discrete_warp_unit_1m_1m']}")
    print(" Total Neps Discrete Weft Unit 1m 1m")
    print(f"Total Neps Discrete Weft Unit 1m 1m: {total_neps_discrete_weft_unit_1m_1m['total_neps_discrete_weft_unit_1m_1m']}")
    print("Probability of Thick Warp")
    print(f"Probability of Thick Warp: {probability_of_thick_warp['probability_of_thick_warp']}")
    print("Probability of Thick Weft")
    print(f"Probability of Thick Weft: {probability_of_thick_weft['probability_of_thick_weft']}")
    print("Probability of Thin Warp")
    print(f"Probability of Thin Warp: {probability_of_thin_warp['probability_of_thin_warp']}")
    print("Probability of Thin Weft")
    print(f"Probability of Thin Weft: {probability_of_thin_weft['probability_of_thin_weft']}")
    print("Probability of Neps Warp")
    print(f"Probability of Neps Warp: {probability_of_neps_warp['probability_of_neps_warp']}")
    print("Probability of Neps Weft")
    print(f"Probability of Neps Weft: {probability_of_neps_weft['probability_of_neps_weft']}")
    print("Norm Places Count Warp")
    print(f"Norm Places Count Warp: {norm_places_count_warp['norm_places_count']}")
    print(f"Discrete Reg Warp Count: {norm_places_count_warp['discrete_reg_warp_count']}")
    print(f"Total Discrete Reg Warp Count: {norm_places_count_warp['total_discrete_reg_warp_count']}")
    print("Norm Places Count Weft")
    print(f"Norm Places Count Weft: {norm_places_count_weft['norm_places_count']}")
    print(f"Discrete Reg Weft Count: {norm_places_count_weft['discrete_reg_weft_count']}")
    print(f"Total Discrete Reg Weft Count: {norm_places_count_weft['total_discrete_reg_weft_count']}")
    print("Probability Reg Plac 1m 1m Warp")
    print(f"Probability Reg Plac 1m 1m Warp: {probability_reg_plac_1m_1m_warp['probability_reg_plac']}")
    print("Probability Reg Plac 1m 1m Weft")
    print(f"Probability Reg Plac 1m 1m Weft: {probability_reg_plac_1m_1m_weft['probability_reg_plac']}")
    print("Dia Yarn Places")
    print(f"Dia Yarn: {dia_yarn_places['dia_yarn']}")
    print(f"Dia Yarn Thick: {dia_yarn_places['dia_yarn_thick']}")
    print(f"Dia Yarn Thin: {dia_yarn_places['dia_yarn_thin']}")
    print(f"Dia Yarn Neps: {dia_yarn_places['dia_yarn_neps']}")
    print("Total Unit Cell Count 1m 1m")
    print(f"Total Unit Cell Count 1m 1m: {total_unit_cell_count_1m_1m['total_unit_cell_count']}")

    