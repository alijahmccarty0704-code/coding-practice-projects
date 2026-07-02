def get_password_request(yes_or_no):

    if yes_or_no.isdigit():
        yes_or_no = int(yes_or_no)
        return yes_or_no


def mark_as_complete(user_input):
    if user_input.isdigit():
        user_input = int(user_input)
        return user_input


def main():

    request_list = []
    while True:
        print("Please select an option\n1.Add request\n2.View pending requests\n3.Mark as complete\n4.Exit")

        password_reset_selection = input()


        menu_selection = get_password_request(password_reset_selection)




        if menu_selection == 1:
                adding_requests = True

                while adding_requests:
                    new_ticket = input("Please label your ticket and give a business justification: ")

                    request_list.append(new_ticket)

                    while True:
                        print("Would you like to enter another ticket? Enter 1 for yes or 2 for no")

                        extra_ticket_input = input()

                        extra_ticket = get_password_request(extra_ticket_input)

                        if extra_ticket == 1:
                            continue
                        elif extra_ticket == 2:
                            adding_requests = False
                            break
                        else:
                            print("Please enter a valid option")
                            continue



        elif menu_selection == 2:
            request_num = 1
            print("Pending Request:\n")

            if len(request_list) == 0:
                print("No pending requests")
            else:
                for request in request_list:
                    print(request_num, request )
                    print()
                    request_num = request_num + 1

        elif menu_selection == 3:
            request_num = 1
            for request in request_list:
                print(request_num, request )
                print()
                request_num = request_num + 1

            print("Which request would you like to mark as complete?")

            markup = input()

            markup_select = mark_as_complete(markup)

            if markup_select is None:
                print("Please select a valid option")
            else:
                index = markup_select - 1

                if index < 0 or index >= len(request_list):
                    print("No request found")
                else:
                    complete_request = request_list[index]

                    request_list.remove(complete_request)

                    print("Marked complete: ", complete_request)

        elif menu_selection == 4:
            print("Thank you for using our app! Goodbye.")
            break

        else:
            print("Please select a valid option")
            continue









if __name__ == "__main__":
    main()