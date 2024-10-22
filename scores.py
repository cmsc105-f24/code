# Function to calculate the average of a list
# params: grades list
# returns: average grade
def calculate_average(grades):
    ### YOUR CODE GOES HERE: ###


# Function to find the maximum grade
# params: grades list
# returns: maximum grade
def find_max(grades):
    ### YOUR CODE GOES HERE: ###


# Function to find the minimum grade
# params: grades list
# returns: minimum grade
def find_min(grades):
    ### YOUR CODE GOES HERE: ###   


# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. Display all grades")
    print("2. Find the highest grade")
    print("3. Find the lowest grade")
    print("4. Calculate the average grade")
    print("5. Sort the grades")
    print("6. Check if a grade exists")
    print("7. Remove a grade")
    print("8. Exit")

# Main program starts here
grades = []

# Get the number of grades
num_grades = int(input("How many grades do you want to input? "))

# Input grades from the user
for i in range(num_grades):
    grade = int(input(f"Enter grade {i + 1}: "))
    grades.append(grade)

# Main loop for the menu
while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        # Display all grades
        print("Grades:", grades)
    
    elif choice == 2:
        # Find the highest grade
        if grades:
            print("Highest grade:", find_max(grades))
        else:
            print("No grades to display.")
    
    elif choice == 3:
        # Find the lowest grade
        if grades:
            print("Lowest grade:", find_min(grades))
        else:
            print("No grades to display.")
    
    elif choice == 4:
        # Calculate the average grade
        avg = calculate_average(grades)
        print("Average grade:", avg)
    
    elif choice == 5:
        # Sort and display grades
        sorted_grades = sorted(grades)
        print("Sorted grades:", sorted_grades)
    
    elif choice == 6:
        # Check if a grade exists
        check_grade = int(input("Enter the grade to check: "))
        if check_grade in grades:
            print("Grade", check_grade, "exists in the list.")
        else:
            print("Grade", check_grade, "does not exist.")
    
    elif choice == 7:
        # Remove a grade
        remove_grade = int(input("Enter the grade to remove: "))
        if remove_grade in grades:
            grades.remove(remove_grade)
            print("Grade", remove_grade, "removed.")
        else:
            print("Grade", remove_grade, "not found.")
    
    elif choice == 8:
        # Exit the program
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please try again.")