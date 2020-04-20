def max_pairwise(numbers, n):
    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i
            
    max_index2 = -1
    for j in range(n):
        if j != max_index1 and (max_index2 == -1 or numbers[j]>numbers[max_index2]):
                                                  max_index2 = j

    return (numbers[max_index1] * numbers[max_index2])



if __name__ == '__main__':
    n = int(input())
    numbers = map(int, input().split())
    numbers_list = list(numbers)
    assert (len(numbers_list) == n)
    
    print(max_pairwise(numbers_list, n))