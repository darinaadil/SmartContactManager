from models import Contact
from storage import StorageHandler

class ContactManager:
    def __init__(self, filename='data.json'):
        self.storage = StorageHandler(filename)
        self.contacts = self.storage.load_contacts()

    def save_to_file(self):
        self.storage.save_contacts(self.contacts)

    def add(self, name, phone, email, group):
        new_contact = Contact(name, phone, email, group)
        self.contacts.append(new_contact)
        self.save_to_file()

    def search(self, query):
        return [c for c in self.contacts if query.lower() in c.name.lower() or query in c.phone]

    def delete(self, name):
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
        if len(self.contacts) < original_count:
            self.save_to_file()
            return True
        return False

def main():
    print("=== SmartContact Manager Setup ===")
    print("1. Work with JSON (data.json)")
    print("2. Work with CSV (data.csv)")
    storage_choice = input("Select storage format (1-2): ")
    
    filename = 'data.csv' if storage_choice == '2' else 'data.json'
    manager = ContactManager(filename)
    print(f" Storage file configured: {filename}")
    
    while True:
        print("\n=== SmartContact Manager ===")
        print("1. Show all contacts")
        print("2. Add new contact")
        print("3. Search (by name/phone)")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")
        
        if choice == '1':
            print("\n" + "="*60)
            print(f"{'Name':<15} | {'Phone':<15} | {'Group':<10} | {'Email'}")
            print("-" * 60)
            if not manager.contacts:
                print("Contact list is empty.")
            for c in manager.contacts:
                print(c)
                
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            group = input("Enter group (Family/Work/Friends): ")
            manager.add(name, phone, email, group)
            print("✅ Contact successfully added!")
            
        elif choice == '3':
            q = input("Enter search query: ")
            results = manager.search(q)
            if results:
                print("\nResults found:")
                for r in results: 
                    print(r)
            else:
                print("No records found.")
                
        elif choice == '4':
            name_to_del = input("Enter the name of the contact to delete: ")
            if manager.delete(name_to_del):
                print(f"🗑 Contact '{name_to_del}' has been deleted.")
            else:
                print("❌ Contact not found.")
                
        elif choice == '5':
            print("Exiting application. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
