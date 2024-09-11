# controller.py
import tkinter as tk
from model import PhoneBookModel
from view import PhoneBookView # type: ignore

class PhoneBookController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Configura o modelo na visão
        self.view.set_model(self.model)
        
        # Define os comandos dos botões
        self.view.set_add_button_command(self.add_contact)
        self.view.set_update_button_command(self.update_contact)
        self.view.set_remove_button_command(self.remove_contact)
        
        # Faz a visão observar as mudanças no modelo
        self.model.add_observer(self.view)
        
        # Configura a interação com a lista de contatos
        self.view.contact_listbox.bind("<<ListboxSelect>>", self.on_contact_select)

    def add_contact(self):
        name, phone, email, cpf = self.view.get_contact_details()
        if name and phone and email and cpf:
            if self.model.get_contact(name):
                tk.messagebox.showwarning("Aviso", "Contato já existe.")
            else:
                self.model.add_contact(name, phone, email, cpf)
                self.view.clear_input_fields()
        else:
            tk.messagebox.showwarning("Aviso", "Preencha todos os campos.")

    def update_contact(self):
        selected_name = self.view.get_selected_contact()
        if selected_name:
            new_name, new_phone, new_email, new_cpf = self.view.get_contact_details()
            if new_name and new_phone and new_email and new_cpf:
                self.model.update_contact(selected_name, new_name, new_phone, new_email, new_cpf)
                self.view.clear_input_fields()
            else:
                tk.messagebox.showwarning("Aviso", "Preencha todos os campos.")
        else:
            tk.messagebox.showwarning("Aviso", "Selecione um contato para atualizar.")

    def remove_contact(self):
        selected_name = self.view.get_selected_contact()
        if selected_name:
            self.model.remove_contact(selected_name)
            self.view.clear_input_fields()
        else:
            tk.messagebox.showwarning("Aviso", "Selecione um contato para remover.")

    def on_contact_select(self, event):
        selected_name = self.view.get_selected_contact()
        if selected_name:
            contact = self.model.get_contact(selected_name)
            if contact:
                self.view.populate_contact_fields(selected_name, contact['phone'], contact['email'], contact['cpf'])