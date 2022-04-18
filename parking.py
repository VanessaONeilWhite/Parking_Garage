#ParkingGarage
#class of parking garage
class Garage(): 
    def __init__(self):
        self.spaces_alloted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.tickets_taken = []

    def take_ticket(self):
        if not self.spaces_alloted:
            print("There are no available spaces, please try again later.")
        else: 
            self.tickets_taken.append(+1)
            self.spaces_alloted.pop(0)
            print(f"Your space is: {self.spaces_alloted[0]}") 

    def pay_ticket(self):
        response = input("Please enter your ticket number: ")
        if int(response) in self.tickets_taken:
            self.tickets_taken.remove(response) 
        if int(response) not in self.spaces_alloted: 
            self.spaces_alloted.append(response)
            print("Thank you, come again")
        else:
            print("This is not a valid ticket number, please try again.")

    
    def leave_garage(self):
        response = input("Please enter your ticket number: ")
        if int(response) in self.tickets_taken:
            print("Please pay your ticket")
            self.pay_ticket()
        elif int(response) not in self.tickets_taken: 
            print("Thank you, your ticket has been paid, you have 15 minutes to exit Vanessa's Garage") 


class UI():
    def __init__(self):
        self.parking_garage = Garage() 
    
        while True:
            response = input("Please choose a selection: Park, pay, or exit? ")
            if response.lower() == "park":
                self.parking_garage.take_ticket()
            elif response.lower() == "pay":
                self.parking_garage.pay_ticket()
            elif response.lower() == "exit":
                self.parking_garage.leave_garage()
        

def main():
    ui = UI()
    ui.open_garage()

if __name__=="__main__":
    main()

open_garage()

#a list of tickets 
#pay function 
# leave function 
# take tickets 
