import json
import os
import csv
from models import Contact 

class StorageHandler:
    def __init__(self, filename='data.json'):
        self.filename = filename

    def load_contacts(self):
        if not os.path.exists(self.filename):
            return []
            
        if self.filename.endswith('.json'):
            with open(self.filename, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    return [Contact.from_dict(item) for item in data]
                except json.JSONDecodeError:
                    return []
                    
        elif self.filename.endswith('.csv'):
            contacts = []
            with open(self.filename, 'r', encoding='utf-8', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row:
                        contacts.append(Contact.from_dict(row))
            return contacts
            
        return []

    def save_contacts(self, contacts):
        if self.filename.endswith('.json'):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([c.to_dict() for c in contacts], f, indent=4, ensure_ascii=False)
                
        elif self.filename.endswith('.csv'):
            if not contacts:
                return
                
            with open(self.filename, 'w', encoding='utf-8', newline='') as f:
                fieldnames = contacts[0].to_dict().keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                writer.writeheader()
                for c in contacts:
                    writer.writerow(c.to_dict())