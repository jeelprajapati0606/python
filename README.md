# 💰 Bill Splitter App - JEEL

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)](#license)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge\&logo=github)](https://github.com/jeelprajapati0606/python)

A simple yet powerful Python application to split bills among friends, colleagues, or group members with automatic tip calculation.

---

## 📋 Table of Contents

* [Features](#features)
* [How It Works](#how-it-works)
* [Formulas](#formulas)
* [Installation](#installation)
* [Usage](#usage)
* [Code Breakdown](#code-breakdown)
* [Input Validation](#input-validation)
* [Example](#example)

---

## ✨ Features

| Feature                      | Description                                                             |
| ---------------------------- | ----------------------------------------------------------------------- |
| 💵 **Bill Amount Input**     | Enter the total bill amount                                             |
| 👥 **Split Among People**    | Specify how many people are splitting the bill                          |
| 🎁 **Tip Calculation**       | Automatically calculate tip based on percentage (0%, 5%, 10%, 15%, 20%) |
| 📊 **Final Breakdown**       | Get detailed breakdown of tip amount and per-person cost                |
| 🔄 **Multiple Calculations** | Calculate multiple bills in a single session                            |
| ✅ **Input Validation**       | Validates all inputs to prevent errors                                  |

---

## 🔧 How It Works

The Bill Splitter App follows a simple workflow:

1. **Input Collection** → User enters bill amount, number of people, and tip percentage
2. **Validation** → System checks if all inputs are valid (positive numbers)
3. **Calculation** → System calculates tip amount and per-person cost
4. **Display Results** → Shows tip amount, final bill, and cost per person
5. **Repeat** → Option to calculate another bill

---

## 📐 Formulas

### Tip Amount Calculation

```text
Tip Amount = (Tip Percentage / 100) × Bill Amount
```

**Example:**

```text
If Bill = ₹1000 and Tip Percentage = 10%
Tip Amount = (10 / 100) × 1000 = ₹100
```

### Final Bill Calculation

```text
Final Bill = Bill Amount + Tip Amount
```

**Example:**

```text
If Bill = ₹1000 and Tip Amount = ₹100
Final Bill = 1000 + 100 = ₹1100
```

### Per Person Cost Calculation

```text
Per Person Cost = Final Bill / Number of People
```

**Example:**

```text
If Final Bill = ₹1100 and Number of People = 5
Per Person Cost = 1100 / 5 = ₹220
```

---

## 📥 Installation

1. **Clone or download the repository**

```bash
git clone https://github.com/jeelprajapati0606/python.git
cd python
```

2. **Ensure Python 3.x is installed**

3. **Run the application**

```bash
python Bill_Splitter_JEEL.py
```

---

## 🚀 Usage

### Step-by-Step Guide

| Step | Input                   | Example                                  |
| ---- | ----------------------- | ---------------------------------------- |
| 1️⃣  | Enter total Bill Amount | `1000`                                   |
| 2️⃣  | Enter Number of People  | `5`                                      |
| 3️⃣  | Enter Tip Percentage    | `15`                                     |
| 4️⃣  | View Results            | Bill: ₹1000, Tip: ₹150, Per Person: ₹230 |
| 5️⃣  | Calculate Another?      | `yes` or `no`                            |

### Sample Run

```text
welcome to the Bill splitter App!

Enter total Bill Amount: 1000
Enter Number of people: 5
Enter tip percentage(0/5/10/15/20): 15

Tip Amount: ₹150.0
Final_Bill: ₹1150.0
Per_Person: ₹230.0

would You like to calculate another bill?(yes/no): no
```

---

## 🔍 Code Breakdown

### Section 1: Welcome & Initial Input

```python
print("welcome to the Bill splitter App!")
Bill = float(input("Enter total Bill Amount:"))
People = int(input("Enter Number of people:"))
Tip_percentage = int(input("Enter tip percentage(0/5/10/15/20):"))
```

### Section 2: Input Validation

```python
if People <= 0:
    print("enter number of people ,ask again:")

if Bill <= 0 or Tip_percentage <= 0:
    if Tip_percentage <= 0:
        print("Error! in Tip_percentage")
    if Bill <= 0:
        print("Error! in Bill")
```

### Section 3: Calculations

```python
Tip_Amount = (Tip_percentage/100)*Bill
Final_Bill = Bill + Tip_Amount
Per_Person = Final_Bill/People
```

### Section 4: Display Results

```python
print("Tip Amount:₹",Tip_Amount)
print("Final_Bill:",Final_Bill)
print("Per_Person:",Per_Person)
```

### Section 5: Repeat Calculation Loop

```python
X = str(input("would You like to calculate another bill?(yes/no):"))
while X != "no":
    # Repeat all steps above
```

---

## ✅ Input Validation

| Input            | Validation Rule  | Valid Range    |
| ---------------- | ---------------- | -------------- |
| Bill Amount      | Positive Number  | > 0            |
| Number of People | Positive Integer | > 0            |
| Tip Percentage   | 0, 5, 10, 15, 20 | Allowed Values |
| Repeat Option    | yes / no         | Valid Options  |

---

## 📊 Example

### Scenario: Friends Splitting a Restaurant Bill

**Input**

```text
Bill Amount: ₹2500
Number of People: 4
Tip Percentage: 20%
```

**Calculation**

| Calculation | Formula         | Result |
| ----------- | --------------- | ------ |
| Tip Amount  | (20/100) × 2500 | ₹500   |
| Final Bill  | 2500 + 500      | ₹3000  |
| Per Person  | 3000 / 4        | ₹750   |

**Output**

```text
Tip Amount: ₹500.0
Final_Bill: ₹3000.0
Per_Person: ₹750.0
```

---

## 🐛 Known Issues & Improvements

### Current Limitations

* Minimal error handling
* No re-input on invalid data
* No history tracking

### Future Enhancement

```python
while True:
    try:
        Bill = float(input("Enter total Bill Amount: "))
        if Bill <= 0:
            print("Please enter a positive amount!")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a number.")
```

---

## 👤 Author

**JEEL Prajapati**

[![GitHub Profile](https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge\&logo=github)](https://github.com/jeelprajapati0606)

[![View Repository](https://img.shields.io/badge/View-Repository-blue?style=for-the-badge\&logo=github)](https://github.com/jeelprajapati0606/python)

---

## 💬 Support & Feedback

[![Open Issue](https://img.shields.io/badge/Open-Issue-red?style=for-the-badge\&logo=github)](https://github.com/jeelprajapati0606/python/issues)

[![Fork Project](https://img.shields.io/badge/Fork-Project-green?style=for-the-badge\&logo=github)](https://github.com/jeelprajapati0606/python/fork)

[![Star Repository](https://img.shields.io/badge/Star-Repository-yellow?style=for-the-badge\&logo=github)](https://github.com/jeelprajapati0606/python)

---

## 📝 License

This project is open source and available for personal and educational use.

---

**Happy Bill Splitting! 🎉💰**
