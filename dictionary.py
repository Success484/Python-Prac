scheme_by_subject = {}
while True:
        scheme_input = int(input('Enter your Choice:\n 1: create Scheme\n 2: Exit\nchoose: '))
        if scheme_input ==  1:
            subject = str(input('Name of subject : '))
            details = str(input('Enter of subject details : '))
            scheme =  {'subject': subject, 'details': details}
            

            if subject not in scheme_by_subject:
                scheme_by_subject[subject] = []

            scheme_by_subject[subject].append(scheme)
            print("\nCurrent Schemes Grouped by Subject:")
            print(scheme_by_subject)
    
        elif scheme_input == 2:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter 1 or 2.")