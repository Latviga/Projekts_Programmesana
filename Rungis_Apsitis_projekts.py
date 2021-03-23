a=int(input("Cik pastaigas bija sarunātas? - "))
n=0

for i in range(1,a+1): #pēc ievadītā "a" skaita, tik pat reizes pieprasa pastaigas garumu
    print("Cik gara bija pastaiga? - ", i) #pajautā "a" reizes
    b=int(input("(min)- "))
    n+=b

pl= 0.17 #minūtes likme pastaigai
bl= 1 # barošanas likme 1 reizei

p= float(input("Jebkādas papildus izmaksas (eur) - ")) #iecadīt jebkādas papildus izmaksas

print("==========================================")
print("Izmaksas par pastaigām ir %.2f "% (n*pl),"eur.")
print("Izmaksas par barošanu ir %.2f "% (a*bl),"eur.")
print("Papildus izmaksas ir %.2f "% p," eur.")
print("Kopējās izmaksas ir %.2f "% ((n*pl)+(a*bl)+p),"eur.")
print("==========================================")