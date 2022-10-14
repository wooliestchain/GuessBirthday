js1=set([1,3,5,7,
        9,11,13,15,
        17,19,21,23,
         25,27,29,31])

js2=set([2,3,6,7,
        10,11,14,15,
        18,19,22,23,
        26,27,30,31])

js3=set([4,5,6,7,
        12,13,14,15,
        20,21,22,23,
        28,29,30,31])

js4=set([8,9,10,11,
        12,13,14,15,
        24,25,26,27,
        28,29,30,31])

js5=set([16,17,18,19,
        20,21,22,23,
        24,25,26,27,
        28,29,30,31])

jour=0

print("Votre anniversaire se trouve dans le set1?")
print(js1)
print('''
1.OUI
0.NON''')
choice=input("Entrer une reponse ")
if (choice=='1'):
        jour = jour+1

print("Votre anniversaire se trouve dans le set2?")
print(js2)
print('''
1.OUI
0.NON''')
choice=input("Entrer une reponse ")
if (choice=='1'):
        jour = jour+ 2

print("Votre anniversaire se trouve dans le set3?")
print(js3)
print('''
1.OUI
0.NON''')
choice=input("Entrer une reponse ")
if (choice=='1'):
        jour =jour+4

print("Votre anniversaire se trouve dans le set4?")
print(js4)
print('''
1.OUI
0.NON''')
choice=input("Entrer une reponse ")
if (choice=='1'):
        jour =jour+8

print("Votre anniversaire se trouve dans le set5?")
print(js5)
print('''
1.OUI
0.NON''')
choice=input("Entrer une reponse ")
if (choice=='1'):
        jour =jour+16

print("Votre date d'anniversaire est",jour,"!")
