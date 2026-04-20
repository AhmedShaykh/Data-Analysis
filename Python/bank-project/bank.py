from pathlib import Path;
import string;
import random;
import json;

class Bank:

    database = "data.json";
    
    @classmethod
    def load_data(cls):
        """Loads data from JSON file, handling empty or missing files.""";
        if not Path(cls.database).exists():
            return [];
        try:
            with open(cls.database, "r") as fs:
                content = fs.read().strip();
                if not content:
                    return [];
                return json.loads(content);
        except (json.JSONDecodeError, IOError):
            return [];

    @classmethod
    def save_data(cls, data):
        """Saves the current state of data to the JSON file.""";
        with open(cls.database, "w") as fs:
            json.dump(data, fs, indent=4);

    @classmethod
    def generate_account_number(cls):
        """Generates a random 7-character account number.""";
        chars = random.choices(string.ascii_letters, k=3) + \
                random.choices(string.digits, k=3) + \
                random.choices("!@#$%^&*", k=1);
        random.shuffle(chars);
        return "".join(chars);

    @classmethod
    def create_account(cls, name, age, email, pin):
        data = cls.load_data();
        if age < 18:
            return None, "Registration failed: You must be 18 or older.";
        if len(str(pin)) != 4:
            return None, "Registration failed: PIN must be exactly 4 digits.";
        acc_no = cls.generate_account_number();
        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo.": acc_no,
            "balance": 0
        };
        data.append(user);
        cls.save_data(data);
        return user, "Account Created Successfully";

    @classmethod
    def find_user(cls, acc_no, pin):
        data = cls.load_data();
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                return user;
        return None;

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        data = cls.load_data();
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                if 0 < amount <= 10000:
                    user["balance"] += amount;
                    cls.save_data(data);
                    return True, f"Successfully deposited ${amount}";
                return False, "Amount must be between 1 and 10,000";
        return False, "Invalid account number or PIN";

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        data = cls.load_data();
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                if amount <= 0:
                    return False, "Invalid amount";
                if user["balance"] >= amount:
                    user["balance"] -= amount;
                    cls.save_data(data);
                    return True, f"Successfully withdrew ${amount}";
                return False, "Insufficient balance";
        return False, "Invalid account number or PIN";

    @classmethod
    def update_user(cls, acc_no, pin, name=None, email=None, new_pin=None):
        data = cls.load_data();
        for user in data:
            if user["accountNo."] == acc_no and user["pin"] == pin:
                user["name"] = name if name else user["name"];
                user["email"] = email if email else user["email"];
                if new_pin:
                    if len(str(new_pin)) == 4:
                        user["pin"] = int(new_pin);
                    else:
                        return False, "New PIN must be 4 digits";
                cls.save_data(data);
                return True, "User details updated successfully";
        return False, "User not found or incorrect PIN";

    @classmethod
    def delete_user(cls, acc_no, pin):
        data = cls.load_data();
        for i, user in enumerate(data):
            if user["accountNo."] == acc_no and user["pin"] == pin:
                data.pop(i);
                cls.save_data(data);
                return True, "Account deleted successfully";
        return False, "Account not found or incorrect PIN";