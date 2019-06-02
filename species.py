class Species:
	def __init__(
		self,
		id: int,
		name: str,
		base_hp: int,
		base_atk: int,
		base_def: int,
		base_sp_atk: int,
		base_sp_def: int,
		base_spd: int
	):
		self.id = id
		self.name = name
		self.base_hp = base_hp
		self.base_atk = base_atk
		self.base_def = base_def
		self.base_sp_atk = base_sp_atk
		self.base_sp_def = base_sp_def
		self.base_spd = base_spd

bulbasaur = Species(1, "Bulbasaur", 45, 49, 49, 65, 65, 45)
charmander = Species(4, "Charmander", 39, 52, 43, 60, 50, 65)
squirtle = Species(7, "Squirtle", 44, 48, 65, 50, 64, 43)
pikachu = Species(25, "Pikachu", 35, 55, 40, 50, 50, 90)