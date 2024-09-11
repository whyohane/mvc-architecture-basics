# view.py
import tkinter as tk
from tkinter import messagebox

class PhoneBookView(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Agenda Telefônica")
        self.geometry("400x350")

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.cpf_var = tk.StringVar()

        # Campo de entrada para nome
        tk.Label(self, text="Nome:").pack(pady=5)
        self.name_entry = tk.Entry(self, textvariable=self.name_var)
        self.name_entry.pack(pady=5)

        # Campo de entrada para telefone
        tk.Label(self, text="Telefone:").pack(pady=5)
        self.phone_entry = tk.Entry(self, textvariable=self.phone_var)
        self.phone_entry.pack(pady=5)

        # Campo de entrada para email
        tk.Label(self, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self, textvariable=self.email_var)
        self.email_entry.pack(pady=5)

        # Campo de entrada para CPF
        tk.Label(self, text="CPF:").pack(pady=5)
        self.cpf_entry = tk.Entry(self, textvariable=self.cpf_var)
        self.cpf_entry.pack(pady=5)

        # Botões
        self.add_button = tk.Button(self, text="Adicionar", command=None)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self, text="Atualizar", command=None)
        self.update_button.pack(pady=5)

        self.remove_button = tk.Button(self, text="Remover", command=None)
        self.remove_button.pack(pady=5)

        # Lista de contatos
        self.contact_listbox = tk.Listbox(self)
        self.contact_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.model = None  # Adiciona um atributo para o modelo

    def set_model(self, model):
        self.model = model

    def set_add_button_command(self, command):
        self.add_button.config(command=command)

    def set_update_button_command(self, command):
        self.update_button.config(command=command)

    def set_remove_button_command(self, command):
        self.remove_button.config(command=command)

    def get_contact_details(self):
        return self.name_var.get(), self.phone_var.get(), self.email_var.get(), self.cpf_var.get()

    def clear_input_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.cpf_var.set("")

    def add_contact_to_list(self, name):
        self.contact_listbox.insert(tk.END, name)

    def update_contact_in_list(self, old_name, new_name):
        idx = self.contact_listbox.get(0, tk.END).index(old_name)
        self.contact_listbox.delete(idx)
        self.contact_listbox.insert(idx, new_name)

    def remove_contact_from_list(self, name):
        idx = self.contact_listbox.get(0, tk.END).index(name)
        self.contact_listbox.delete(idx)

    def get_selected_contact(self):
        try:
            return self.contact_listbox.get(self.contact_listbox.curselection())
        except:
            messagebox.showwarning("Aviso", "Nenhum contato selecionado.")
            return None

    def populate_contact_fields(self, name, phone, email, cpf):
        self.name_var.set(name)
        self.phone_var.set(phone)
        self.email_var.set(email)
        self.cpf_var.set(cpf)

    def update(self):
        if self.model:
            contacts = self.model.get_contacts()
            self.contact_listbox.delete(0, tk.END)
            for name in contacts:
                self.contact_listbox.insert(tk.END, name)