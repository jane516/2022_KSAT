from base.problem_generator import ProblemGenerator
import random


class JaneProblem2(ProblemGenerator):
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    @classmethod
    def generate_random_input(cls):
        x_list = [i for i in range(5, 21)]
        y_list = [1, 2]

        x = x_list[random.randrange(len(x_list))]
        y = y_list[random.randrange(len(y_list))]

        return x, y

    def validate(self):
        x = self.x
        y = self.y
        if x < 5 or x > 20:
            return False
        if x % 2 == 0 and y != 1:
            return False
        if x % 2 == 1 and y != 2:
            return False
        if 180 * y / (x + y) != int(180 * y / (x + y)):
            return False
        return True

    @property
    def answer(self):
        answer = (self.x + 2) * (self.x - 1) // 2
        return answer

    @property
    def problem_text(self):
        x = self.x
        y = self.y
        problem_text = (
            f"한 내각의 크기와 한 외각의 크기의 비가 {{{x} : {y}}} 인 " f"정다각형의 대각선의 개수를 구하시오."
        )
        return problem_text

    @property
    def solution_text(self):
        x = self.x
        y = self.y
        if x % 2 == 0:
            x //= 2

        solution_text = (
            f"한 내각의 크기와 한 외각의 크기의 합은 $180^{{\circ}}$이므로 주어진 정다각형의 한 외각의 크기는"
            f"\n$\qquad 180^{{\circ}}\\times\dfrac{{{y}}}{{{x + y}}}={180 * y // (x + 2)}^{{\circ}}$"
            f"\n주어진 정다각형을 정$n$각형이라 하면"
            f"\n$\qquad \dfrac{{360^ {{\circ}}}}{{n}}={180 * y // (x + 2)}^{{\circ}}$"
            f"\n$\qquad \\therefore\ n={2 * (x + 2) // y}$"
            f"\n따라서 정십오각형의 대각선의 개수는"
            f"\n$\qquad \dfrac{{{2 * (x + 2) // y}\\times({2 * (x + 2) // y}-3)}}{{2}}={self.answer}$"
        )
        return solution_text