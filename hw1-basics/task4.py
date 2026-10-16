"""
Задание 4. Валидация CTR.

Следующий шаг - посчитать средний CTR по рекламным объявлениям. Часть
записей в выгрузке повреждена ИИ-ассистентом и должна быть исключена из
расчёта.
"""


def average_ctr(records: list[dict]) -> float:
    """
    records - список словарей вида
    {"ad_id": str, "impressions": int, "clicks": int}.

    Для каждой ЧИСТОЙ записи посчитать CTR = clicks / impressions и вернуть
    среднее арифметическое CTR по всем чистым записям (не взвешенное по
    показам).

    Запись считается «грязной» и должна быть исключена из расчёта, если
    выполняется хотя бы одно из условий:
      - impressions <= 0;
      - clicks < 0;
      - clicks > impressions.

    Если чистых записей не осталось вообще, вернуть 0.0.

    Пример:
        average_ctr([{"ad_id": "a", "impressions": 100, "clicks": 10}])
        -> 0.1
    """
    # Сумма CTR всех чистых записей
    total_ctr = 0.0
    # Сколько чистых записей нашли
    clean_count = 0

    for record in records:
        impressions = record["impressions"]
        clicks = record["clicks"]

        # Проверяем, что запись грязная: если да, пропускаем её
        if impressions <= 0:
            continue
        if clicks < 0:
            continue
        if clicks > impressions:
            continue

        # Запись чистая: считаем её CTR и добавляем к общей сумме
        ctr = clicks / impressions
        total_ctr = total_ctr + ctr
        clean_count = clean_count + 1

    # Если чистых записей нет, возвращаем 0.0
    # (эта проверка защищает от деления на ноль)
    if clean_count == 0:
        return 0.0

    # Среднее арифметическое = сумма CTR / количество записей
    return total_ctr / clean_count


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    import csv

    with open("data/task4_ads.csv", encoding="utf-8", newline="") as f:
        records = [
            {
                "ad_id": row["ad_id"],
                "impressions": int(row["impressions"]),
                "clicks": int(row["clicks"]),
            }
            for row in csv.DictReader(f)
        ]

    print(average_ctr(records))
