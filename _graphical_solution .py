#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#QUESTION 1 ---Maximizing Profit for a Factory
import matplotlib.pyplot as plt
import numpy as np

# Define the constraints
x = np.linspace(0, 10, 400)

# Constraint 1: 2x + 3y <= 12
y1 = (12 - 2 * x) / 3

# Constraint 2: x + 2y <= 8
y2 = (8 - x) / 2

# Non-negativity constraints
y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

# Plot the constraints
plt.plot(x, y1, label=r'$2x + 3y \leq 12$')
plt.plot(x, y2, label=r'$x + 2y \leq 8$')

# Shade the feasible region
plt.fill_between(x, np.minimum(y1, y2), where=(x >= 0), color='grey', alpha=0.5)

# Mark the corner points
corners = np.array([
    [0, 0],
    [6, 0],
    [0, 4],
    [3, 2]
])

plt.scatter(corners[:, 0], corners[:, 1], color='red')

# Annotate the corner points
for i, txt in enumerate(['(0, 0)', '(6, 0)', '(0, 4)', '(3, 2)']):
    plt.annotate(txt, (corners[i, 0], corners[i, 1]), textcoords="offset points", xytext=(0, 10), ha='center')

# Mark the optimal solution
optimal_point = [8, 0]
plt.scatter(*optimal_point, color='blue', zorder=5)
plt.annotate('Optimal Solution (8, 0)', (optimal_point[0], optimal_point[1]), textcoords="offset points", xytext=(0, -15), ha='center')

# Labels and title
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('Feasible Region and Optimal Solution')

# Show the plot
plt.show()


# In[ ]:


#QUESTION 2 ----. Minimizing Cost for a Manufacturer
import numpy as np
import matplotlib.pyplot as plt

# Define the constraints
def labor_constraint(x):
    return (6 - x) / 2  # From x + 2y <= 6

def material_constraint(x):
    return 5 - 2*x  # From 2x + y <= 5

# Generate x values for the graph
x_vals = np.linspace(0, 6, 400)

# Generate y values based on the constraints
y_vals_labor = labor_constraint(x_vals)
y_vals_material = material_constraint(x_vals)

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the constraints as lines
plt.plot(x_vals, y_vals_labor, label=r'$x + 2y \geq 6$', color='b')
plt.plot(x_vals, y_vals_material, label=r'$2x + y \geq 5$', color='g')

# Fill the feasible region (greater than or equal to area)
plt.fill_between(x_vals, np.maximum(y_vals_labor, y_vals_material), where=(y_vals_labor >= 0) & (y_vals_material >= 0), color='gray', alpha=0.3)

# Mark the axes and labels
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xlabel('x (Units of Product X)')
plt.ylabel('y (Units of Product Y)')

# Highlight the feasible region (Non-negativity)
plt.xlim(0, 6)
plt.ylim(0, 6)

# Add the optimal solution x=5
plt.plot(5, 0, 'ro')  # Optimal point at (5, 0)
plt.text(5, 0, '  5', fontsize=12, verticalalignment='bottom')

# Add the corner point (2.5, 0)
plt.plot(2.5, 0, 'bo')  # Corner point at (2.5, 0)
plt.text(2.5, 0, '  (2.5, 0)', fontsize=12, verticalalignment='bottom')

# Add title
plt.title('Most Optimal Solution is x = 5 and Corner Point at (2.5, 0)')

# Add grid
plt.grid(True)

# Display the legend
plt.legend()

# Show the plot
plt.show()


# In[ ]:


#QUESTION 3 --Maximizing Production with Multiple Resources
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the constraints
def labor_constraint(A):
    return (20 - 2 * A)  # 2A + B <= 20 --> B <= 20 - 2A

def material_constraint(A):
    return (30 - 3 * A) / 2  # 3A + 2B <= 30 --> B <= (30 - 3A) / 2

def machine_time_constraint(A):
    return (18 - A) / 2  # A + 2B <= 18 --> B <= (18 - A) / 2

# Step 2: Create an array of A values
A = np.linspace(0, 10, 400)  # A values from 0 to 10 (reasonable range)

# Step 3: Calculate the corresponding B values for each constraint
B_labor = labor_constraint(A)
B_material = material_constraint(A)
B_machine_time = machine_time_constraint(A)

# Step 4: Plot the constraints
plt.figure(figsize=(10, 8))

