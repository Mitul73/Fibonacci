
def fibonacci():
    number=int(input("Enter a number = "))
    sequence=[0,1]
    if number<=0:
        return "Please enter positive number."
    elif number==1:
        return [0]
    else :
        for i in range (2,number):
             next= sequence[i-1] + sequence[i-2]
             sequence.append(next)
        return sequence

sequence=fibonacci()
print(sequence)                                        
