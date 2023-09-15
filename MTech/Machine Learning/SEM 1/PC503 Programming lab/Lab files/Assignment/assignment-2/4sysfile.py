import sys

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

if len(sys.argv) != 4:
    print("Usage: python script.py arg1 arg2 arg3")
    sys.exit(1)

arg1 = (sys.argv[1])
arg2 = (sys.argv[2])
arg3 = (sys.argv[3])

if is_palindrome(arg1):
    print(f"{arg1} is a palindrome.")
if is_palindrome(arg2):
    print(f"{arg2} is a palindrome.")
if is_palindrome(arg3):
    print(f"{arg3} is a palindrome.")
