class Customer:
    static_id = 0
    def __init__ (self, name, oldm3, newm3):
        Customer.static_id += 1
        self.id = 'KH' + str(Customer.static_id).zfill(2)
        self.name = name
        self.consumed = newm3 - oldm3

def get_bill(customer):
    if customer.consumed <= 50:
        return (customer.consumed * 100) * 1.02
    elif customer.consumed <= 100:
        return (50*100 + (customer.consumed-50)*150) * 1.03
    else:
        return (50*100 + 50*150 + (customer.consumed-100)*200) * 1.05

def rank_customers(customers):
    return sorted(customers, key = get_bill, reverse = True)

def input_customer(tess):
    customers = []
    for i in range(tess):
        name = input()
        oldm3 = int(input())
        newm3 = int(input())
        customers.append(Customer(name, oldm3, newm3))
    return customers

def main():
    tess = int(input())
    customers = input_customer(tess)
    customers = rank_customers(customers)
    for customer in customers:
        print(customer.id , customer.name, round(get_bill(customer)))

    
main()