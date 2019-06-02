from typing import Dict, List
from enum import IntEnum, IntFlag, auto

class Type(IntEnum):
	Normal = 1,
	Fire = 2,
	Water = 3,
	Electric = 4,
	Grass = 5,
	Ice = 6,
	Fighting = 7,
	Poison = 8,
	Ground = 9,
	Flying = 10,
	Psychic = 11,
	Bug = 12,
	Rock = 13,
	Ghost = 14,
	Dragon = 15,
	Dark = 16,
	Steel = 17,
	Fairy = 18

TYPE_MATCH_DMG_MULT: List[float] = [1.0, 2.0, 0.5, 0.0]

class TypeMatch(IntEnum):
	Normal = 0,
	Strong = 1,
	Weak = 2,
	Immune = 3

	def dmg_mult(self) -> float:
		return TYPE_MATCH_DMG_MULT[self.value]

def type_match(a: Type, b: Type) -> TypeMatch:
	if a in TYPE_WEAK_TO[b]:
		return TypeMatch.Strong
	elif b in TYPE_WEAK_AGAINST[a]:
		return TypeMatch.Weak
	elif a in TYPE_IMMUNE_TO[b]:
		return TypeMatch.Immune
	else:
		return TypeMatch.Normal

TYPE_WEAK_TO: Dict[Type, List[Type]] = {
	Type.Normal: [Type.Fighting],
	Type.Fire: [Type.Water, Type.Ground, Type.Rock],
	Type.Water: [Type.Electric, Type.Grass],
	Type.Electric: [Type.Ground],
	Type.Grass: [Type.Fire, Type.Ice, Type.Poison, Type.Flying, Type.Bug],
	Type.Ice: [Type.Fire, Type.Fighting, Type.Rock, Type.Steel],
	Type.Fighting: [Type.Flying, Type.Psychic, Type.Fairy],
	Type.Poison: [Type.Ground, Type.Psychic],
	Type.Ground: [Type.Water, Type.Grass, Type.Ice],
	Type.Flying: [Type.Electric, Type.Ice, Type.Rock],
	Type.Psychic: [Type.Bug, Type.Ghost, Type.Dark],
	Type.Bug: [Type.Fire, Type.Flying, Type.Rock],
	Type.Rock: [Type.Water, Type.Grass, Type.Fighting, Type.Ground, Type.Steel],
	Type.Ghost: [Type.Ghost, Type.Dark],
	Type.Dragon: [Type.Ice, Type.Dragon, Type.Fairy],
	Type.Dark: [Type.Fighting, Type.Bug, Type.Fairy],
	Type.Steel: [Type.Fire, Type.Fighting, Type.Ground],
	Type.Fairy: [Type.Poison, Type.Steel]
}

TYPE_WEAK_AGAINST: Dict[Type, List[Type]]  = {
	Type.Normal: [Type.Rock, Type.Steel],
	Type.Fire: [Type.Fire, Type.Water, Type.Rock, Type.Dragon],
	Type.Water: [Type.Water, Type.Grass, Type.Dragon],
	Type.Electric: [Type.Electric, Type.Grass, Type.Dragon],
	Type.Grass: [Type.Fire, Type.Grass, Type.Poison, Type.Flying, Type.Dragon],
	Type.Ice: [Type.Fire, Type.Water, Type.Ice, Type.Steel],
	Type.Fighting: [Type.Poison, Type.Flying, Type.Psychic, Type.Bug, Type.Fairy],
	Type.Poison: [Type.Poison, Type.Ground, Type.Rock, Type.Ghost],
	Type.Ground: [Type.Grass, Type.Bug],
	Type.Flying: [Type.Electric, Type.Rock, Type.Steel],
	Type.Psychic: [Type.Psychic, Type.Steel],
	Type.Bug: [Type.Fire, Type.Fighting, Type.Poison, Type.Flying, Type.Ghost, Type.Steel, Type.Fairy],
	Type.Rock: [Type.Fighting, Type.Ground, Type.Steel],
	Type.Ghost: [Type.Dark],
	Type.Dragon: [Type.Steel],
	Type.Dark: [Type.Fighting, Type.Dark, Type.Fairy],
	Type.Steel: [Type.Fire, Type.Water, Type.Electric, Type.Steel],
	Type.Fairy: [Type.Fire, Type.Poison, Type.Dark]
}

TYPE_IMMUNE_TO: Dict[Type, List[Type]]  = {
	Type.Normal: [Type.Ghost],
	Type.Fire: [],
	Type.Water: [],
	Type.Electric: [],
	Type.Grass: [],
	Type.Ice: [],
	Type.Fighting: [],
	Type.Poison: [],
	Type.Ground: [Type.Electric],
	Type.Flying: [Type.Ground],
	Type.Psychic: [],
	Type.Bug: [],
	Type.Rock: [],
	Type.Ghost: [Type.Normal, Type.Fighting],
	Type.Dragon: [],
	Type.Dark: [Type.Psychic],
	Type.Steel: [Type.Poison],
	Type.Fairy: [Type.Dragon]
}