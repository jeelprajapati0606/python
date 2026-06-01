# 💰 Bill Splitter App - JEEL

A simple yet powerful Python application to split bills among friends, colleagues, or group members with automatic tip calculation.

---

## 📋 Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Formulas](#formulas)
- [Installation](#installation)
- [Usage](#usage)
- [Code Breakdown](#code-breakdown)
- [Input Validation](#input-validation)
- [Example](#example)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💵 **Bill Amount Input** | Enter the total bill amount |
| 👥 **Split Among People** | Specify how many people are splitting the bill |
| 🎁 **Tip Calculation** | Automatically calculate tip based on percentage (0%, 5%, 10%, 15%, 20%) |
| 📊 **Final Breakdown** | Get detailed breakdown of tip amount and per-person cost |
| 🔄 **Multiple Calculations** | Calculate multiple bills in a single session |
| ✅ **Input Validation** | Validates all inputs to prevent errors |

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

```
Tip Amount = (Tip Percentage / 100) × Bill Amount
```

**Example:**
```
If Bill = ₹1000 and Tip Percentage = 10%
Tip Amount = (10 / 100) × 1000 = ₹100
```

### Final Bill Calculation

```
Final Bill = Bill Amount + Tip Amount
```

**Example:**
```
If Bill = ₹1000 and Tip Amount = ₹100
Final Bill = 1000 + 100 = ₹1100
```

### Per Person Cost Calculation

```
Per Person Cost = Final Bill / Number of People
```

**Example:**
```
If Final Bill = ₹1100 and Number of People = 5
Per Person Cost = 1100 / 5 = ₹220
```

---

## 📥 Installation

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/jeelprajapati0606/python.git
   cd python
   ```

2. **Ensure Python 3.x is installed** on your system

3. **Run the application:**
   ```bash
   python Bill_Splitter_JEEL.py
   ```

---

## 🚀 Usage

### Step-by-Step Guide

| Step | Input | Example |
|------|-------|---------|
| 1️⃣ | Enter total Bill Amount | `1000` |
| 2️⃣ | Enter Number of People | `5` |
| 3️⃣ | Enter Tip Percentage | `15` |
| 4️⃣ | View Results | Bill: ₹1000, Tip: ₹150, Per Person: ₹230 |
| 5️⃣ | Calculate Another? | `yes` or `no` |

### Sample Run

```
welcome to the Bill splitter App!

Enter total Bill Amount: 1000
Enter Number of people: 5
Enter tip percentage(0/5/10/15/20: 15

Tip Amount:₹ 150.0
Final_Bill: 1150.0
Per_Person: 230.0

would You like to calculate another bill?(yes/no): no
```

---

## 🔍 Code Breakdown

### Section 1: Welcome & Initial Input

```python
print("welcome to the Bill splitter App!")
Bill = float(input("Enter total Bill Amount:"))
People = int(input("Enter Number of people:"))
Tip_percentage = int(input("Enter tip percentage(0/5/10/15/20:"))
```

**Purpose:** Collect user inputs for the first bill calculation

---

### Section 2: Input Validation (Part 1)

```python
if People <= 0:
    print("enter number of people ,ask again:")

if Bill <= 0 or Tip_percentage <= 0:
    if Tip_percentage <= 0:
        print("Error! in Tip_percentage")
    if Bill <= 0:
        print("Error! in Bill")
```

**Purpose:** Validates that:
- Number of people is greater than 0
- Bill amount is greater than 0
- Tip percentage is greater than 0

| Validation Check | Condition | Error Message |
|------------------|-----------|---------------|
| People Validation | `People <= 0` | "enter number of people, ask again:" |
| Bill Validation | `Bill <= 0` | "Error! in Bill" |
| Tip Validation | `Tip_percentage <= 0` | "Error! in Tip_percentage" |

---

### Section 3: Calculations & Results

```python
Tip_Amount = (Tip_percentage/100)*Bill
Final_Bill = Bill + Tip_Amount
Per_Person = Final_Bill/People

print("Tip Amount:₹",Tip_Amount)
print("Final_Bill:",Final_Bill)
print("Per_Person:",Per_Person)
```

**Purpose:** Calculate and display:
- 🎁 Tip amount based on percentage
- 💵 Final bill (original + tip)
- 👤 Cost per person

---

### Section 4: Repeat Calculation Loop

```python
X = str(input("would You like to calculate another bill?(yes/no):"))
while X != "no":
    # Repeat all steps above
    if X == "no":
        break
```

**Purpose:** Allow users to perform multiple bill calculations in one session

---

## ✅ Input Validation

### Validation Rules

| Input | Validation Rule | Valid Range | Invalid Input Handling |
|-------|-----------------|-------------|----------------------|
| **Bill Amount** | Must be positive number | > 0 | Shows error message |
| **Number of People** | Must be positive integer | > 0 | Shows error message |
| **Tip Percentage** | Must be non-negative integer | 0, 5, 10, 15, 20 | Shows error message |
| **Repeat Option** | Must be "yes" or "no" | yes/no | Repeats until "no" |

---

## 📊 Example

### Scenario: Friends splitting a restaurant bill

**Input:**
```
Bill Amount: ₹2500
Number of People: 4
Tip Percentage: 20%
```

**Calculation:**
| Calculation | Formula | Result |
|-------------|---------|--------|
| Tip Amount | (20/100) × 2500 | ₹500 |
| Final Bill | 2500 + 500 | ₹3000 |
| Per Person | 3000 / 4 | ₹750 |

**Output:**
```
Tip Amount: ₹500.0
Final_Bill: 3000.0
Per_Person: 750.0
```

---

## 🐛 Known Issues & Improvements

### Current Limitations:
- Minimal error handling (doesn't re-ask for input on invalid data)
- Doesn't handle negative number inputs gracefully
- No persistence of calculation history

### Suggested Improvements:
```python
# Future enhancement: Loop validation until valid input
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

## 📝 License

This project is open source and available for personal and educational use.

---

## 👤 Author

**JEEL Prajapati**  
GitHub: [@jeelprajapati0606](https://github.com/jeelprajapati0606)

---

## 💬 Support & Feedback

Feel free to open issues or submit pull requests for improvements!

---

**Happy Bill Splitting! 🎉💰**
