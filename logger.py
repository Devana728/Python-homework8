def write_to_base(a):
    with open('base.txt', 'a', encoding='utf-8') as base:
        base.write(f'{a}')

def read_base():
    a = []
    with open ('base.txt', 'r', encoding='utf-8') as base:
    
        for i in base:
            a.append(i)
    return a
def write_edited (mass):
    with open ('base.txt', 'w+', encoding='utf-8') as base:
        for i in mass:
            base.write(i)

