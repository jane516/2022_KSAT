from base.problem_generator import ProblemGenerator
import math
import random


class JaneProblem5(ProblemGenerator):
    def __init__(self, a: int, b: int):
        self.a: int = a
        self.b: int = b

    @classmethod
    def generate_random_input(cls):
        a_list = [i for i in range(1, 10)]
        b_list = [i for i in range(2, 100)]

        a = a_list[random.randrange(len(a_list))]
        b = b_list[random.randrange(len(b_list))]

        return a, b

    def validate(self):
        if self.a < 1:
            return False
        if self.b <= self.a ** 2:
            return False
        size_of_vec_squared = 4 * self.a ** 2 + 1
        if (self.a ** 2 - self.b) ** 2 % size_of_vec_squared != 0:
            return False
        if size_of_vec_squared == int(math.sqrt(size_of_vec_squared)) ** 2:
            return False
        return True

    @property
    def answer(self):
        answer = (self.a**2 - self.b)**2 // (4 * self.a**2 + 1)
        return answer

    @property
    def problem_text(self):
        problem_text = f"곡선 $y=x^{{2}}$ 위의 점과 직선 $y={2 * self.a}x-{self.b}$ " \
                       f"사이의 거리의 최솟값을 $k$라 할 때, $k^{{2}}$의 값을 구하시오."
        return problem_text

    @property
    def solution_text(self):
        line = f'$y={2 * self.a}x-{self.b}$'
        diff_line = f"f'(t)=2t={2 * self.a}"
        size_of_vec_squared = 4 * self.a ** 2 + 1

        solution_text = f"$f(x)=x^{{2}}$이라 하면" \
                        f"\n$\qquad f'(x)=2x$" \
                        f"\n곡선 $y=f(x)$의 접선 중에서 직선 {line}과 평행한 접선의 접점의 좌표를 $(t,\ t^{{2}})$이라 하면 " \
                        f"이 점에서의 접선의 기울기가 ${2 * self.a}$이어야 하므로" \
                        f"\n$\qquad {diff_line}$" \
                        f"\n$\qquad \\therefore\ t={self.a}$" \
                        f"\n그러므로 접점의 좌표는 $({self.a},\ {self.a**2})$이고, " \
                        f"점 $({self.a},\ {self.a**2})$과 " \
                        f"직선 {line}, 즉 ${2 * self.a}x-y-{self.b}=0$ 사이의 거리가 구하는 최솟값이므로" \
                        f"\n$\qquad \dfrac{{|{2 * self.a ** 2} - {self.a ** 2} - {self.b}|}}{{\sqrt{{{2 * self.a}^{{2}}+(-1)^{{2}}}}}}" \
                        f"=\sqrt{{{(self.a ** 2 - self.b) ** 2 // size_of_vec_squared}}}$" \
                        f"\n따라서 $k=\sqrt{{{(self.a ** 2 - self.b) ** 2 // size_of_vec_squared}}}$이므로" \
                        f"\n$\qquad k^{{2}}={(self.a ** 2 - self.b) ** 2 // size_of_vec_squared}$"
        return solution_text