import random
from species import Species
from stat_stage import StatStage, AccuracyStage, EvasionStage
from weather import WeatherType

class Monster:
	def __init__(self, species: Species, level: int = 1, nickname: str = None):
		self.species = species
		self.level = level
		self.nickname = nickname or species.name
		self.curr_hp = species.base_hp
		self.atk_stage = StatStage()
		self.def_stage = StatStage()
		self.sp_atk_stage = StatStage()
		self.sp_def_stage = StatStage()
		self.spd_stage = StatStage()
		self.acc_stage = AccuracyStage()
		self.eva_stage = EvasionStage()
	
	def health(self) -> int:
		return self.curr_hp
	
	def attack(self) -> float:
		return self.species.base_atk * self.atk_stage.get_mult()
	
	def defense(self) -> float:
		return self.species.base_def * self.def_stage.get_mult()
	
	def sp_attack(self) -> float:
		return self.species.base_sp_atk * self.sp_atk_stage.get_mult()
	
	def sp_defense(self) -> float:
		return self.species.base_sp_def * self.sp_def_stage.get_mult()
	
	def speed(self) -> float:
		return self.species.base_spd * self.spd_stage.get_mult()
	
	def accuracy(self) -> float:
		return self.acc_stage.get_mult()
	
	def evasion(self) -> float:
		return self.eva_stage.get_mult()