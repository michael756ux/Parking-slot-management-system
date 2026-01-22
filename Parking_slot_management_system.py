parking_slots = []

def allocate_slot():
    vehicle = input("Enter vehicle number: ")
    slot = input("Enter parking slot number: ")
    parking_slots.append({
        "vehicle": vehicle,
        "slot": slot
    })
    print("Parking slot allocated")

def view_slots():
    if not parking_slots:
        print("No parking slots allocated")
    else:
        for p in parking_slots:
            print("Vehicle:", p["vehicle"], "| Slot:", p["slot"])

def main():
    while True:
        print("1. Allocate Parking Slot")
        print("2. View Parking Slots")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            allocate_slot()
        elif choice == "2":
            view_slots()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
