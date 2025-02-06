def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))
#print("Compound Interest: "+str(intrest))

    total_amount = client_one_principal * ( 1 + client_one_rate/100)**client_one_time
    #print (total_amount)
    compound_intrest = total_amount - client_one_principal
    final_compound_intrest = round (compound_intrest, 2)
    print (final_compound_intrest)

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()