# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def _process(self, request):
        curr_request_start_time, curr_request_processing_time = request
        curr_request_end_time = curr_request_start_time+curr_request_processing_time

        ## if nothing in queue...
        if not self.finish_time:
            ## add the end of the processing time to finish time
            self.finish_time.append(curr_request_end_time)
            return Response(False, curr_request_start_time)
            
        ## else if something in queue...
        else:
            ## if the new item starts after the previous item ends
            if curr_request_start_time >= self.finish_time[-1]:
                
                ## Reset deque
                self.finish_time = deque()
                self.finish_time.append(curr_request_end_time)
                return Response(False, curr_request_start_time)

            ## if new item starts before previous item ends
            else:
                
                ## Check start time of new item against the earliest finish time of previous items. If it does not exceed, it means the earliest item is still processing when this item arrives. Else, it means the earliest is already completed, so pop from the queue
                while curr_request_start_time >= self.finish_time[0]:
                    self.finish_time.popleft()

                # if the queue is full, the item is dropped
                if len(self.finish_time) >= self.size:
                    return Response(True, -1)
                
                # otherwise, the item is added to the queue, and the time of processing is delayed by the end time of the last processing end time in the queue
                else:
                    last_processing_end_time = self.finish_time[-1]
                    self.finish_time.append(
                        last_processing_end_time + curr_request_processing_time
                    )
                    return Response(False, last_processing_end_time)
        
    def process_requests(self, requests):
        responses = []
        for request in requests:
            # print(self.finish_time)
            response = self._process(request)
            responses.append(response)
        return responses

# def process_requests(requests, buffer):
#     responses = []
#     for request in requests:
#         responses.append(buffer.process(request))
#     return responses

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = buffer.process_requests(requests)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
