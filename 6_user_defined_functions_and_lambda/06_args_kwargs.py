def total(*numbers):
    return sum(numbers)

def show_profile(**details):
    print(details)

print(total(10, 20, 30))
show_profile(name="Asha", role="Analyst")
