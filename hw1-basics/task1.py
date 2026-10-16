"""
Задание 1. Расшифровка.

ИИ-ассистент выгрузил маркетинговый отчёт зашифрованным шифром Цезаря -
теперь его нужно расшифровать вручную.
"""


def decode_caesar_cipher(text: str, shift: int) -> str:
    """
    Расшифровать text, зашифрованный шифром Цезаря со сдвигом shift.

    Каждая латинская буква в исходном (незашифрованном) тексте была сдвинута
    вперёд по алфавиту на shift позиций (с переходом с 'z' на 'a' и с 'Z' на 'A').
    Регистр буквы должен сохраняться. Все остальные символы - цифры, пробелы,
    знаки препинания - в тексте не менялись при шифровании и должны остаться
    как есть при расшифровке.

    Пример: decode_caesar_cipher("Khoor!", 3) -> "Hello!"
    """
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""
    for symbol in text:
        if symbol in small_letters:
            position = small_letters.index(symbol)
            new_position = (position - shift) % 26
            result = result + small_letters[new_position]
        elif symbol in big_letters:
            position = big_letters.index(symbol)
            new_position = (position - shift) % 26
            result = result + big_letters[new_position]
        else:
            result = result + symbol

    return result


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("data/task1_encoded.txt", encoding="utf-8") as f:
        encoded_text = f.read().strip()

    shift = 7
    print(decode_caesar_cipher(encoded_text, shift))
