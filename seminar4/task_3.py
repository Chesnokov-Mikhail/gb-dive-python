"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""
from decimal import Decimal

# Сумма денег в банкомате. начальная = 0
summ_atm = Decimal(0)
# Счетчик операций
count_oper = 0
# Список для сохранения всех операций поступления и снятия средств
operation_list = list()

# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
PERCENT_ISSUE = 1.5
MIN_COMMISSION = 30
MAX_COMMISSION = 600

# процент начисления после каждой PROCENT_COUNT_NUM операции - 3%
PROCENT_COUNT = 3
# Число операций для начисления процентов
PROCENT_COUNT_NUM = 3
# налог на богатство в процентах
WEALTH_TAX = 10
# минимальная сумма для налога на богатство в процентах
MIN_SUMM_WEALTH_TAX = 5_000_000

def save_operation(sum: int):
    """Функция для сохранения операций поступления и снятия"""
    global operation_list
    operation_list.append(sum)

def deduct_wealth_tax():
    """вычитать налог на богатство 10% перед каждой операцией, даже ошибочной"""
    global summ_atm
    if summ_atm > MIN_SUMM_WEALTH_TAX:
        print(f"Сумма {summ_atm.quantize(Decimal('1.00'))} больше {MIN_SUMM_WEALTH_TAX}. Вычитание налога на богатство {WEALTH_TAX}%")
        summ_atm = Decimal(summ_atm) * Decimal((100 - WEALTH_TAX) / 100)

def interest_calculation():
    """После каждой третей операции пополнения или снятия начисляются проценты PROCENT_COUNT"""
    global summ_atm
    if count_oper % 3 == 0:
        summ_atm = Decimal(summ_atm) * Decimal((100 + PROCENT_COUNT)/100)
        print(f"Номер операции {count_oper}. Начисление процентов за {PROCENT_COUNT_NUM} операции пополнения или снятия {PROCENT_COUNT}%")

def print_sum_atm():
    """выводит сумму денег в банкомате"""
    print(f"Сумма в банкомате: {summ_atm.quantize(Decimal('1.00'))} у.е.")
def replenish(sum: int) -> bool:
    """Пополнить счет в банкомате"""
    global summ_atm
    global count_oper
    summ_atm = Decimal(summ_atm) + Decimal(sum)
    count_oper += 1
    save_operation(sum)
    return True

def issue(sum: int) -> bool:
    """Выдать сумму из банкомата"""
    global summ_atm
    global count_oper
    if summ_atm >= sum:
        summ_atm = Decimal(summ_atm) - Decimal(sum)
        count_oper += 1
        save_operation(-sum)
    else:
        return False
    return True

def go_out():
    """Выйти из банкомата"""
    exit()

def main():
    while True:
        print("Работа с банкоматом.")
        choice = input('Укажите действие (1 - пополнить; 2 - снять; 3 - выход): ')
        match int(choice):
            case 1:
                deduct_wealth_tax()
                sum_input = int(input("Введите сумму пополнения, кратную 50 у.е.: "))
                if sum_input % 50 == 0:
                    if replenish(sum_input):
                        print(f"Сумма {sum_input} внесена")
                    else:
                        print(f"Сумма {sum_input} не внесена")
                else:
                    print(f"Сумма {sum_input} не кратна 50 у.е., в операции отказано")
                interest_calculation()
            case 2:
                deduct_wealth_tax()
                sum_input = int(input("Введите сумму снятия, кратную 50 у.е.: "))
                if sum_input % 50 == 0:
                    if issue(sum_input):
                        print(f"Сумма {sum_input} снята")
                    else:
                        print(f"Сумма {sum_input} не может быть снята")
                else:
                    print(f"Сумма {sum_input} не кратна 50 у.е., в операции отказано")
                interest_calculation()
            case 3:
                go_out()

        print_sum_atm()

if __name__ == "__main__":
    main()