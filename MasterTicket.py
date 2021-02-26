TICKET_PRICE = 10 # Variable inits
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(num): # Function to handle ticket cost calculations
    return num * TICKET_PRICE + SERVICE_CHARGE

while tickets_remaining > 0: # While loop will run only when there are tickets remaining
    name = input('What is your name?  ')
    print(f'Hi {name}. There are {tickets_remaining} tickets remaining.')
    try: # Error expected here if user enters a non int input
        tickets_requested = int(input('How many tickets would you like to purchase?  '))
    except ValueError: # Handling of Value Error for non int input
        print('Sorry, that is not a valid number. Please try again.  ')
    else:
        if tickets_requested <= tickets_remaining:
            price_total = calculate_price(tickets_requested) # Price calculation function call
            print(f'You have requested {tickets_requested} tickets which will cost ${price_total} which includes a $2 Service Charge')
            proceed = input('Would you like to proceed Y/N?') # User confirmation request

            if proceed[0].upper() == 'Y': # 1st character upper used to avoid errors
                tickets_remaining = tickets_remaining - tickets_requested
                print(f'Thank you. You purchased {tickets_requested} tickets which will be with you soon!')

            else:
                print('Thank you. Your order has been cancelled.')
        else:
            print(f'Sorry there are only {tickets_remaining} left. Please try again')
else:
    print('''
    ***** Sorry all tickets have been sold *****''')
