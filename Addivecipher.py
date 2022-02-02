#Additive cipher 
#formulas for Encryption :
#ciphertext=(plain text+key)mod26
#decryption p=(c+k)mod26



# messge=input("Enter you message: ")
# if(messge.isalpha()):
#     print(messge.upper())
#     messge=messge.upper()
#     print(messge)
# else:
#     print("Error ,message has an alphabet charactter") 

msg="The jay pig fox zebra and my wolves quack"   
    
key=input("ENter the key for additive cipher in Z26 :")
key=int(key)

if key>26:
    key=key%26

cipher=""
for i in msg:
    j=ord(i) - 65
    c=(j+key)%26
    cipher=cipher+ chr(c+65)
    #here to print (chr(c+65))
print("cipher:",cipher)    

    

