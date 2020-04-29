from car_function import *

#I have test my program on picking wrong menu number it can not proceed if you select
#wrong number, it will take you back

main()   #calling main function

y = True #asigning true to y
while y == y:  #creating endless loop
    #prompting user to select Yes to continue or No to exit
    y = input("If you want to CONTINUE enter Y and if  you want to EXIT enter N : ")
    if y.casefold() == "Y".casefold(): #checking if user choose yes
        main()                          #calling main function
    elif y.casefold() == 'N'.casefold(): #checking if user choose no
        exit_this()                      #calling function to teriminate program
    else:
        #text to display if user doesn't choose any
        print("You did not choose any ")
        exit()          #clos program