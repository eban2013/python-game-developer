adress=(21 ,"triq' san albert","sliema","slm3621" )
print(adress)
print(type(adress))
print(adress[1])

for item in adress:
    print(item)

#packing

numbers=(2,8,3)
print(numbers)

#unpacking

n1,n2,n3=numbers
print(n1)
print(n2)
print(n3)

#one itemm touple

test=("apple",)
print(type(test))

#touple without brackets 

nobrackets= "apple","banana","orange","pear"
print(type(nobrackets))

notest=list(nobrackets)
print(notest)
print(type(notest))

dicttest=dict(nobrackets)
print(dicttest)
print(type(dicttest))