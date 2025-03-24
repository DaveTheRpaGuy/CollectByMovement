import random

def main():
    seed = 69
    if (seed):
        random.seed(seed)
    print("testing")
    item_types = [line.strip() for line in open("resources/item_types.txt", 'r')]
    collected = {}
    countdown = 10
    
    while (countdown > 0):
        countdown-=1
        item_index = random.randint(0, len(item_types)-1)
        item_name = item_types[item_index]
        item_count = random.randint(1, 20)
        #print(f"Item Index: {item_index}")
        #print(f"Picked up {item_count} {item_name}")
        if (item_name in collected):
            collected[item_name] += item_count
        else:
            collected[item_name] = item_count
    print("Here is a summary of what you collected:")
    for item_name in collected.keys():
        print(f"{collected[item_name]} {item_name}")

    #next_step = input("ENTER to e")

main()