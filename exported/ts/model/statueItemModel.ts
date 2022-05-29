import { BonusItemModel } from './bonusItemModel';
import { StatueDataModel } from './statueDataModel';
import { TypeGen } from './typeGen';

export interface StatueItemModel extends BonusItemModel {
    statueData: StatueDataModel
}
