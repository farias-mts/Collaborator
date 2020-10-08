from .models import new_line

def destroy_childrens(frame_view):
    for children in frame_view.winfo_children():
        children.destroy()

def insert_line(nameLine, abbreviation, typeLine):
    from .views import return_status
    status = new_line(nameLine, abbreviation, typeLine)
    return_status(status)
    