from .models import new_collaborator

def destroy_childrens(frame_view):
    for children in frame_view.winfo_children():
        children.destroy()

def insert_collab(ifile, nameCollab, registration, manager, line, job):
    from .views import return_status
    photo = open(ifile.name, 'rb').read()
    status = new_collaborator(photo, nameCollab, registration, manager, line, job)
    return_status(status)



