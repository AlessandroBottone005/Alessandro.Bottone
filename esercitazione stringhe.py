s=str(input ("inserisci una stringa: "))
ripetizioni=0
for i in range (0, len(s)):
    r=l
    x=s [i]
    for j in range (i+1, len(s)):
        if s [i] == s[j]:
            r= r+l
            if r > ripetizioni:
                carattere = x
                ripetizioni = r
                print (carattere)
                print (ripetizioni)
