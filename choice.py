# # Initialize an empty dictionary to store employee information
# employee_data = {}
#
# # Get at least 5 employee names and designations
# for _ in range(5):
#     employee_name = input("Enter the employee name: ")
#     employee_designation = input("Enter the employee designation (backend or frontend): ")
#
#     # Check if the entered designation is valid
#     if employee_designation.lower() not in ['backend', 'frontend']:
#         print("Invalid designation. Please enter 'backend' or 'frontend'.")
#     else:
#         # Add the employee information to the dictionary
#         employee_data[employee_name] = employee_designation
#
# # Print the final result
# print("Employee Information:")
# for name, designation in employee_data.items():
#     print(f"{name}: {designation}")

# Initialize empty dictionaries to store frontend and backend employee information
frontend_employees = {}
backend_employees = {}

# Get at least 5 employee names and designations
for _ in range(3):
    employee_name = input("Enter the employee name: ")
    employee_designation = input("Enter the employee designation (backend or frontend): ")

    # Check if the entered designation is valid
    if employee_designation.lower() not in ['backend', 'frontend']:
        print("Invalid designation. Please enter 'backend' or 'frontend'.")
    else:
        # Add the employee information to the respective dictionaries
        if employee_designation.lower() == 'backend':
            backend_employees[employee_name] = True
        else:
            frontend_employees[employee_name] = True

# Find employees who work in both frontend and backend
both_departments = set(frontend_employees.keys()) & set(backend_employees.keys())

# Print the result
if both_departments:
    print("Employees who work in both frontend and backend:")
    for employee in both_departments:
        print(employee)
else:
    print("No employees found who work in both frontend and backend.")

