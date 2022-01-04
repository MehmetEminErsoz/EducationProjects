#100 öğrenci oluştur 100 random not oluştur,
#sort ve reverse komutu kullanmadan sırala

import random 
import string
capraztab=[]
captab2=[]


sozluk ={}
def rndharf():
    harf = random.choice(string.ascii_uppercase)
    harf1 = random.choice(string.ascii_uppercase)
    harf2 = random.choice(string.ascii_uppercase)
    harf3 = random.choice(string.ascii_uppercase)   
    harf4 = random.choice(string.ascii_uppercase)
    harf5 = random.choice(string.ascii_uppercase)
    return(harf+harf1+harf2+harf3+harf4+harf5)
          


for i in range(100):
    notdeg=random.randrange(10,100)
    capraztab.append(str(notdeg) +" "+rndharf())
    captab2.append(notdeg)
    
    

def metinol(sayı):

    metin= capraztab[i]
    
    sayı =int(metin[0:3])
    
    
    

def bubbleSort(arr):
    n = len(arr)
  
    
    for i in range(n):
  
        
        for j in range(0, n-i-1):
  
           
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(captab2)




#Tersi için -i
for i in range(len(capraztab)):
    print ("%d" %captab2[-i]+" "+rndharf()), 
    





