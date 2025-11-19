###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##


import numpy as np
import matplotlib.pyplot as plt
from simple_package.graphics import histogram

def check_dependencies():
    #Check if required packages are installed
    try:
        import numpy
        import matplotlib
    except ImportError as e:
        raise ImportError(f"Required package not installed: {e}. Please install numpy and matplotlib.")

def validate_input(data):
    #Validate input and convert to numpy array if needed
    check_dependencies()
    
    if not isinstance(data, (list, np.ndarray)):
        raise TypeError("Input must be a list or numpy array")
    
    if isinstance(data, list):
        data = np.array(data)
    
    if data.size == 0:
        raise ValueError("Input data cannot be empty")
    
    return data

def calculate_statistics(data):
    data = validate_input(data)
    
    # Calculate statistics
    mean_val = np.mean(data)
    median_val = np.median(data)
    std_val = np.std(data)
    
    stats = {
        'mean': mean_val,
        'median': median_val,
        'std': std_val
    }
    
    # Printing results
    print(f"Mean: {mean_val:.4f}")
    print(f"Median: {median_val:.4f}")
    print(f"Standard Deviation: {std_val:.4f}")
    
    return stats

def plot_histogram(data):
    data = validate_input(data)
    stats = calculate_statistics(data)  # This will also print the stats
    
    # Use the graphics module to create the plot
    histogram(data, stats['mean'], stats['median'])
