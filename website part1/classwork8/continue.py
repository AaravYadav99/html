try:
    # Trying to convert an invalid string to integer
    value = int("abc")  # This will raise a ValueError
except ValueError as e:
    print(f"A ValueError occurred: {e}")

