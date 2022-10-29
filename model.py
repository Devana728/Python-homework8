def search_data(user_data):
    with open ('base.txt', 'r', encoding='utf-8') as base:
        for i in base:
            if i.find(user_data)!=-1:
                return i

