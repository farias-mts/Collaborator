from tkinter import *
from tkinter import filedialog
from .controller import destroy_childrens

back_color = '#333'
fore_color = '#ffffff'

def scr_searchCollaborator(frame_view):
    destroy_childrens(frame_view)

    label_nameCollaborator = Label(
        frame_view,
        text='Colaborador',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_nameCollaborator.place(x=10, y=30)

    label_registrationCollabaorator = Label(
        frame_view,
        text='Matrícula',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_registrationCollabaorator.place(x=10, y=60)

    label_manager = Label(
        frame_view,
        text='Gestor',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_manager.place(x=10, y=90)

    label_line = Label(
        frame_view,
        text='Linha',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_line.place(x=10, y=120)

    label_job = Label(
        frame_view,
        text='Área',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_job.place(x=10, y=150)

    collaborator_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        fg='#333'
    )
    collaborator_box.place(x=140, y=30)

    registration_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        bg='#ffffff',
        fg='#333',
    )
    registration_box.place(x=140, y=60)

    manager_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        bg='#ffffff',
        fg='#333',
    )
    manager_box.place(x=140, y=90)

    line_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        bg='#ffffff',
        fg='#333',
    )
    line_box.place(x=140, y=120)

    job_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        bg='#ffffff',
        fg='#333',
    )
    job_box.place(x=140, y=150)

    search_button = Button(
        frame_view,
        text='Pesquisar',
        font=('Calibri', '11'),
        bg='#ffffff',
        fg='#333',
        command=lambda:search_collab(
            frame_view,
            collaborator_box.get(), 
            registration_box.get(),
            manager_box.get(), 
            line_box.get(), 
            job_box.get()
        )
    )
    search_button.place(x=230, y=180)