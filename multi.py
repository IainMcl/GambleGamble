from multiprocessing import Pool, current_process


def worker(a):
    """worker function"""
    print(f'Worker {current_process().name} {a}')
    return


if __name__ == '__main__':
    p = Pool(10)
    with p:
        p.map(worker, range(10))
