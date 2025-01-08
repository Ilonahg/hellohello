from typing import List, Dict

def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список банковских операций по заданному состоянию.

    :param transactions: Список словарей с данными о банковских операциях.
    :param state: Состояние для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список, содержащий только те операции, у которых ключ 'state' равен переданному значению.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список банковских операций по дате.

    :param transactions: Список словарей с данными о банковских операциях.
    :param descending: Порядок сортировки (по умолчанию убывание).
    :return: Новый список, отсортированный по дате.
    """
    return sorted(transactions, key=lambda x: x.get('date'), reverse=descending)
