import random

from base.problem_generator import ProblemGenerator
from fractions import Fraction


class JaneProblem3(ProblemGenerator):
    def __init__(self, p1: int, q1: int, p2: int, q2: int, k: int):
        self.p1: int = p1
        self.q1: int = q1
        self.p2: int = p2
        self.q2: int = q2
        self.k: int = k

    @classmethod
    def generate_random_input(cls):
        p1_list = [i for i in range(2, 11)]
        q1_list = [i for i in range(1, 11)]
        p2_list = [i for i in range(2, 11)]
        q2_list = [i for i in range(1, 11)]
        k_list = [i for i in range(2, 11)]

        p1 = p1_list[random.randrange(len(p1_list))]
        q1 = q1_list[random.randrange(len(q1_list))]
        p2 = p2_list[random.randrange(len(p2_list))]
        q2 = q2_list[random.randrange(len(q2_list))]
        k = k_list[random.randrange(len(k_list))]

        return p1, q1, p2, q2, k

    def validate(self):
        if self.p1 < 2 or self.p1 > 10:
            return False
        if self.p2 < 2 or self.p2 > 10 or self.p1 == self.p2:
            return False
        if self.q1 < 1 or self.q1 > 10:
            return False
        if self.q2 < 1 or self.q2 > 10:
            return False
        if self.k < 2 or self.k > 10:
            return False
        return True

    @property
    def answer(self):
        fraction = Fraction(self.q1 * self.p2, self.p1 * self.q2)
        return fraction

    @property
    def problem_text(self):
        p1 = self.p1
        q1 = self.q1
        p2 = self.p2
        q2 = self.q2
        k = self.k
        wide = Fraction(q1, p1 * k)
        area = Fraction(q2, p2 * k)

        problem_text = (
            f"넓이가 $\dfrac{{{wide.numerator}}}{{{wide.denominator}}}\ \mathrm{{m}}^{{2}}$인 직사각형의 "
            f"가로의 길이가 $\dfrac{{{area.numerator}}}{{{area.denominator}}}\ \mathrm{{m}}$라면, "
            f"세로의 길이는 몇 $\mathrm{{m}}$입니까$?$"
        )
        return problem_text

    @property
    def solution_text(self):
        p1 = self.p1
        q1 = self.q1
        p2 = self.p2
        q2 = self.q2
        k = self.k
        wide = Fraction(q1, p1 * k)
        area = Fraction(q2, p2 * k)
        long = Fraction(q1 * p2, p1 * q2)

        solution_text = (
            f"직사각형의 세로를 $\square\ \mathrm{{cm}}$라고 하면"
            f"\n$\qquad (직사각형의\ 넓이)=\square\\times\dfrac{{{wide.numerator}}}{{{wide.denominator}}}"
            f"=\dfrac{{{area.numerator}}}{{{area.denominator}}}$"
            f"\n따라서"
            f"\n$\qquad\\begin{{aligned}}\square"
            f"&=\dfrac{{{area.numerator}}}{{{area.denominator}}}\div\dfrac{{{wide.numerator}}}{{{wide.denominator}}}"
            f"=\dfrac{{{area.numerator}}}{{{area.denominator}}}\\times\dfrac{{{wide.numerator}}}{{{wide.denominator}}}\\\[2ex]"
            f"&=\dfrac{{{long.numerator}}}{{{long.denominator}}}"
            f"\end{{aligned}}$"
        )
        return solution_text