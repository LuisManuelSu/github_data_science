# Function to generate a "to do" list with the option of add new items, mark as complete and view the list

def to_do_list():
    print('Welcome to the "To do List" App.')
    to_do = [] # Initialization of the List of activities
    completed = [] # Initialization of the List of completed activities
    while True:
        # Try/Exception block to limit the answer from the user to the wished action (1), (2), (3) or (4)
        try:
            # The answer should be an integer
            user = int(input('What do you want to do: \n(1) Add an Activity \n(2) Mark as Completed \n(3) View the list \n(4) Exit \n>>> '))
        except Exception:
            print('Invalid input. Please select 1, 2, 3, or 4')
            continue
        if user != 1 and user != 2 and user != 3 and user != 4:
                print('Invalid input. Please add 1, 2, 3, or 4')
        # Block for add a new activity (1)
        elif user == 1:
            activity = input('Add a new Activity: \n>>>')
            to_do.append(activity)
            print('Activity added: "{}"'.format(activity))
        # Block for mark an activity as completed (2)
        elif user == 2:
            print('Select the activity you have completed:')
            for num in range(len(to_do)):
                print('{} - {}'.format(num, to_do[num]))
            while True:
                comp = input('>>> ')
                try:
                    comp = int(comp)
                except Exception:
                    if comp == 'none': break
                    else:
                        print('Invalid input. Please select the number of the activity')
                        print('If you do not want to mark an activity as completed type "none"')
                        continue
                if comp in range(len(to_do)):
                    print('Activity completed: "{}"'.format(to_do[comp]))   
                    completed.append(to_do[comp])
                    to_do.remove(to_do[comp])
                    break
                else:
                    print('The activity is not in the list')
        # Block for view the lists of activities and completed activities (3)
        elif user == 3:
            if len(to_do) > 0:
                print('\nTo do List: ')
                for act in to_do:
                    print('- {}'.format(act))
            if len(completed) > 0:
                print('\nCompleted Activities: ')
                for act in completed:
                    print('- {} - Completed'.format(act))
            print('')
        # Block for exit the function (4)
        else:
            print('Thanks, back soon!!!')
            break
    return to_do

to_do_list()