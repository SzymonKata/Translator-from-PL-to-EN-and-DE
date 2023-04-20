from tkinter import *
from mtranslate import translate

def translate_word():
    slowo = entry.get()
    if slowo.lower() == 'q':
        output.config(text="Wyszedłeś z programu.")
        root.destroy()  # Close the Tkinter window
    else:
        try:
            tlumaczenie_en = translate(slowo, "en")
            tlumaczenie_de = translate(slowo, "de")
            output.config(text=f"Tłumaczenie na angielski: {tlumaczenie_en}\nTłumaczenie na niemiecki: {tlumaczenie_de}")

        except Exception as e:
            output.config(text=f"Wystąpił nieoczekiwany błąd: {str(e)}")

root = Tk()
root.title("Translator")
root.geometry("400x300")

root.configure(bg="#FDFEFE")

label = Label(root, text="Podaj słowo lub zdanie do przetłumaczenia (lub wpisz samo 'q' aby wyjść z programu): ",
              bg="#FDFEFE", font=("Helvetica", 12), wraplength=300)
label.pack(pady=10)

entry = Entry(root, font=("Helvetica", 14))
entry.pack(pady=10)

button = Button(root, text="Tłumacz", command=translate_word, font=("Helvetica", 14),
                bg="#3498DB", fg="white")
button.pack()

output = Label(root, wraplength=400, font=("Helvetica", 12), justify="left", bg="#FDFEFE", fg="#E74C3C")
output.pack(pady=10)

root.mainloop()
