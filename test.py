from ortools.linear_solver import pywraplp

solver = pywraplp.Solver("Logistics: ", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# x_11 + x_12 + x_13 <= 100
# x_21 + x_22 + x_23 <= 120
# x_11 + x_21 = 80
# x_12 + x_22 = 70
# x-13 + x_23 = 50
# x_ij >= 0
# min: 4x_11+6x_12+9x_13+5x_21+4x_22+7x_23

x_11=solver.IntVar(0, solver.infinity(), "x_11") 
x_12= solver.IntVar(0, solver.infinity(), "x_12")
x_13=solver.IntVar(0, solver.infinity(), "x_13")

x_21= solver.IntVar(0, solver.infinity(), "x_21")
x_22= solver.IntVar(0, solver.infinity(), "x_22")
x_23= solver.IntVar(0, solver.infinity(), "x_23")

solver.Add(x_11 + x_12 + x_13 <= 100)
solver.Add(x_21 + x_22 + x_23 <= 120)
solver.Add(x_11 + x_21 == 80)
solver.Add(x_12 + x_22 == 70)
solver.Add(x_13 + x_23 == 50)

solver.Minimize(4*x_11+6*x_12+9*x_13+5*x_21+4*x_22+7*x_23)

sol = solver.Solve()

print("Cost:", solver.Objective().Value())
print("x_12:", x_11.solution_value())
print("x_13:", x_12.solution_value())
print("x_11:", x_13.solution_value())
print("x_21:", x_21.solution_value())
print("x_22:", x_22.solution_value())
print("x_23:", x_23.solution_value())
