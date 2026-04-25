 while True:
            #get the users input and store to a variable
            choice = input('Please input your guess:')
            if choice in choices:
                chosen_decision = random.choice(choices)

                if(choice == location_smallship):
                    print(f"You:{choice}     Computer: {location_smallship}         small ship hit!")
                if(choice == location_largeship):
                    print(f"You:{choice}     Computer: {location_largeship}         large ship hit!")
                
                elif(choice == empty_space):
                    print(f"You: {choice}     Computer: {empty_space}       Miss!")
            if choice not in choices:
                print(f"not a valid input")
                
