from stat_stage import StatStage, AccuracyStage, EvasionStage
from monster import Monster
from poketypes import type_match, Type

for type_a in Type:
	for type_b in Type:
		tm = type_match(type_a, type_b)
		print("[{} x {}]: {} => {}x".format(type_a.name, type_b.name, tm.name, tm.dmg_mult()))

print("StatStage:")
for i in range(-6, 7):
	print(" ", StatStage(i).value())

print("AccuracyStage:")
for i in range(-6, 7):
	print(" ", AccuracyStage(i).value())

print("EvasionStage:")
for i in range(-6, 7):
	print(" ", EvasionStage(i).value())