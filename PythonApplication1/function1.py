def read_file(file: str) -> list:
    """
    loeme failist
    :param str file: faili nimi
    :param list mas: nimekiri
    """
    fail = open(file, 'r', encoding="utf-8-sig")
    mas = []
    for row in fail:
        if row.isdigit():
            mas.append(row.strip())
        else:
            mas.append(row.strip())
    fail.close()
    return mas


def save_to_file(mas: list, file: str):
    """
    salvestame loetelu failisse
    :param str file: faili nimi
    :param list mas: loetelu
    """
    f = open(file, 'w', encoding="utf-8-sig")
    for item in mas:
        f.write(item + '\n')
    f.close()


def write_workers_and_birthdays_to_file(b: list, l: list):
    n = int(input('How many worker do you want to add ?:'))
    for j in range(n):
        name = input('name:')
        l.append(name)
        birthday = input('birthday:')
        b.append(birthday)
    return b, l


def delete_worker(name: str, b: list, l: list):
    n = l.count(name)
    pos = 0
    print(name, n)
    for i in range(n):
        ind = l.index(name, pos)
        pos = ind + 1
        l.remove(name)
        b.pop(ind)
    return l, b


def youngest_workers(zipped: list):
    """
    :param zipped:list
    """
    top_low = sorted(zipped)[:10]
    print(f"number of top 10 the youngest workers: {top_low}")

def oldest_workers(zipped: list):
    """
    :param zipped:list
    """
    top_high = sorted(zipped, reverse = True)[:10]
    print(f"number of top 10 oldest workers: {top_high}")



def average_ages(b: list, l: list):
    """
    :param p:list
    :param i:list
    """
    b = list(map(int, b))
    avg_age = sum(b) / len(b)
    avg_age = int(avg_age)
    if avg_age in b:
        v = b.index(avg_age)
        print(f'{avg_age} {l[v]}')
    else:
        print(f'average year of birth is {avg_age}')
    return avg_age


def year_worker(l:list,b:list):
    """
    :param p:list
    :param i:list
    """
    b=list(map(int,b))
    pos=0
    n=int(input('input year:'))
    ind=b.index(n,pos)
    n=print(l[ind])
    pos=ind+1


def pensioner(zipped: list):
    """
     reunions elements
    : param zipped: list
    """
    pensioner_year = 1962
    now_year = 2023
    for i in zipped:
        birth_year = int(i[0])
        age = now_year - birth_year
        if birth_year < pensioner_year:
            print(f"name  {i[1]}. date of birth {i[0]}. him {age} year.")