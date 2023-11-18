"""
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""
# def points(games):
#     point = 0
#     lista = [list(map(int, match))
#              for match in ((i.split(':')) for i in games)]

#     for match in lista:
#         if match[0] > match[1]:
#             point += 3
#         elif match[0] == match[1]:
#             point += 1
#     return point


# PYTONICO
def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))

print(points(['1:4', '2:0', '3:0', '4:4', '2:2',
      '3:3', '1:4', '2:3', '2:4', '3:4']))
