"""
Задание 1. Рефакторинг отчёта по кампаниям.

Скрипт ИИ-ассистента (messy_code.py) считает то же самое, но написан плохо и
содержит баги. Ваша задача - реализовать те же вычисления как отдельные
функции с чёткими контрактами и БЕЗ багов оригинала. Посмотрите
messy_code.py и запустите его (`python messy_code.py`), прежде чем начинать -
там видно, что именно идёт не так.
"""


def parse_campaign(line: str) -> dict:
    """
    line - строка вида "CID-001;15320;412;530.40"
    (campaign_id;impressions;clicks;spend), поля разделены `;`.

    Вернуть {"campaign_id": str, "impressions": int, "clicks": int, "spend": float}.

    Пример:
        parse_campaign("ADV01-001;1000;50;30.0")
        -> {"campaign_id": "ADV01-001", "impressions": 1000, "clicks": 50, "spend": 30.0}
    """
    # Делим строку по ";" на четыре части
    parts = line.split(";")

    # Превращаем текст в нужные типы: id остаётся строкой,
    # показы и клики становятся int, расходы - float
    campaign = {
        "campaign_id": parts[0],
        "impressions": int(parts[1]),
        "clicks": int(parts[2]),
        "spend": float(parts[3]),
    }
    return campaign


def calc_ctr(clicks: int, impressions: int) -> float:
    """
    CTR = clicks / impressions.

    Если impressions <= 0 - вернуть 0.0 (а не бросать исключение и не
    округлять до целого).

    Пример:
        calc_ctr(50, 1000) -> 0.05
        calc_ctr(0, 0) -> 0.0
    """
    # Защита от деления на ноль (и от отрицательных показов)
    if impressions <= 0:
        return 0.0

    # В Python 3 оператор / даёт дробное число, ничего не округляется
    return clicks / impressions


def calc_cpc(spend: float, clicks: int) -> float:
    """
    CPC = spend / clicks.

    Если clicks <= 0 - вернуть 0.0 (а не бросать исключение).

    Пример:
        calc_cpc(30.0, 50) -> 0.6
        calc_cpc(75.0, 0) -> 0.0
    """
    # Защита от деления на ноль (и от отрицательных кликов)
    if clicks <= 0:
        return 0.0

    return spend / clicks


def merge_duplicate_campaigns(records: list[dict]) -> list[dict]:
    """
    records - список словарей вида
    {"campaign_id": str, "impressions": int, "clicks": int, "spend": float},
    возможно с повторяющимися campaign_id (экспортёр иногда выгружает одну
    кампанию дважды).

    Для каждого повторяющегося campaign_id сложить impressions, clicks и
    spend в одну запись. Порядок записей в результате - по первому
    появлению campaign_id в records.

    Исходный список records и словари в нём менять нельзя: вернуть новые
    словари, а не дописывать суммы в записи из records.

    Пример:
        merge_duplicate_campaigns([
            {"campaign_id": "a", "impressions": 100, "clicks": 10, "spend": 5.0},
            {"campaign_id": "b", "impressions": 200, "clicks": 20, "spend": 8.0},
            {"campaign_id": "a", "impressions": 50, "clicks": 5, "spend": 2.0},
        ])
        -> [
            {"campaign_id": "a", "impressions": 150, "clicks": 15, "spend": 7.0},
            {"campaign_id": "b", "impressions": 200, "clicks": 20, "spend": 8.0},
        ]
    """
    # Словарь с итогами: {campaign_id: новая запись}.
    # Ключи лежат в порядке первого появления, это и нужный нам порядок
    merged = {}

    for record in records:
        campaign_id = record["campaign_id"]

        if campaign_id in merged:
            # Кампания уже встречалась - прибавляем к нашей копии
            merged[campaign_id]["impressions"] = merged[campaign_id]["impressions"] + record["impressions"]
            merged[campaign_id]["clicks"] = merged[campaign_id]["clicks"] + record["clicks"]
            merged[campaign_id]["spend"] = merged[campaign_id]["spend"] + record["spend"]
        else:
            # Кампания встретилась впервые - создаём НОВЫЙ словарь,
            # чтобы не менять запись из исходного списка
            merged[campaign_id] = {
                "campaign_id": campaign_id,
                "impressions": record["impressions"],
                "clicks": record["clicks"],
                "spend": record["spend"],
            }

    # Собираем результат в список в порядке первого появления
    result = []
    for campaign_id in merged:
        result.append(merged[campaign_id])
    return result


def format_report(rows: list[dict]) -> str:
    """
    rows - список словарей вида
    {"campaign_id": str, "impressions": int, "clicks": int, "spend": float}
    (уже без дублей - предполагается, что merge_duplicate_campaigns вызван
    раньше).

    Вернуть многострочный отчёт: по одной строке на кампанию, в том же
    порядке, что и в rows, в формате
    "{campaign_id}: CTR={ctr:.2%} CPC={cpc:.2f}", используя calc_ctr и
    calc_cpc.

    Пример:
        format_report([{"campaign_id": "a", "impressions": 1000, "clicks": 50, "spend": 30.0}])
        -> "a: CTR=5.00% CPC=0.60"
    """
    lines = []
    for row in rows:
        # Считаем метрики через уже написанные функции
        ctr = calc_ctr(row["clicks"], row["impressions"])
        cpc = calc_cpc(row["spend"], row["clicks"])

        # :.2% превращает 0.05 в "5.00%", :.2f оставляет два знака после точки
        line = f"{row['campaign_id']}: CTR={ctr:.2%} CPC={cpc:.2f}"
        lines.append(line)

    # Склеиваем строки через перевод строки (после последней он не нужен)
    return "\n".join(lines)


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("data/campaigns_sample.txt", encoding="utf-8") as f:
        records = [parse_campaign(line) for line in f if line.strip()]

    merged = merge_duplicate_campaigns(records)
    print(format_report(merged))
