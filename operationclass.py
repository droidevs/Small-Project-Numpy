# Import the numpy library for numerical operations
import numpy as np
# Import the matplotlib library for plotting
import matplotlib.pyplot as plt

# Define a class to handle integer arrays
class IntArray:
    """
    A class to represent and operate on a numpy array of integers.

    Attributes
    ----------
    int_array : np.ndarray
        a numpy array of integers
    """

    def __init__(self, int_array):
        """
        Constructs all the necessary attributes for the IntArray object.

        Parameters
        ----------
            int_array : np.ndarray
                a numpy array of integers
        """
        # Check if the input is a numpy array of integers
        if not isinstance(int_array, np.ndarray) or int_array.dtype != int:
            # Raise a ValueError if the input is not valid
            raise ValueError("Input must be a numpy array of integers")

        # Assign the input array to the instance variable
        self.int_array = int_array

    def display(self):
        """Prints the integer array to the console."""
        # Print the integer array
        print(self.int_array)

    def salary(self):
        """Calculates and prints the salaries of the employees based on their productivity."""
        # Get the shape of the integer array
        array_shape = self.int_array.shape
        # Create a numpy array of the same shape with all elements as 7
        money_per_product = np.full(array_shape, 7)
        # Multiply the number of products with the money per product to get the salaries
        salaries = self.int_array * money_per_product
        # Print the number of products and the corresponding salaries
        print(f"People made {self.int_array} products and this is their salaries {salaries}")

    def show_data(self):
        """Displays the productivity of employees as a plot."""
        # Create an array of x-coordinates for the plot
        x = np.arange(len(self.int_array))
        # Plot the integer array with markers
        plt.plot(x, self.int_array, marker = 'o')
        # Set the title of the plot
        plt.title("Productivity of employees")
        # Set the label for the x-axis
        plt.xlabel("rank of employees")
        # Set the label for the y-axis
        plt.ylabel("products/month")
        # Set the x-ticks to be the indices of the employees
        plt.xticks(x)
        # Display a grid on the plot
        plt.grid()
        # Show the plot
        plt.show()
