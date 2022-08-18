# This program was written to count using the Superduper counter.
from datetime import datetime

def intro():
    print("Hello.\n Welcome to the... \n (drumroll please!) \n ***drumroll*** \n Superduper counter!")
def main():
    intro()
    while True:
        try:
            print("Enter the number you want the Superduper counter to count to to below:")
            num_count = int(input())
            print("Enter the number you want the Superduper counter to count by below:")
            num_step = int(input())
            today = datetime.now()
            print("Day: ", today.day)
            print("Month: ", today.month)
            print("Year: ", today.year)
            print("Hour: ", today.hour)
            print("Minute: ", today.minute)
            print("Second: ", today.second)
            for i in range(0,num_count+1,num_step):
                print(i)
            today = datetime.now()
            print("Day: ", today.day)
            print("Month: ", today.month)
            print("Year: ", today.year)
            print("Hour: ", today.hour)
            print("Minute: ", today.minute)
            print("Second: ", today.second)
        except:
            print("Exception!")
main()