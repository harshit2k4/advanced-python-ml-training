import random
import math

# Create a simple sample data using ramdom library
random.seed(43)

# Generate random height data (in cm)

heights = [random.randint(150,190) for i in range(20)]
print("Smaple Height in cm is: ", heights)

# Standard Normal Distrbution
# Calculate the mean and standard deviation normally
mean = sum(heights) / len(heights)
variance =  sum ((x - mean) ** 2 for x in heights) / len(heights)
std_dev = math.sqrt(variance)

print("Mean: ", mean)
print("Standard Deviation: ", std_dev)

# calcuate the z score 
z_score = (heights[0] - mean) / std_dev
print("Person 1 height: ", heights[0])
print("Z-score: ", z_score)

# add an oulier in the dataset and detect it
heights.append(1000)
print("Smaple Height in cm is: ", heights)

# Calculate the mean and standard deviation normally
mean = sum(heights) / len(heights)
variance =  sum ((x - mean) ** 2 for x in heights) / len(heights)
std_dev = math.sqrt(variance)

print("Mean: ", mean)
print("Standard Deviation: ", std_dev)

h = heights[-1]
z = (h - mean) / std_dev
print(f"Height: {h}, z-score: {z:.2f}")