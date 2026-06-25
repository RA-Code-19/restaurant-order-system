import csv
import os

MANAGER_PASSWORD = "manager123"

def view_orders(filename, title):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print(f"No {title} orders found.")
        return

    print(f"\n========== {title.upper()} ==========")
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter="|")
        for n, row in enumerate(reader):
            if n == 0:
                print(" | ".join(row))
                print("-" * 60)
            else:
                print(" | ".join(row))
    print("=" * 60)

def sales_summary():
    filename = "master_summary.csv"
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("No sales data found.")
        return

    totals = []
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter="|")
        next(reader)
        for row in reader:
            try:
                totals.append(float(row[2]))
            except (ValueError, IndexError):
                continue

    if not totals:
        print("No completed orders yet.")
        return

    total_sales = sum(totals)
    average = total_sales / len(totals)
    print(f"\n========== SALES SUMMARY ==========")
    print(f"  Total Orders  : {len(totals)}")
    print(f"  Total Sales   : Rs.{total_sales:,.2f}")
    print(f"  Average Order : Rs.{average:,.2f}")
    print(f"====================================\n")

def view_staff_log():
    filename = "E_code.csv"
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("No staff data found.")
        return

    print(f"\n========== STAFF LOG ==========")
    with open(filename, "r") as f:        
        reader = csv.reader(f, delimiter="|")
        for n, row in enumerate(reader):
            if n == 0:
                print(" | ".join(row))
                print("-" * 40)
            else:
                print(" | ".join(row))
    print("=" * 40)

def manager_menu():
    
    while True:
        q = input("Enter the password: ")
        if q == MANAGER_PASSWORD:
            break
        print("Wrong password. Try again.")

    
    while True:
        print("\n========== MANAGER REPORTS ==========")
        print("1 - Dine In orders")
        print("2 - Delivery orders")
        print("3 - Takeaway orders")
        print("4 - Sales summary")
        print("5 - Staff log")
        print("6 - Exit")

        q2 = input("Select (1-6): ").strip()

        if q2 == "1":
            view_orders("dine_in_orders.csv", "Dine In")
        elif q2 == "2":
            view_orders("delivery_orders.csv", "Delivery")
        elif q2 == "3":
            view_orders("takeaway_orders.csv", "Takeaway")
        elif q2 == "4":
            sales_summary()
        elif q2 == "5":
            view_staff_log()
        elif q2 == "6":
            print("Goodbye!")
            break
        else:
            print("Please choose from 1-6.")