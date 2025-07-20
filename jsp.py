num=int(input("Enter a number:"))
if num<=1:
    print(num,"is not a prime number")
else:
    is_prime=True
    for i in range(2,int(num**0.5)+1):
