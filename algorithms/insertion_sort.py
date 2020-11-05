def insertion_sort(A):
    '''Sort list of comparable elements into nondecreasing order.'''
    for k in range(1, len(A)):
        cur = A[k]                      # current element to be inserted
        j = k                           # find correct index j for current
        while j > 0 and A[j-1] > cur:   # element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = cur                      # current is now in the right place


if __name__ == "__main__":
    A = ['B', 'C', 'D', 'A', 'E', 'H', 'G', 'F']
    insertion_sort(A)
    print(A)