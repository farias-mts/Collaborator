from tkinter import *
from tkinter import filedialog
from .controller import destroy_childrens, insert_line

back_color = '#333'
fore_color = '#ffffff'

def scr_newLine(frame_view):
    destroy_childrens(frame_view)
    label_nameLine = Label(
        frame_view,
        text='Nome da Linha',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_nameLine.place(x=10, y=30)

    label_abbreviationLine = Label(
        frame_view,
        text='Abreviação',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_abbreviationLine.place(x=10, y=60)

    label_typeLine = Label(
        frame_view,
        text='Tipo de Linha',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_typeLine.place(x=10, y=90)

    nameLine_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        fg='#333'
    )
    nameLine_box.place(x=140, y=30)

    abbreviationLine_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        bg='#ffffff',
        fg='#333',
    )
    abbreviationLine_box.place(x=140, y=60)

    typeLine_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        bg='#ffffff',
        fg='#333',
    )
    typeLine_box.place(x=140, y=90)

    save_button = Button(
        frame_view,
        text='Salvar',
        font=('Calibri', '12'),
        bg='#ffffff',
        fg='#333',
        command=lambda:insert_line(nameLine_box.get(), abbreviationLine_box.get() ,typeLine_box.get())
    )
    save_button.place(x=230, y=120)