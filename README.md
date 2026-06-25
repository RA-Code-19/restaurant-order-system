# Restaurant Order System 🍕

A multi-file Python POS (Point of Sale) system for restaurant management.

## Features
- Cashier interface — take dine-in, delivery, and takeaway orders
- Manager interface — password protected with full reporting
- Live sales tracking across 4 CSV files
- Receipt generation with itemized billing
- Staff login logging with timestamps

## Project Structure
- `models.py` — MenuItem class and full restaurant menu data
- `check.py` — Cashier interface (orders, billing, file saving)
- `report.py` — Manager reports (sales summary, order history, staff log)

## Built With
Python — OOP, File Handling, CSV, Error Handling, Modules, DateTime

## How to Run
1. Run `check.py` to start the cashier/manager interface
2. Login as cashier to take orders
3. Login as manager with password to view reports
