n = "tamrin_07f.txt"
file = open(n,"r")
x = file.readlines()
alphabet, alphaLower, alphaUpper, alphabetCount, lower, upper = [], [], [], [], [], []
for i in range(26):
    lower.append(0)
    upper.append(0)
for f in x:
    for i in f:
        Asc = ord(i)
        if(Asc >= 97 & Asc <= 122):
            count = 0
            for alp in range(97,123):
                if(alp == Asc):
                    lower[count] += 1
                count += 1
        if(Asc >= 65 & Asc <= 91):
            count = 0
            for alp in range(65,92):
                if(alp == Asc):
                    upper[count] += 1
                count += 1
for i in range(26):
    alphaLower.append(chr(i + 97))
    alphaUpper.append(chr(i + 65))
alphabet = alphaUpper + alphaLower
alphabetCount = upper + lower
print("----------\nalphabet :\n")
for i in range(len(alphabet)):
    print(f"{alphabet[i]} : {alphabetCount[i]}")
file.close()