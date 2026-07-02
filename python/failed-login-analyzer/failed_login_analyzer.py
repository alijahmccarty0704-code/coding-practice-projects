# Build this from scratch using the README checklist.
def print_menu(menu):
    if menu.isdigit():
        menu_num = int(menu)
        return menu_num




def main():
    failed_login_list = []

    while True:
        print("Select which option would you would like to see\n1.Add failed login, 2.View failed logins, 3.Count failures for username, 4.Show high risk usernames, 5.Exit")

        menu_choice = input()

        menu_selection = print_menu(menu_choice)

        if menu_selection == 1:
            print("Enter the failed login")

            failed_login_username = input("Username: ")
            failed_login_IP = input("IP: ")
            failed_login_reason = input("Reason: ")

            record = [failed_login_username, failed_login_IP , failed_login_reason]

            failed_login_list.append(record)
            continue

        elif menu_selection == 2:
             if not failed_login_list:
                 print("No failed login to list")
                 continue
             else:
                for record in failed_login_list:
                    print("Username:", record[0])
                    print("IP: ", record[1])
                    print("Reason:", record[2])

        elif menu_selection == 3:
            target_username = input("Enter the username you would like to view the logs for: ")
            target_count = 0

            for record in failed_login_list:
                if target_username == record[0]:
                    target_count = target_count + 1

            print(target_username, target_count)

        elif menu_selection == 4:
            high_risk_usernames = []
            target_count = 0

            for record in failed_login_list:
                current_username = record[0]
                target_count = 0

                for check_record in failed_login_list:
                    if check_record[0] == current_username:
                        target_count = target_count + 1

                if target_count >= 3:
                    if current_username not in high_risk_usernames:
                        high_risk_usernames.append(current_username)
            if high_risk_usernames == []:
                print("No high risk users.")
            else:
                print("High Risk: ")
                print(high_risk_usernames)
        elif menu_selection == 5:
            break
        else:
            print("Please select a valid option")
            continue








if __name__ == "__main__":
    main()