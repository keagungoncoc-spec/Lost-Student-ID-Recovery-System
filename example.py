#ADMIN LOGIN 
def login():
    print("=== Admin Login ===")
    username = input("Username: ")
    password = input("Password: ")
    
    if username == "admin" and password == "1122334455":
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials. Access denied.\n")
        return False


while not login():  
    pass

# CRUD FUNCTIONS
records = []
id_counter = 1

def add_id():
    global id_counter
    print("\n=== Add Found Student ID ===")
    name = input("Student Name on ID: ")
    sid = input("Student ID Number (if visible): ")
    location = input("Where was it found?: ")
    date = input("Date Found (YYYY-MM-DD): ")
    finder = input("Finder's Name: ")

    record = {
        'id': id_counter,
        'student_name': name,
        'student_id': sid,
        'found_location': location,
        'date_found': date,
        'finder_name': finder,
        'status': 'Unclaimed'
    }
    records.append(record)
    id_counter += 1
    print("----------------------------------")
    print("Lost ID record added successfully!")
    print("----------------------------------")

def view_all():
    print("\n( All Lost Student IDs )")
    if records:
        for record in records:
            print(f"ID: {record['id']}")
            print(f"Student Name: {record['student_name']}")
            print(f"Student ID: {record['student_id']}")
            print(f"Found Location: {record['found_location']}")
            print(f"Date Found: {record['date_found']}")
            print(f"Finder: {record['finder_name']}")
            print(f"Status: {record['status']}")
            print("-------------------------------")
    else:
        print("No records found.\n")

def search_id():
    print("\n( Search Lost ID )")
    name = input("Enter Student Name to search: ")
    results = [r for r in records if name.lower() in r['student_name'].lower()]
    if results:
        for record in results:
            print(f"ID: {record['id']} | Name: {record['student_name']} | Status: {record['status']}")
    else:
        print("No matching record found.\n")

def update_status():
    print("\n(Update ID Claim Status)")
    try:
        id_num = int(input("Enter Record ID to update: "))
    except ValueError:
        print("Invalid ID. Please enter a number.\n")
        return
    record = next((r for r in records if r['id'] == id_num), None)
    if record:
        print(f"Current Status: {record['status']}")
        new_status = input("Enter new status (Unclaimed/Claimed): ")
        record['status'] = new_status
        print("Status updated successfully!\n")
    else:
        print("Record not found.\n")

def delete_record():
    print("\n( Delete Record )")
    try:
        id_num = int(input("Enter Record ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.\n")
        return
    record = next((r for r in records if r['id'] == id_num), None)
    if record:
        confirm = input("Are you sure you want to delete this record? (y/n): ")
        if confirm.lower() == 'y':
            records.remove(record)
            print("Record deleted successfully!\n")
        else:
            print("Deletion cancelled.\n")
    else:
        print("Record not found.\n")


#MAIN MENU LOOP 
while True:
    print("LOST ID RECOVERY SYSTEM")
    print("[1] Add ID")
    print("[2] View Records")
    print("[3] Search ID")
    print("[4] Update ID Status")
    print("[5] Delete Record")
    print("[6] Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1': add_id()
        
    elif choice == '2': view_all()
       
    elif choice == '3': search_id()
        
    elif choice == '4': update_status()
        
    elif choice == '5': delete_record()
        
    elif choice == '6':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
else:
    exit()
