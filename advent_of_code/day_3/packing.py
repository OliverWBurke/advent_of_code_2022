def find_value(letter):
    raw_value = ord(letter)
    if raw_value > 96:
        return raw_value - 96
    else:
        return raw_value - 38


def find_duplicate_value(items):

    number_of_items = len(items)
    compartment_1 = items[:int(number_of_items/2)]

    compartment_2 = items[int(number_of_items/2):]

    duplicate = set(compartment_1) & set(compartment_2)

    duplicate_raw_value = ord(list(duplicate)[0])
    if duplicate_raw_value > 96:
        duplicate_value = duplicate_raw_value - 96
    else:
        duplicate_value = duplicate_raw_value - 38
    return find_value(list(duplicate)[0])


with open("advent_of_code\day_3\data.txt", mode="r") as data_file:
    data = data_file.read().split("\n")


duplicate_values = [find_duplicate_value(rucksack) for rucksack in data[:-1]]

print(f"Duplicate Values are: {sum(duplicate_values)}")


badge_total = 0
for i in range(0, len(data)-1, 3):
    bag_1 = set(data[i])
    bag_2 = set(data[i+1])
    bag_3 = set(data[i+2])

    common = set(bag_1) & set(bag_2) & set(bag_3)
    value = find_value(list(common)[0])
    badge_total += value

print(f"The total priority for badges is : {badge_total}")
