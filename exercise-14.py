# by Kami Bigdely
# Consolidate conditional expressions


def check_ingredients(ingredients, recipe):
  for ingredient in recipe:
      if ingredient not in ingredients:
        print('lacks ingredients' )
        return
def dice(ingredients):
    print("diced all ingredients.")
def mix_all(diced_ingredients):
    print("mixed all.")
def add_salt():
    print('added salt.')
def pour(liquid):
    print('poured', liquid + '.',)

def make_shirazi_salad(ingredients, recipe=['cucumber', 'tomato', 'lemon juice', 'onion']):
    check_ingredients(ingredients, recipe)
    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')

if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])