# Plot each constraint
plt.plot(A, B_labor, label=r'$2A + B \leq 20$ (Labor)')
plt.plot(A, B_material, label=r'$3A + 2B \leq 30$ (Material)')
plt.plot(A, B_machine_time, label=r'$A + 2B \leq 18$ (Machine Time)')

# Step 5: Fill the feasible region
plt.fill_between(A, 0, np.minimum(np.minimum(B_labor, B_material), B_machine_time), where=(A >= 0), color='grey', alpha=0.5)

# Step 6: Plot axis limits and labels
plt.xlim((0, 10))
plt.ylim((0, 15))
plt.xlabel(r'$A$')
plt.ylabel(r'$B$')

# Step 7: Calculate and annotate the intersection points (corner points)
# Calculate the intersection points of the constraints

# Intersection of labor_constraint and material_constraint
def intersection_labor_material():
    # 2A + B = 20 and 3A + 2B = 30
    A = np.linalg.solve([[2, 1], [3, 2]], [20, 30])  # Solve the system of equations
    return A[0], A[1]

# Intersection of labor_constraint and machine_time_constraint
def intersection_labor_machine_time():
    # 2A + B = 20 and A + 2B = 18
    A = np.linalg.solve([[2, 1], [1, 2]], [20, 18])  # Solve the system of equations
    return A[0], A[1]

# Intersection of material_constraint and machine_time_constraint
def intersection_material_machine_time():
    # 3A + 2B = 30 and A + 2B = 18
    A = np.linalg.solve([[3, 2], [1, 2]], [30, 18])  # Solve the system of equations
    return A[0], A[1]

# Get the intersection points
points = [
    (0, 10),  # The intersection with the B-axis
    intersection_labor_material(),  # Intersection of labor and material constraints
    intersection_labor_machine_time(),  # Intersection of labor and machine time constraints
    intersection_material_machine_time(),  # Intersection of material and machine time constraints
    (18, 0)  # The corner point (18, 0) as per your request
]

# Plot the corner points as red dots
for point in points:
    plt.plot(point[0], point[1], 'ro')

# Annotate the corner points
for point in points:
    plt.annotate(f"({point[0]:.2f}, {point[1]:.2f})", (point[0], point[1]), textcoords="offset points", xytext=(0,5), ha='center')

# Step 8: Define the objective function (profit function)
def objective(A, B):
    return 5 * A + 4 * B  # Profit function: P = 5A + 4B

# Step 9: Evaluate the objective function at the optimal point (18, 0)
optimal_A, optimal_B = 18, 0
max_profit = objective(optimal_A, optimal_B)  # Maximum profit at the point (18, 0)

# Step 10: Print the optimal solution (maximum profit and corresponding corner point)
print(f"Optimal solution: Maximum profit is {max_profit} at point ({optimal_A}, {optimal_B})")

# Step 11: Display the plot with the title changed
plt.title(f'Maximum profit is {max_profit} at point ({optimal_A}, {optimal_B})')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:


#QUESTION 4---Maximizing Revenue from Sales
import numpy as np
import matplotlib.pyplot as plt

# Define the constraint equations
def constraint1(A):
    return (20 - A) / 2  # Advertising budget: A + 2B <= 20

def constraint2(A):
    return (15 - A) / 2  # Production capacity: A + 2B <= 15

# Generate values for A
A = np.linspace(0, 15, 200)

# Calculate the B values based on the constraints
B1 = constraint1(A)  # from A + 2B <= 20
B2 = constraint2(A)  # from A + 2B <= 15

# Plot the feasible region
plt.figure(figsize=(10, 6))

# Fill the feasible region where both constraints hold
plt.fill_between(A, 0, np.minimum(B1, B2), where=(B1 >= 0) & (B2 >= 0), color='lightgray', label='Feasible Region')

# Plot the constraints
plt.plot(A, B1, label=r'$A + 2B \leq 20$', color='red')  # Advertising budget constraint
plt.plot(A, B2, label=r'$A + 2B \leq 15$', color='green')  # Production capacity constraint

# Mark the corner points
corner_points = [(0, 0), (0, 7.5), (10, 5), (15, 0)]

# Plot the corner points
for point in corner_points:
    plt.scatter(*point, color='black')
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', color='black', fontsize=12, ha='right')

# Labeling the axes
plt.xlim(0, 15)
plt.ylim(0, 10)
plt.xlabel('Units of Product A')
plt.ylabel('Units of Product B')

