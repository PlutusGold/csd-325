#Dario Gomez Assignment 4.2
import csv, sys

from datetime import datetime

from matplotlib import pyplot as plt

def main():
    filename = 'sitka_weather_2018_simple.csv' #set filename to file
    while True:
        try:
            print(f'Welcome to Sitka Weather App\n' #menu
            '1. See Highs\n' 
            '2. See Lows\n'
            '3. Exit' )
            choice = int(input('Enter your choice: ')) #get choice
            if choice == 1: #plot highs
                dates, highs = readData(filename, 5) #read csv and create lists for dates and highs in column 5
                plot(dates, highs, 'Daily high temperatures - 2018', 'red') #create chart and show plot. Pass title and color as arguments
            elif choice == 2: #plot lows
                dates, lows = readData(filename, 6) #read csv and create lists for dates and highs in column 6
                plot(dates, lows, 'Daily low temperatures - 2018', 'blue') #create chart and show plot. Pass title and color as arguments
            elif choice == 3: #quit program
                print('Thank you for using the Stika Weather App\nGoodbye')
                sys.exit()
        except ValueError:
            print('Please enter a valid number from menu.')

def readData(filename, temperature_column): #function to read dates and temps
    dates, temperatures = [], [] #create empty lists
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader) #skip header
        for row in reader: #get dates and temps per row
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date) #add date to date list
            temp = int(row[temperature_column])
            temperatures.append(temp) #add temp to temperatures list
        return dates, temperatures #return dates, and temperatures to main

def plot(dates, temperatures, title, color): #show graph function
    fig, ax = plt.subplots() #create plot
    ax.plot(dates, temperatures, c=color)

    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show() #display plot

if __name__ == '__main__':
    main()