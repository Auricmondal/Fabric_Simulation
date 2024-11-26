import matplotlib.patheffects as path_effects


def create_matrix(per_mm_yarn):
    matrix =[]
    for i in range(0, 1000*per_mm_yarn):
       matrix.append( i*1/per_mm_yarn)
    return matrix
    


# # create a matrix that contains points of regular fabric cell corners considering the faults are all up
# matrix_warp = [i*1/ep_mm] in range 1 to 1000*ep_mm
# matrix_weft = [i*1/pp_mm] in range 1 to 1000*pp_mm

# Now we can use that to create the fabric
# i ===row
# j ===column
# if i is even then up else down
# in case of down draw from prev up to next point - yarn dia /2 leave a space of yarn dia then follow the same

def create_fabric(plt,fig,warp_matrix, weft_matrix, ep_mm, pp_mm,yarn_dia_warp, yarn_dia_weft):
    
    # Warp 
    i=0
    
    for j in range(1, 1000*ep_mm,2):
        if j==1000*ep_mm-1:
            line1,= plt.plot([i,i],[warp_matrix[j-1],warp_matrix[j]-yarn_dia_warp/2], color='yellow', linewidth=yarn_dia_warp)
            shadow_effect = path_effects.withStroke(linewidth=yarn_dia_warp, foreground='gray')
            line1.set_path_effects([shadow_effect])
            break
        
        line1,=plt.plot([i,i],[warp_matrix[j-1],warp_matrix[j]-yarn_dia_warp/2], color='yellow', linewidth=yarn_dia_warp)
        line2,=plt.plot([i,i],[warp_matrix[j]+yarn_dia_warp/2,warp_matrix[j+1]], color='yellow', linewidth=yarn_dia_warp)
        shadow_effect = path_effects.withStroke(linewidth=yarn_dia_warp, foreground='black')
        line1.set_path_effects([shadow_effect])
        line2.set_path_effects([shadow_effect])
    i= i+1/ep_mm

    while i<1000*ep_mm:
        line_property ={
            "color": "yellow",
            "linewidth": yarn_dia_warp
        }
        fig.get_lin
    
    print("Warp done")

    # # Weft
    # i=0
    # while i<5*pp_mm:
    #     for j in range(1, 5*pp_mm,2):
    #         if j==5*pp_mm-1:
    #             line1,=plt.plot([weft_matrix[j-1],weft_matrix[j]-yarn_dia_weft/2],[i,i], color='yellow', linewidth=yarn_dia_weft)
    #             shadow_effect = path_effects.withStroke(linewidth=yarn_dia_warp, foreground='gray')
    #             line1.set_path_effects([shadow_effect])
    #             break

    #         line1,=plt.plot([weft_matrix[j-1],weft_matrix[j]-yarn_dia_weft/2],[i,i], color='yellow', linewidth=yarn_dia_weft)
    #         line2,=plt.plot([weft_matrix[j]+yarn_dia_weft/2,weft_matrix[j+1]],[i,i], color='yellow', linewidth=yarn_dia_weft)
    #         shadow_effect = path_effects.withStroke(linewidth=yarn_dia_warp, foreground='gray')
    #         line1.set_path_effects([shadow_effect])
    #         line2.set_path_effects([shadow_effect])
    #     i= i+1/pp_mm