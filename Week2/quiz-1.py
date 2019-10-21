#escpae velocity for Earth 2.0
G = 6.67e-11 #gravitational constant (m^3.kg^-1.s^-2)
R_Earth = 6378e+3 #max. radius earth (m)
M_Earth = 5.9722e+24 + 6.0e+20 #max. mass of earth (kg)
r = (1.5-0.22) * R_Earth #worst case radius 
M = (5+2) * M_Earth #worst case mass
v_E = ((2*G*M_Earth)/R_Earth) ** 0.5 #escape velocity of Earth
v_K = ((2*G*M)/r) ** 0.5 #escape velocity of Kepler-452b
print(f"v_E:{v_E}, v_K:{v_K}, ratio:{v_K/v_E}")
