are_you_done = "no" 
want_to_change = "no"  
name_on_dokument = input ("Name you dokument: ")
skip_two_rows = "\n"
while are_you_done == "no":  

    while want_to_change == "no":  
        

        pick_letter = input("write the letter you want: ")
        print (pick_letter) 
        
        with open("/Abbe/.vscode-insiders/python_programs/enkryptering/test_txt_files"+name_on_dokument+".txt", "w+") as file:
            file.write(pick_letter)
         
        pick_letter = input ("Now encryt it with wath you want: ")
        print (pick_letter) 
        
        with open("/home/Abbe/python_programs/enkryptering/test_txt_files/"+name_on_dokument+".txt", "r+") as file:
            file = file.read ()
            newfile= file + "\n" +pick_letter

        with open("/home/Abbe/python_programs/enkryptering/test_txt_files/"+name_on_dokument+".txt", "w+") as file:
            file.write(newfile)

        if pick_letter == "":
            print ("you forgot to write something")
            want_to_change = "no"
    
        want_to_change = input ("want to change? yes or no: ")

        if want_to_change == "yes":
            print ("sad")
    
        are_you_done = input ("Are you done? yes or no? ")
    want_to_change = input ("do you want to stop?: yes or no ")

if are_you_done == "yes":
    print ("klar")