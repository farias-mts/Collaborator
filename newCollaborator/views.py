from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from .controller import destroy_childrens, insert_collab

back_color = '#333'
fore_color = '#ffffff'

def scr_newCollaborator(frame_view):   
    destroy_childrens(frame_view)
    frame_photo = Frame(
        frame_view,
        width=113,
        height=141,
        bg='#ffffff'
    )
    frame_photo.place(x=100, y=10)
    frame_photo.bind('<Button-1>', lambda event, frame_photo=frame_photo: add_photo(event, frame_photo))

    label_nameCollaborator = Label(
        frame_view,
        text='Colaborador',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_nameCollaborator.place(x=10, y=170)

    label_registrationCollabaorator = Label(
        frame_view,
        text='Matrícula',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_registrationCollabaorator.place(x=10, y=200)

    label_manager = Label(
        frame_view,
        text='Gestor',
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_manager.place(x=10, y=230)

    label_line = Label(
        frame_view,
        text='Linhas', 
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_line.place(x=10, y=260)

    label_job = Label(
        frame_view,
        text='Área', 
        bg=back_color,
        fg=fore_color,
        font=('Calibri', '14', 'bold')
    )
    label_job.place(x=10, y=290)

    collaborator_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        fg='#333'
    )
    collaborator_box.place(x=140, y=170)

    registration_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        bg='#ffffff',
        fg='#333',
    )
    registration_box.place(x=140, y=200)

    manager_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        bg='#ffffff',
        fg='#333',
    )
    manager_box.place(x=140, y=230)

    line_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        bg='#ffffff',
        fg='#333',
    )
    line_box.place(x=140, y=260)

    job_box = Entry(
        frame_view,
        width=15,
        font=('Calibri', '13'),
        bg='#ffffff',
        fg='#333',
    )
    job_box.place(x=140, y=290)

    save_button = Button(
        frame_view,
        text='Salvar',
        font=('Calibri', '11'),
        bg='#ffffff',
        fg='#333',
        command=lambda:insert_collab(
            ifile,
            collaborator_box.get(), 
            registration_box.get(),
            manager_box.get(),
            line_box.get(),
            job_box.get())
    )
    save_button.place(x=230, y=320)

def add_photo(event, frame_photo):
    def clear_photo(event, frame_photo):
        for children in frame_photo.winfo_children():
            children.destroy()
    try:
        clear_photo(event, frame_photo)
        global ifile
        ifile = filedialog.askopenfile(parent=frame_photo,mode='rb',title='Choose a file')
        #get_photo(ifile)
        path = Image.open(ifile).resize((113, 141), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(path)
        label_image = Label(frame_photo)
        label_image.pack()
        label_image.configure(image=image)
        label_image.image = image
        label_image.bind('<Double-Button-1>', lambda event, frame_photo=frame_photo: add_photo(event, frame_photo))
        label_image.bind('<Button-3>', lambda event, frame_photo=frame_photo:clear_photo(event, frame_photo))
    except:
        pass

def return_status(status):
    popup = Tk()
    popup.title('STATUS')
    popup.geometry('200x150')
    popup.resizable(False, False)
    popup.config(bg='#333')
    status_label = Label(
        popup,
        text=status,
        font=('Calibri', '13'),
        bg='#333',
        fg='#ffffff'
    )
    status_label.pack()
    popup.mainloop()