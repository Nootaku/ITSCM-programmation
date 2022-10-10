def recursive_factorial(n):
    if n == 1:
        return n

    else:
        return n * recursive_factorial(n - 1)


def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))


def recursive_student(my_dict):
    if my_dict['genre'] == 'étudiant':
        return f"{my_dict['nom']} {my_dict['prénom']}"

    else:
        return [recursive_student(i) for i in my_dict['étudiants']]


def flatten_list(my_list):
    flat_list = []

    for i in my_list:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)

    return flat_list
