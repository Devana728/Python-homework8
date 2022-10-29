
import ui
import model
import logger


def start_work():
    return ui.get_user_data()


def search_work():
    user_data = ui.get_user_data('Введите данные сотрудника для поиска: \n')
    return model.search_data(user_data)


def add_data_work():
    id = ui.get_user_data('Введите id сотрудника: ')
    name = ui.get_user_data('Введите ФИО сотрудника: ')
    phone = ui.get_user_data('Введите номер телефона сотрудника: ')
    post = ui.get_user_data('Введите должность сотрудника: ')
    cost = ui.get_user_data('Введите зарплату сотрудника: ')
    return (f'\n{id} || {name} || {phone} || {post} || {cost}\n')


def write_to_file(a):
    logger.write_to_base(a)

#def edit_work():
    #old_string = search_work()
    #ui.print_data(old_string)
    #ui.print_data('Введите новые данные для сотрудника:')
    #new_string = add_data_work()
    #logger.edit_base(old_string, new_string)
def edit_work(mass):
    a = input ('Введите данные сотрудника для редактирования: \n')
    
    staff = []
    index = 0
    for i in range(len(mass)):
        if mass[i].find(a) != -1:
            staff = mass[i].split('||')
            print(staff)
            index = i
    atr = int(input(f'Выберите позицию для редактирования:\n \
        {staff[0]} - 0\n \
        {staff[1]} - 1\n \
        {staff[2]} - 2\n \
        {staff[3]} - 3\n \
        {staff[4]} - 4\n \
            '))
    staff[atr] = input('Новое значение: ')
    staff = '||'.join(staff)
    mass[index] = staff
    return mass

while True:
    mode = int(start_work())
    if mode == 1:
        ui.print_data(search_work())
    elif mode == 2:
        write_to_file(add_data_work())
    elif mode == 3:
        
        base = logger.read_base()
        new_base = edit_work(base)
        logger.write_edited(new_base)
        
    else:
        print('такого режима нет')
        break
