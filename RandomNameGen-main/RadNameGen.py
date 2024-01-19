import colorama
from colorama.ansi import Fore 
import time
from datetime import datetime
import names
import logging
from os import system 
import os 


colorama.init()

now = datetime.now()


path = f'output\\output.txt'


def update():
        
        os.popen(f"title GENERATOR  │  Success :  {loop}  │ File : {path}" )

def first():
        

        logging.basicConfig(filename=path,format='%(message)s')

        first_rand_name = names.get_first_name()

        print(f'{Fore.YELLOW}[{datetime.now()}] - Generating First Name - '+first_rand_name)
        logging.warning(first_rand_name)
        print(f'{Fore.GREEN}[{datetime.now()}] - First Name Successfully Generated !!!')
        global loop
        loop +=1
        update()


def last():

        

        logging.basicConfig(filename=path,format='%(message)s')

        last_rand_name = names.get_last_name()

        print(f'{Fore.YELLOW}[{datetime.now()}] - Generating Last Name - '+last_rand_name)
        logging.warning(last_rand_name)
        print(f'{Fore.GREEN}[{datetime.now()}] - Last Name Successfully Generated !!!')
        global loop
        loop +=1
        update()


def full():
        

        logging.basicConfig(filename=path,format='%(message)s')

        full_rand_name = names.get_full_name()

        print(f'{Fore.YELLOW}[{datetime.now()}] - Generating Last Name - '+full_rand_name)
        logging.warning(full_rand_name)
        print(f'{Fore.GREEN}[{datetime.now()}] - Last Name Successfully Generated !!!')
        global loop
        loop +=1
        update()



def tar():
       global loop,target
       loop = 0
       var = input("\nTarget Number : ")   
       target = int(var)  



def main():
        print(f'{Fore.YELLOW}-----------------------------------------------------------------------------------------------------------------')

        print(f'{Fore.GREEN} WELCOME BACK !!!   ')
        print(f'{Fore.YELLOW}-----------------------------------------------------------------------------------------------------------------')

        print("-----------------------------------------------------------------------------------------------------------------")

        print("-----------------------------------------------------------------------------------------------------------------")

        print("-----------------------------------------------------------------------------------------------------------------") 
        system("title " + "Random Name Generator  "   )

        print(f"{Fore.CYAN}1. FIRST NAME GENERATOR")
        
        print("2. LAST NAME GENERATOR")

        print("3. FULL NAME GENERATOR")


        print("4. EXIT")
        print(f"{Fore.WHITE}")

        b=input("\nEnter the number of your choice -> ")
        if b=="1":
               tar()
               first()
               while loop < target:
                      first()

               print(f'{Fore.RED}[{datetime.now()}] - Target Number Reached !!!')
               time.sleep(3)
               os.system('cls')
               main()
        
        



        if b=="2":
               tar()
               last()
               while loop < target:
                      last()

               print(f'{Fore.RED}[{datetime.now()}] - Target Number Reached !!!')
               time.sleep(3)
               os.system('cls')
               main()

           
         

        if b=="3":
               tar()
               full()
               while loop < target:
                      full()

               print(f'{Fore.RED}[{datetime.now()}] - Target Number Reached !!!')
               time.sleep(3)
               os.system('cls')
               main()
        
        if b=="4":
           print(f"{Fore.MAGENTA}Closing Generator in 5 seconds...")
           time.sleep(5)
           quit()
        

  
        else:
           print(f'{Fore.RED}Error Input !!!')
           time.sleep(3)
           os.system('cls')
           main()
        
        







main()



























