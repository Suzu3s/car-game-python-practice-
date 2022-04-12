print("\t\t\t\t\tHere you  can check your weight conversion into pounds or kg")
weight = int(input("Enter Your Weight"))
inp = input("\n(L) for lbs\n (K) for kg")

if inp.upper() == "L" :
    Conv_weight = weight * 0.45
    print(f"Your weight is {Conv_weight} kg ")
else:
    Conv_weight = weight / 0.45
    print (f"Your weight is {Conv_weight} pounds")

