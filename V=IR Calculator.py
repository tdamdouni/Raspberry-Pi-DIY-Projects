print("Please enter a value for two fields, and leave the other as 0.")
print(" ")

V = 0
I = 0
R = 0

def V1():
    global V
    V = 0
    I = 0
    R = 0
    try:
        V = float(input("Please enter a voltage: "))
        I1()
    except:
        print("You entered an invalid symbol. Please use numbers only.")
        print(" ")
        V1()
        
def I1():
    global I
    try:
        I = float(input("Please enter a current: "))
        R1()
    except:
        print("You entered an invalid symbol. Please use numbers only.")
        print(" ")
        I1()
        
def R1():
    global R
    try:
        R = int(input("Please enter a resistance: "))
    except:
        print("You entered an invalid symbol. Please use numbers only.")
        print(" ")
        R1()
    pass
        
def again():
    print(" ")
    try:
        again1 = str(input("Would you like to calculate another set? Y/n "))
    except:
        print("You entered an invalid symbol. Please use Y or N only.")
        print(" ")
        again()
    again1 = again1.lower()
    if again1 == "y":
        pass
        
    else:
        print("Quitting...")
        exit()


while True:
    
    V1()
   
    if V > 0 and I > 0:
        print(" ")
        print("You entered {} Volts and {} Amps; finding resistance...".format(V, I))
        print(" ")
        R = int(V / I)
        print("{} Volts / {} Amps = {} Ohms".format(V, I, R))
        W = I*V
        print("This gives you {} Watts of power.".format(W))
        again()
        
    elif V > 0 and R > 0:
        print(" ")
        print("You entered {} Volts and {} Ohms; finding current...".format(V, R))
        print(" ")
        I = round(V / R, 2)
        if I > 1:
            print("{} Volts / {} Ohms = {} Amps".format(V, R, I))
        else:
            I1 = I * 100
            print("{} Volts / {} Ohms = {} Milliamps".format(V, R, I1))
        W = I*V
        print(" ")
        print("This gives you {} Watts of power.".format(W))
        again()
        
    elif I > 0 and R > 0:
        print(" ")
        print("You entered {} Amps and {} Ohms; finding voltage...".format(I, R))
        print(" ")
        V = round(I * R, 2)
        if V > 1:
            print("{} Amps * {} Ohms = {} Volts".format(I, R, V))
        else:
            V = V * 100
            print("{} Amps * {} Ohms = {} Millivolts".format(I, R, V))
        again()
    else:
        print(" ")
        print("You haven't entered enough values to complete an equation. Please enter two or more values.")
        V1()
    
    print(" ")
    

