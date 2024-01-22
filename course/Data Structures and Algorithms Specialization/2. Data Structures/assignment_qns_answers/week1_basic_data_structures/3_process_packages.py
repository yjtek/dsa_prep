# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def _process(self, request):
        time_start_processing, time_end_processing = request

        ## if nothing in queue...
        if not self.finish_time:
            ## add the end of the processing time to finish time
            self.finish_time.append(time_end_processing)
            return Response(False, time_start_processing)
            
        ## else if something in queue...
        else:
            queue_len = len(self.finish_time)
            if time_start_processing >= self.finish_time[-1]:
                self.finish_time.popleft()
                self.finish_time.append(time_end_processing)
                return Response(False, time_start_processing)

            ## if queue length is max, check if we can process this now
            if queue_len >= self.size:
                return Response(True, -1)
            else:
                return Response(False, time_start_processing)

    def process_requests(self, requests):
        responses = []
        for request in requests:
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
