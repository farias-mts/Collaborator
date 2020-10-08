from .models import query_collaborator
import os

def destroy_childrens(frame_view):
    for children in frame_view.winfo_children():
        children.destroy()

def search_collab(frame_view, colaborador, matricula, gestor, linha, area):
    from .views import insert_data
    title_table = ['nome', 'matricula', 'gestor', 'linhas', 'area']
    datas = [colaborador, matricula, gestor, linha, area]
    query = 'WHERE'
    x=0
    indice = 0
    for data in datas:
        if data != '':
            for char in '*':
                data = data.replace(char, '%') 
            if x != 0:
                query = query + 'AND'
            query = query + ('(%s LIKE "%s") ' % (str(title_table[indice]), str(data)))
            x += 1
        indice += 1
    if x == 0:
        query = ''
    results = query_collaborator(query)
    ind_list=0
    global matrix
    matrix = edit_fetchall(results)
    insert_data(ind_list, frame_view, matrix)

def edit_fetchall(results):
    matrix_data = []
    list_data = []
    for data in results:
        list_data.clear()
        for item in data:
            list_data.append(item)
        matrix_data.append(list_data[:])
    return matrix_data
    
def next_collaborator(event, ind_list, frame_view):
    from .views import insert_data
    ind_list += 1
    if ind_list>=len(matrix):
        ind_list=len(matrix)-1
    else: 
        destroy_childrens(frame_view)
        insert_data(ind_list, frame_view, matrix)

def previous_collaborator(event, ind_list, frame_view):
    from .views import insert_data
    ind_list -= 1
    if ind_list<=0:
        ind_list = 0
    else:
        destroy_childrens(frame_view)
        insert_data(ind_list, frame_view, matrix)

def save_edit(collaborator_box, registration_box, manager_box, line_box, job_box):
    print(collaborator_box)
    