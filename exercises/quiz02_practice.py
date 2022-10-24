def odd_and_even(a: list[int]) -> list[int]:
    new_list: list[int] = []
    index: int = 0
    for i in a:
        if index % 2 == 0 and i % 2 != 0:
                new_list.append(a[index])
        index += 1
    return new_list 

print(odd_and_even([2,9,4,17,9,10,15,13,14,21]))