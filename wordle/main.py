import random #random import is to choose a random word
import re #regex import is to check input for letters


def menu():
#menu text generated with text to ascii art generator at https://patorjk.com/ :)
    print("""
    
                             
█╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ ███████╗
██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗██╔════╝
██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║█████╗  
██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║██╔══╝  
╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝     
==================================================================
    Try to guess the 5 letter word!

    Green blocks signify the correct letter and the correct placment

    Yellow blocks signify the correct letter, but the incorrect placement 

    White blocks signify an incorrect letter
    

    """)

def show_words(array_words,assigned_word):
    for word in array_words:
        listed_block = ""       
        for i,letter in enumerate(word):  #goes through words 
            if letter in assigned_word:
                if word[i] == assigned_word[i]:  #checks if our guessed letter matches the assigned letter
                    block = "🟩"     #if so print green block 
                else:
                    block = "🟨"     #if not print yellow
            else:
                block = "🔲"       #outside of both scenarios has to be white 

            listed_block += block   
        
        print(word.replace("", " ")[1: -1])
        print(listed_block)


if __name__ == "__main__":
    with open('validwords.txt','r+') as f: # read text files 
     possible_words =f.read().splitlines()   

    assigned_word = random.choice(possible_words)  #assign a random word from possible words
    word_length = len(assigned_word)  #get word length to use later
    word_guessed = False   #create word we guess to use for comparison to our assigned word later
    array_words = []
    
    


while word_guessed == False:
    menu()
    
    show_words(array_words,assigned_word) 
    try:
        word = input(f"Hit some word of {word_length} length here:")
        
        if len(word) != word_length:   #checks for length to make sure we have specified letter words 
            raise ValueError(f"it must be {word_length} length word!")  


        elif not re.search(r"[a-zA-Z]{"+str(word_length)+"}",word):  #regex form validation to only match letters
            raise ValueError(f"input must only be letters!") 


        elif word == assigned_word:  #check if the guessed word matches the selected randomized word
            print(word.replace("", " ")[1: -1])
            print("🟩🟩🟩🟩🟩")
            print("""
    
            _  _  _ _____ __   _ __   _ _______  ______   /   /   /
            |  |  |   |   | \  | | \  | |______ |_____/  /   /   / 
            |__|__| __|__ |  \_| |  \_| |______ |    \_ .   .   .  
                                                        
                                                  

                """)
            word_guessed = True
        else:
            array_words.append(word)
            
    except ValueError as e:  # excepting errors makes it so when something goes wrong we can continue
        print(e)
        a = input("please press enter to continue")