# by Kami Bigdely
# Consolidate duplicate conditional fragments
import json

class Drink:
  def __init__(self, mix=None):
    self.mix = mix if mix is not None else []
    pass

  def add_to_mix(self, something):
    self.mix.append(something)
    print(f'added {something} to mix.')
    return self.mix

  def mix_a_with_b(self, a, b):
    print(f'mixed {a} with {b}.')
    return [f'{a}', f'{b}']

if __name__ == "__main__":
  final_drink = Drink()
  final_drink.add_to_mix('carrots')
  print(final_drink.mix)