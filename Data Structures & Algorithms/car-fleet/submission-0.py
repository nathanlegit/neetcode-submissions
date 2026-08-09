class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)
        for pos, spd in cars: 
            time = (target - pos)/spd
            if not stack:
                stack.append(time)
            else:
                if time <= stack[-1]:
                    continue
                else:
                    stack.append(time)
        return len(stack)
