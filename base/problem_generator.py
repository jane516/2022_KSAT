class ProblemGenerator:
	def execute(self):
		results = []
		return results

	def validate(self):
		raise NotImplementedError

	@classmethod
	def generate_random_input(cls):
		raise NotImplementedError

	@property
	def problem_text(self):
		raise NotImplementedError

	@property
	def solution_text(self):
		raise NotImplementedError

	@property
	def answer(self):
		raise NotImplementedError

	def print(self):
		if not self.validate():
			print('입력값이 조건을 만족시키지 않습니다')
			return
		print('문제: ')
		print(self.problem_text)
		print('---------------------------------')
		print(f'답: {self.answer}')
		print('---------------------------------')
		print('해설: ')
		print(self.solution_text)