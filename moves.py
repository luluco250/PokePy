from types import Type
from monster import Monster
from typing import List
import random

def calc_damage(
		user: Monster,
		targets: List[Monster],
		move: Move,
		weather: WeatherType = WeatherType.Clear,
		critical_hit: bool = False,
		random_mult: float = random.uniform(0.85, 1.0)
	):
		return 0

class Move:
	def __init__(self, typing: Type):
		self.typing = typing
	
	def action(self, user: Monster, targets: List[Monster]):
		pass

class AttackMove(Move):
	def __init__(self, typing: Type, base_power: int):
		super().__init__(typing)
		self.base_power = base_power
	
	def action(self, user: Monster, targets: List[Monster]):
		pass
