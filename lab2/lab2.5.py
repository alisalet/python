numbers=list(range(1,21))
even=list(filter(lambda x:x%2==0,numbers))
print(even)
add=list(map(lambda x:x+10,numbers))
print(add)
sort=sorted(numbers,key=lambda x:-x)
print(sort)