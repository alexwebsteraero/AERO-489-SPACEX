import numpy as np
import matplotlib.pyplot as plt

#first, get gross takeoff weights/empty wights for all the planes

########### General Aviation—Single Engine ##############

#Cessna 152, Beech sierra 200, Piper Saratoga
W_e_1 = np.array([1112, 1694, 1935])
W_0_1 = np.array([1670, 2750, 3600])
WeW0_1 = W_e_1/W_0_1
labels_1 = ["Cessna 152", "Beech Sierra 200", "Piper Saratoga"]
#lin reg
# Calculate line of best fit
# coefficients = np.polyfit(W_0_1, WeW0_1, 1)
# polynomial = np.poly1d(coefficients)

# # Create plot points
# x_1 = np.linspace(min(W_0_1), max(W_0_1), 100)
# y_1 = polynomial(x_1)

log_x = np.log(W_0_1)
log_y = np.log(WeW0_1)

# Fit on log-transformed data
coefficients = np.polyfit(log_x, log_y, 1)
b = coefficients[0]  # Power/exponent
a = np.exp(coefficients[1])  # Coefficient

# Create plot points
x_1 = np.linspace(min(W_0_1), max(W_0_1), 100)
y_1 = a * x_1**b

################ General Aviation—Twin Engine ##############

# Piper Seminole PA-44-180, Cessna 340A, Beech King Air C90
W_e_2 = np.array([2354, 3948, 5765])
W_0_2 = np.array([3800, 5990, 9650])
WeW0_2 = W_e_2/W_0_2
labels_2 = ["Piper Seminole PA-44-180", "Cessna 340A", "Beech King Air C90"]
#lin reg
# # Calculate line of best fit
# coefficients = np.polyfit(W_0_2, WeW0_2, 1)
# polynomial = np.poly1d(coefficients)

# # Create plot points
# x_2 = np.linspace(min(W_0_2), max(W_0_2), 100)
# y_2 = polynomial(x_2)

log_x = np.log(W_0_2)
log_y = np.log(WeW0_2)

# Fit on log-transformed data
coefficients = np.polyfit(log_x, log_y, 1)
b = coefficients[0]  # Power/exponent
a = np.exp(coefficients[1])  # Coefficient

# Create plot points
x_2 = np.linspace(min(W_0_2), max(W_0_2), 100)
y_2 = a * x_2**b

############## Jet Transport ##############

# "McDonnell-Douglas DC9-30", "Airbus A300-B4-200", "Boeing 747-200B"
W_e_3 = np.array([57190, 195109, 380000])
W_0_3 = np.array([121000, 363760, 775000])
WeW0_3 = W_e_3/W_0_3
labels_3 = ["McDonnell-Douglas DC9-30", "Airbus A300-B4-200", "Boeing 747-200B"]
#linear regression:
# # Calculate line of best fit
# coefficients = np.polyfit(W_0_3, WeW0_3, 1)
# polynomial = np.poly1d(coefficients)

# # Create plot points
# x_3 = np.linspace(min(W_0_3), max(W_0_3), 100)
# y_3 = polynomial(x_3)

log_x = np.log(W_0_3)
log_y = np.log(WeW0_3)

# Fit on log-transformed data
coefficients = np.polyfit(log_x, log_y, 1)
b = coefficients[0]  # Power/exponent
a = np.exp(coefficients[1])  # Coefficient

# Create plot points
x_3 = np.linspace(min(W_0_3), max(W_0_3), 100)
y_3 = a * x_3**b

############## Military Cargo ##############

# "Lockheed C-130J", "Boeing KC-135A", "McDonnell-Douglas C17"
W_e_4 = np.array([77000, 98466, 259000])
W_0_4 = np.array([175000, 245000, 572000])
WeW0_4 = W_e_4/W_0_4
labels_4 = ["Lockheed C-130J", "Boeing KC-135A", "McDonnell-Douglas C17"]
#lin reg
# # Calculate line of best fit
# coefficients = np.polyfit(W_0_4, WeW0_4, 1)
# polynomial = np.poly1d(coefficients)

# # Create plot points
# x_4 = np.linspace(min(W_0_4), max(W_0_4), 100)
# y_4 = polynomial(x_4)

log_x = np.log(W_0_4)
log_y = np.log(WeW0_4)

# Fit on log-transformed data
coefficients = np.polyfit(log_x, log_y, 1)
b = coefficients[0]  # Power/exponent
a = np.exp(coefficients[1])  # Coefficient

# Create plot points
x_4 = np.linspace(min(W_0_4), max(W_0_4), 100)
y_4 = a * x_4**b

############### High altitude UAV ##############


# "General Atomics MQ-1 Predator", "MQ-9 Reaper", "RQ-4 Global Hawk"
W_e_5 = np.array([1130, 4900, 14950])
W_0_5 = np.array([2250, 10500, 32250])
WeW0_5 = W_e_5/W_0_5
labels_5 = ["General Atomics MQ-1 Predator", "MQ-9 Reaper", "RQ-4 Global Hawk"]
#lin reg
# # Calculate line of best fit
# coefficients = np.polyfit(W_0_5, WeW0_5, 1)
# polynomial = np.poly1d(coefficients)

# # Create plot points
# x_5 = np.linspace(min(W_0_5), max(W_0_5), 100)
# y_5 = polynomial(x_5)

log_x = np.log(W_0_5)
log_y = np.log(WeW0_5)

# Fit on log-transformed data
coefficients = np.polyfit(log_x, log_y, 1)
b = coefficients[0]  # Power/exponent
a = np.exp(coefficients[1])  # Coefficient

# Create plot points
x_5 = np.linspace(min(W_0_5), max(W_0_5), 100)
y_5 = a * x_5**b


# Plotting #

plt.figure(figsize=(12, 8))  # Make the figure larger

plt.plot(W_0_1, WeW0_1, "go", label = "General Aviation—Single Engine")
plt.plot(W_0_2, WeW0_2, "ro", label = "General Aviation—Twin Engine")
plt.plot(W_0_3, WeW0_3, "bo", label = "Jet Transport")
plt.plot(W_0_4, WeW0_4, "ko", label = "Military Cargo")
plt.plot(W_0_5, WeW0_5, "co", label = "High altitude UAV")

plt.plot(x_1, y_1, 'g--')
plt.plot(x_2, y_2, 'r--')
plt.plot(x_3, y_3, 'b--')
plt.plot(x_4, y_4, 'k--')
plt.plot(x_5, y_5, 'c--')

## labeling
W_e = np.concatenate([W_e_1, W_e_2, W_e_3, W_e_4, W_e_5])
W_0 = np.concatenate([W_0_1, W_0_2, W_0_3, W_0_4, W_0_5])
WeW0 = W_e/W_0
labels = np.concatenate([labels_1, labels_2, labels_3, labels_4, labels_5])

for i, label in enumerate(labels):
    plt.annotate(label,
                 (W_0[i], WeW0[i]),
                 textcoords="offset points",
                 xytext=(10, -5),
                 ha='left',
                 fontweight="bold",
                 fontsize=8)  # Smaller font size

plt.xlabel("Gross Takeoff weight (lbs)")
plt.ylabel("Empty Weight Fraction")
plt.title("Gross Takeoff Weight vs Empty Weight Fraction")

# Move legend outside the plot area
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.xscale('log')
plt.margins(x=0.15, y=0.1)  # Add padding to prevent text cutoff
plt.tight_layout()
plt.show()