from enum import IntFlag, auto

class Condition(IntFlag):
	BURN = auto(),
	FREEZE = auto(),
	PARALYSIS = auto(),
	POISON = auto(),
	BAD_POISON = auto(),
	SLEEP = auto(),

class PassiveCondition(IntFlag):
	BOUND = auto(),
	CANT_ESCAPE = auto(),
	CONFUSION = auto(),
	CURSE = auto(),
	EMBARGO = auto(),
	ENCORE = auto(),
	FLINCH = auto(),
	HEAL_BLOCK = auto(),
	IDENTIFIED = auto(),
	INFATUATED = auto(),
	LEECH_SEED = auto(),
	NIGHTMARE = auto(),
	PERISH_SONG = auto(),
	TAUNT = auto(),
	TELEKINESIS = auto(),
	TORMENT = auto(),

class ActiveCondition(IntFlag):
	AQUA_RING = auto(),
	BRACING = auto(),
	CHARGING_TURN = auto(),
	CENTER_OF_ATTENTION = auto(),
	DEFENSE_CURL = auto(),
	ROOTING = auto(),
	MAGIC_COAT = auto(),
	MAGNETIC_LEVITATION = auto(),
	MINIMIZE = auto(),
	PROTECTION = auto(),
	RECHARGING = auto(),
	SEMI_INVULNERABLE = auto(),
	SUBSTITUTE = auto(),
	TAKING_AIM = auto(),
	WITHDRAWING = auto(),