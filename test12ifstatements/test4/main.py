def should_serve_customer(customer_age, on_break, time):
    return (customer_age >= 21) and (on_break == False) and (time >= 5 and time <= 10)

test = should_serve_customer(41, False, 1)
print(test) 
