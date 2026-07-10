total = 0

file = open(r"C:\Users\User\OneDrive\Documents\thomas jet learn coding\python game developer\FILE HW\numbers.txt", "r")

for line in file:
    total = total + int(line)

file.close()

print("Sum =", total)