# Add title and legend
plt.title('Graphical Solution for Maximizing Revenue\nOptimal Solution: Revenue = 80')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()


# In[ ]:


#QUESTION 5--Resource Allocation for Two Projects
import numpy as np
import matplotlib.pyplot as plt

# Define the constraints
def constraint1(x1):
    return (12 - 3*x1) / 4  # From 3x1 + 4x2 <= 12

def constraint2(x1):
    return (6 - 2*x1) / 1  # From 2x1 + x2 <= 6

# Generate values for x1
x1 = np.linspace(0, 6, 200)

# Calculate the corresponding x2 values for each constraint
x2_1 = constraint1(x1)  # From constraint 1
x2_2 = constraint2(x1)  # From constraint 2

# Plot the feasible region
plt.figure(figsize=(10, 6))

# Fill the feasible region where both constraints hold
plt.fill_between(x1, 0, np.minimum(x2_1, x2_2), where=(x2_1 >= 0) & (x2_2 >= 0), color='lightgray', label='Feasible Region')

# Plot the constraints
plt.plot(x1, x2_1, label=r'$3x_1 + 4x_2 \leq 12$', color='red')  # Labor hours constraint
plt.plot(x1, x2_2, label=r'$2x_1 + x_2 \leq 6$', color='green')  # Capital constraint

# Mark the corner points
corner_points = [(0, 0), (0, 6), (2, 3), (4, 0)]

# Plot the corner points
for point in corner_points:
    plt.scatter(*point, color='black')
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', color='black', fontsize=12, ha='right')

# Labeling the axes
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xlabel('Units of Project P1')
plt.ylabel('Units of Project P2')

# Add title and legend
plt.title('Graphical Solution for Maximizing Profit')
plt.legend()

# Display optimal solution above the plot
plt.figtext(0.5, 0.95, 'Optimal Solution: Profit = 32 at (4, 0)', ha='center', fontsize=14, color='blue')

# Show the plot
plt.grid(True)
plt.show()


# In[ ]:


#QUESTION 6--Production Planning for a Bakery
import numpy as np
import matplotlib.pyplot as plt

# Define the constraints
def constraint1(x1):
    return (8 - x1) / 2  # From x1 + 2x2 <= 8

def constraint2(x1):
    return (12 - 3*x1) / 2  # From 3x1 + 2x2 <= 12

# Generate values for x1
x1 = np.linspace(0, 8, 200)

# Calculate the corresponding x2 values for each constraint
x2_1 = constraint1(x1)  # From constraint 1
x2_2 = constraint2(x1)  # From constraint 2

# Plot the feasible region
plt.figure(figsize=(10, 6))

# Fill the feasible region where both constraints hold
plt.fill_between(x1, 0, np.minimum(x2_1, x2_2), where=(x2_1 >= 0) & (x2_2 >= 0), color='lightgray', label='Feasible Region')

# Plot the constraints
plt.plot(x1, x2_1, label=r'$x_1 + 2x_2 \leq 8$', color='red')  # Baking time constraint
plt.plot(x1, x2_2, label=r'$3x_1 + 2x_2 \leq 12$', color='green')  # Flour constraint

# Mark the corner points
corner_points = [(0, 0), (8, 0), (2, 3)]

# Plot the corner points
for point in corner_points:
    plt.scatter(*point, color='black')
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', color='black', fontsize=12, ha='right')

# Labeling the axes
plt.xlim(0, 8)
plt.ylim(0, 6)
plt.xlabel('Units of Chocolate Cake')
plt.ylabel('Units of Vanilla Cake')

# Add title and legend
plt.title('Graphical Solution for Maximizing Profit')
plt.legend()

# Display optimal solution above the plot
plt.figtext(0.5, 0.95, 'Optimal Solution: Profit = 40 at (8, 0)', ha='center', fontsize=14, color='blue')

# Show the plot
plt.grid(True)
plt.show()


# In[ ]:


#QUESTION 7 --Minimizing Cost for a Transport Company
import numpy as np
import matplotlib.pyplot as plt

# Define the constraints
def constraint1(x1):
    return (18 - 3*x1) / 4  # From 3x1 + 4x2 >= 18

def constraint2(x1):
    return (10 - 2*x1) / 1  # From 2x1 + x2 >= 10

# Generate values for x1
x1 = np.linspace(0, 6, 200)

