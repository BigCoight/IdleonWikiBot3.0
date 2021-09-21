from ItemDetails import ItemDetails


class ResourceDetails(ItemDetails):
    ''' 
    This dataclass contails all of the base details of the the items whose type
    contains description and that
    '''
    desc_line1: str
    desc_line2: str
    desc_line3: str
    desc_line4: str
    desc_line5: str
    desc_line6: str
    desc_line7: str
    desc_line8: str
    Effect: str
    Amount: int
    Trigger: int
    Cooldown: int
    consumeable: int
