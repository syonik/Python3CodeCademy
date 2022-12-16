tables = {
    1: {
        'name': 'Chioma',
        'vip_status': False,
        'order': {
            'drinks': 'Orange Juice, Apple Juice',
            'food_items': 'Pancakes',
            'total': [534.50, 20.0, 5]
        }
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}


def assign_table(table_number, name, vip_status=False):
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = {}


assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)


def assign_food_items(table_number, **order_items):
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks


print('\n --- tables after update --- \n')

assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')
print(tables)


def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)


table_2_total = [534.50, 20.0, 5]
calculate_price_per_person(*table_2_total)
