
from random import randint

################# DICES FUNCTS ##################


def throw_dices():
  dices = sorted([randint(1,6) for _ in range(5)], reverse=True)
  return dices 


def calculate_matches(dices):
  matches = {}
  for x in dices:
    if x not in matches:
      matches[x] = 1
    else:
      matches[x] += 1

  return matches


################# BOARD FUNTCS ################

def print_board():
  for k, v in board.items():
    if v is None:
      print('{}:'.format(k))
    else:
      print('{}: {}'.format(k, v))


def total_score():
  result = 0
  for v in board.values():
    if v is not None:
      result += v
  return result


def end_game():
  for v in board.values():
    if v is None:
      return False
  return True


################ PERMISSIONS FUNCTS ##############


def is_stairs(matches):
  v = sorted(matches.values())
  if v == [1,2,3,4,5]:
    return True
  elif v == [2,3,4,5,6]:
    return True
  elif v == [1,3,4,5,6]:
    return True
  else:
    return False


def empty_place(key):
  return board[key] is None


def special_move(matches):
  frequencies = sorted(matches.items(), key=lambda x: x[1], reverse=True)
  if len(frequencies) == 1:
    return 'generala'
  elif len(frequencies) == 2: 
    if frequencies[0] == 4:
      return 'poker'
    else:
      return 'full'
  elif len(frequencies) == 5:
    if is_stairs(matches):
      return 'escalera'
  else:
    return None


def available_to_discard():
  posibilities = []
  for k in board.keys():
    if board[k] is None:
      posibilities.append(k)
  for ix, keys in enumerate(posibilities):
    print('{} - {}'.format(ix, keys))
  result = posibilities[int(input(''))]
  return result
# Muy bien! Pero acordate de validar el input porque sino te puede romper feo

def disable_key():
  print_board()
  print('Los casilleros para esta jugada estan llenos, elige un casillero vacío para eliminar\n')
  board[available_to_discard()] = 0



################## SCORE FUNCTS #################


def get_score(matches):
  move = special_move(matches)
  if (move is None) or (not empty_place(move)):
    move = sorted(matches.items(), key=lambda x: x[1], reverse=True)  # Aca estas ordenando 2 veces esto (aca y cuando llamas a special_move antes. Podrias hacerlo 1 sola vez)
    for key, value in move:
      if empty_place(key):
        board[key] = key * value
        return
    disable_key()
  else: # move is a special_move
    board[move] = special_score[move]



special_score = {
  'escalera': 25,
  'full': 35,
  'poker': 45,
  'generala': 50
}  

board = {
  1: None,
  2: None,
  3: None,
  4: None,
  5: None,
  6: None,
  'escalera': None,
  'full': None,
  'poker': None,
  'generala': None
}


while True:
  action = input('Presiona ENTER para lanzar los dados, o "0" para salir\n')
  if action == '0':
    break
  elif not action == '':
    continue

  dices = throw_dices()
  print(dices)
  matches = calculate_matches(dices)
  get_score(matches)
  print_board()
  if end_game():
    break

print_board()
print('Puntaje total: {}'.format(total_score()))


