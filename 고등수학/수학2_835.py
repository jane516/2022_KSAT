import random

from base.problem_generator import ProblemGenerator
import math


class JaneProblem6(ProblemGenerator):
    def __init__(self, n: int, k: int, S: int):
        self.n: int = n
        self.k: int = k
        self.S: int = S

    @classmethod
    def generate_random_input(cls):
        k_list = [1, 2, 3]
        n_list = [i for i in range(1, 6)]
        S_list = [i for i in range(2, 300)]

        k = k_list[random.randrange(len(k_list))]
        n = n_list[random.randrange(len(n_list))]
        S = S_list[random.randrange(len(S_list))]

        return n, k, S

    def validate(self):
        if self.k not in [1, 2, 3]:
            return False
        if self.S <= 2 * self.n * self.k**3:
            return False
        if self.S / (2 * self.n * self.k) != int(self.S / (2 * self.n * self.k)):
            return False
        if (
            self.S // (2 * self.n * self.k)
            != int(math.sqrt(self.S // (2 * self.n * self.k))) ** 2
        ):
            return False
        return True

    @property
    def answer(self):
        result = int(math.sqrt(self.S // (2 * self.n * self.k)))
        return result

    @property
    def problem_text(self):
        n = self.n
        k = self.k
        S = self.S
        m = 2 * n * k
        l = 2 * m * k - 3 * n * k**2

        problem_text = (
            f"함수 $f(x)=\left\{{\\begin{{array}}{{ll}} {2 * m}x &(x\ge{k})\\\[1ex]"
            f"{3 * n}x^{{2}}+{l} &(x\le{k})\end{{array}}\\right.$"
            f"에 대하여 $\displaystyle\int_{{0}}^{{a}}f(x)={S}$"
            f"을 만족시키는 상수 $a$의 값을 구하시오. $(단,\ a>{k})$"
        )
        return problem_text

    @property
    def solution_text(self):
        n = self.n
        k = self.k
        S = self.S
        m = 2 * n * k
        l = 2 * m * k - 3 * n * k**2

        solution_text = (
            f"$\\begin{{aligned}}\displaystyle\int_{{0}}^{{a}}f(x)"
            f"&=\displaystyle\int_{{0}}^{{{k}}}({3 * n}x^{{2}}+{l})dx"
            f"+\displaystyle\int_{{{k}}}^{{a}}{2 * m}xdx\\\[2ex]"
            f"&=\Big[{n}x^{{3}}+{l}x\Big]_{{0}}^{{{k}}}+\Big[{m}x^{{2}}\Big]_{{{k}}}^{{a}}\\\[2ex]"
            f"&={n * k**3 + l * k}+({m}a^{{2}}-{m * k**2})={m}a^{{2}}\end{{aligned}}$"
            f"\n따라서 ${m}a^{{2}}={S}$에서 $a^{{2}}={S // m}$이므로"
            f"\n$\qquad a={self.answer}\ (\\because\ a>{k})$"
            f"\n[정답]{self.answer}"
        )
        return solution_text