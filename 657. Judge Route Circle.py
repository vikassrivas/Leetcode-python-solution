class Solution(object):
  def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    return (moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D'))

    x, y = 0, 0
    for c in moves:
      if c == 'U':
        y += 1
      elif c == 'D':
        y -= 1
      elif c == 'L':
        x += 1
      else:
        x -= 1
    return x == 0 and y == 0