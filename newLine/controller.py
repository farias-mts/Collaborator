def destroy_childrens(frame_view):
    for children in frame_view.winfo_children():
        children.destroy()