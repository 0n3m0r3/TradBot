import deepl
from tkinter import *


DEEPL_API_KEY = "184caa89-f0f7-2a57-5514-a9e824ae37cf:fx"


def trad():
    var_text_trad = text_entry.get(1.0, END)
    translator = deepl.Translator(DEEPL_API_KEY)
    result = translator.translate_text(var_text_trad, target_lang="DE")
    text_output.delete(1.0, END)
    text_output.insert(END, result)




window = Tk()
window.title("TradBot")
window.geometry('968x500')
window.iconbitmap("")
window.resizable(False, False)

menubar = Menu(window)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(
    label='Quitter',
    command=window.destroy,
)
menubar.add_cascade(
    label="Fichier",
    menu=file_menu,
)

window.config(menu=menubar)

container = Frame(window)
container.pack(fill=BOTH)

frame_top = Frame(container)
frame_top.grid(row=0, columnspan=2)

frame_1 = Frame(container)
frame_1.grid(column=0, row=1)

text_entry = Text(frame_1, width=60, height=20)
text_entry.grid(row=0)

button_submit = Button(frame_1, text="Traduire", command=trad)
button_submit.grid(row=1)


frame_2 = Frame(container)
frame_2.grid(column=1, row=1)

text_output = Text(frame_2, width=60, height=20)
text_output.grid(row=0)

button_tweet = Button(frame_2, text="Tweeter(dev)")
button_tweet.grid(row=1)




window.mainloop()

















