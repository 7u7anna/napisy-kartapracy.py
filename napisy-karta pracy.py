# KARTA PRACY NAPISY - Powodzenia!

# 1. Generowanie napisów (wielkie litery A-Z)

# a) napisz skrytp, który wygeneruje 10 dowolnych
#    trzyliterowych słów. Wypisz je na ekran. 

import random

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

T = []
for i in range(10):
  m = random.choice(alfabet)
  T.append(m)
  for j in range(2):
    T[i]+= random.choice(alfabet)
T = " ".join(T)
print(T)


# b) wiedząc, że ludzkie DNA to ciąg 4 białek A, G, C, T stwórz losowy 
#    łańcuch DNA składający się z 4000 znaków. 
#import random

#for i in range(4000):
  #x = (random.choice('AGCT'))
  #print(x, end = "")


#    Sprawdź czy gdzieś udało się
#    uzyskać 4 takie same literki koło siebie

#K = []
#for x in range(4000):
  #x = (random.choice('AGCT'))
  #K.append(x)
#print(K)

#s = 0
#for i in range(len(K)-1):
   # if K[i] == K[i+1] == K[i+2] == K[i+3]:
     # print(K[i], K[i+1], K[i+2], K[i+3])
     # s+= 1
#print(s)

# 2. Napisy z klawiatury (wielkie litery A-Z)

# a) sprawdź czy wpisane przez usera imię jest żeńskie

#a = str(input())
#def check(a):
   #for i in a:
     # if a[-1] == 'A':
      #   return True
      #else:
      #   return False
#print(check(a))

# b) popraw błąd. Załóż, że user wpisuje jakieś słowo z "Ó", 
#  a powinien z "U". Popraw ten błąd i wypisz poprawne słowo na ekran

#slowo = str(input())
#slowo = slowo.replace("Ó", "U")
#print(slowo)

# c) usuń wszystkie spacje z napisu-zdania wpisanego przez usera

#slowo = str(input())
#slowo = slowo.replace(" ", "")
#print(slowo)

# d) niech user wpisze date w formacie D-M-R 
#    Wypisz tą datę w formacie R-M-D 

#data = str(input())
#data = data.split(sep="-")
#data[0], data[2] = data[2], data[0]
#x = "-".join(data)
#print(x)

# 3. Praca z plikiem loko.txt (wielkie litery bez polskich znaków)

#with open("lokomotywa.txt", "r") as plik:
  #T = []
  #for x in plik:
  #  T.append(x.strip())

#plik.close()

# a) policz wiersze w pliku

#s = 0
#for i in T:
  #s+= 1
#print(s)

# b) policz słowa w pliku

#K = []
#for x in T:
#  x = x.split()
   #K.append(x)

#s = 0
#for elem in K:
  #for j in elem:
     # s+= 1
#print(s)

# c) policz spacje w pliku

#s = 0
#for i in T:
 # for j in i:
   # if j == ' ':
    #  s+= 1
#print(s)

# d) policz literki "A" w parzystych wierszach

#s = 0
#for i in T[::2]:
  #for j in i:
    #if j == 'A':
    #  s+= 1
#print(s)
  

# e) Których literek jest więcej, "Z", czy "W"?

#z = 0
#w = 0
#for i in T:
 # for j in i:
   # if j == 'W':
    #  w+= 1
   # if j == 'Z':
     # z+= 1
#if w > z:
  #print("wiecej jest liter W")
#else:
  #print("wiecej jest liter Z")
    
# f) podaj ilość wierszy o liczbie słów większej niż 8

#K = []
#for x in T:
  #x = x.split()
  #K.append(x)

#s = 0
#for i in range(len(K)):
   # if len(K[i]) > 8:
    #  print(K[i])
     # s+= 1
#print(s)

# g) podaj ilość wierszy rozpoczynających 
#    i kończących się na tą samą literę

#s = 0
#for i in range(len(T)):
    #if T[i][0] == T[i][-1]:
      #print(T[i])
      #s+= 1
#print(s)


# h) podaj ilość słów rozpoczynających 
#    i kończących się na tą samą literę


#K = []
#for x in T:
 # x = x.split()
 # K.append(x)

#s = 0
#for i in range(len(K)):
 # for j in range(len(K[i])):
  #  for y in range(len(K[i][j])):
   #   if K[i][j][0] == K[i][j][-1]:
   #     print(K[i][j])
    #    s+= 1
#print(s)


# i) wypisz tekst małymi literami

#for x in T:
   # print(x.lower())

# j) policz w ilu miejscach pliku występują 
#    dwa takie same znaki koło siebie

#s = 0
#for i in range(len(T)):
 # for j in range(len(T[i])-1):
    #  if T[i][j] == T[i][j+1]:
     #   s+= 1
#print(s)

# k*) policz w ilu miejscach pliku występują dwie
#     takie same literki koło siebie (nawet jeśli oddziela je spacja)

#K = []
#for x in T:
  # x = x.replace(" ", "")
  # K.append(x)

#s = 0
#for i in range(len(K)):
 # for j in range(len(K[i])-1):
  #  if K[i][j] == K[i][j+1]:
    #  s+= 1
#print(s)