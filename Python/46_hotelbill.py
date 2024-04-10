class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def count_leaf_years(date):
    years = date.year
    if date.month <= 2:
        years -= 1
    return years // 4 - years // 100 + years // 400

def count_days(date):
    total_days = date.year * 365 + date.day
    for i in range(date.month - 1):
        total_days += month_days[i]
    total_days += count_leaf_years(date)
    return total_days

def calc_days_diff(date1, date2):
    d1, m1, y1 = map(int, date1.split('/'))
    d2, m2, y2 = map(int, date2.split('/'))
    date1 = Date(d1, m1, y1)
    date2 = Date(d2, m2, y2)
    total_days1 = count_days(date1)
    total_days2 = count_days(date2)
    return abs(total_days2 - total_days1) + 1

class Customer:
    static_id = 0
    def __init__ (self, name, room_number, day_in, day_out, cost_overrun):
        Customer.static_id += 1
        self.id = 'KH' + str(Customer.static_id).zfill(2)
        self.name = name
        self.room_number = room_number
        self.day_in = day_in
        self.day_out = day_out
        self.cost_overrun = cost_overrun

def get_bill(customer):
    floor_cost = [25, 34, 50, 80]
    days = calc_days_diff(customer.day_in, customer.day_out)
    return floor_cost[int(customer.room_number[0]) - 1] * days + customer.cost_overrun

def rank_customers(customers):
    return sorted(customers, key = get_bill, reverse = True)

def input_customer(tess):
    customers = []
    for _ in range(tess):
        name = input()
        room_number = input()
        day_in = input()
        day_out = input()
        cost_overrun = int(input())
        customers.append(Customer(name, room_number, day_in, day_out, cost_overrun))
    return customers

def main():
    tess = int(input())
    customers = input_customer(tess)
    customers = rank_customers(customers)
    for customer in customers:
        print(customer.id , customer.name, customer.room_number, calc_days_diff(customer.day_in, customer.day_out), round(get_bill(customer)))

    
main()