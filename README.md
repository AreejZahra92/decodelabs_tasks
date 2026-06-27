# Cybersecurity Internship – DecodeLabs

This repository contains my project submissions for the Cybersecurity Internship at DecodeLabs. Each task focuses on a core security concept, implemented from scratch in Python.

---

## 🔐 Project 1: Password Strength Checker

### Description
A program that evaluates whether a password is **Weak**, **Medium**, or **Strong** based on length and character variety. Built to demonstrate fundamental principles of input validation and security logic before moving on to cryptographic concepts.

### Features
- Checks password length (minimum 8 characters)
- Checks for uppercase letters, lowercase letters, numbers, and symbols
- Flags common/leaked passwords
- Gives feedback on what's missing to improve a weak password
- Displays a clear strength result (Weak / Medium / Strong)

### Tech Used
Python

**File:** `Task-1.py`

---

## 🔑 Project 2: Basic Encryption & Decryption (Caesar Cipher)

### Description
This project implements a basic Caesar Cipher to demonstrate the core concepts of data encryption and decryption. It takes plaintext input from the user, encrypts it by shifting each letter forward in the alphabet by a user-defined key, and then decrypts it back to verify the process is fully reversible.

### Features
- Encrypts user-input text using a shift-based cipher logic
- Decrypts the encrypted text back to the original plaintext
- Displays the original, encrypted, and decrypted text
- Handles edge cases like spaces, numbers, and punctuation (left unchanged)
- Validates correctness by comparing decrypted output with the original input

### How It Works
1. Each letter is converted to its ASCII value
2. The shift key is added (encryption) or subtracted (decryption)
3. Modulo 26 is applied to wrap around the alphabet (so Z + 1 = A, etc.)
4. The result is converted back into a letter

### Tech Used
Python

**File:** `Task-2.py`

---

## 📌 About
Industrial Training Kit – Cyber Security Track
Powered by DecodeLabs