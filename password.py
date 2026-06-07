import json

def save_file(passwords, file_name = "passwords.json"):
  with open(file_name, "w") as f:
    json.dump(passwords, f, indent=4)


def load_file(file_name = "passwords.json"):
  try:
    with open(file_name, "r") as f:
      passwords = json.load(f)
      return passwords
  
  except FileNotFoundError:
    return {}   # returns an empty dictionary if the file doesnt exist
  

def store_password(passwords):
  print("\n--- Store password ---\n")
  account = input("Enter the name of an account: ")
  
  if account in passwords:
    while True:
      choice = input("\nThe account already exists. Do you want to overwrite it?(y/n) ").lower()

      if choice == 'y':
        password = input("Enter the password: ")
        passwords[account] = password
        save_file(passwords)
        print("--- Password Saved successfully ---\n")
        break

      elif choice == 'n':
        print("--- Exiting ---\n")
        break
      
      else:
        print("--- Please enter a valid option ---\n")
  
  else:
    password = input("Enter the password: ")
    passwords[account] = password
    save_file(passwords)
    print("--- Password Saved successfully ---\n")


def get_password(passwords):
  print("\n--- Retrieve Password ---\n")

  account = input("Enter the name of an account: ")
  
  if account in passwords:
    password = passwords[account]
    print(f"Your password is: {password}")
  
  else:
    while True:
      choice = input("The account does not exist. Would you like to create one?(y/n) ").lower()

      if choice == 'y':
        store_password(passwords)
        break
      
      elif choice == 'n':
        print("--- Exiting ---")
        break
      
      else:
        print("--- Please enter a valid option ---")


def main():
  passwords = load_file()
  while True:
    print("--- Welcome to Password Manager ---\n")
    print("--- Menu ---\n")
    print("1. Store password")
    print("2. Get password")
    print("3. Exit")

    try:
      choice = int(input("\nEnter your choice: "))

      if choice == 1:
        store_password(passwords)

      elif choice == 2:
        get_password(passwords)

      elif choice == 3:
        print("--- Exiting ---\n")
        break

      else:
        print("--- Please choose a valid option ---\n")

    except ValueError:
      print("--- Invalid input ---\n")

if __name__ == "__main__":
  main()


