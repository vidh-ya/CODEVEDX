# Password Security & Cracking Analysis Project

## 📌 Overview
This project demonstrates password security concepts:
- Checking password strength
- Generating strong random passwords
- Simulating dictionary attacks
- Simulating brute force attacks

It highlights why weak passwords are dangerous and how attackers exploit them.

---

## 🛠 Features
1. **Password Strength Checker**
   - Analyzes length, uppercase, lowercase, digits, and special characters.
   - Provides feedback and suggestions.

2. **Password Generator**
   - Creates random strong passwords with letters, numbers, and symbols.
   - User can choose password length.

3. **Dictionary Attack Simulation**
   - Tests passwords against a list of common weak passwords (`common_password.txt`).
   - Shows how quickly common passwords can be cracked.

4. **Brute Force Attack Simulation**
   - Attempts all possible combinations (short passwords only).
   - Demonstrates why brute force is slow for strong passwords.

---

## 📂 Project Structure
Password security and cracking analysis/
│── main.py
│── password_checker.py
│── password_cracker.py
│── password_generator.py
│── common_password.txt
│── README.md

---

## ▶️ How to Run
1. Clone or download the project folder.
2. Open terminal and run:
   ```bash
   python main.py
Choose from the menu:

Option 1 → Check password strength

Option 2 → Generate strong password

Option 3 → Dictionary attack simulation

Option 4 → Brute force attack simulation

⚠️ Ethical Note
This project is for educational purposes only.

Do not use against real systems or personal accounts.

Always test with sample or dummy passwords.

📊 Example Output
குறியீடு
==== Password Security Project ====
1. Check Password Strength
2. Generate Strong Password
3. Simulate Dictionary Attack
4. Simulate Brute Force Attack
Enter choice: 3
Enter password to test: admin
Password cracked in 8 attempts!
🎯 Learning Outcomes
Understand password strength and entropy.

Learn how dictionary and brute force attacks work.

Gain practical coding experience in Python.

Build a portfolio‑ready cybersecurity project.