class Calculator:
    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y

    @staticmethod
    def subtract(x: float, y: float) -> float:
        return x - y

    @staticmethod
    def multiply(x: float, y: float) -> float:
        return x * y

    @staticmethod
    def divide(x: float, y: float) -> float | str:
        try:
            return x / y
        except ZeroDivisionError:
            return "You can't divide by zero!"
        except ValueError:
            return "That's not a valid number!"

    def execute_task(self, x: float, y: float, operation: str) -> float | str:
        if operation == '+':
            return self.add(x, y)
        if operation == '-':
            return self.subtract(x, y)
        if operation == '*':
            return self.multiply(x, y)
        if operation == '/':
            return self.divide(x, y)
        else:
            return "Wrong operation type!"


def get_user_input() -> list[float | str]:
    user_str_arr = input("Input simple math problem: ").split()
    x, operation, y = user_str_arr
    try:
        return [float(x), float(y), operation]
    except ValueError:
        print("Given argument is not a number!")


calculator = Calculator()

x, y, operation = get_user_input()
result = calculator.execute_task(x, y, operation)
print(result)
