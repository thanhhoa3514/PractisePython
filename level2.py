# import math
# c=50
# h=30

# values=[]
# items=[x for x in input("Enter the number of items").split(',')]
# for d in items:
#     values.append(str(int(round(math.sqrt((2*c*float(d))/h)))))
    
# print(', '.join(values))    


################################################################

#Sort the values in ascending
    # items=[x for x in input("Enter the number of items").split(',')]
    # items.sort(reverse=True)
    # print(', '.join(items))


#Convert the lower string to upper string

    # l=[]
    # # items=[x for x in input("Enter the number of items").split(',')]
    # while True:
    #     s=input("Enter a string (or 'quit' to exit): ")
    #     if s.lower()=='quit':
    #         break
    #     l.append(s.upper())
        
    # print(', '.join(l)) 



################################################################
#Remove the duplicate from the list of items

    # s=input("Enter the string to put in the list of items")
    # l=[x for x in s.split(' ') ]
    # print(', '.join(sorted(list(set(l)))))


################################################################
#Convert string binary to integer array

    # value=[]
    # item=[x for x in input("Enter the number of items").split(',')]
    # for p in item:
    #     intp=int(p,2)
    #     if not intp%5:
    #         value.append(p)
    # print (','.join(value))      


## Finding the number of elements in range of 2000 to 3000.Make sure each position within the range
# divided by 2

    # Value=[]
    # for i in range(2000,3001):
    #     s=str(i)
    #     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
    #         Value.append(s)

    # print(','.join(Value))


# Count the number of characters and the number of numbers in string

    # s=input("Enter the string: ")

    # count_characters=0

    # count_numbers=0

    # for i in s:
    #     if i.isalpha():
    #         count_characters+=1
    #     elif i.isdigit():
    #         count_numbers+=1
            

    # # Check if the string contains numbers or characters.
    # if count_numbers==0 and count_characters>0:
    #     print("This string only contain characters")
        
    # elif count_characters ==0 and count_numbers>0:
    #     print("This string only contain number")
        
    # else:        
    #     print(f"Number of characters: {count_characters}")

    #     print(f"Number of digits: {count_numbers}")   
    
    #////////////////////////////////////////////////////////////////
    
    # s=input("Enter the string ")
    
    # dic={"Digits":0,"Chars":0}
    
    # for i in s:
    #     if i.isdigit():
    #         dic["Digits"]+=1
    #     elif i.isalpha():
    #         dic["Chars"]+=1
    #     else:
    #         pass
            
    # print("Number of digits",dic["Digits"])
    
    # print("Number of characters",dic["Chars"])
    
    
    # /////// Counting the number of characters upper and lower//////
    
    # s=input("Enter the string ")

    # dic={"Uppers":0,"Lowers":0}

    # s.strip()

    # for i in s:
    #     if i.isupper() :
    #         dic["Uppers"]+=1
    #     elif i.islower():
    #         dic["Lowers"]+=1
    #     else:
    #         pass
            
    # print("Number of characters Upper",dic["Uppers"])

    # print("Number of characters Lower",dic["Lowers"])   
    
    
    
    
##########################  END
#Enter the characters and calculating  them
    # a = input("Nhập số a: ")

    # n1 = int(a)
    # n2 = int( "%s%s" % (a,a) )
    # n3 = int( "%s%s%s" % (a,a,a) )
    # n4 = int( "%s%s%s%s" % (a,a,a,a) )

    # print ("Tổng cần tính là: ",n1+n2+n3+n4)
    
################################################################
# Filter the even digits of array
    # values=[x for x in input("Enter the number : ").split(",")]
    # words=[word for word in values if int(word)%2!=0] 
    # print(",".join(words))
    
################################################################

#Deposit and Withdraw from the bank
    # netAmount = 0
    # transactions = [
    #     "D 100",
    #     "W 50",
    #     "D 200",
    #     "W 75",
    #     "D 150"
    # ]
    # for s in transactions:
    #     values = s.split(" ")
    #     operation = values[0]
    #     amount = int(values[1])
    #     if operation == "D":
    #         netAmount += amount
    #     elif operation == "W":
    #         netAmount -= amount
    # print (netAmount)          
                
                
                
                          

                 
        
        



