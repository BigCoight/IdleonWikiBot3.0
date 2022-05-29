import { BonusItemModel } from './bonusItemModel';
import { StampDataModel } from './stampDataModel';
import { TypeGen } from './typeGen';

export interface StampItemModel extends BonusItemModel {
    ID: number,
    stampData: StampDataModel
}
