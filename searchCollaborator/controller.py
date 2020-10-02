from .models import query_collaborator

def destroy_childrens(frame_view):
    for children in frame_view.winfo_children():
        children.destroy()

def search_collab(frame_view, colaborador, matricula, gestor, linha, area):
    title_table = ['nome', 'matricula', 'gestor', 'linhas', 'area']
    datas = [colaborador, matricula, gestor, linha, area]
    query = ''
    x = 0
    for data in datas:
        if data != '':
            for char in '*':
                data = data.replace(char, '%') 
            if x != 0:
                query = query + 'AND'
            query = query + ('(%s LIKE "%s") ' % (str(title_table[x]), str(data)))
            x += 1
    
    results = query_collaborator(query)
    show_results(frame_view, results)

def show_results(frame_view, results):
    def edit_fetchall(results):
        matrix = []
        list_data = []
        for data in results:
            for item in data:
                list_data.append(item)
            matrix.append(list_data)
        return matrix
    
    def next_collaborator(x):
        x += 1

    def previous_collaborator(x):
        x -= 1
        if x < 0:
            x = 0

    def insert_data(matrix):
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

    x = 0
    matrix = edit_fetchall(results) 
    insert_data(matrix)    

    btn_before = Button(
        frame_view,
        text='Anterior',
        command=lambda x=x:previous_collaborator(x)
    )
    btn_before.place(x=10, y=10)

    btn_next = Button(
        frame_view,
        text= 'Próximo',
        command=lambda x=x:next_collaborator(x)
    )
    btn_next.place(x=300, y=10)