print("hello world")
#Count the occurrence of each vowel in the sentence given as input by the user.
vouels={'a':0,'e':0,'i':0,'o':0,'u':0}
ui=input("pleas give us a word you want to anylize")
for c in ui:
    if c in vouels :
        vouels[c]=vouels[c]+1
print(vouels)
