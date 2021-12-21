from typing import List

from pydantic import BaseModel
from helpers.CustomTypes import Integer

class TaskDescription(BaseModel):
	name: str
	description: str
	extraStr: str
	number1: Integer
	descLine2: str
	numbers: List[Integer]


# "Faceless_Deathmachine Defeat_a_total_of_{_monsters._Thats_{_},_all_thanks_to_you! broken_homes|more_widows|sad_children|grieving_families|life_insurance_claims|extra_gravestones|bitter_memories|steps_to_extinction|lives_cut_short|loot_rolls 5 1|0|Was_it_worth_it?_All_that_bloodshed,_all_for_nothi--_oh_wow_thats_some_cool_loot! 2000 10000 20000 100000 500000 2000000 6000000 12000000 25000000 50000000"
# "Just_One_More_Before_Bed Level_up_{_times._This_is_shared_between_all_characters,_as_is_every_other_task! Blank420q 5 1|0|Be_honest,_you_just_kept_playing_in_bed_from_your_phone_didn't_you 30 70 150 300 600 1200 2500 8000 15000 25000"
# "Super_Explosive_Gameplay Claim_{_hours_of_AFK_gains. Blank420q 5 1|0|The_waiiiiiiiting_is_the_hardest_parrrt._Well,_and_the_everything_else_too. 10 70 300 1000 2500 8000 20000 60000 140000 250000"
# "Achievement_Hunter Complete_{_Blunder_Hills_achievements,_accessed_with_that_button_in_the_top_left! 5 2|0|Filler_lol 5 10 15 20 25 30 40 50 60 70"
# "It's_a_me,_Regularigi! Defeat_{_Poops._Try_to_resist_your_urge_to_jump_on_them_though... Blank420q 4 0 69 _ _ _ _ _ _ _ _ _"
# "Sayin'_yo_to_your_bro Say_hi_to_Funguy._Like..._literally_say_hi. Blank420q 2 0 1 _ _ _ _ _ _ _ _ _"