import { BaseItemModel } from './baseItemModel';
import { CardDataModel } from './cardDataModel';
import { TypeGen } from './typeGen';

export interface CardItemModel extends BaseItemModel {
    cardData?: CardDataModel,
    dropChance: number
}
