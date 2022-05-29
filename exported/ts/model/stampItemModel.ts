import { StampDataModel } from './stampDataModel';
import { BonusItemModel } from './bonusItemModel';
import { TypeGen } from './typeGen';

export interface StampItemModel extends BonusItemModel {
    ID: number,
    stampData: StampDataModel
}
