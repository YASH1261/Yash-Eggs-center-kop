from datetime import datetime

class EggBill:
    def __init__(self, customer_name, tray_qty, rate_per_egg, payment_mode):
        self.shop_name = "YASH EGGS CENTER"
        self.address = "Gandhinagar, Kopargaon"
        self.contact = "9011959159"
        self.owner = "Mr. Chandrakant Jadhav"
        self.product = "White Eggs (Wholesale)"
        self.eggs_per_tray = 30
        self.tray_qty = tray_qty
        self.total_eggs = self.tray_qty * self.eggs_per_tray
        self.rate_per_egg = rate_per_egg
        self.total_amount = round(self.total_eggs * self.rate_per_egg, 2)
        self.customer_name = customer_name
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M")
        self.bill_no = f"YEC-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.payment_mode = payment_mode

    def generate_bill(self):
        bill = f"""
        ==================================================
                       {self.shop_name}
                  {self.address}
              Contact: {self.contact}
              Owner: {self.owner}
        ==================================================
        Bill No        : {self.bill_no}
        Date & Time    : {self.date}
        Customer Name  : {self.customer_name}
        Payment Mode   : {self.payment_mode}

        Product        : {self.product}
        Quantity       : {self.tray_qty} Trays
        Eggs per Tray  : {self.eggs_per_tray} eggs
        Total Eggs     : {self.total_eggs} eggs
        Rate per Egg   : ₹{self.rate_per_egg:.2f}
        --------------------------------------------------
        Total Amount   : ₹{self.total_amount:.2f}
        ==================================================
               Thank you for shopping with us!
        ==================================================
        """
        return bill

    def save_bill_to_file(self):
        file_name = f"Bill_{self.customer_name}_{self.date.replace(':', '-').replace(' ', '_')}.txt"
        with open(file_name, "w") as file:
            file.write(self.generate_bill())
        print(f"Bill saved to {file_name}")

# --- Run this code ---
if __name__ == "__main__":
    customer_name = input("Enter customer name: ")
    trays = int(input("Enter number of trays: "))
    rate = float(input("Enter wholesale rate per egg: "))
    payment_mode = input("Enter payment mode (Cash/UPI): ")

    bill = EggBill(customer_name, trays, rate, payment_mode)
    print(bill.generate_bill())
    bill.save_bill_to_file()
