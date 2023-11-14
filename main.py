import tkinter as tk
from tkinter import ttk


def create_column(parent, title):
    frame = tk.Frame(parent, borderwidth=2, relief='groove')
    label = tk.Label(frame, text=title, bg='lightgrey', fg='black')
    label.pack(fill='x')
    return frame


# Основное окно
root = tk.Tk()
root.title('Kanban Board')

# Контейнер для столбцов
columns = tk.Frame(root)
columns.pack(fill='both', expand=True)

# Создание столбцов

backlog_column = create_column(columns, 'Backlog')
backlog_column.pack(side='left', fill='both', expand=True)

grooming_column = create_column(columns, 'Grooming')
grooming_column.pack(side='left', fill='both', expand=True)

todo_column = create_column(columns, 'To Do')
todo_column.pack(side='left', fill='both', expand=True)

in_progress_column = create_column(columns, 'In Progress')
in_progress_column.pack(side='left', fill='both', expand=True)

done_column = create_column(columns, 'Done')
done_column.pack(side='left', fill='both', expand=True)


# Запуск главного цикла
root.mainloop()
