"""
Задание 2. Парсинг лога.

В расшифрованном в задании 1 отчёте указано, для какого пользователя и с
какого времени искать подозрительную активность. Нужно найти в логе все
события этого пользователя, случившиеся строго позже указанного времени.
"""


def filter_events_after(log_lines: list[str], user: str, after_time: str) -> list[str]:
    """
    Вернуть строки лога log_lines, относящиеся к пользователю user, время
    которых строго позже after_time.

    Формат каждой строки лога: "<время> <пользователь> <событие>",
    например "19:05 alice export". Время - часы:минуты в 24-часовом
    формате; часы могут быть записаны без ведущего нуля (например, "9:05").

    Порядок строк в результате должен совпадать с их порядком во входных
    данных log_lines.

    Пример:
        filter_events_after(["10:00 alice login", "14:30 alice click"], "alice", "12:00")
        -> ["14:30 alice click"]
    """
    # переводим время, после которого ищем, в минуты
    after_parts = after_time.split(":")
    after_minutes = int(after_parts[0]) * 60 + int(after_parts[1])

    result = []
    for line in log_lines:
        parts = line.split()
        if len(parts) < 2:
            continue  # пропускаем пустые или странные строки

        line_time = parts[0]
        line_user = parts[1]

        # переводим время из строки лога в минуты
        time_parts = line_time.split(":")
        line_minutes = int(time_parts[0]) * 60 + int(time_parts[1])

        if line_user == user and line_minutes > after_minutes:
            result.append(line)

    return result


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("data/task2_log.txt", encoding="utf-8") as f:
        log_lines = [line.strip() for line in f if line.strip()]

    result = filter_events_after(log_lines, "mktbot7", "19:00")
    print(result)
