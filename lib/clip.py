from helpers import (
    exit_program,
    list_roles, find_role_by_name, find_role_by_id,
    create_role, update_role, delete_role,
    list_auditions, find_audition_by_id,
    create_audition, update_audition, delete_audition,
    call_back_audition, list_role_auditions,
    get_role_lead, get_role_understudy
)

def print_role(role):
    print(f"ID: {role.id}")
    print(f"Character Name: {role.character_name}")

def print_audition(audition):
    print(f"ID: {audition.id}")
    print(f"Actor: {audition.actor}")
    print(f"Location: {audition.location}")
    print(f"Phone: {audition.phone}")
    print(f"Hired: {'Yes' if audition.hired else 'No'}")
    print(f"Role ID: {audition.role_id}")

def main():
    while True:
        print("\nTheater Work CLI")
        print("1. List all roles")
        print("2. Find role by name")
        print("3. Find role by ID")
        print("4. Create role")
        print("5. Update role")
        print("6. Delete role")
        print("7. List all auditions")
        print("8. Find audition by ID")
        print("9. Create audition")
        print("10. Update audition")
        print("11. Delete audition")
        print("12. Call back audition")
        print("13. List auditions for a role")
        print("14. Get lead actor for a role")
        print("15. Get understudy for a role")
        print("16. Exit")

        choice = input("Enter your choice (1-16): ")

        if choice == "1":
            roles = list_roles()
            for role in roles:
                print_role(role)
                print("---")

        elif choice == "2":
            role = find_role_by_name()
            if role:
                print_role(role)
            else:
                print("Role not found")

        elif choice == "3":
            role = find_role_by_id()
            if role:
                print_role(role)
            else:
                print("Role not found")

        elif choice == "4":
            role = create_role()
            if role:
                print("Created role:")
                print_role(role)

        elif choice == "5":
            role = update_role()
            if role:
                print("Updated role:")
                print_role(role)

        elif choice == "6":
            role = delete_role()
            if role:
                print(f"Deleted role {role.id}")

        elif choice == "7":
            auditions = list_auditions()
            for audition in auditions:
                print_audition(audition)
                print("---")

        elif choice == "8":
            audition = find_audition_by_id()
            if audition:
                print_audition(audition)
            else:
                print("Audition not found")

        elif choice == "9":
            audition = create_audition()
            if audition:
                print("Created audition:")
                print_audition(audition)

        elif choice == "10":
            audition = update_audition()
            if audition:
                print("Updated audition:")
                print_audition(audition)

        elif choice == "11":
            audition = delete_audition()
            if audition:
                print(f"Deleted audition {audition.id}")

        elif choice == "12":
            audition = call_back_audition()
            if audition:
                print("Audition called back:")
                print_audition(audition)

        elif choice == "13":
            auditions = list_role_auditions()
            for audition in auditions:
                print_audition(audition)
                print("---")

        elif choice == "14":
            lead = get_role_lead()
            print(lead)

        elif choice == "15":
            understudy = get_role_understudy()
            print(understudy)

        elif choice == "16":
            exit_program()

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()