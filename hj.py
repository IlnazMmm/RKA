import tkinter as tk
from PIL import Image, ImageTk
# 1564399367.jpg

class Attraction:
    def __init__(self, name, description, image_path, adress):
        self.name = name
        self.description = description
        self.image_path = image_path
        self.adress = adress

def add_end_date():
    entry_window = tk.Toplevel(root)
    entry_window.title("Добавить дату завершения мероприятия")

    entry_label = tk.Label(entry_window, text="Введите дату завершения мероприятия:")
    entry_label.pack()

    entry = tk.Entry(entry_window)
    entry.pack()

# Функция для создания окна с полной информацией
def show_details(attraction):
    details_window = tk.Toplevel(root)
    details_window.title("Детали достопримечательности")

    frame = tk.Frame(details_window, bg="lightgrey")
    frame.pack(fill=tk.BOTH, expand=True)


    # Изменение размера изображения
    image = Image.open(attraction.image_path)
    image = image.resize((200, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(details_window, image=photo)
    image_label.image = photo
    image_label.pack()

    # Добавление названия и описания
    name_label = tk.Label(details_window, text=f"Название: {attraction.name}")
    name_label.pack()

    description_label = tk.Label(details_window, text="Описание:")
    description_label.pack()

    description_text = tk.Text(details_window, height=10, width=30)
    description_text.insert(tk.END, attraction.description)
    description_text.config(state='disabled')
    description_text.pack()

    adress_label = tk.Label(details_window, text=f"Адресс: {attraction.adress}")
    adress_label.pack()

# Функция добавления достопримечательности
def add_attraction():
    name = attraction_name_entry.get()
    description = attraction_description_entry.get()
    image_path = image_path_entry.get()
    adress = adress_entry.get()
    attraction = Attraction(name, description, image_path, adress)
    create_attraction_frame(attraction)

# Функция создания рамки для достопримечательности
def create_attraction_frame(attraction):
    attraction_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
    attraction_frame.pack(padx=5, pady=5, fill=tk.X)

    # Добавление изображения
    image = Image.open(attraction.image_path)
    image = image.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(attraction_frame, image=photo)
    image_label.image = photo
    image_label.pack(side=tk.LEFT, padx=5, pady=5)

    # Добавление названия и описания
    name_label = tk.Label(attraction_frame, text=f"Название: {attraction.name}")
    name_label.pack(anchor=tk.W, padx=5, pady=5)

    description_label = tk.Label(attraction_frame, text=f"Описание: {attraction.description}")
    # description_label.pack(anchor=tk.W, padx=5, pady=5)
    description_text = tk.Text(attraction_frame, height=3, width=30)
    description_text.insert(tk.END, attraction.description)
    description_text.config(state='disabled')
    description_text.pack(anchor=tk.W, padx=5, pady=5)

    # Кнопка "Подробнее"
    details_button = tk.Button(attraction_frame, text="Подробнее", command=lambda: show_details(attraction))
    details_button.pack(padx=5, pady=5)

    delete_button = tk.Button(attraction_frame, text="Удалить", command=lambda: delete_attraction(attraction_frame))
    delete_button.pack(padx=5, pady=5)


def delete_attraction(attraction_frame):
    attraction_frame.destroy()


# Создание основного окна
root = tk.Tk()
root.title("Travel Helper")

# Создание виджетов
attraction_name_label = tk.Label(root, text="Название достопримечательности:")
attraction_name_label.pack()

attraction_name_entry = tk.Entry(root)
attraction_name_entry.pack()

attraction_description_label = tk.Label(root, text="Описание:")
attraction_description_label.pack()

attraction_description_entry = tk.Entry(root)
attraction_description_entry.pack()

image_path_label = tk.Label(root, text="Путь к изображению:")
image_path_label.pack()

image_path_entry = tk.Entry(root)
image_path_entry.pack()

adress_label = tk.Label(root, text="Адресс:")
adress_label.pack()

adress_entry = tk.Entry(root)
adress_entry.pack()

add_button = tk.Button(root, text="Добавить", command=add_attraction)
add_button.pack(side=tk.LEFT)

add_date_button = tk.Button(root, text="Дату мероприятия", command=add_end_date)
add_date_button.pack(side=tk.RIGHT)

# Запуск приложения
root.mainloop()
