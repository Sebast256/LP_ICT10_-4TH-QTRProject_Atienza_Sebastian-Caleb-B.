from pyscript import document, display
import numpy as ___

# Suppress matplotlib font logs
import logging
logging.getLogger('________').setLevel(logging.ERROR)

import matplotlib.pyplot as ____

# Preload to avoid font cache message
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# Store data globally
days = []
absences = []

def displaying(e):
day = document.getElementById('______').value
absence = int(document.getElementById('_______').value)

# Save data
days.________(day)
absences.append(absence)

# Convert to NumPy array
converted_absences = __________(absences)

# Clear previous plot
plt.clf()

# Create graph
________(days, converted_absences, marker='o')
plt.title("Weekly Attendance (Absences)")
________("Day")