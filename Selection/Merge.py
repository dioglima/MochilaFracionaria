def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide a lista ao meio
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Chama o merge_sort recursivamente nas duas metades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Mescla as duas metades ordenadas
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Compara elementos de left e right e os insere no resultado em ordem
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Adiciona os elementos restantes, se houver
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


# Exemplo de uso:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
