#Decode a String, google/leetcode challenge. 15/04/2021
#note this is my first draft so it can not decode nested strings, making nested strings
#took an extra 30 mins so I uploaded a new file for it
#sample input: 3[a]2[bc]
#sample output: aaabcbc
#sample input 2: 3[a2[c]]
#sample output 2: accaccacc
#sample input 3: 2[abc]3[cd]ef
#sample output 3: abcabccdcdcdef
#sample input 4: abc3[cd]xyz
#sample input 4: abccdcdcdxyz
s = input("input: ")
i = 0
num = 0
letters = ""
while i < len(s)-1:
    if s[i].isnumeric():
        num += int(s[i])
    if s[i].isalpha():
        letters = letters + s[i]
        num = 0
    if s[i] == "[":
        i+=1
        letters1 = ""
        while s[i] != "]":
            letters1 = letters1 + s[i]
            i+=1
        j = 0
        while j < num:
            letters = letters + letters1
            j+=1
        num = 0
    i+=1
print(letters)
        
    
