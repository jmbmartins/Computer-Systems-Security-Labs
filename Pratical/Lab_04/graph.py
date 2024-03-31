import matplotlib.pyplot as plt
import numpy as np

# Define the range of password lengths
password_lengths = np.arange(1, 11, 1)

# Define the number of possible passwords for each length
# Assuming a character set of 94 printable ASCII characters
num_passwords = 94 ** password_lengths

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(password_lengths, num_passwords)

# Add title and labels
plt.title('Exponential Wall of Brute Force Cracking')
plt.xlabel('Password Length')
plt.ylabel('Number of Possible Passwords')

# Display the plot
plt.show()
