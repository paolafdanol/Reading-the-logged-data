#--------------------------------------------
# Read and Display the Logged Data
#============================================
# This porgram open the file where the
# temperature data was saved and displays its
# contents on PC Screen
#--------------------------------------------

file = open("Temp.txt", "r") # Open the file
for i in range(3): # Read 3 lines
    print(file.readline()) # Display the data
    
file.close()    # Close the file