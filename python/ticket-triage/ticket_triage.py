


def categorize_ticket(ticket_text):
    ticket_info = ticket_text.lower()
    if "password" in ticket_info or "login" in ticket_info or "reset" in ticket_info or "locked" in ticket_info:
        return "password"
    elif "wifi" in ticket_info or "vpn" in ticket_info or "internet" in ticket_info or "connection" in ticket_info:
        return "network"
    elif "laptop" in ticket_info or "keyboard" in ticket_info or "monitor" in ticket_info or "printer" in ticket_info:
        return "hardware"
    elif "app" in ticket_info or "install" in ticket_info or "update" in ticket_info or "error" in ticket_info:
        return "software"
    elif "back" in ticket_info:
        return "back"
    else:
        return "general"


def main():
    print("Welcome to the ticket triage app.\n")

    while True:

        menu_selection = input("If you would like to see the category guide press 1\nIf you would like to enter your ticket info press 2\nIf you would like to exit the app press 3.\n")

        if menu_selection.lower() == "back":
            break
        elif menu_selection.isdigit():
            menu_selection = int(menu_selection)
        else:
            print("Please select a valid option.")
            continue

        if menu_selection == 1:
                print("Password: password, login, reset, locked\n")
                print("Network: wifi, internet, vpn, connection\n")
                print("Hardware: laptop, keyboard, monitor, printer\n")
                print("Software: app, install, update, error\n")
                print("General: anything unclear\n")
                continue
        elif menu_selection == 2:

                print("Enter back to exit to main menu\n")
                ticket_info = input("Please enter your ticket info: ")
                ticket_details = categorize_ticket(ticket_info)
                print(ticket_details)
                continue

        elif menu_selection == 3:
            print("Thank you for using our app!")
            break
        else:
            print("Please select a valid option")
            continue



















if __name__ == "__main__":
    main()
