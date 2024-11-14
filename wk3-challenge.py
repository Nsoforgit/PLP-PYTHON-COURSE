def large_power(base, exponent):
  """Checks if base raised to the exponent is greater than 5000.

  Args:
    base: The base number.
    exponent: The exponent power.

  Returns:
    True if base**exponent > 5000, False otherwise.
  """

  result = base ** exponent
  if result > 5000:
    return True
  else:
    return False