# Calculate the corresponding x2 values for each constraint
x2_1 = constraint1(x1)  # From constraint 1
x2_2 = constraint2(x1)  # From constraint 2

# Plot the feasible region
plt.figure(figsize=(10, 6))

# Fill the feasible region where both constraints hold
plt.fill_between(x1, 0, np.minimum(x2_1, x2_2), where=(x2_1 >= 0) & (x2_2 >= 0), color='lightgray', label='Feasible Region')

# Plot the constraints
plt.plot(x1, x2_1, label=r'$3x_1 + 4x_2 \geq 18$', color='red')  # Fuel constraint
plt.plot(x1, x2_2, label=r'$2x_1 + x_2 \geq 10$', color='green')  # Driver time constraint

# Mark the corner points
corner_points = [(0, 0), (6, 0), (2, 4), (5, 0)]

# Plot the corner points
for point in corner_points:
    plt.scatter(*point, color='black')
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', color='black', fontsize=12, ha='right')

# Labeling the axes
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xlabel('Trips by Vehicle X')
plt.ylabel('Trips by Vehicle Y')

# Add title and legend
plt.title('Graphical Solution for Minimizing Cost')
plt.legend()

# Display optimal solution above the plot
plt.figtext(0.5, 0.95, 'Optimal Solution: Cost = $30 at (5, 0)', ha='center', fontsize=14, color='blue')

# Show the plot
plt.grid(True)
plt.show()


# In[ ]:


#QUESTION 8 --Maximizing Revenue from Two Products
import numpy as np
import matplotlib.pyplot as plt

# Define the constraints
def constraint1(x1):
    return (30 - 4*x1) / 3  # From 4x1 + 3x2 <= 30

def constraint2(x1):
    return (18 - x1) / 2  # From x1 + 2x2 <= 18

def constraint3(x1):
    return (24 - 3*x1) / 2  # From 3x1 + 2x2 <= 24

# Generate values for x1 within the range of 0 to 18
x1 = np.linspace(0, 18, 200)

# Calculate the corresponding x2 values for each constraint
x2_1 = constraint1(x1)  # From constraint 1
x2_2 = constraint2(x1)  # From constraint 2
x2_3 = constraint3(x1)  # From constraint 3

# Plot the feasible region
plt.figure(figsize=(10, 6))

# Fill the feasible region where all constraints hold
plt.fill_between(x1, 0, np.minimum(np.minimum(x2_1, x2_2), x2_3), where=(x2_1 >= 0) & (x2_2 >= 0) & (x2_3 >= 0), color='lightgray', label='Feasible Region')

# Plot the constraints
plt.plot(x1, x2_1, label=r'$4x_1 + 3x_2 \leq 30$', color='red')  # Labor constraint
plt.plot(x1, x2_2, label=r'$x_1 + 2x_2 \leq 18$', color='green')  # Raw material constraint
plt.plot(x1, x2_3, label=r'$3x_1 + 2x_2 \leq 24$', color='blue')  # Machine time constraint

# Mark the corner points
corner_points = [(0, 6), (6, 0), (4, 3), (18, 0)]  # Including (18, 0)

# Plot the corner points
for point in corner_points:
    plt.scatter(*point, color='black')
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', color='black', fontsize=12, ha='right')

# Labeling the axes
plt.xlim(0, 18)  # Set x-axis range from 0 to 18
plt.ylim(0, 12)  # Set y-axis range from 0 to 12
plt.xlabel('Units of Product P1')
plt.ylabel('Units of Product P2')

# Add title and legend
plt.title('Graphical Solution for Maximizing Revenue')
plt.legend()

# Display optimal solution above the plot
plt.figtext(0.5, 0.95, 'Optimal Solution: Revenue = $180 at (18, 0)', ha='center', fontsize=14, color='blue')

# Show the plot
plt.grid(True)
plt.show()


# In[ ]:


#QUESTION NUMBER 9 --Advertising Campaign Budget Allocation
import numpy as np
import matplotlib.pyplot as plt

# Define the constraints
def constraint1(x):
   return (5000 - 4000 * x) / 3000  # From 4000x + 3000y <= 5000

def constraint2(x):
   return (4500 - 2000 * x) / 2500  # From 2000x + 2500y <= 4500

def constraint3(x):
   return (3000 - 1000 * x) / 1500  # From 1000x + 1500y <= 3000

def constraint4(x):
   return 1.42857 - x  # From 7000x + 7000y <= 10000, simplifies to x + y <= 1.42857

