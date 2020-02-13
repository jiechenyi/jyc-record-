"""
155.最小栈
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。


"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.stack.append(x)
        if self.helper == []:
            self.helper.append(x)
        elif x < self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        """
        :rtype: None
        """
        if self.stack != []:
            self.stack.pop()
            self.helper.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack != []:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """

        if self.helper != []:
            return self.helper[-1]
