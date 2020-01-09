mass_list = [int(line.rstrip('\n')) for line in open("input_assignment3.txt")]
from assignment_4 import timer

def calc_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel(fuel)

@timer
def total_fuel(mass):
    return sum([calc_fuel(m) for m in mass_list])

print(f"Total fuel necessary is {total_fuel(mass_list)}")