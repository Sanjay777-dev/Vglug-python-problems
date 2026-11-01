#Method 1
n=input("Enter the number:")
if str(n)==str(n)[::-1]:
    print("True")
else:
    print("False")

#Method 2
def ispalindrome(x):
    if x < 0:
        return False
    elif str(x) == str(x)[::-1]:
        return True
    else:
        return False
num = int(input("Enter no: "))
print(ispalindrome(num))