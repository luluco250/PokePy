from enum import IntEnum, auto

class StatStage:
	def __init__(self, stage: int = 0):
		self._stage = stage
	
	def get_mult(self):
		if self._stage >= 0:
			return (self._stage + 2) / 2
		else:
			return 2 / abs(self._stage - 2)
	
	def up(self, amount: int = 1) -> StatStage:
		self._set_stage(self._stage + amount)
		return self
	
	def down(self, amount: int = 1) -> StatStage:
		self._set_stage(self._stage - amount)
		return self
	
	def reset(self) -> StatStage:
		self._stage = 0
		return self
	
	def get_stage(self) -> int:
		return self._stage
	
	def _set_stage(self, value: int) -> None:
		self._stage = min(max(value, -6), 6)

class AccuracyStage(StatStage):
	def get_mult(self):
		if self._stage >= 0:
			return abs(self._stage + 3) / 3
		else:
			return 3 / (self._stage - 3)

class EvasionStage(StatStage):
	def get_mult(self):
		if self._stage >= 0:
			return 3 / (self._stage + 3)
		else:
			return abs(self._stage - 3) / 3