# coding: utf-8

# クイックソート
def quicksort(seq):
    if len(seq) < 1:
        return seq
    pivot = seq[0]
    left = []
    right = []
    for x in range(1, len(seq)):
        if seq[x] <= pivot:
            left.append(seq[x])
        else:
            right.append(seq[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right



if __name__ == '__main__':
    a = [42,634423,6,2,4,632,1]
    print('before:', a)
    print('after:', quicksort(a))