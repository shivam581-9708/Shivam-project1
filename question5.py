def calculate_total_trek_length(A, B, C):
    total_length = 3 * B + A + 2 * C
    return total_length
A = int(input("Enter the distance Amit beats Suman by (in meters)\n "))
B = int(input("Enter the distance Amit beats Ravi by (in meters)\n"))
C = int(input("Enter the distance Suman beats Ravi by (in meters)\n"))

total_length = calculate_total_trek_length(A, B, C)
print("Total length of the trek\n", total_length, "m")
