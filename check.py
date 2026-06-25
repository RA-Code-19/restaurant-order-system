import report as r
import models as m
import csv
from datetime import datetime
import os

def save_to_file(filename, row, header):
    """Save a row to a CSV file, writing header if file is new."""
    file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        if not file_exists:
            writer.writerow(header)
        writer.writerow(row)

def bill(E_code, selected_items, quantities):
    """Handle order type, calculate total, save to correct file."""
    
    print("\nOrder Type:")
    print("1 - Dine In")
    print("2 - Delivery")
    print("3 - Takeaway")
    
    while True:
        order_choice = input("Select (1/2/3): ").strip()
        if order_choice in ["1", "2", "3"]:
            break
        print("Invalid choice.")

    if order_choice == "1":
        order_type = "dine_in"
        location_info = input("Table number: ").strip()
    elif order_choice == "2":
        order_type = "delivery"
        location_info = input("Delivery address: ").strip()
    else:
        order_type = "takeaway"
        location_info = input("Phone Number of customer: ").strip()

    
    items_str = " - ".join(
        [f"{m.menu[i-1].name} x{q} @ Rs.{m.menu[i-1].price}" 
         for i, q in zip(selected_items, quantities)]
    )
    total = sum(m.menu[i-1].price * q for i, q in zip(selected_items, quantities))

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    
    order_files = {
        "dine_in":  "dine_in_orders.csv",
        "delivery": "delivery_orders.csv",
        "takeaway": "takeaway_orders.csv"
    }
    filename = order_files[order_type]
    header = [f"{'Time':^20}", f"{'Order Type':^20}", f"{'Location':^20}", f"{'Items':^20}", f"{'Total':^20}", f"{'Staff'}"]
    row = [f"{now:^20}", f"{order_type:^20}", f"{location_info:^20}", f"{items_str:^20}", f"{total:^20}", f"{E_code:^20}"]
    save_to_file(filename, row, header)
    
    master_header = [f"{'Time':^20}", f"{'Order Type':^20}", f"{'Total Sale':^20}", f"{'Staff':^20}"]
    master_row = [f"{now:^20}", f"{order_type:^20}", f"{total:^20}", f"{E_code:^20}"]
    save_to_file("master_summary.csv", master_row, master_header)
    
    print("\n========== RECEIPT ==========")
    for i, q in zip(selected_items, quantities):
        item = m.menu[i-1]
        print(f"  {item.name:<25} x{q}  Rs.{item.price * q}")
    print(f"{'':30}----------")
    print(f"  {'TOTAL':<29} Rs.{total}")
    print(f"  Staff: {E_code}")
    print(f"  Time:  {now}")
    print("==============================\n")
    print(f"✅ Order saved to {filename}")


def start():
    
    while True:
        role = input("Are you Cashier or Manager: ").strip().lower()
        if role in ["cashier", "manager"]:
            if role == "manager":
                r.manager_menu()
                return
            break
        print("Please enter 'cashier' or 'manager'.")
        

    E_code = input("Enter your E-code: ").strip()


    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    save_to_file(
        "E_code.csv",
        [f"{E_code:^20}", f"{now:^20}", f"{role.capitalize():^20}"],
        [f"{'E-code':^20}", f"{'Shift Start':^20}", f"{'Designation':^20}"]
    )

    
    while True:
        print("\n1 - Take new order")
        print("2 - Exit")
        choice = input("Select: ").strip()

        if choice == "2":
            print("Goodbye!")
            break

        if choice != "1":
            print("Invalid choice.")
            continue

        
        m.final_show_menu()

        while True:
            try:
                raw = input("\nSelect items by number (comma separated, e.g. 1,3,5): ")
                selected_items = [int(x.strip()) for x in raw.split(",")]
                if all(1 <= i <= len(m.menu) for i in selected_items):
                    break
                print(f"Please enter numbers between 1 and {len(m.menu)}.")
            except ValueError:
                print("Numbers only, separated by commas.")

        
        quantities = []
        for i in selected_items:
            while True:
                try:
                    q = int(input(f"Quantity for {m.menu[i-1].name}: "))
                    if q > 0:
                        quantities.append(q)
                        break
                    print("Quantity must be at least 1.")
                except ValueError:
                    print("Please enter a valid number.")

        
        bill(E_code, selected_items, quantities)

start()

