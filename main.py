#MapPlot.py
#Name:Addy Duering
#Date:4/9/26
#Assignment:Lab 10

import csv
import matplotlib.pyplot as plt

# Read the CSV data
trials = []
reaction_times = []

with open('reaction_time_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        trials.append(int(row[0]))
        reaction_times.append(int(row[1]))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(trials, reaction_times, marker='o', linestyle='-', color='b')
plt.xlabel('Trial Number')
plt.ylabel('Reaction Time (ms)')
plt.title('Reaction Time Data Over Trials')
plt.grid(True)

# Save the plot to a file
plt.savefig('reaction_time_graph.png')
print("Graph saved as 'reaction_time_graph.png'")

# Optionally show the plot (may not work in terminal)
# plt.show()
