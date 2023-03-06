from function1 import *

while True:
    print(f'-----------------------------------------------------------------------------------------------')
    print(
        f'\n0 Read from the file\n1 Insert workers and birthday,'
        f'\n2 Save to the file.\n3 The Youngest workers,'
        f'\n4 The Oldest workers,'
        f'\n5 An Average year of 'f'birth,\n6 Worker years '
        f'\n7 Pensioners\n8 Delete'
        f'\n9 Exit')
    v = input('---:')
    if v == '0':
        workers = []
        birthday = []
        workers = read_file('workers_file.txt')
        birthday = read_file('birthday_file.txt')

        zipped = list(zip(workers, birthday))
        #Функция zip() принимает на входе несколько итерируемых объектов (iterable) или итераторов (iterators) и поэлементно группирует в кортежи
        print(workers)
        print(birthday)



    elif v == '1':
        workers, birthday = write_workers_and_birthdays_to_file(workers, birthday)
        print(birthday)
        print(workers)

    elif v == '2':
        save_to_file(workers, 'workers_file.txt')
        save_to_file(birthday, 'birthday_file.txt')


    elif v == '3':
        youngest_workers(zipped)
    elif v == '4':
        oldest_workers(zipped)
    elif v == '5':
        average_ages(workers, birthday)
    elif v == '6':
        year_worker(birthday, workers)
    elif v == '7':
        pensioner(zipped)
    elif v == '8':
        birthday, workers = delete_worker(input('name:'), birthday, workers)
        print(workers)
        print(birthday)

    elif v == '9':
        break