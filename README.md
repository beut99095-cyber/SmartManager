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

def say_shynakov():
    print("shynakov")

say_shynakov()

print("Это главная ветка main")


print('Это именная ветка shynakov')

print('Это главная ветка main')
