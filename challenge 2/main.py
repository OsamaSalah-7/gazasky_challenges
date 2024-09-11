
def is_valid_input(arr):
    if not isinstance(arr, list):
        return False, "Input should be a list."

    if not all(isinstance(i, int) for i in arr):
        return False, "Input should only contain integers."

    return True, "Valid input."

def find_missing_numbers(arr):

    full_range = set(range(min(arr), max(arr) + 1))
    missing_numbers = full_range - set(arr)
    return sorted(list(missing_numbers))


def missing_number_game(arr):

    valid, message = is_valid_input(arr)
    if not valid:
        return message

    missing_numbers = find_missing_numbers(arr)

    if not missing_numbers:
        return "No numbers are missing from the list."

    return f"Missing numbers: {missing_numbers}"

numbers = [2, 1, 5, 4, 6, 9, 7, 8, 10]
result = missing_number_game(numbers)
print(result)
