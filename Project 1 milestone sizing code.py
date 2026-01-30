import numpy as np

### we need gross takeoff, empty and feul weight

#start with crew/pax, payload weight (given):
crew_mem = 410
mem_weight = 200 #lbs

w_crew = crew_mem * mem_weight #lbs

num_ppl = 400 #do crew bags count?

w_baggage = 30 * num_ppl  #lbs

#next split up mission into phases, focus on cruis/loiter. other phases have tables with feul fractions

cruise_range = 3500 + 200 #nm 
loiter_endurnace = 0.5 #hrs
reserve_per = 5 #%

#values from table in notes
#cruise
LD_c = 14
cj_c = 0.7

#assuming cruisng altitude of 35000 ft, mach 0.8, typical of this class of jets
M_c = 0.8
T_c = -65.61 + 459.67 #R
a_c = np.sqrt(1.4*1716*T_c)
V_c = M_c*a_c/6076.12*3600 #nm/hr
#loiter
LD_l = 16
cj_l = 0.5
#from range eq in notes, using jet eq, accounts for unit conversions
FF_cruise = np.exp(-cruise_range*cj_c/V_c/LD_c)
#from endurance eq in notes, using jet eq, accounts for unit conversions
FF_loiter = np.exp(-loiter_endurnace*cj_l/LD_l)
#non-cruise/loiter feul fractions are from table in notes, using transport jet
w_endW0 = 0.99*0.99*0.995*0.98*FF_cruise*FF_loiter*.99*.992



#5% feul reserves + trapped oil is negligible
WfW0 = (1 - w_endW0) * (1+reserve_per/100)

#this function gives the empty wieght fraction based on the function from roskam (basing off military patrol props)
def empty_weight(W_0):
    
    #A, B for regression line from transport jets
    A, B = 0.0833, 1.0383

    W_e = 10**((np.log10(W_0)-A)/B)
    WeW0 = W_e/W_0

    WeW0 = 1.02*W_0**-0.06

    return WeW0

#first guess for W_0
W_0_guess = 70000 #lbs
err = 1
#loop to find W_0
while err > 1e-3 or W_0 < 0:

    WeW0 = empty_weight(W_0_guess)
    
    W_0 = (w_crew + w_baggage)/(1-WfW0-WeW0)
    err = abs(W_0 - W_0_guess)
    W_0_guess = W_0

#getting empty weight from the estimated takeoff weight
W_e = WeW0 * W_0
W_f = WfW0 * W_0


print("Estimated Values:")
print(f"Gross Takeoff Weight W_0 = {W_0:.2f} lbs")
print(f"Empty Weight W_E = {W_e:.2f} lbs")
print(f"Feul Weight W_F = {W_f:.2f} lbs")