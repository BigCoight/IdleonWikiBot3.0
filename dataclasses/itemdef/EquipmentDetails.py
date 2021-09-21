from ItemDetails import ItemDetails


class EquipmentDetails(ItemDetails):
    ''' 
    This dataclass contails all of the base details of the items that contain
    combat stats
    '''
    lvReqToEquip: int
    Class: str
    Speed: int
    Reach: int
    Weapon_Power: int
    STR: int
    AGI: int
    WIS: int
    LUK: int
    Defence: int
    UQ1txt: int
    UQ1val: str
    UQ2txt: int
    UQ2val: str
    Upgrade_Slots_Left: int
    equip: str
