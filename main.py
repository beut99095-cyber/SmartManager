import os


def setup_smart_manager():
    # Список папок для сортировки документов
    folders = ['Incoming_Docs', 'Sorted_Images', 'Reports']

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"✅ Создана папка: {folder}")
        else:
            print(f"ℹ️ Папка {folder} уже есть")


if __name__ == "__main__":
    print("--- Запуск SmartManager ---")
    setup_smart_manager()
    print("--- Подготовка завершена ---")

import os


def check_incoming():
    path = 'Incoming_Docs'
    files = os.listdir(path)

    if not files:
        print(f"📁 В папке '{path}' пока пусто. Положи туда что-нибудь!")
    else:
        print(f"🚀 Найдено файлов для обработки: {len(files)}")
        for f in files:
            print(f" - {f}")


if __name__ == "__main__":
    # Сначала создаем структуру (на всякий случай)
    folders = ['Incoming_Docs', 'Sorted_Images', 'Reports']
    for f in folders:
        if not os.path.exists(f):
            os.makedirs(f)

    print("--- Анализ документов ---")
    check_incoming()

import os
import shutil


def organize_files():
    incoming = 'Incoming_Docs'
    images_dir = 'Sorted_Images'
    docs_dir = 'Reports'

    files = os.listdir(incoming)

    if not files:
        print("📭 В папке Incoming_Docs пусто.")
        return

    for file in files:
        # Узнаем расширение файла
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            shutil.move(os.path.join(incoming, file), os.path.join(images_dir, file))
            print(f"📸 Картинка {file} перемещена в {images_dir}")

        elif file.lower().endswith(('.txt', '.pdf', '.doc', '.docx')):
            shutil.move(os.path.join(incoming, file), os.path.join(docs_dir, file))
            print(f"📄 Документ {file} перемещен в {docs_dir}")


if __name__ == "__main__":
    print("--- Запуск автоматической сортировки ---")
    organize_files()
    print("--- Готово! ---")

import os
import shutil
import time


def organize_files():
    incoming = 'Incoming_Docs'
    images_dir = 'Sorted_Images'
    docs_dir = 'Reports'

    files = os.listdir(incoming)

    for file in files:
        # Узнаем расширение файла
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            shutil.move(os.path.join(incoming, file), os.path.join(images_dir, file))
            print(f"📸 Картинка {file} перемещена в {images_dir}")

        elif file.lower().endswith(('.txt', '.pdf', '.doc', '.docx')):
            shutil.move(os.path.join(incoming, file), os.path.join(docs_dir, file))
            print(f"📄 Документ {file} перемещен в {docs_dir}")


if __name__ == "__main__":
    print("🚀 SmartManager запущен и следит за файлами...")
    print("Нажми Ctrl+C в консоли, чтобы остановить программу.")

    try:
        while True:
            organize_files()
            time.sleep(5)  # Ждем 5 секунд перед следующей проверкой
    except KeyboardInterrupt:
        print("\n👋 Программа остановлена.")

print("Изменино локально")

