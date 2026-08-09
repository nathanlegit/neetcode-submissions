class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        running_stack = []
        for symbol in tokens:
            if symbol not in "+-*/":
                running_stack.append(symbol)
            else:
                if symbol == "+":
                    last_value = int(running_stack.pop())
                    second_last_value = int(running_stack.pop())
                    new_value = last_value + second_last_value
                    running_stack.append(str(new_value))
                elif symbol == "-":
                    last_value = int(running_stack.pop())
                    second_last_value = int(running_stack.pop())
                    new_value = second_last_value - last_value
                    running_stack.append(str(new_value))
                elif symbol == "*":
                    last_value = int(running_stack.pop())
                    second_last_value = int(running_stack.pop())
                    new_value = second_last_value * last_value
                    running_stack.append(str(new_value))
                elif symbol == "/":
                    last_value = int(running_stack.pop())
                    second_last_value = int(running_stack.pop())
                    new_value = int(second_last_value / last_value)
                    running_stack.append(str(new_value))
        return int(running_stack[0])
