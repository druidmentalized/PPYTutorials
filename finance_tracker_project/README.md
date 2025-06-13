# Personal Finance Tracker

A console-based application to manage personal income, expenses, and savings. Built with Python using an object-oriented and modular architecture, it allows users to securely track their finances, view reports, and export summaries.

---

## Features

### Core Functionality
- **Multiple Bank Accounts**: Each with a name, currency, balance, and transaction history.
- **Transaction Management**:
  - Add income and expense transactions.
  - Each transaction stores date, amount, category, and type (+/-).
- **Filtered Transaction Viewing**:
  - Filter by date, type, and category.
- **Bank Account CRUD**:
  - Create, read, update (name and currency), and delete bank accounts.
- **Reporting**:
  - Generate general spending reports over time.
  - Generate category-based spending reports.
- **Data Persistence**:
  - Save and load all user data via JSON.
  - Transaction logging via context managers.

### Reporting & Export
- **Graphical Summaries**:
  - Line charts for temporal spending.
  - Pie or bar charts for category-based summaries.
- **Excel Export**:
  - Export reports as `.xlsx` using `openpyxl`.

### Input Validation & Error Handling
- All inputs are validated (dates, currency, numerical amounts).
- Custom exceptions:
  - `InvalidAmountError`
  - `DuplicateBankError`
  - `InvalidCurrencyError`
  - `BlankDataError`
- Custom warning:
  - `NegativeBalanceWarning`

---

## Project Structure
- `finance_tracker_project/`
    - `controllers/` — UI-level logic and input handling
    - `services/` — Business logic (account, transactions, reports)
    - `models/` — Data models (User, Account, Transaction)
    - `errors/` — Custom exceptions
    - `warnings/` — Custom warnings
    - `enums/` — Enums (e.g., Currency)
    - `repositories/` — Data access and persistence logic
    - `config/` — Configurable constants and color themes
    - `ui/` — Console UI utilities
    - **context.py** — Dependency provider (DI container)
    - **main.py** — Entry point
    - `data/` — User JSON files and report exports

---

## Technologies Used

- **Python 3.12**
- `colorama` – For colored CLI output
- `openpyxl` – For Excel exports
- `matplotlib` – For graphical summaries
- `enum`, `datetime`, `json`, `os`, `warnings`

---

## Getting Started

### Prerequisites
Make sure Python 3.12+ is installed.

### Installation
1. **Install Python** (Pyton 3.12 recommended)

2. **Install dependencies** (from the given `requirements.txt` file):
```bash
    pip install -r requirements.txt
```

3. **Run the application** from the project root:
```bash
    python main.py
```

---

## Example usage
```text
-- Finance Tracker --
1. Login
2. Register
e. Exit
Choose an option: 2.
Invalid choice. Please try again.

-- Finance Tracker --
1. Login
2. Register
e. Exit
Choose an option: 2
Username: Dmitriy
Password: somePassword123
Confirm Password: somePassword123

--- Session Menu ---
1. Enter bank account
2. Create bank account
3. Generate general report
4. Generate general category report
e. Exit session
Choose an option: 1
No bank accounts found. Please create one first.

--- Session Menu ---
1. Enter bank account
2. Create bank account
3. Generate general report
4. Generate general category report
e. Exit session
Choose an option: 2
-- Create New Bank Account --
Bank name: Bank1

Supported currencies: PLN, USD, EUR, RUB, ARS
Currency(abbreviation/sign): USD
Bank account 'Bank1' created successfully.

--- Session Menu ---
1. Enter bank account
2. Create bank account
3. Generate general report
4. Generate general category report
e. Exit session
Choose an option: e
Exiting session...

-- Finance Tracker --
1. Login
2. Register
e. Exit
Choose an option: e
```

---

## License
This project is for educational purposes and may be reused or extended freely.