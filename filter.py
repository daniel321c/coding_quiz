from abc import ABC, abstractmethod


class BaseFilter(ABC):

    def __init__(self, field, constraint):
        self.field = field
        self.constraint = constraint

    @abstractmethod
    def apply(self, object):
        print("i am abstract")
        pass


class EquationFilter(BaseFilter):

    def __init__(self, field, constraint):
        super().__init__(field, constraint)

    def apply(self, object):
        super().apply(self)
        if(getattr(object, self.field) == self.constraint):
            return True
        return False
class Node:

    def __init__(self, type):
        self.type = type

node = Node('file')
filter = EquationFilter('type', 'folder')

print(filter.apply(node))


