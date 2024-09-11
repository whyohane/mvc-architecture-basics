# model.py
class PhoneBookModel:
    def __init__(self):
        self.contacts = {}
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def add_contact(self, name, phone, email, cpf):
        self.contacts[name] = {'phone': phone, 'email': email, 'cpf': cpf}
        self.notify_observers()

    def update_contact(self, old_name, new_name, new_phone, new_email, new_cpf):
        if old_name in self.contacts:
            del self.contacts[old_name]
            self.contacts[new_name] = {'phone': new_phone, 'email': new_email, 'cpf': new_cpf}
            self.notify_observers()

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.notify_observers()

    def get_contacts(self):
        return self.contacts

    def get_contact(self, name):
        return self.contacts.get(name, None)