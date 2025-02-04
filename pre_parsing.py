import re

ver = "2.27"

re_big_list = re.compile(r'var bigList=\{.*?\},')
re_parse = re.compile(r"..\.parse\('\{.*?\),")
re_worming = re.compile(r"%_chance to wake_")

spaced = [
	(
		""""TALENT_POINT;1;1;1;1.3;Liquid1;Liquid2;Blank;Blank;Gives_a_redeemable_talent_point_for_the_2nd_Talent Tab._Applies_to_all_characters._Also,_this_item's_cost_will_never_reset,_never_ever_ever!;1;3;1;0;0;0;0".split(";")""",
		(
			""""TALENT_POINT 1 1 1 1.3 Liquid1 Liquid2 Blank Blank Gives_a_redeemable_talent_point_for_the_2nd_Talent_Tab._Applies_to_all_characters._Also,_this_item's_cost_will_never_reset,_never_ever_ever! 1 3 1 0 0 0 0".split(" ")""")
	),
	(
		""""TALENT_POINT;1;1;1;1.27;Liquid3;Blank;Blank;Blank;Gives_a_redeemable_talent_point_for_the_3rd_Talent Tab._Applies_to_all_characters._This_item's_cost_will_reset_every_50,000,000_years.;4;3;0;0;0;0;0".split(";")""",
		""""TALENT_POINT 1 1 1 1.27 Liquid3 Blank Blank Blank Gives_a_redeemable_talent_point_for_the_3rd_Talent_Tab._Applies_to_all_characters._This_item's_cost_will_reset_every_50,000,000_years. 4 3 0 0 0 0 0".split(" ")"""
	),
	(
		""""EquipmentKeychain0;TIER_1_KEYCHAIN;Gives_you_40_keychain_fragments,_enough_to_claim_a_Tier_1_Keychain_from_the_Frog_Dungeon_Lobby!_These_keychains_randomly_give_the_following_bonuses:_Base_Def, Accuracy,_Move_speed,_Base_Dmg,_Card_Drop_rate,_Money,_Base_Stat;150;86;100000;0;0".split(";")""",
		""""EquipmentKeychain0 TIER_1_KEYCHAIN Gives_you_40_keychain_fragments,_enough_to_claim_a_Tier_1_Keychain_from_the_Frog_Dungeon_Lobby!_These_keychains_randomly_give_the_following_bonuses:_Base_Def,_Accuracy,_Move_speed,_Base_Dmg,_Card_Drop_rate,_Money,_Base_Stat 150 86 100000 0 0".split(" ")"""
	)

]

with open("N.js", mode = 'r', encoding = 'utf-8') as infile:
	text = infile.read()
	text = re_big_list.sub(r"", text)
	text = re_parse.sub(r"", text)
	text = re_worming.sub(r"%_chance_to_wake_", text)

	for old, new in spaced:
		text = text.replace(old, new)

with open(f"codefiles/idleon{ver}.txt", mode = "w", encoding = 'utf-8') as outfile:
	outfile.write(text)

import subprocess

subprocess.run(["powershell",
                f"npx prettier --print-width 240 --tab-width 4 --trailing-comma es5 --write --parser babel codefiles/idleon{ver}.txt"],
               cwd = ".")
