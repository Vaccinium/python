"""
Задание 4. Функции высшего порядка и lambda.
"""

from collections.abc import Callable


def filter_and_sort(
    campaigns: list[dict],
    predicate: Callable[[dict], bool],
    key: Callable[[dict], object] | None = None,
    reverse: bool = False,
) -> list[dict]:
    """
    Отфильтровать campaigns по predicate(campaign) -> bool, затем
    отсортировать оставшиеся по key (как key= в sorted()).

    Вернуть НОВЫЙ список - campaigns не должен изменяться (в том числе его
    порядок).

    Пример:
        filter_and_sort(
            [{"campaign_id": "a", "clicks": 10}, {"campaign_id": "b", "clicks": 0}],
            predicate=lambda c: c["clicks"] > 0,
        )
        -> [{"campaign_id": "a", "clicks": 10}]
    """
    # Новый список для кампаний, прошедших фильтр
    filtered = []
    for campaign in campaigns:
        # predicate - это функция, которую нам передали: она отвечает True или False
        if predicate(campaign):
            filtered.append(campaign)

    # sorted() сам создаёт новый список. Если key равен None,
    # sorted сортирует элементы как есть, так что отдельная проверка не нужна
    result = sorted(filtered, key=key, reverse=reverse)
    return result


# TODO: замените None на lambda-выражение (именно lambda, не def).
#
# Ключ для сортировки кампаний: по CTR (clicks / impressions) по убыванию;
# при равном CTR - по campaign_id по возрастанию (лексикографически).
# Если impressions == 0, считать CTR равным 0 (а не бросать исключение).
#
# Использование: sorted(campaigns, key=ctr_desc_then_id_asc)
ctr_desc_then_id_asc = lambda c: (
    (-c["clicks"] / c["impressions"]) if c["impressions"] > 0 else 0,
    c["campaign_id"],
)


if __name__ == "__main__":
    sample = [
        {"campaign_id": "ADV01-002", "impressions": 1000, "clicks": 50, "spend": 30.0},
        {"campaign_id": "ADV01-001", "impressions": 1000, "clicks": 50, "spend": 25.0},
        {"campaign_id": "ADV02-001", "impressions": 0, "clicks": 0, "spend": 0.0},
    ]
    print(sorted(sample, key=ctr_desc_then_id_asc))
    print(filter_and_sort(sample, predicate=lambda c: c["impressions"] > 0, key=ctr_desc_then_id_asc))
