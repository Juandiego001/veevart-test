'''
  Los valores al ingresar el input están invertidos,
  es decir, primero se ingresa el valor, luego el peso separados por comas.

  Ejemplo:
  10,5 donde 10 es el valor y 5 es el peso.
'''

def get_total_value(items: list):
  total_value = 0
  for item in items:
    total_value += item[0]
  return total_value

all_possible_tuples = []
def set_tuples(item_index: int, tuples_combination: list, all_items: list):
  if (item_index == len(all_items)):
    all_possible_tuples.append(tuples_combination.copy())
  else:
    tuples_combination.append(all_items[item_index])
    set_tuples(item_index + 1, tuples_combination, all_items)
    tuples_combination.pop()
    set_tuples(item_index + 1, tuples_combination, all_items)


def init():
  max_weight = int(input('Ingrese el peso máximo de la mochila: '))

  # Validación
  while max_weight <= 0:
    max_weight = int(input('El peso de la mochila debe ser mayor a 0: '))

  items = input('Ingrese cada elemento de la mochila como dos números ' +
                'separados por comas donde el ' +
                'primer número corresponde al VALOR del elemento y ' +
                'el segundo número al PESO.\n' +
                'Ejemplo: 20,10 30,5 25,5\n' +
        ': ').split(' ')
  
  new_items = []
  for item in items:
    value, weight = item.split(',')
    new_items.append((float(value), float(weight)))
  
  set_tuples(0, [], new_items)
  best_value = 0
  possible_answers = []
  counter = 0
  accepted_answer = 0
  for tuple_list in all_possible_tuples:
    sum_weights = 0
    temp_value = 0
    if len(tuple_list):
      possible_answers.append([])
      for tuple_element in tuple_list:
        temp_sum = sum_weights + tuple_element[1]
        if temp_sum <= max_weight:
          possible_answers[counter].append(tuple_element)
          temp_value += tuple_element[0]
          sum_weights = temp_sum
          if temp_value > best_value:
            accepted_answer = counter
            best_value = temp_value
    counter += 1


  response = f'\nItems llevados\n'
  counter = 1
  for item in possible_answers[accepted_answer]:
    response += f'Item #{counter} con un valor de {item[0]} y un peso de {item[1]}\n'
    counter += 1

  response += f'\nItems NO llevados\n'
  for item in new_items:
    if not item in possible_answers[accepted_answer]:
      response += f'Item {item} con un valor de {item[0]} y un peso de {item[1]}\n'

  response += f'\nValor total llevado: {best_value}\n'
  print(response)

if __name__ == '__main__':
  init()
