# Import the numpy library for numerical operations
import numpy as np
# Import the IntArray class from the operationclass module
from operationclass import IntArray

def productivity_of_company(order, data_frame):
    """
    Calculates the total productivity of a company.

    Args:
        order (int): The index of the company in the data_frame.
        data_frame (np.ndarray): A numpy array containing the productivity data of all companies.

    Returns:
        int: The sum of all products of the company.
    """
    # Return the sum of all the products of the company
    return np.sum(data_frame[order])

def max_productivity(data_frame):
    """
    Finds the company with the maximum productivity and prints the result.

    Args:
        data_frame (np.ndarray): A numpy array containing the productivity data of all companies.
    """
    # Initialize the index of the best company
    i = 0
    # Initialize the best company to the first one
    best_company = i + 1
    # Initialize the number of products to 0
    num_products = 0

    # Iterate over the data_frame to find the company with the maximum productivity
    for i in range(len(data_frame)):
        # Calculate the productivity of the company
        result = productivity_of_company(i, data_frame)
        # If the productivity of the current company is greater than the maximum productivity found so far
        if result > num_products:
            # Update the maximum productivity
            num_products = result
            # Update the best company
            best_company = i + 1
    # Print the best company and its productivity
    print(f"The best company is the {best_company}. company with {num_products}")

def min_productivity(data_frame):
    """
    Finds the company with the minimum productivity and prints the result.

    Args:
        data_frame (np.ndarray): A numpy array containing the productivity data of all companies.
    """
    # Initialize the index of the worst company
    i = 0
    # Initialize the worst company to the first one
    worst_company = i + 1
    # Initialize the number of products to the productivity of the first company
    num_of_products = productivity_of_company(0, data_frame)

    # Iterate over the data_frame to find the company with the minimum productivity
    for i in range(len(data_frame)):
        # Calculate the productivity of the company
        result = productivity_of_company(i, data_frame)
        # If the productivity of the current company is less than or equal to the minimum productivity found so far
        if result <= num_of_products:
            # Update the minimum productivity
            num_of_products = result
            # Update the worst company
            worst_company = i + 1

    # Print the worst company and its productivity
    print(f"The worst company is the {worst_company}. company with {num_of_products}")

def file_handling():
    """
    Reads the company data from the file "company.txt" and returns it as a numpy array.

    Returns:
        np.ndarray: A numpy array containing the productivity data of all companies.
    """
    # Initialize an empty list to store the lines from the file
    lines = []

    # Open the file "company.txt" in read mode
    with open("company.txt", "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Strip the newline character and split the line by comma
            values = line.strip().split(",")
            # Convert the values to integers
            int_values = [int(val) for val in values]
            # Append the integer values to the lines list
            lines.append(int_values)

        # Convert the list of lists to a numpy array of objects
        data_frame = np.array([np.array(row) for row in lines], dtype="object")

        # Iterate over each row in the data_frame
        for row in data_frame:
            # Iterate over each item in the row
            for i in row:
                # Print the type of the item
                print(type(i))
        # Return the data_frame
        return data_frame

def mean_products(data_frame):
    """
    Calculates and prints the mean number of products for each company.

    Args:
        data_frame (np.ndarray): A numpy array containing the productivity data of all companies.
    """
    # Iterate over the data_frame to calculate the mean number of products for each company
    for i in range(len(data_frame)):
        # Calculate the mean of the products of the company
        average = np.mean(data_frame[i])
        # Print the average number of products for the company
        print(f"On average, on employee from {i}. company produced {average} products")


def main():
    """
    The main function of the script.
    """
    # Get the data_frame from the file
    data_frame = file_handling()
    # Print the data_frame
    print(data_frame)
    # Create an IntArray object for the first branch
    first_branch = IntArray(data_frame[0])
    # Display the data of the first branch
    first_branch.display()
    # Calculate the salary for the first branch
    first_branch.salary()
    # Show the data of the first branch as a plot
    first_branch.show_data()

    # Find the company with the maximum productivity
    max_productivity(data_frame)
    # Find the company with the minimum productivity
    min_productivity(data_frame)

# Call the main function
main()