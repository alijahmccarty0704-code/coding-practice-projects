import java.util.Scanner;

public class DeviceInventoryChecker {
    public static int menu(Scanner scnr){
        String menu_option = scnr.next();
        int menu_num;

        try {
            menu_num = Integer.parseInt(menu_option);
        } catch (NumberFormatException e) {
            return -1;
        }
        return menu_num;
    }

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);

        String[] inventory = {"1.Laptop Inventory: ", "2.Desktop Inventory: ", "3.VM Inventory: ", "4.Exit: "};
        String[] inventoryStatus = {"Laptops: 80", "Desktops: 100", "VM: 200"};

        System.out.println("What device would you like to see inventory for?");

        boolean menuLoop = true;

        int index;

        while (menuLoop == true) {
            for(int i = 0; i < inventory.length; ++i ){
                System.out.println(inventory[i]);
            }

            int menu_selection = menu(scnr);

            if (menu_selection >= 1 && menu_selection <= inventoryStatus.length) {
                index = menu_selection - 1;
                System.out.println(inventoryStatus[index]);
            }
            else if (menu_selection == 4) {
                System.out.println("Goodbye thank you for using our app!");
                menuLoop = false;
            }
            else{
                System.out.println("Invalid option");
            }

        }


        scnr.close();
    }
}
