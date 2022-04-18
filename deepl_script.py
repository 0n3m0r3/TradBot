import deepl
from tkinter import *


#deepl token
DEEPL_API_KEY = "184caa89-f0f7-2a57-5514-a9e824ae37cf:fx"

#fonction de traduction
def trad():
    #récupère le texte en entrée
    var_text_trad = text_entry.get(1.0, END)
    #crée l'instannce deepl
    translator = deepl.Translator(DEEPL_API_KEY)
    #traduit en allemand
    result = translator.translate_text(var_text_trad, target_lang="DE")
    #supprime tout ce qui se trpouvait en sortie
    text_output.delete(1.0, END)
    #affiche le texte traduit en sortie
    text_output.insert(END, result)



#parametres de la fenetre
window = Tk()
window.title("TradBot")
window.geometry('968x500')
window.iconbitmap("")
window.resizable(False, False)

#parametres du menu
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

#conteuneur principal
container = Frame(window)
container.pack(fill=BOTH)

#barre de séparation en hauteur
frame_top = Frame(container)
frame_top.grid(row=0, columnspan=2)

#zone d'entrée
frame_1 = Frame(container)
frame_1.grid(column=0, row=1)

text_entry = Text(frame_1, width=60, height=20)
text_entry.grid(row=0)

button_submit = Button(frame_1, text="Traduire", command=trad)
button_submit.grid(row=1)

#zone de sortie
frame_2 = Frame(container)
frame_2.grid(column=1, row=1)

text_output = Text(frame_2, width=60, height=20)
text_output.grid(row=0)

button_tweet = Button(frame_2, text="Tweeter(dev)")
button_tweet.grid(row=1)




window.mainloop()

















