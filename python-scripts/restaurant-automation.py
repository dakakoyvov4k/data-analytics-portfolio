tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
    6: None,
    7: None,
    8: None,
    9: None,
}

lst = ['salad', 'soup', 'main_dish', 'drink', 'desert']

def delete_reservation(a: int) -> None:
    global tables
    tables[a] = None

def get_free_tables() -> list:
    global tables
    a = []
    for i in tables:
        if tables[i] is None:
            a.append(i)
    return a

def is_table_free(a: int) -> bool:
    global tables
    if tables[a] is None:
        return True
    else:
        return False

def reserve_table(a: int, name: str, is_vip=False):
    global tables
    if is_table_free(a) == True:
        tables[a] = {'name': name, 'is_vip': is_vip, 'order': {}}

def make_order(n: int, **kwargs):
    for k, v in kwargs.items():
        if k in lst:
            tables[n]['order'][k] = tables[n]['order'].get(k, []) + v.split(',')

def delete_order(*, number_table: int, delete_all=False, **kwargs):
    if delete_all == True:
        tables[number_table]['order'] = {}
    else:
        for k, v in kwargs.items():
            if k in lst and v == True:
                tables[number_table]['order'].pop(k, None)
