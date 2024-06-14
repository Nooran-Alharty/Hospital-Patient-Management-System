import sys
import string

maxsize = 10
specializations = {
    1: "Cardiologist",
    2: "Dentist",
    3: "Orthopedic Surgeon",
    4: "Pediatrician",
    5: "Ophthalmologist",
    6: "Gynecologist",
    7: "Neurologist",
    8: "Dermatologist",
    9: "ENT Specialist",
    10: "Urologist"
}

# Initialize hospital data structure
hos = {i: [] for i in specializations.keys()}


def add(specialization, name, case):
    """Function to add a new patient to a specialization."""
    if len(hos[specialization]) >= maxsize:
        print("Error: Maximum patient limit reached for this specialization.")
        return

    newpatient = {"name": name, "case": case}
    if case == 0:
        hos[specialization].append(newpatient)
    elif case == 1:
        for i, x in enumerate(hos[specialization]):
            if x["case"] == 0:
                hos[specialization].insert(i, newpatient)
                break
        else:
            hos[specialization].append(newpatient)
    elif case == 2:
        for i, x in enumerate(hos[specialization]):
            if x["case"] == 0 or x["case"] == 1:
                hos[specialization].insert(i, newpatient)
                break
        else:
            hos[specialization].append(newpatient)

    print1(specialization)


def print1(specialization):
    """Function to print all patients in a specialization."""
    for i, p in hos.items():
        if i == specialization:
            num = len(p)
            if num == 0:
                continue
            print(f'Specialization: {specializations[i]} - There are {num} patients')
            for n in p:
                case = "normal" if n["case"] == 0 else "urgent" if n["case"] == 1 else "superurgent"
                print(f'Patient: {n["name"]} is {case}')


def printallpatients():
    """Function to print all patients in all specializations."""
    has_patients = False
    for i, p in hos.items():
        num = len(p)
        if num == 0:
            continue
        has_patients = True
        print(f'Specialization: {specializations[i]} - There are {num} patients')
        for n in p:
            case = "normal" if n["case"] == 0 else "urgent" if n["case"] == 1 else "superurgent"
            print(f'Patient: {n["name"]} is {case}')
    if not has_patients:
        print("There are no patients currently at any specialization.")


def getnextpatient(specialization):
    """Function to get the next patient in a specialization."""
    for i, p in hos.items():
        if i == specialization:
            if len(p) > 0:
                print(f"Next patient for {specializations[i]}: {p[0]['name']} go to the doctor")
                del p[0]
            else:
                print("Error: No patients in this specialization.")


def removepatient(specialization, name):
    """Function to remove a patient from a specialization."""
    for i, p in hos.items():
        if i == specialization:
            for n in p:
                if n["name"] == name:
                    p.remove(n)
                    print(f"{name} has been removed from {specializations[i]}.")
                    return
            else:
                print(f"Error: Patient '{name}' not found in {specializations[i]}.")


# Main program loop
while True:
    print("\nProgram options:")
    print("1) Add new patient")
    print("2) Print all patients")
    print("3) Get next patient")
    print("4) Remove patient")
    print("5) End the program")

    try:
        program = int(input("Enter your choice (1-5): "))
        if program not in [1, 2, 3, 4, 5]:
            raise ValueError("Invalid input. Please enter a number from 1 to 5.")

        if program == 1:  # Add new patient
            print("List of Doctor Specializations:")
            for idx in specializations:
                print(f"{idx}) {specializations[idx]}")

            while True:
                try:
                    spec_choice = int(input("Choose the specialization number: "))
                    if spec_choice not in specializations.keys():
                        raise ValueError("Invalid specialization number.")
                    break
                except ValueError as ve:
                    print(f"Error: {ve}")

            while True:
                name = input("Enter the name of the patient: ")
                if not all(char.isalpha() or char.isspace() for char in name):
                    print("Error: Name should only contain alphabets and spaces.")
                else:
                    break

            while True:
                try:
                    case = int(input("Enter the case (0:normal, 1:urgent, 2:superurgent): "))
                    if case not in [0, 1, 2]:
                        raise ValueError("Invalid case type. Please enter 0, 1, or 2.")
                    break
                except ValueError as ve:
                    print(f"Error: {ve}")

            add(spec_choice, name, case)

        elif program == 2:  # Print all patients
            printallpatients()
            print("--------------------------")

        elif program == 3:  # Get next patient
            print("List of Doctor Specializations:")
            for idx in specializations:
                print(f"{idx}) {specializations[idx]}")

            while True:
                try:
                    spec_choice = int(input("Choose the specialization number: "))
                    if spec_choice not in specializations.keys():
                        raise ValueError("Invalid specialization number.")
                    break
                except ValueError as ve:
                    print(f"Error: {ve}")

            getnextpatient(spec_choice)
            print("----------------------------")

        elif program == 4:  # Remove patient
            print("List of Doctor Specializations:")
            for idx in specializations:
                print(f"{idx}) {specializations[idx]}")

            while True:
                try:
                    spec_choice = int(input("Choose the specialization number: "))
                    if spec_choice not in specializations.keys():
                        raise ValueError("Invalid specialization number.")
                    break
                except ValueError as ve:
                    print(f"Error: {ve}")

            name = input("Enter the name of the patient to remove: ")
            removepatient(spec_choice, name)

        elif program == 5:  # End the program
            print("End of the program.")
            sys.exit()

    except ValueError as ve:
        print(f"Error: {ve}. Please try again.")
