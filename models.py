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

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name", ""),
            phone=data.get("phone", ""),
            email=data.get("email", ""),
            group=data.get("group", "")
        )

    def __str__(self):
        return f"{self.name:<15} | {self.phone:<15} | {self.group:<10} | {self.email}"