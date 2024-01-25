#python3
import sys

class StackWithMax():
    '''
    To get a max value in O(1) time, we need to keep a record of the maximum value. There are 2 ways to do this
        - We can do this in O(N) space, by maintaining another stack with max values. With every pop or push operation, we recompute what the maximum value is up to that index, and whenever we are asked, simply read the last index in the max stack
    '''
    def __init__(self):
        self.__stack = []
        self.__maxstack = []

    def Push(self, a):
        self.__stack.append(a)
        
        if self.__maxstack == []:
            self.__maxstack.append(a)
        else:
            if self.__maxstack[-1] >= a:
                self.__maxstack.append(self.__maxstack[-1])
            else:
                self.__maxstack.append(a)

    def Pop(self):
        if len(self.__stack):
            stackval = self.__stack.pop()
            self.__maxstack.pop()
            return stackval
        else:
            return None


    def Max(self):
        if len(self.__stack):
            return self.__maxstack[-1]
        return None
    

if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
