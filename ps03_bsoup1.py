from deep_translator import GoogleTranslator
import requests
from bs4 import BeautifulSoup


# Функция получения случайного английского слова и его определения
def get_word():
    url = "https://randomword.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    word = soup.find("div", id="random_word").text.strip()
    definition = soup.find("div", id="random_word_definition").text.strip()

    return word, definition


# Основная функция игры
def word_game():
    print("🎮 Добро пожаловать в игру! Угадай слово по его определению 🎯")

    score_correct = 0  # счёт правильных ответов
    score_wrong = 0  # счёт ошибок

    while True:
        word, definition = get_word()

        # Переводим слово и определение на русский
        translated_word = GoogleTranslator(source='auto', target='ru').translate(word)
        translated_definition = GoogleTranslator(source='auto', target='ru').translate(definition)

        print(f"\n📘 Значение слова: {translated_definition}")
        user_input = input("👉 Что это за слово на английском? ").strip().lower()

        if user_input == word.lower():
            print("✅ Верно! Молодец!")
            score_correct += 1
        else:
            print(f"❌ Неверно. Загаданное слово было: {word}")
            score_wrong += 1

        again = input("\n🔁 Хотите сыграть ещё раз? (y/n): ")
        if again.strip().lower() != 'y':
            print("\n📊 Ваш счёт:")
            print(f"✅ Правильных ответов: {score_correct}")
            print(f"❌ Неправильных ответов: {score_wrong}\n")
            print("Спасибо за игру! 👋")
            break


if __name__ == "__main__":
    word_game()
