class Customer:
    static_id = 0
    def __init__(self, name, threshold, index_before, index_after):
        Customer.static_id += 1
        self.id = 'KH' + str(Customer.static_id).zfill(2)
        self.name = name
        self.classification = threshold
        self.index_before = index_before
        self.index_after = index_after

    def get_threshold(self):
        if self.classification == 'A':
            return 100
        elif self.classification == 'B':
            return 500
        elif self.classification == 'C':
            return 200
            
def get_bill(customer):
    threshold = customer.get_threshold()
    electric_used = customer.index_after - customer.index_before
    if electric_used <= threshold:
        return (electric_used * 450, 0, 0)
    else:
        money_exceed = (electric_used - threshold)*1000
        return (threshold * 450, money_exceed, money_exceed // 20)
    
def total_cost(customer):
    return sum(get_bill(customer))

def rank(customers):
    return sorted(customers, key=total_cost, reverse=True)

def standardization(name):
    for i in range(len(name)):
        if not name[i].isalpha() and name[i] != " ":
            name = name[:i] + name[i + 1:]
    name = name.split()
    name = [x.capitalize() for x in name]
    return " ".join(name)

def input_customers(tess):
    customers = []
    for _ in range(tess):
        name = standardization(input())
        threshold, index_before, index_after = input().split()
        index_before, index_after = map(int, [index_before, index_after])
        customers.append(Customer(name, threshold, index_before, index_after))

    return customers

def main():
    tess = int(input())
    customers = input_customers(tess)
    customers = rank(customers)

    for customer in customers:
        money_under, money_exceed, tax = get_bill(customer)
        print(customer.id, customer.name, money_under, money_exceed, tax, total_cost(customer))


main()
