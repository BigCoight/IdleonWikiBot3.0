from typing import List, Dict

from definitions.misc.UpgradeVault import UpgradeVault
from helpers.HelperFunctions import replaceUnderscores, getFromSplitArray
from repositories.master.Repository import Repository


class UpgradeVaultRepo(Repository[UpgradeVault]):
    # Mapping of upgrade index to tooltip text from the UI code
    TOOLTIP_TEXTS: Dict[int, str] = {
        1: "These talent points are just for the 1st Tab.",
        4: "As a Beginner you... wait, why are you a beginner? Go get a class!",  # This varies by class but we'll use the default
        6: "These talent points are just for the 2nd Tab.",
        10: "You can actually craft from ANYWHERE! Open your Codex, go to Quik Ref tab, then click Anvil! Boom!",
        11: "This bonus INCREASES for every ore you mine! It also counts ores mined from any player, so go make a 2nd player!",
        12: "Create more characters at the Main Menu! Open MENU\\SWAP PLAYERS\\_PLAYER_MENU in the top left corner! Ez Pz!",
        14: "POW 10 means Power of 10. So you get more bonus at 100, 1000, and so on! ALSO, this counts kills from ALL your players!",
        15: "A Knockout, or KO, is when you kill the target monster in a single hit using your bare hands, no weapon equipped!",
        19: "He a happy boi!",
        20: "POW 10 means Power of 10. So you get more bonus at 100, 1000, and so on! ALSO, this counts kills from ALL your players!",
        21: "Orion the Owl can be found in the SECRET portal on the Bored Beans map! Ok, it's not really a secret, but like whatever...",
        24: "Click the PRODUCE tab at the anvil, it will flash if you haven't found it yet!",
        27: "POW 10 means Power of 10. So you get more bonus at 100, 1000, and so on! ALSO, this counts kills from ALL your players!",
        31: "Can't find poops? The sewer entrance is literally where you started the game!"
    }

    @classmethod
    def getCategory(cls) -> str:
        return "Misc"

    @classmethod
    def getSections(cls) -> List[str]:
        return ["UpgradeVault"]

    @classmethod
    def generateRepo(cls) -> None:
        vault_data = getFromSplitArray(cls.getSection())
        
        for index, data in enumerate(vault_data):
            if not data or len(data) < 11:  # We need at least 11 fields since we use index 10
                continue
                
            name = replaceUnderscores(data[0])
            has_tooltip = "製" in name
            
            # Mapping based on game's UI code:
            # data[0] is name
            # data[1] is base_cost
            # data[2] is scaling_factor
            # data[3] is x1 (unknown purpose)
            # data[4] is max_level (used in level checks)
            # data[5] is value (used in bonus calculations)
            # data[6] is unlock_req (used in unlock checks)
            # data[8] is x2 (unknown purpose)
            # data[9] is description_line1
            # data[10] is description_line2
            description_line1 = data[9]
            description_line2 = None if data[10] == "_" else data[10]
            x2 = data[8]
            
            # Get tooltip text if it exists for this index
            tooltip_text = cls.TOOLTIP_TEXTS.get(index)
            
            upgrade = UpgradeVault(
                name=name,
                base_cost=int(data[1]),
                scaling_factor=float(data[2]),
                x1=int(data[3]),
                max_level=int(data[4]),
                value=int(data[5]),
                unlock_req=int(data[6]),
                x2=x2,
                description_line1=description_line1,
                description_line2=description_line2,
                has_tooltip=has_tooltip,
                tooltip_text=tooltip_text
            )
            
            cls.add(name, upgrade)
            cls.addList(upgrade) 