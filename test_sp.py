###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

import simple_package as sp

if __name__ == '__main__':
    ## Define two numbers
    a = 1
    b = 2
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {a + b}")

    ## Now do the same for the function in sp
    print(f"The product of {a} and {b} is {sp.add(a,b)}")

    #operations.py
    sp.interface()

    #statistics.py
    data = [1,2,3,4,5,5,6,7,8,9,10,10,10,11,12,13,14,15] 
    sp.calculate_statistics(data)
    sp.plot_histogram(data)
  