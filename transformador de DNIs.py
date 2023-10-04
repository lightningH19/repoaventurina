import math
import time as w

print("Choose a log(,0,1,2,10)")
log = input()

if log == "0":

    def power_of_10_representation(number):
        x = math.log(number)   
        return f"{x}"
elif log == "1":
    def power_of_10_representation(number):
        x = math.log1p(number)   
        return f"1^{x}"
elif log == "2":
    def power_of_10_representation(number):
        x = math.log2(number)   
        return f"2^{x}"
else:
    def power_of_10_representation(number):
        x = math.log10(number)   
        return f"10^{x}"
    
# Example usage:
number = float(input("Enter a number: "))
result = power_of_10_representation(number)
print(f"The representation of {number} with 10 to the power of x is: {result}")
w.sleep(20)