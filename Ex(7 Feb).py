# this is a python script 

# Calculate Simple Intrest 
def simple_intrest(p: int|float, n: int, r: float|int) -> tuple:

    """
        p: Principal in INR
        n : Number of Years
        r : Rate of intrest in percent per annum
        Output : intrest & amount
    """

    i =(p*n*r)/100
    a = p + i
    return p,i

# Take p,n,r as input from user 
p = float(input("Enter Principle in INR : "))
n = int(input("Enter Number of Years : "))
r = float(input("Enter rate of Intrest in % P.A : "))

# Call the simple intrest function
i,a = simple_intrest(p,n,r)

# Print the Intrest & Amount
print(f"Simple Intrest : {i:.2f} INR.")
print(f"Amount : {a:.2f} INR.")