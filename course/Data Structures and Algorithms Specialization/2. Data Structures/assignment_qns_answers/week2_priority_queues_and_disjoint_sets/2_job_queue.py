from collections import namedtuple
from dataclasses import dataclass
import math

@dataclass
class Thread:
    thread_id: int
    next_available_time: int

    def __repr__(self):
        return f'(id={self.thread_id}, {self.next_available_time})'

def left_child(index):
    child_index = (2*index) + 1
    return child_index

def right_child(index):
    child_index = (2*index) + 2
    if child_index < len(pqueue):
        return child_index
    return child_index

def sift_down(index, pqueue, verbose=False):
    curr_index = index

    while True:
        if verbose:
            print('='*50)
            print('sift_down')
            print(f"{curr_index=}, {left_child_index=}, {right_child_index=}, {pqueue=}")

        left_child_index = left_child(curr_index) if left_child(curr_index) < len(pqueue) else None
        right_child_index = right_child(curr_index) if right_child(curr_index) < len(pqueue) else None

        if (left_child_index is None) and (right_child_index is None):
            return

        compare_index = [x for x in [curr_index, left_child_index, right_child_index] if x is not None]

        ordered_index = sorted(
            compare_index,
            key = lambda i: [pqueue[i].next_available_time, pqueue[i].thread_id]
        )
        
        if verbose:
            print(f"{ordered_index=}")

        if ordered_index[0] == curr_index:
            return
        else:
            pqueue[curr_index], pqueue[ordered_index[0]] = pqueue[ordered_index[0]], pqueue[curr_index]
            curr_index = ordered_index[0]
        
def heapify(pqueue, verbose=False):
    start_index = (len(pqueue)-1)//2
    for index in range(start_index, -1, -1):
        sift_down(index, pqueue, verbose)
    return pqueue

n_workers = 4
jobs = [1]*20
pqueue = [Thread(i, 0) for i in range(n_workers)]

def assign_jobs(n_workers, jobs, pqueue, verbose=False):

    job_queue = jobs
    process_log = []
    heapify(pqueue, verbose)

    for job_time_taken in job_queue:
        if verbose:
            print('='*50)
            print('assign_jobs')
            print([(x.thread_id, x.next_available_time) for x in pqueue])
        
        assigned_thread = pqueue[0]
        process_log.append((assigned_thread.thread_id, assigned_thread.next_available_time))
        assigned_thread.next_available_time += job_time_taken
        
        if verbose:
            print([(x.thread_id, x.next_available_time) for x in pqueue])
        heapify(pqueue, verbose)
        if verbose:
            print([(x.thread_id, x.next_available_time) for x in pqueue])
    
    return process_log

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    
    pqueue = [Thread(i, 0) for i in range(n_workers)]
    assigned_jobs = assign_jobs(n_workers, jobs, pqueue)

    for job in assigned_jobs:
        print(job[0], job[1])

if __name__ == "__main__":
    main()
