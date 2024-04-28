if __name__ == "__main__":
  # Introduction to recursive functions

  def fn():
    # ...
    fn()
    # ...

  """
  Also, a recursive function needs to have a condition to stop calling itself.
  So you need to add an if statement like this
  """

  # def fn():
  #   # ...
  #   if condition:
  #     # stop calling itself
  #   else:
  #     fn()
  #   # ...

  # Python recursive function examples

  # A simple recursive function example in Python

  def count_down(start):
    """Count down from a number"""
    print(start)

    # call the count_down if the next
    # number is greater than 0
    next = start - 1
    if (next > 0):
      count_down(next)

  count_down(3)

  # Using a recursive function to calculate the sum of a sequence

  def sum(n):
    total = 0
    for number in range(n + 1):
      total += number

    return total
  print(sum(100))

  def sum_recursive(n):
    if n == 0:
      return 0

    return n + sum_recursive(n - 1)
  print(sum_recursive(100))
