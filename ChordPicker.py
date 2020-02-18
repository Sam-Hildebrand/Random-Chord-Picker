#!/usr/bin/python3

import argparse # To handle commandline options
import random # The only reason random is needed here is for the PickFromListAction class.
import charts # Imports the custom lists in charts.py 

def RootPkr(): # Selects at random from the list of Root notes in Charts.py
	return(random.choice(charts.Roots))

def AccidentPkr(): # Selects at random from the list of Accidents in Charts.py
	return(random.choice(charts.Accidents))

def ModifierPkr(): # Selects at random from the list of "Modifiers" in Charts.py
	return(random.choice(charts.Modifiers))

def NumberPkr(modifier): # Selects at random from either the MajScale or MinScale in Charts.py based on "Modifier".
	if modifier == "":
		number = random.choice(charts.MajScale)
	elif modifier == "m":
		number = random.choice(charts.MinScale)
	else:
		number = "ERROR"
	return(number)

def PickChord(): # Selects a random root, accident, and modifier and returns them as a combined string.
		root	 = RootPkr()
		accident = AccidentPkr()
		modifier = ModifierPkr()
		return(root + accident + modifier)

def PickNumber(): # Selects a random modifier, uses it to select a random chord number and return it.
	modifier = ModifierPkr()
	return(NumberPkr(modifier))

def CheckChord(chord): # Checks that a chord is not a unusual chord such a Fb and returns the correct enharmonic
	if chord == "Fb":
		return("E")
	elif chord == "Fbm":
		return("Em")
	elif chord == "Cb":
		return("B")
	elif chord == "Cbm":
		return("Bm")
	elif chord == "E#":
		return("F")
	elif chord == "E#m":
		return("Fm")
	elif chord == "B#":
		return("C")
	elif chord == "B#m":
		return("Cm")
	else:
		return(chord)

class PickRootAction(argparse.Action): # A class structure for RootPkr() that is compatible with argparse.
	def __call__(self, parser, namespace, values, option_string=None):
		print(RootPkr())

class PickAccidentAction(argparse.Action): # A class structure for AccidentPkr() that is compatible with argparse.
	def __call__(self, parser, namespace, values, option_string=None):
		print(AccidentPkr())

class PickModifierAction(argparse.Action): # A class structure for ModifierPkr() that is compatible with argparse.
	def __call__(self, parser, namespace, values, option_string=None):
		print(ModifierPkr())

class PickChordAction(argparse.Action): # A class structure for PickChord() that is compatible with argparse.
	def __call__(self, parser, namespace, values, option_string=None):
		print(PickChord())

class CheckChordAction(argparse.Action): # A class structure for CheckChord() that is compatible with argparse.
	def __call__(self, parser, namespace, values, option_string=None):
		print(CheckChord(PickChord()))

class PickNumberAction(argparse.Action): # A class structure for NumberPkr(modifier) that is compatible with argparse.
	def __call__(self, parser, namespace, values, option_string=None):
		print('Select either major (" ") or minor ("m") scale: ')
		ipt = input()
		print(NumberPkr(ipt))

class PickFromListAction(argparse.Action): # A class structure that picks at random from a list inputed by the user. Compatible with argparse.
	def __call__(self, parser, namespace, values, option_string=None):
		print("Enter items to be selected from: ")
		ipt = input()
		print(random.choice(ipt))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='ChordPicker_v.0.2: Picks a random root, accidental, mode, chord or chord number') # Initiates argparse.
	parser.add_argument('-r', '--root', action=PickRootAction, nargs='?', help='Picks a random root note ("A","B", "C", etc.) and prints it as a string') 
	parser.add_argument('-a', '--accidental', action=PickAccidentAction, nargs='?', help='Picks a random accidental ("#", "b", or "") and prints it as a string')
	parser.add_argument('-m', '--modifier', action=PickModifierAction, nargs='?', help='Picks a random tone modifier ("" or "m") and prints it as a string')
	parser.add_argument('-c', '--chord', action=PickChordAction, nargs='?', help='Picks a random root note, accidental, and modifier and prints them in a string')
	parser.add_argument('-C', '--CheckChord', action=CheckChordAction, nargs='?', help='Picks a random root note, accidental, and modifier, replaces it with its enharmonic chord in the case of Fb, B#, etc, and prints it in a string')
	parser.add_argument('-n', '--number', action=PickNumberAction, nargs='?', help='Picks a random roman numeral chord number ("I", "ii", etc.)')
	parser.add_argument('-i', '--input', action=PickFromListAction, nargs='?', help='Picks a random item from input provided')
	args = parser.parse_args()

