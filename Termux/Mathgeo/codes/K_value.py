import sys 
sys.path.insert(0, '/home/faraz090906/Python/matgeo/codes/CoordGeo')
from sympy import symbols, Eq, solve

# Define the variable
k = symbols('k')

# Define the equation
equation = Eq(3*k - 6, 0)

# Solve the equation
solution = solve(equation, k)

# Write the result to a file
with open('solution.txt', 'w') as f:
    f.write(str(solution[0]))

print(f"The solution for the equation 3k - 6 = 0 is k = {solution[0]}")

