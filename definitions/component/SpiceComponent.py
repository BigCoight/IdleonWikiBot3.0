from definitions.component.ComponentBase import ComponentBase
from helpers.CustomTypes import Integer


class SpiceComponent(ComponentBase):
	spiceNo: str
	quantity: Integer
