import numpy as np
import matplotlib.pyplot as plt


########### PART A ##############

### we need gross takeoff, empty and feul weight

#start with crew, payload weight (given):
crew_mem = 6
mem_weight = 200 #lbs

w_crew = crew_mem * mem_weight #lbs
w_payload = 6500 #lbs

#next split up mission into phases, focus on cruis/loiter. other phases have tables with feul fractions

cruise_range = 1500 #nm 
loiter_endurnace = 3 #hrs

#values from table in notes
#cruise
LD_c = 15
cp_c = 0.4
np_c = 0.82
#loiter
LD_l = 18
cp_l = 0.5
np_l = 0.77
V_l = 120 #kts
#from range eq in notes, using prop eq, accounts for unit conversions
FF_cruise = np.exp(-cruise_range*1.151/375*cp_c/np_c/LD_c)
#from endurance eq in notes, using prop eq, accounts for unit conversions
FF_loiter = np.exp(-loiter_endurnace/375*cp_l/np_l*V_l/LD_l*1.151)



#non-cruise/loiter feul fractions are from table in notes, 2 cruise phases, so 2 cruise FF
w_endW0 = 0.99*0.99*0.995*0.98*FF_cruise**2*FF_loiter*.99*.992


#no fuel reserves, and assuming trapped oil is negligible
WfW0 = 1 - w_endW0

#this function gives the empty wieght fraction based on the function from roskam (basing off military patrol props)
def empty_weight(W_0):
    
    #A, B for regression line from military patrol turboprops (this fits better IMO: correlates well with E-2, mission profile seems more like military patrol/reconasnece)
    A, B = -0.4179, 1.1446

    #A, B for regression line from twin props
    # A, B = 0.0966, 1.0298

    W_e = 10**((np.log10(W_0)-A)/B)
    WeW0 = W_e/W_0
    return WeW0



#first guess for W_0
W_0_guess = 70000 #lbs
err = 1
#loop to find W_0
while err > 1e-3 or W_0 < 0:

    WeW0 = empty_weight(W_0_guess)
    
    W_0 = (w_crew + w_payload)/(1-WfW0-WeW0)
    err = abs(W_0 - W_0_guess)
    W_0_guess = W_0

#getting empty weight from the estimated takeoff weight
W_e = WeW0 * W_0
W_f = WfW0 * W_0


print("Estimated Values:")
print(f"Gross Takeoff Weight W_0 = {W_0:.2f} lbs")
print(f"Empty Weight W_E = {W_e:.2f} lbs")
print(f"Feul Weight W_F = {W_f:.2f} lbs")


########### PART B ##############

#varying endurace from 1 hr to 5 hrs
endurance = np.linspace(1, 5, 50)


#recalc-ing loicter ff
FF_loiter = np.exp(-endurance/375*cp_l/np_l*V_l/LD_l*1.151)
w_endW0 = 0.99*0.99*0.995*0.98*FF_cruise**2*FF_loiter*.99*.992
WfW0 = 1 - w_endW0


#first guess for W_0
W_0_guess = 70000 #lbs
err = 1
#loop to find W_0
while np.all(err > 1e-3):

    WeW0 = empty_weight(W_0_guess)
    
    W_0 = (w_crew + w_payload)/(1-WfW0-WeW0)
    err = abs(W_0 - W_0_guess)
    W_0_guess = W_0

#calc the average derivative over the graph
dW0dE = (W_0[-1] - W_0[1])/(endurance[-1] - endurance[1])



print(f"\ndW_0/dE = {dW0dE} lbs/hr")


plt.plot(endurance, W_0)
plt.xlabel("Endurance (hrs)")
plt.ylabel("Gross Takeoff weight (lbs)")
plt.title("Endurance vs Gross Takeoff Weight")
plt.show()