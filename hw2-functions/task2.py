"""
Задание 2. Уникальные рекламодатели.
"""


def unique_advertisers(campaign_ids: list[str]) -> list[str]:
    """
    campaign_ids - список ID кампаний вида "ADV07-014": рекламодатель
    ("ADV07") и номер кампании ("014") через дефис.

    Вернуть список рекламодателей без повторов, в порядке их ПЕРВОГО
    появления в campaign_ids. Пустой список на входе -> пустой список.

    Пример:
        unique_advertisers(["ADV07-014", "ADV01-002", "ADV07-015", "ADV03-009"])
        -> ["ADV07", "ADV01", "ADV03"]
    """
    result = []

    for campaign_id in campaign_ids:
        # Делим "ADV07-014" по дефису: первая часть - рекламодатель
        advertiser = campaign_id.split("-")[0]

        # Добавляем, только если такого рекламодателя ещё нет в результате
        if advertiser not in result:
            result.append(advertiser)

    return result


if __name__ == "__main__":
    sample = ["ADV07-014", "ADV01-002", "ADV07-015", "ADV03-009", "ADV01-003"]
    print(unique_advertisers(sample))
