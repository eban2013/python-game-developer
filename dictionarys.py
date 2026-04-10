print("hello world")
#Count the occurrence of each vowel in the sentence given as input by the user.
vouels={'a':0,'e':0,'i':0,'o':0,'u':0}
ui=input("pleas give us a word you want to anylize")
for c in ui:
    if c in vouels :
        vouels[c]=vouels[c]+1
print(vouels)
#Count the occurrence of each alphabet that occurs in the sentence given as input by the user.
alphabet={}
ui=input("can you give us a sentence to anylize")
for i in ui:
    if i in alphabet:
        alphabet[i]=alphabet[i]+1
    else:
        alphabet[i]=1
print(alphabet)

#Find if a given number entered by the user is a pangram or not ?
#A pangram number is a number which contains at least one occurrence of each digit.

digits={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
ui=input("can you pleas give us any number to see if it is a pangram")
l=len(ui)
if l < 10:
    print("this is not a pangram")
else:
    for i in ui:
        if i in digits:
            digits[i]=digits[i]+1
print(digits)
if 0 in digits.values():
    print("this is not a panogram")
else:
    print("this is a panogram")

    

    
