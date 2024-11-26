

def get_total_yarn_length(per_inch_count_mm):
    #total yarn length in mm = lenght of warp or weft * EPMM or PPMM * length of weft or warp
    # as if there are EPMM yarns in 1 mm then there will be 1000 * EPMM yarns in 1m
    # and as we need a fabric of dimension 1 m x 1 m so we each yarn needs to be 1000 mm long
    # so total yarn length = 1000 * 1000 * EPMM or PPMM

    total_yarn_length = int(1000 * 1000 * per_inch_count_mm)

    return total_yarn_length