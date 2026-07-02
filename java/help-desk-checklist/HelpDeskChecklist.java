import java.util.Scanner;

public class HelpDeskChecklist {

public static int getMenuChoice(Scanner scnr) {
    String menuChoice = scnr.next();
    int menuNum;

    try {
        menuNum = Integer.parseInt(menuChoice);
    } catch (NumberFormatException e) {
        System.out.println("Please enter a valid option");
        return -1;
    }
    return menuNum;
}


public static void printChecklist(String scenario){
    if (scenario.equals("Password reset")) {
        System.out.println("Password Reset Checklist\n" + //
                                    "1. Confirm this is a practice request with fake account details only.\n" + //
                                    "2. Verify the user can identify the account they are trying to access.\n" + //
                                    "3. Check whether the account is locked or the password was forgotten.\n" + //
                                    "4. Follow the approved reset steps for the practice scenario.\n" + //
                                    "5. Ask the user to sign in and confirm access.\n" + //
                                    "6. Remind the user to use a strong password.\n" + //
                                    "7. Document the fake resolution note.");
    }
    else if (scenario.equals("Network issue")) {
        System.out.println("Network Issue Checklist\n" + //
                                "1. Confirm whether the issue affects one device or multiple devices.\n" + //
                                "2. Ask whether the user is on Wi-Fi, wired network, or VPN.\n" + //
                                "3. Check if other websites or apps are working.\n" + //
                                "4. Have the user restart the connection or reconnect to the network.\n" + //
                                "5. Check for a generic outage pattern.\n" + //
                                "6. Escalate if the issue affects multiple users or does not improve.\n" + //
                                "7. Document the fake troubleshooting steps.");
    }
    else if (scenario.equals("Printer issue")) {
        System.out.println("Printer Issue Checklist\n" + //
                                "1. Confirm the printer is powered on.\n" + //
                                "2. Check that the printer has paper and no visible error message.\n" + //
                                "3. Confirm the user selected the correct printer.\n" + //
                                "4. Check whether the print job is stuck in the queue.\n" + //
                                "5. Ask the user to try a small test print.\n" + //
                                "6. Escalate if the printer still does not respond.\n" + //
                                "7. Document the fake resolution note.");
    }
}

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);

        System.out.println("Thank you for using the HelpDeskChecklist app");

        System.out.println("Please select which checklist you would like to see");

        while (true) {

            System.out.println("1. Password reset, 2. Network Issue, 3. Printer Issue");
            System.out.println("Enter 4 to exit.");

            String[] scenarios = {"Password reset", "Network issue", "Printer issue"};


            int numSelection = getMenuChoice(scnr);

            if (numSelection == 1){

                int index = numSelection - 1;

                System.out.println(scenarios[index]);

                printChecklist(scenarios[index]);


            }
            else if (numSelection == 2) {
            int index = numSelection - 1;

            System.out.println(scenarios[index]);

            printChecklist(scenarios[index]);

            }
            else if (numSelection == 3) {
            int index = numSelection - 1;

            System.out.println(scenarios[index]);

            printChecklist(scenarios[index]);

            }
            else if (numSelection == 4) {
                System.out.println("Thank you for using our app!");
                break;
            }
            else{
                System.out.println("Please enter a valid option");
                continue;
            }
        }
    }
}
