#Method 1
n=int(input("Enter the number:"))
while n%2==0:
    n=n//2
if n==1:
    print("True")
else:
    print("False")

#Method 2
def isPowerOfTwo(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2
    if n == 1:
        return True
    else:
        return False
num=int(input("Enter the number:"))
print(isPowerOfTwo(num))
