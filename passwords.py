print('''
 ▄         ▄                     ▄         ▄                  
▐░▌       ▐░▌   █████╗ ██╗  ██╗ ▐░▌       ▐░▌   █████╗                           
▐░▌       ▐░▌  ██╔══██╗██║  ██║ ▐░▌       ▐░▌  ██╔══██╗                          
▐░▌       ▐░▌  ███████║███████║ ▐░▌       ▐░▌  ███████║                       
▐░█▄▄▄▄▄▄▄█░▌  ██╔══██║██╔══██║ ▐░█▄▄▄▄▄▄▄█░▌  ██╔══██║                             
▐░░░░░░░░░░░▌  ██║  ██║██║  ██║ ▐░░░░░░░░░░░▌  ██║  ██║                    
 ▀▀▀▀█░█▀▀▀▀   ╚═╝  ╚═╝╚═╝  ╚═╝  ▀▀▀▀█░█▀▀▀▀   ╚═╝  ╚═╝
     ▐░▌                             ▐░▌   
     ▐░▌                             ▐░▌                    
     ▐░▌                             ▐░▌             
      ▀                               ▀  x.ALSHAMSI.x

__
                            Hacking Password Genertaor For BruteForce
                            
                
---------------------------------------

++ The developer : Yahya Alshamsi (F5R Oman)

instagram : 94alshamsi94

-----------------------------------



''')



list=[]
names=[]
temp_names=[]
phoneNo=''
dob=input("يوم مولدك(سنه-شهر-يوم):")
if(len(dob)==8):
    day=dob[:2]
    month=dob[2:4]
    year=dob[4:]
else:
    print("Wrong format for DOB, make sure it is 8 numbers in DDMMYYYY")
    exit()

phoneNo=input("رقم هاتف الضحيه:")

def ListOfImportantWords():
    names.append(input("اسمك:"))
    names.append(input("قبيله:"))
    names.append(input("كرر اول حرف من اسم الضحيه بوضع الكبيتل:"))
    print("\n")
    names.append(input("كرر اول حرف من حروف الضحيه ثلاث مرات :"))
    names.append(input("كرر اول حرف من حروف الضحيه اربع مرات:"))
    print("Enter all other keywords: ")
    while True:
        inp = input()
        if inp == '':
            break
        names.append(inp)
    while('' in names) : 
        names.remove('') 

def permute(inp): 
    n = len(inp) 
   
    mx = 1 << n 
   
    inp = inp.lower() 
      
    for i in range(mx): 
        combination = [k for k in inp] 
        for j in range(n): 
            if (((i >> j) & 1) == 1): 
                combination[j] = inp[j].upper() 
   
        temp = "" 
        for i in combination: 
            temp += i 
        temp_names.append(temp) 



def WordListCreator(list):
    for word in names:
        for i in range(0,len(word)+1):
            list.append(word[:i]+day+word[i:])
            list.append(word[:i]+month+word[i:])
            list.append(word[:i]+year+word[i:])
            if len(year)==4:
                list.append(word[:i]+year[2:]+word[i:])
            list.append(word[:i]+phoneNo+word[i:])
    if not phoneNo=='':
        list.append(phoneNo)

def WriteToFile(list):
    with open('wordlist.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)



ListOfImportantWords()
for i in names:
    permute(i)       
names=names+temp_names
WordListCreator(list)
WriteToFile(list)
