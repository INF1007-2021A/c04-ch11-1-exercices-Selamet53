"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20

	def __init__(self, name: str, power: float, min_level: int) -> None:
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self) -> str:
		return self.__name

	"""
	@property
	def power(self) -> float:
		return self.__power

	@power.setter
	def power(self, value: float) -> None:
		self.__power = value

	@property
	def min_level(self) -> int:
		return self.__min_level

	@min_level.setter
	def min_level(self, value: int) -> None:
		self.__min_level = value
	"""

	@classmethod
	def make_unarmed(self):
		return self("Unarmed", self.UNARMED_POWER, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name: str, max_hp: float, attack: float, defense: float, level: int) -> None:
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp

	@property
	def name(self) -> str:
		return self.__name

	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, value) -> None:
		if value is None:
			value = Weapon.make_unarmed()
		if value.min_level > self.level:
			raise ValueError(Weapon)
		self.__weapon = value

	@property
	def hp(self) -> float:
		return self.__hp

	@hp.setter
	def hp(self, value: float):
		self.__hp = utils.clamp(value, 0, self.max_hp)

	def compute_damage(self, other) -> float:
		level_factor = (2 * self.level) / 5 + 2
		weapon_factor = self.weapon.power
		attack_defense_factor = self.attack / other.defense
		critical = random.random() <= 1/16
		modifier_factor = (2 if critical else 1) * (random.uniform(0.85, 1))
		damage = ((level_factor * weapon_factor * attack_defense_factor) / 50 + 2) * modifier_factor
		return int(round(damage)), critical


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
	# TODO: Retourner nombre de tours effectués
