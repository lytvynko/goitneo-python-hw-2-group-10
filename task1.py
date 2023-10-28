def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number updated for {name}."
    else:
        return f"Contact {name} does not exist."

def get_username_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Contact {name} does not exist."

def show_all_contacts(contacts):
    if contacts:
        contact = ''
        for name, phone in contacts.items():
            contact += f"{name}: {phone}\n"
        return contact
    else:
        return "No contacts found."



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(get_username_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()