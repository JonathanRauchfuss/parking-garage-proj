class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.total_tickets = total_tickets
        self.total_parking_spaces = total_parking_spaces
        self.available_tickets = total_tickets
        self.available_parking_spaces = total_parking_spaces
        self.current_ticket = {}

    def takeTicket(self):
        if self.available_tickets > 0 and self.available_parking_spaces > 0:
            self.available_tickets -= 1
            self.available_parking_spaces -= 1
            self.current_ticket = {"ticket_number": self.total_tickets - self.available_tickets, "paid": False}
            print(f"Ticket {self.current_ticket['ticket_number']} issued. Please pay for parking on the way out.")

    def payForParking(self):
        if self.current_ticket.get("ticket_number") is not None:
            amount_paid = input("Enter the amount to pay for parking: ")
            if amount_paid:
                print("Ticket has been paid. You have 15 minutes to leave.")
                self.current_ticket["paid"] = True
            else:
                print("Payment not received. Please pay to exit.")

    def leaveGarage(self):
        if self.current_ticket.get("paid"):
            print("Thank you, have a nice day!")
            self.available_parking_spaces += 1
            self.available_tickets += 1
        else:
            self.payForParking()
            print("Thank you, have a nice day!")





jonGarage= ParkingGarage(75,75)

def Run():
    while True:
        Response=input("do you want to: 'enter' 'leave' or 'quit?'")

        if Response=="enter":
            jonGarage.takeTicket()
            
        elif Response=="leave":
            jonGarage.payForParking()
            jonGarage.leaveGarage()
            
        
        elif Response=="quit":
            break
        else:
            print(" type 'take ticket','pay','leave' or 'quit'")

Run()
        

        





