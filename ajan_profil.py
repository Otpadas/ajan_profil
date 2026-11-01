code_name = input("Enter your code name: ")
age = int(input("Enter your age: "))

password = code_name[::-1]
Palindrome = code_name == password

print(f"--- Agent Profile ---\nCode Name:\t{code_name}\nAge:\t\t{age}\nPassword:\t{password}\nPalindrom:\t{Palindrome}")
