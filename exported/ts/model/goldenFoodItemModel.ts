import { DescItemModel } from './descItemModel';
import { GoldenFoodDataModel } from './goldenFoodDataModel';
import { TypeGen } from './typeGen';

export interface GoldenFoodItemModel extends DescItemModel {
    goldenFoodData: GoldenFoodDataModel
}
