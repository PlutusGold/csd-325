#Dario Gomez CSD 325 Assignment 1.3
#99 bottles of beer on the wall program


def main(): #create main function
    bottle_count = get_bottle_count() #call get bottle count and set = bottle count variable
    run_song(bottle_count) #call run sonf and pass bottle count as arguement
    print('Time to buy more bottles beer') #print once song has ended

def run_song(bottle_count): #defin run song function
    for x in range(bottle_count): # for loop to iterate through each bottle of beer
            print(f'{bottle_count} bottles of beer on the wall, {bottle_count} bottles of beer.')
            bottle_count -= 1 # subtract 1 bottle
            print(f'Take one down and pass it around, {bottle_count} bottles of beer on the wall.')


def get_bottle_count(): #create get bottle count function with validation
    while True:
        try:
            bottle_count = int(input("How many bottles of beer on the wall? "))
            if bottle_count < 0: #must be positive
                print("Please enter a positive bottle amount")
            elif bottle_count == 0: #must have at least one
                print("Please enter at least one bottle")
            else:
                return bottle_count #pass bottle count to main
        except ValueError:
            print("Invalid input. Please enter a whole number")

main()