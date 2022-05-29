import { GoldenFoodDataModel } from './goldenFoodDataModel';
import { DescItemModel } from './descItemModel';
import { TypeGen } from './typeGen';

export interface GoldenFoodItemModel extends DescItemModel {
    goldenFoodData: GoldenFoodDataModel
}
