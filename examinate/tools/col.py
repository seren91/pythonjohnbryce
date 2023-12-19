def my_zip(it1, it2):
    
    if len(it1) != len(it2):
        raise ValueError("Collections must have the same length.")

    
    return ((it1[i], it2[i]) for i in range(len(it1)))

# Example usage:
list1 = [12, 322, 323]
list2 = ['agg', 'brr', 'crr']

result = list(my_zip(list1, list2))
print(result)