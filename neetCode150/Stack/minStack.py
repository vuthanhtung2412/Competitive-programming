class MinStack(object):
    def __init__(self):
        self.val = []
        self.mini = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.val.append(val)
        if not self.mini or val < self.getMin():
            self.mini.append(val)
        else:
            self.mini.append(self.getMin())

    def pop(self):
        """
        :rtype: None
        """
        self.val.pop()
        self.mini.pop()

    def top(self):
        """
        :rtype: int
        """

        return self.val[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini[-1]