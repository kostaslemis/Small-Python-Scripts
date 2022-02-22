class Stack:
    def __init__(self):
        self.__list = []
        self.__size = 0

    def push(self, char):
        self.__list.append(char)
        self.__size += 1

    def pop(self):
        self.__size -= 1
        return self.__list.pop()

    def empty(self):
        return self.__size == 0


def input_check(string):
    for char in string:
        if char not in ['{', '[', '(', ')', ']', '}']:
            return False
    return True


def chars_match(x, y):
    if (x == '{' and y == '}') or (x == '[' and y == ']') or (x == '(' and y == ')'):
        return True
    return False


def string_is_balanced(string):
    stack = Stack()

    for char in string:
        if char in ['{', '[', '(']:
            stack.push(char)
        elif char in ['}', ']', ')']:
            if stack.empty() or not chars_match(stack.pop(), char):
                return False

    return stack.empty()


def main():
    string = input()

    while not input_check(string):
        print("Only characters allowed : {, [, (, ), ], }")
        string = input()

    if string_is_balanced(string):
        print("String is balanced")
    else:
        print("String is not balanced")


if __name__ == "__main__":
    main()
