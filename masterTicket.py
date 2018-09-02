import math
TicketPrice = 10

TicketsRemain =100

KCst = .09

sCharge = float(2.00)

def iPrice(tRequest):
	return tRequest*TicketPrice

while TicketsRemain  >=1:
		
	#print("There are {} tickets left.".format(TicketsRemain))
	cust= input("Customer name: ")
	tRequest = input("Hello, {}, how many tickets would you like to purchase today?".format(cust))
	try:
		tRequest = int(tRequest)
		if tRequest > TicketsRemain:
			raise ValueError("Sorry, We only got {} left. We thought about printing more on Spam, but we don't think it will taste very good.".format(TicketsRemain))
	except ValueError as err:
		print(" {} please try your request again.".format(err))
	else:
		ticketTotal =iPrice(tRequest)
		ticketTax = ticketTotal * KCst
		ticketWtax = ticketTotal + ticketTax
		endCharge = ticketWtax + sCharge
		print("Your total amount comes to {}. Plus a {} dollar service charge".format(ticketWtax,sCharge))
		finalizePurchase = input("would you like to purchase {} tickets for a total of {} ? (y/n)" .format(tRequest,endCharge))
		if finalizePurchase.lower() == "y":
			print("Thank you, {} , for your purchase".format(cust))
			TicketsRemain -= tRequest
		else:
			print("Perhaps another time")

	
		print("There are {} tickets remaining" .format(TicketsRemain))

print("Sorry, the event has sold out.")
