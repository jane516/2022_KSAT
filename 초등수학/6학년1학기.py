from base.problem_generator import ProblemGenerator
from fractions import Fraction
import random


class JaneProblem4(ProblemGenerator):
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    @classmethod
    def generate_random_input(cls):
        x_list = [i for i in range(6, 16)]
        y_list = [i for i in range(4, 21)]

        x = x_list[random.randrange(len(x_list))]
        y = y_list[random.randrange(len(y_list))]

        return x, y

    def validate(self):
        if self.x < 6 or self.x > 15:
            return False
        if self.y % self.x == 0:
            return False
        return True

    @property
    def answer(self):
        result = Fraction(self.y, self.x)
        return result

    @property
    def problem_text(self):
        x = self.x
        y = self.y
        problem_text = (
            f"어떤 자연수를 {x}(으)로 나누어야 할 것을 잘못하여 "
            f"{x}을/룰 곱했더니 {x * y}이/가 되었다. "
            f"바르게 계산한 값을 분수로 나타내시오."
        )
        return problem_text

    @property
    def solution_text(self):
        x = self.x
        y = self.y
        fraction = Fraction(self.y, self.x)

        solution_text = (
            f"어떤 자연수를 $\square$라고 하여 잘못 계산한 식을 세우면 "
            f"\n$\qquad \square\\times{x}={x * y}$"
            f"\n$\qquad \square={x * y}\div {x}= {y}$"
            f"\n따라서 바르게 계산하면"
            f"\n$\qquad {y}\div{x}=\dfrac{{{fraction.numerator}}}{{{fraction.denominator}}}$"
        )

        return solution_text
