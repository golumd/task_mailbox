"""Функция, которая подсчитывает число покупателей,
попадающих в каждую группу, если нумерация ID сквозная и начинается с 0.
На вход функция получает целое число n_customers (количество клиентов).
Функция, аналогичная первой, если ID начинается с произвольного числа.
На вход функция получает целые числа: n_customers (количество клиентов)
и n_first_id (первый ID в последовательности)."""

## Don't forget to pip numpy and pandas

import numpy as np
from collections import Counter

def customers_per_group(n_customers=0, n_first_id=0):

    ids = np.arange(n_first_id, n_first_id+n_customers)
    summed_ids = list(map(lambda x: np.array(list(map(int, list(str(x))))).sum(), ids))
    counter_res = Counter(summed_ids)

    if not summed_ids:
      return None

    return dict(counter_res)

def main():

    n_customers_in = 100 # test data
    n_first_id = 25 # test data


    print('RESULTS \n')

    # Manual tests

    cpg = customers_per_group()
    print(f'customers_per_group(): {cpg} \n')

    cpg = customers_per_group(n_customers_in)
    print(f'customers_per_group({n_customers_in}): {cpg} \n')

    cpg = customers_per_group(n_customers_in, n_first_id)
    print(f'customers_per_group({n_customers_in},{n_first_id}): {cpg} \n')

    # User input
    
    while True:
        try:
            n_custs = int(input('Input int positive N for amount of customers: '))
            first_id = input('Input int positive M to determine the first id: ')

            if first_id != "":
                first_id = int(first_id)
            else:
                first_id = 0

        except ValueError:
            print("illiquid value \n")
            continue

        if n_custs < 0 or first_id < 0:
            print("Sorry, your response must be positive.\n")
            continue

        else:
            cpg = customers_per_group(n_custs, first_id)
            print(f'customers_per_group({n_custs}, {first_id}): {cpg} \n')
            break

if __name__=='__main__':
    main()