"Shadows calculation"
"---------------------parameter definition--------------------"
latitude=41.38 #in degrees
height_panel=1.134 #in meters
inclination_grads=10
total_surface=62
total_surface_wslope= 152 #total surface with the slope of the roof
installed_surface=0.95*total_surface_wslope
width_panel=2.279 #meters
panel_output=0.36 #kW

"---------------------calculations: recommended distance between panels--------------------"
inclination_rad=inclination_grads*2*math.pi/360
height=height_panel*math.sin(inclination_rad)
min_distance=height/(math.tan(((61-latitude)*2*math.pi)/365))
D_recommended=min_distance*1.05


"Calculation: FLAT SURFACE (WITHOUT THE SLOPE OF THE ROOF) "

min_shadow=math.cos(inclination_rad)*height_panel
max_shadow=min_shadow+D_recommended
max_width=width_panel*1.04 #with 4% safety distance
matrix_area=max_shadow*max_width

"Number of matrices"
number_total_matrices=total_surface/matrix_area
round_matrices=round(number_total_matrices)
installed_power=round_matrices*panel_output
installed_power


"Calculation: FLAT SURFACE (INSTALL DIRECTLY WITH THE SLOPE OF THE ROOF)"

max_shadow_wslope=math.cos(0)*width_panel+0.09 #with 9cm safety distance 
#why width instead of height here? (different from previous calc)

max_height_wslope=height_panel+0.1 #with 10cm safety distance
matrix_area_wslope=max_height_wslope*max_shadow_wslope

#Number of matrices with slope
number_total_matrices_wslope=total_surface_wslope/matrix_area_wslope
round_matrices_wslope=math.trunc(number_total_matrices_wslope) 
installable_power_wslope=round_matrices_wslope*panel_output
