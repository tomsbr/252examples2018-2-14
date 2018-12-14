
from blackjack_functions import hit, result

# write a smoke test
def test_smoke():
  assert True == True

def test_hit():
  c = hit()
  assert hit() >= 1 and c <= 11


#test the result function
  def test_result_push():
    p = [11,10]
    h = [8,8,5]
    assert result(p, h) == "push"

  def test_result_bust():
    p = [11,10,3]
    h = [8,8,4]
    assert result(p, h) == "bust"

  def test_result_blackjack():
    p = [11,10]
    h = [8,10]
    assert result(p, h) == "blackjack"

  def test_result_win():
    p = [8,10]
    h = [8,9]
    assert result(p, h) == "win"

  def test_result_lose():
    p = [9,10]
    h = [8,8,5]
    assert result(p, h) == "lose"