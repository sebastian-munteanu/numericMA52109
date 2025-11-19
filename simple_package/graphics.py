import matplotlib.pyplot as plt

def histogram(data, mean, median):
    
    plt.figure(figsize=(8, 5))
    
    # Plot histogram
    plt.hist(data, alpha=0.7, color='skyblue', edgecolor='black')
    
    # Add vertical lines for mean and median
    plt.axvline(mean, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean:.2f}')
    plt.axvline(median, color='green', linestyle='--', linewidth=2, label=f'Median: {median:.2f}')
    
    # Customize the plot
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()