import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

def bubble_sort(A):
    k = len(A)
    for i in range(k - 1):
        for j in range(k - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

def selection_sort(A):
    k = len(A)
    for i in range(k - 1):
        min = i
        for j in range(i + 1, k):

            if (A[min] > A[j]):
                min = j
        if min != i:
            A[min], A[i] = A[i], A[min]
    return A

def insertion_sort(A):
    i = 1
    k = len(A)
    while i < k:
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
        i += 1
    return A

num_elements = np.arange(1000, 100001, 1000)
size = num_elements.size
print(size)
print(num_elements)
t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)
t_quick_sort = np.zeros(size)

for i, n in enumerate(num_elements) :
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    bubble_sort(vector_ord)
    t_final = perf_counter_ns()
    t_bubble[i] = t_final - t_inicio

    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    selection_sort(vector_ord)
    t_final = perf_counter_ns()
    t_selection[i] = t_final - t_inicio

    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    insertion_sort(vector_ord)
    t_final = perf_counter_ns()
    t_insertion[i] = t_final - t_inicio

plt.plot(num_elements, t_bubble, "g-", num_elements, t_selection, "r-", num_elements, t_insertion, "b-")
plt.show()
