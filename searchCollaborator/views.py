from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from .controller import destroy_childrens, search_collab, next_collaborator, previous_collaborator, save_edit
import tempfile

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

def insert_data(x, frame_view, matrix):
    destroy_childrens(frame_view)
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as photo:
        photo.write(matrix[x][0])
        image = photo.name
    path = Image.open(image).resize((113, 141), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(path)
    pth_label = Label(frame_view)
    pth_label.place(x=95 , y=10)
    pth_label.config(image=image)
    pth_label.image = image

    back_color = '#333'
    fore_color = '#ffffff'

    label_nameCollaborator = Label(
        frame_view,
        text='Colaborador',
        font=('Calibri', '14', 'bold'),
        bg = back_color, 
        fg = fore_color
    )
    label_nameCollaborator.place(x=10, y=170)

    label_registration = Label(
        frame_view,
        text='Matrícula',
        font=('Calibri', '14', 'bold'),
        bg = back_color, 
        fg = fore_color
    )
    label_registration.place(x=10, y=200)

    label_manager = Label(
        frame_view,
        text='Gestor',
        font=('Calibri', '14', 'bold'),
        bg=back_color,
        fg=fore_color
    )
    label_manager.place(x=10, y=230)

    label_line = Label(
        frame_view,
        text='Linha',
        font=('Calibri', '14', 'bold'),
        bg=back_color,
        fg=fore_color
    )
    label_line.place(x=10, y=260)

    label_job = Label(
        frame_view,
        text='Área',
        font=('Calibri', '14', 'bold'),
        bg=back_color,
        fg=fore_color
    )
    label_job.place(x=10, y=290)

    collaborator_box = Entry(
        frame_view,
        font=('Arial','13'),
        bg='#ffffff',
        fg='#333'
    )
    collaborator_box.insert(0, matrix[x][1])
    collaborator_box.config(state=DISABLED)
    collaborator_box.place(x=140, y=170)

    registration_box = Entry(
        frame_view,
        font=('Arial', '13'),
        bg='#ffffff',
        fg='#333'
    )
    registration_box.insert(0, matrix[x][2])
    registration_box.config(state=DISABLED)
    registration_box.place(x=140, y=200)

    manager_box = Entry(
        frame_view,
        font=('Arial', '13'),
        bg='#ffffff',
        fg='#333'
    )
    manager_box.insert(0, matrix[x][3])
    manager_box.config(state=DISABLED)
    manager_box.place(x=140, y=230)

    line_box = Entry(
        frame_view,
        font=('Arial', '13'),
        bg='#ffffff',
        fg='#333'
    )
    line_box.insert(0, matrix[x][4])
    line_box.config(state=DISABLED)
    line_box.place(x=140, y=260)

    job_box = Entry(
        frame_view,
        font=('Arial', '13'),
        bg='#ffffff', 
        fg='#333'
    )
    job_box.insert(0, matrix[x][5])
    job_box.config(state=DISABLED)
    job_box.place(x=140, y=290)

    image_l = ImageTk.PhotoImage(Image.open(r'static\setaVerde.png').resize((30, 15), Image.ANTIALIAS).rotate(180))
    canvasLeft = Label(
        frame_view, 
        image=image_l,
        bg='#333'
    )
    canvasLeft.image=image_l
    canvasLeft.place(x=52, y=77)
    canvasLeft.bind('<Button-1>', lambda event, x=x, frame_view=frame_view:previous_collaborator(event, x, frame_view))

    image_r = ImageTk.PhotoImage(Image.open(r'static\setaVerde.png').resize((30, 15), Image.ANTIALIAS))
    canvasNext = Label(
        frame_view, 
        image=image_r,
        bg='#333'
    )
    canvasNext.image = image_r
    canvasNext.place(x=220, y=77)
    canvasNext.bind('<Button-1>', lambda event, x=x, frame_view=frame_view:next_collaborator(event, x, frame_view))

    image_edit = ImageTk.PhotoImage(Image.open(r'static\lapis.png').resize((20, 20), Image.ANTIALIAS))
    labelEdit = Label(
        frame_view,
        image=image_edit,
        bg='#333'
    )
    labelEdit.image = image_edit
    labelEdit.place(x=290, y=6)
    labelEdit.bind('<Button-1>', lambda event, frame_view=frame_view:enable_edit(event, frame_view, collaborator_box, registration_box, manager_box, line_box, job_box))

def enable_edit(event, frame_view, collaborator_box, registration_box, manager_box, line_box, job_box):
    collaborator_box.config(state=NORMAL) 
    registration_box.config(state=NORMAL) 
    manager_box.config(state=NORMAL) 
    line_box.config(state=NORMAL) 
    job_box.config(state=NORMAL) 
    oldCollaborator_box = collaborator_box.get()
    oldRegistration_box = registration_box.get()
    oldManager_box = manager_box.get()
    oldLine_box = line_box.get()
    oldJob_box = job_box.get()

    btn_save = Button(
        frame_view,
        text='Salvar',
        bg='#28662E',
        fg='#ffffff',
        command=lambda:save_edit(collaborator_box.get(), registration_box.get(), manager_box.get(), line_box.get(), job_box.get()),
    )
    btn_save.place(x=450, y=330)