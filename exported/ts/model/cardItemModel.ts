import { CardDataModel } from './cardDataModel';
import { BaseItemModel } from './baseItemModel';
import { TypeGen } from './typeGen';

export interface CardItemModel extends BaseItemModel {
    cardData?: CardDataModel,
    dropChance: number
}
