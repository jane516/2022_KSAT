from base.problem_generator import ProblemGenerator
from fractions import Fraction
import random


class JaneProblem1(ProblemGenerator):
    def __init__(self, x: int, y: int, z: int):
        self.x: int = x
        self.y: int = y
        self.z: int = z

    @classmethod
    def generate_random_input(cls):
        x_list = [i for i in range(2, 11)]
        y_list = [i for i in range(1, 21)]
        z_list = [i for i in range(1, 10)]

        x = x_list[random.randrange(len(x_list))]
        y = y_list[random.randrange(len(y_list))]
        z = z_list[random.randrange(len(z_list))]

        return x, y, z

    def validate(self):
        if self.x < 2 or self.x > 10:
            return False
        if self.y < 1 or self.y > 20:
            return False
        if self.z >= self.x or self.z < 0:
            return False
        answer = self.answer
        if answer != int(answer):
            return False
        return True

    @property
    def answer(self):
        answer = int((1000 * self.y) / (self.x - self.z))
        return answer

    @property
    def problem_text(self):
        problem_text = (
            f"어떤 상품을 원가에 ${5 * self.x}\%$의 이익을 붙여서 정가를 정하고, "
            f"정가에서 ${50 * self.y}$원을 할인하여 판매하였더니 $1$개를 팔 때마다 "
            f"원가의 ${5 * self.z}\%$의 이익을 얻었다. "
            f"이 상품의 원가를 $k$원이라 할 때, $k$의 값을 구하시오."
        )
        return problem_text

    @property
    def solution_text(self):
        fraction_1 = Fraction(5 * self.x + 100, 100)
        fraction_2 = Fraction(5 * self.z, 100)
        fraction_3 = Fraction(5 * (self.x - self.z), 100)

        solution_text = (
            f"원가를 $k$원이라 하면"
            f"\n$\qquad (정가)=k+\dfrac{{{5 * self.x}}}{{100}}k"
            f"=\dfrac{{{fraction_1.numerator}}}{{{fraction_1.denominator}}}k(원)$"
            f"\n$\qquad (판매\ 가격)"
            f"=\dfrac{{{fraction_1.numerator}}}{{{fraction_1.denominator}}}k-{50 * self.y}(원)$"
            f"\n$\qquad (이익)=\dfrac{{{5 * self.z}}}{{100}}k"
            f"=\dfrac{{{fraction_2.numerator}}}{{{fraction_2.denominator}}}k(원)$"
            f"\n이때 $(판매\ 가격)-(원가)=(이익)$이므로 "
            f"\n$\qquad\left(\dfrac{{{fraction_1.numerator}}}{{{fraction_1.denominator}}}k-{50 * self.y}\\right)-k"
            f"=\dfrac{{{fraction_2.numerator}}}{{{fraction_2.denominator}}}k$"
            f"\n$\qquad \dfrac{{{fraction_3.numerator}}}{{{fraction_3.denominator}}}k={50 * self.y}$"
            f"\n$\qquad \\therefore\ k={self.answer}$"
            f"\n따라서 원가는 ${self.answer}$원이다."
        )
        return solution_text