testsuly=float(input("Adja meg a testsúlyának tömegét (kg-ban): "))
magassag=float(input("Adja meg a magasságát (cm-ben): "))

bmi=(testsuly)/(magassag/100)**2

print(bmi)

if(bmi<18):
    print("Sovány testalkat")

elif(bmi>18) and (bmi<25):
    print("Normál testsúly")

elif(bmi==18) and (bmi==25):
    print("Normál testsúly")

elif(bmi>25):
    print("Túlsúlyosság")

else:
    print("Valami nem jó")