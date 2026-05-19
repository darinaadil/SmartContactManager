import json
import os

class Contact:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def to_dict(self):
        return {
            "name": self.name, 
            "phone": self.phone, 
            "email": self.email, 
            "group": self.group
        }

    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'], data['email'], data['group'])

    def __str__(self):
        return f"{self.name:<15} | {self.phone:<15} | {self.group:<10} | {self.email}"

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_from_file()

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    return [Contact.from_dict(item) for item in data]
                except:
                    return []
        return []

    def save_to_file(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4, ensure_ascii=False)

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
    manager = ContactManager()
    
    while True:
        print("\n=== SmartContact Manager ===")
        print("1. Показать все контакты")
        print("2. Добавить новый контакт")
        print("3. Поиск (по имени/номеру)")
        print("4. Удалить контакт")
        print("5. Выход")
        
        choice = input("\nВыберите действие (1-5): ")
        
        if choice == '1':
            print("\n" + "="*60)
            print(f"{'Имя':<15} | {'Телефон':<15} | {'Группа':<10} | {'Email'}")
            print("-" * 60)
            if not manager.contacts:
                print("Список контактов пуст.")
            for c in manager.contacts:
                print(c)
                
        elif choice == '2':
            name = input("Введите имя: ")
            phone = input("Введите телефон: ")
            email = input("Введите email: ")
            group = input("Введите группу (Family/Work/Friends): ")
            manager.add(name, phone, email, group)
            print("✅ Контакт успешно добавлен!")
            
        elif choice == '3':
            q = input("Введите запрос для поиска: ")
            results = manager.search(q)
            if results:
                print("\nНайдено:")
                for r in results: print(r)
            else:
                print("Ничего не найдено.")
                
        elif choice == '4':
            name_to_del = input("Введите имя контакта для удаления: ")
            if manager.delete(name_to_del):
                print(f"🗑 Контакт '{name_to_del}' удален.")
            else:
                print("❌ Контакт не найден.")
                
        elif choice == '5':
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()