# Generate values for x
x = np.linspace(0, 4, 200)

# Calculate the corresponding y values for each constraint
y_1 = constraint1(x)  # From constraint 1
y_2 = constraint2(x)  # From constraint 2
y_3 = constraint3(x)  # From constraint 3
y_4 = constraint4(x)  # From the total budget constraint

# Plot the feasible region
plt.figure(figsize=(10, 6))

# Fill the feasible region where all constraints hold
plt.fill_between(x, 0, np.minimum(np.minimum(np.minimum(y_1, y_2), y_3), y_4), 
                where=(y_1 >= 0) & (y_2 >= 0) & (y_3 >= 0) & (y_4 >= 0), 
                color='lightgray', label='Feasible Region')

# Plot the constraints
plt.plot(x, y_1, label=r'$4000x + 3000y \leq 5000$', color='red')  # Television budget constraint
plt.plot(x, y_2, label=r'$2000x + 2500y \leq 4500$', color='green')  # Print media budget constraint
plt.plot(x, y_3, label=r'$1000x + 1500y \leq 3000$', color='blue')  # Social media budget constraint
plt.plot(x, y_4, label=r'$7000x + 7000y \leq 10000$', color='purple')  # Total budget constraint

# Mark the corner points
corner_points = [(0, 1.42857), (3, 0), (0, 0)]  # Based on solving equations

# Plot the corner points
for point in corner_points:
   plt.scatter(*point, color='black')
   plt.text(point[0], point[1], f'({point[0]:.2f}, {point[1]:.2f})', color='black', fontsize=12, ha='right')

# Labeling the axes
plt.xlim(0, 4)  # Set x-axis range
plt.ylim(0, 2)  # Set y-axis range
plt.xlabel('Campaign A')
plt.ylabel('Campaign B')

# Add title and legend
plt.title('Graphical Solution for Maximizing Reach')
plt.legend()

# Display optimal solution above the plot
plt.figtext(0.5, 0.95, 'Optimal Solution: Reach = 1.5 million at (3, 0)', ha='center', fontsize=14, color='blue')

# Show the plot
plt.grid(True)
plt.show()


# In[ ]:


#QUESTION 10 ----Meal Planning for a School Cafeteria
import numpy as np
import matplotlib.pyplot as plt

# Define the constraints
def constraint1(x):
    return (30 - 2*x) / 4  # From 2x + 4y <= 30

def constraint2(x):
    return (24 - 3*x) / 2  # From 3x + 2y <= 24

def constraint3(x):
    return (20 - x) / 2  # From x + 2y <= 20

# Generate values for x
x = np.linspace(0, 20, 200)

# Calculate the corresponding y values for each constraint
y_1 = constraint1(x)  # From meat constraint
y_2 = constraint2(x)  # From vegetable constraint
y_3 = constraint3(x)  # From rice constraint

# Plot the feasible region
plt.figure(figsize=(10, 6))

# Fill the feasible region where all constraints hold
plt.fill_between(x, 0, np.minimum(np.minimum(y_1, y_2), y_3), 
                 where=(y_1 >= 0) & (y_2 >= 0) & (y_3 >= 0), 
                 color='lightgray', label='Feasible Region')

# Plot the constraints
plt.plot(x, y_1, label=r'$2x + 4y \leq 30$', color='red')  # Meat constraint
plt.plot(x, y_2, label=r'$3x + 2y \leq 24$', color='green')  # Vegetable constraint
plt.plot(x, y_3, label=r'$x + 2y \leq 20$', color='blue')  # Rice constraint

# Mark the corner points (calculated from the intersection of constraints)
corner_points = [(6, 3), (9, 0), (20, 0)]

# Plot the corner points
for point in corner_points:
    plt.scatter(*point, color='black')
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', color='black', fontsize=12, ha='right')

# Labeling the axes
plt.xlim(0, 20)  # Set x-axis range to include the optimal point (20, 0)
plt.ylim(0, 12)  # Set y-axis range
plt.xlabel('Meals A (x)')
plt.ylabel('Meals B (y)')

# Add title and legend
plt.title('Graphical Solution for Maximizing Revenue')
plt.legend()

# Display optimal solution above the plot
plt.figtext(0.5, 0.95, 'Optimal Solution: Revenue = $120 at (20, 0)', ha='center', fontsize=14, color='blue')

# Show the plot
plt.grid(True)
plt.show()

