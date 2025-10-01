import multiprocessing as mp



def my_worker(num):
    print(f'Worker {num} is running...')



def square(x):
    return x * x



def func(num, arr):
    num.value = 3.1415927
    for i in range(len(arr)):
        arr[i] = -arr[i]



if __name__ == '__main__':

    processes = []
    for i in range(5):
        p = mp.Process(target=my_worker, args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

    with mp.Pool(4) as p:
        result = p.map(square, [1, 2, 3, 4, 5])
    print(result)

    # Use of shared memory
    num = mp.Value('d', 0.0)
    arr = mp.Array('i', range(10))
    p = mp.Process(target=func, args=(num, arr))
    p.start()
    p.join()
    print(num.value, arr[:])
