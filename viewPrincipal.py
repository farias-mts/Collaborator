from tkinter import *
from tkinter import filedialog
from newLine.views import scr_newLine
from newCollaborator.views import scr_newCollaborator
from searchCollaborator.views import scr_searchCollaborator


back_color = '#333'
fore_color = '#ffffff'

root = Tk()
root.title('Colaboradores')
root.geometry('500x400')
root.resizable(False, False)
root.configure(bg=back_color)

frame_menu = Frame(
    root,
    bg='#28662E',
    width=140,
    height=500
)
frame_menu.place(x=0, y=0)

frame_view = Frame(
    root,
    width = 320,
    height=380,
    bg=back_color
)
frame_view.place(x=170, y=10)

frame_white = Frame(
    root,
    bg='red',
    width=5,
    height=500
)
frame_white.place(x=142,y=0)

btn_newLine = Button(
    root,
    text='Adicionar Linha',
    bg='#28662E',
    font=('Calibri', '13', 'bold'),
    fg='#ffffff',
    command=lambda:scr_newLine(frame_view),
    borderwidth=0
)
btn_newLine.place(x=5, y=50)

btn_newColaborator = Button(
    root,
    text='Adicionar\nColaborador',
    bg='#28662E',
    font=('Calibri', '13', 'bold'),
    fg='#ffffff',
    command=lambda:scr_newCollaborator(frame_view),
    borderwidth=0
)
btn_newColaborator.place(x=15, y=90)

btn_searchCollaborator = Button(
    root,
    text='Pesquisar\nColaborador',
    bg='#28662E',
    font=('Calibri', '13', 'bold'),
    fg='#ffffff',
    command=lambda:scr_searchCollaborator(frame_view),
    borderwidth=0
)
btn_searchCollaborator.place(x=15, y=150)

root.mainloop()