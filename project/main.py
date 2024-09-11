# main.py
from model import PhoneBookModel
from view import PhoneBookView # type: ignore
from controller import PhoneBookController # type: ignore

def main():
    model = PhoneBookModel()
    view = PhoneBookView()
    controller = PhoneBookController(model, view)
    
    view.mainloop()

if __name__ == "__main__":
    main()