def verify_matrix_and_words(matrix: list):
  before_len = len(matrix[0])
  for i in range(1, len(matrix)):
    after_len = len(matrix[i])
    if before_len != after_len:
      raise Exception('Una o más palabras de la matriz o palabras búscadas \n' +
                      'tiene un tamaño diferente')
    else:
      before_len = after_len


def search_horizontal_combinations(horizontal_word: str, searched: str,
                                   pos_y: int):
  len_word = len(horizontal_word)
  for i in range(0, len_word):
    all_word = horizontal_word[i]
    for j in range(i + 1, len_word):
      all_word += horizontal_word[j]
      if all_word == searched:
        print_founded = ''
        counter = i
        for characters in all_word:
          print_founded += f'{characters} - [{pos_y}, {counter}]\n'
          counter += 1
        return print_founded      
  return False


def search_vertical_combinations(matrix: list, searched: str,
                                   pos_x: int):
  rows = len(matrix)
  for i in range(0, rows):
    all_word = matrix[i][pos_x]
    for j in range(i + 1, rows):
      all_word += matrix[j][pos_x]
      if all_word == searched:
        print_founded = ''
        counter = i
        for characters in all_word:
          print_founded += f'{characters} - [{counter}, {pos_x}]\n'
          counter += 1
        return print_founded
  return False


def do_search(word: str, matrix: list):
  print_founded = False
  rows = len(matrix)
  cols = len(matrix[0])

  # Búsqueda en horizontal
  for row in range(0, rows):
    print_founded = search_horizontal_combinations(matrix[row], word, row)
    if print_founded:
      return print_founded

  # Búsqueda en vertical
  for col in range(0, cols):
    print_founded = search_vertical_combinations(matrix, word, col)
    if print_founded:
      return print_founded
  
  return f'"{word}" Not found'


def init():
  matrix = input('Ingrese la matriz agregando cada fila de la ' +
        'sopa de letras separada por espacios.\n\n' +
        'Ejemplo: SOL UNO NUT, para formar:\n' +
        '\t[ S O L ]\n' +
        '\t[ U N O ]\n' +
        '\t[ N U T ]\n' +
        ': ').split(' ')
  
  verify_matrix_and_words(matrix)

  search_words = input('Ingrese las palabras a buscar ' +
                        'separadas por espacio: ').split(' ')
  
  verify_matrix_and_words(search_words)
  
  # Se repite la iteración por cada palabra buscada.
  for word in search_words:
    print(f'Searching "{word}"')
    print(do_search(word, matrix))

if __name__ == '__main__':
  init()
