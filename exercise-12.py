# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

def toxin_list(ingredients):
  if 'sodium nitrate' in ingredients:
    return True
  elif 'sodium benzoate' in ingredients:
    return True
  elif 'sodium oxide' in ingredients:
    return True
  return False

def check_for_toxins(ingredients):
    if (toxin_list(ingredients)):
        print('!!!')
        print('there is a toxin in the food!')    
        print('!!!')
        make_alert_sound()
        return
    else:
        print('***')
        print('Toxin Free')
        print('***')
        make_accept_sound()
        return

# test

if __name__ == "__main__":
  ingredients = ['sodium benzoate']
  check_for_toxins(ingredients)
  