import random

from base.problem_generator import ProblemGenerator


class JaneProblem7(ProblemGenerator):
    def __init__(self, square_factor: int, constant: int, degree: int, a_value: int, sub: int):
        self.square_factor: int = square_factor
        self.constant: int = constant
        self.degree: int = degree
        self.a_value: int = a_value
        self.sub: int = sub

    @classmethod
    def generate_random_input(cls):
        square_factor_list = [i for i in range(2, 10)]
        constant_list = [i for i in range(1, 11)]
        degree_list = [3, 4, 5]
        a_value_list = [i for i in range(2, 7)]
        sub_list = [i for i in range(-3, 4)]

        square_factor = square_factor_list[random.randrange(len(square_factor_list))]
        constant = constant_list[random.randrange(len(constant_list))]
        degree = degree_list[random.randrange(len(degree_list))]
        a_value = a_value_list[random.randrange(len(a_value_list))]
        sub = sub_list[random.randrange(len(sub_list))]

        return square_factor, constant, degree, a_value, sub

    def validate(self):
        if self.square_factor < 2 or self.square_factor > 9:
            return False
        if self.constant < 1 or self.constant > 10:
            return False
        if self.degree not in [3, 4, 5]:
            return False
        if self.a_value < 2 or self.a_value > 6:
            return False

        fx_factor1 = self.fx_factor1
        fx_factor2 = self.fx_factor2
        if fx_factor1 * fx_factor2 == 0:
            return False

        return True

    @property
    def fx_factor1(self):
        return self.square_factor * pow(self.sub, 2) + self.a_value * self.sub - self.constant

    @property
    def fx_factor2(self):
        return 2 * self.square_factor * self.sub + self.a_value

    @property
    def answer(self):
        fx_factor1 = self.fx_factor1
        fx_factor2 = self.fx_factor2

        result = self.degree * pow(fx_factor1, self.degree - 1) * fx_factor2
        return result

    @property
    def problem_text(self):
        square_factor = self.square_factor
        constant = self.constant
        rev_constant = -1 * constant
        degree = self.degree
        a_value = self.a_value
        sub = self.sub
        fx_prime = degree * pow(rev_constant, degree - 1) * a_value

        problem_text = (
            f"함수 $f(x) = ({square_factor}x ^ {{2}}+ax-{constant}) ^ {{{degree}}}$에 대하여 "
            f"$f'(0)={fx_prime}$일 때, "
            f"$f'({sub})$의 값을 구하시오. $($단, $a$는 상수이다.$)$"
        )
        return problem_text

    @property
    def solution_text(self):
        square_factor = self.square_factor
        constant = self.constant
        rev_constant = -1 * constant
        degree = self.degree
        a_value = self.a_value
        sub = self.sub
        fx_factor1 = self.fx_factor1
        fx_factor2 = self.fx_factor2
        fx_prime = degree * pow(rev_constant, degree - 1) * a_value

        solution_text = (
            f"$\\begin{{aligned}}"
            f"f'(x)&={degree}({square_factor}x^{{2}}+ax-{constant})^{{{degree - 1}}}"
            f"({square_factor}x^{{2}}+ax-{constant})'\\\[1ex]"
            f"\n&={degree}({square_factor}x^{{2}}+ax-1)^{{{degree - 1}}}({2 * square_factor}x+a)"
            f"\n\end{{aligned}}$"
            f"\n$f'(0)={fx_prime}$이므로"
            f"\n$\qquad {degree}\\times({rev_constant})^{{{degree - 1}}}\\times a={fx_prime}$"
            f"\n$\qquad {degree * pow(rev_constant, degree - 1)}a={fx_prime}$"
            f"\n$\qquad\\therefore\ a={a_value}$"
            f"\n따라서 $f'(x)={degree}({square_factor}x^{{2}}+{a_value}x-{constant})^{{{degree - 1}}}({2 * square_factor}x+{a_value})$이므로"
            f"\n$\qquad f'({sub})={degree}\\times({fx_factor1})^{{{degree - 1}}}\\times({fx_factor2})={self.answer}$"
        )
        return solution_text
