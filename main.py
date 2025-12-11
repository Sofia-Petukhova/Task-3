def is_cbs(lisp_reference: str) -> int:
    """
    Проверяет, является ли строка правильной скобочной последовательностью.

    Возвращает:
    1  — если строка является ПСП
    0  — если строка НЕ является ПСП
    -1 — если строка некорректна
    """
    if not isinstance(lisp_reference, str):
        return -1

    if len(lisp_reference) % 2 != 0:
        return -1

    if any(ch not in "()" for ch in lisp_reference):
        return -1

    balance = 0
    for ch in lisp_reference:
        balance += 1 if ch == "(" else -1

        if balance < 0:
            return 0  # закрывающей скобки больше, чем открывающих

    return 1 if balance == 0 else 0


def need_to_move(lisp_reference: str) -> int:
    """
    Возвращает минимальное количество перемещений одной скобки
    в начало или конец строки, чтобы сделать её ПСП.

    Возвращает -1, если строка некорректна.
    """
    if not isinstance(lisp_reference, str):
        return -1

    if len(lisp_reference) % 2 != 0:
        return -1

    if any(ch not in "()" for ch in lisp_reference):
        return -1

    if is_cbs(lisp_reference) == 1:
        return 0

    balance = 0
    min_balance = 0

    for ch in lisp_reference:
        balance += 1 if ch == "(" else -1
        min_balance = min(min_balance, balance)

    return -min_balance


def main():
    """Основной цикл программы."""
    print("Программа запущена")


if __name__ == "__main__":
    main()