import json
import parse_puzzle


def upload_puz(json):
  """Uploads to the DownForAcross API."""
  base_url = "api.foracross.com"


def parse_puz(path_to_file):
  """Parse a .puz file."""
  p = parse_puzzle.read(path_to_file)
  print(p.clue_numbering())

  # Clues are stored in row-major (reading) order.
  print(p.width, p.height, p.width * p.height)
  print(len(p.solution))
  print(p.solution)

  # List of lists (2d array).
  grid = []
  for row in range(p.height):
    letters_this_row = []
    for col in range(p.width):
      letters_this_row.append(p.solution[row*p.width + col])
    grid.append(letters_this_row)

  raw_across = p.clue_numbering().across
  raw_down = p.clue_numbering().down

  # List of clues, where the index corresponds to the clue number in the puzzle.
  # For example, across[5] should be "5-Across" in the puzzle.
  across_clues = ['null' for _ in range(raw_across[-1]['num'] + 1)]
  down_clues = ['null' for _ in range(raw_down[-1]['num'] + 1)]
  # print(len(across_clues), len(down_clues))

  for clue in raw_across:
    across_clues[int(clue['num'])] = clue['clue']
  for clue in raw_down:
    down_clues[int(clue['num'])] = clue['clue']

  # Markup squares have extra annotations. These should just be the circled letters.
  markup_squares = p.markup().get_markup_squares()

  jsonified = {
    'puzzle': {
      'grid': grid,
      'circles': markup_squares,
      'shades': [],
      'info': {
        "type": 'NYT Daily Puzzle',
        "title": p.title,
        "author": p.author,
        "description": p.preamble
      },
      'clues': {
        'across': across_clues,
        'down': down_clues
      },
      'private': False
    },
    'pid': 1234,
    'isPublic': True,
  }

  print(jsonified)


if __name__ == '__main__':
  parse_puz('./examples/20220505.puz')
