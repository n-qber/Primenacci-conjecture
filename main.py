from time import sleep

def fibonacci(cicles=10e5):
  a, b = 1, 1
  for _ in range(int(cicles)):
    yield a
    a, b = b, a+b


fibonacci_iterator = enumerate(fibonacci())
next(fibonacci_iterator)
for position, number in fibonacci_iterator:
  print('\r', end='')
  remainder = number % position
  #print(f"[{position}] The number: [{number}] is at the [{position}] position, the [{number}/{position}] has {['no', str(remainder) + ' as'][bool(remainder)]} remainder", end='')
  print(f"[{position}] The number: [not printable] is at the [{position}] position, the [not printable/{position}] has {['no', str(remainder) + ' as'][bool(remainder)]} remainder", end='')
  if not remainder:  # remainder == 0
    print(f" so [{position}] is prime")
  #sleep(.1)
