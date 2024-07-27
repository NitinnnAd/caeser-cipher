x=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
list =[]

def encrypt(text,shift):
        newt =''   
        for j in text:
            if j.isalpha():
                v = x.index(j) +shift
                if v>= 26:
                    newt+=x[v-26]
                else:
                    newt+=x[v]
            else:
                newt+=j        

        return newt

def decrypt(text,shift):
        nst=''
        for i in text:
            if i.isalpha():   
                if x.index(i)<shift:
                    nst+= x[x.index(i) + 26 - shift]
                else:
                    nst+=x[x.index(i) - shift]
            else:
                nst+=i
        return nst


while True:
    arg=input("type 'encrypt' or 'decrypt' or 'stop':")
    if arg == "encrypt":
        text =input("enter the message :")
        shift =int(input("enter the shift number :"))
        encrypted_message= encrypt(text,shift)
        print("the encrypted message is: ",encrypted_message)
        list.append(encrypted_message) 
    
    elif arg == 'decrypt':
        if len(list)==0:
            print("no message to be decrypted")
        else:
            print(list)
            input_index = int(input("enter the index number of the message to decrypt it: "))
            shift =int(input("enter the shift number :"))
            decrypted_message= decrypt(list[input_index-1],shift) 
            print('the decrypted message is :',decrypted_message)   
    
    elif arg == 'stop':
        print("thank you")
        break

    else:
        print('invalid action')    
        
