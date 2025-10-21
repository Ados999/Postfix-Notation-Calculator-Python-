# Postfix-Notation-Calculator-Python-

🧮 Postfix Notation Calculator (Python)

This Python script evaluates mathematical expressions written in postfix notation (Reverse Polish Notation) using a custom singly linked list instead of a stack.
It reads input character by character from standard input and performs arithmetic operations step by step.

⚙️ Features

Supports integer operations: +, -, *, /

Handles multi-digit numbers and whitespace-separated input

Detects and reports invalid expressions (Chyba!)

Uses a custom linked list (spojak + spojs) to simulate stack behavior

🧠 How It Works

Reads numbers and operators from standard input.

Pushes each number onto a linked list (stack).

When an operator is encountered, it pops the top two numbers, applies the operation, and pushes the result back.

After the entire input is processed, the remaining number on the stack is printed as the result.

If an error occurs (e.g. missing operand, division by zero), it prints Chyba! and exits.

🧩 Example

Input:

5 3 + 2 *


Output:

16
