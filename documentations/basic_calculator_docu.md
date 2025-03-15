# Basic Calculator Documentation

## Overview
The **Basic Calculator** is a simple command-line tool that performs four fundamental arithmetic operations: addition, subtraction, multiplication, and division.

## Features
- Accepts two numerical inputs from the user.
- Supports the following operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`), with error handling for division by zero.
- Displays the calculated result based on the selected operation.

## How It Works

### 1. User Input
The program prompts the user to enter:
1. The first number
2. The desired mathematical operation (`+`, `-`, `*`, or `/`)
3. The second number

### 2. Performing Calculations
The script processes the input and returns the corresponding result based on the chosen operation.

### 3. Example Usage
#### Addition:
```
Enter first number: 10
Enter operation (+, -, *, /): +
Enter second number: 5
Result: 15.0
```
#### Division (with zero handling):
```
Enter first number: 8
Enter operation (+, -, *, /): /
Enter second number: 0
Result: Error! Division by zero.
```

## Notes
- This only accpts numeric values for calculations.
- If an invalid operation is entered, the program displays an error message.

## Author
This module was created as part of my coding documentation and compilation project.
