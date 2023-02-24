

# by Kami Bigdely
# Remove control flag

def find_item_in_container(item, container):
    for checked_item in container:
        if item == checked_item:
            return item
    return None

if __name__ == "__main__":
    food = 'wesabi'
    food_list = ['onion', 'cucumber','Guacamole', 'kabob barg', 'wesabi']
    found_item = find_item_in_container(food, food_list)
    print(food, "Found: " + found_item  if found_item != None else "not found")