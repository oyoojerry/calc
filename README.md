### Simple Python Calculator

This is a simple command-line calculator that performs basic arithmetic operations on two numbers.

## Features
- Performs addition, subtraction, multiplication, and division
- Handles invalid operations gracefully
- Prevents division by zero errors
- Clean output showing the full calculation

## Usage
1. Run the script in a Python environment:
   ```bash
   python calculator.py
   ```
2. Follow the prompts:
   - Enter the first number
   - Enter the second number
   - Choose an operation (+, -, *, /)

## Example Output
```
Enter the first number: 10
Enter the second number: 5
Enter an operation (+, -, *, /): *
10.0 * 5.0 = 50.0
```

## Error Handling
The program handles two special error cases:
1. **Division by zero**:
   ```
   Enter the first number: 8
   Enter the second number: 0
   Enter an operation (+, -, *, /): /
   Error: Division by zero is not allowed.
   ```
2. **Invalid operations**:
   ```
   Enter an operation (+, -, *, /): $
   Invalid operation. Please use +, -, *, or /.
   ```

## Requirements
- Python 3.x

---

To use this calculator, simply copy the code into a file named `calculator.py` and run it using Python.
