import { DescItemModel } from './descItemModel';
import { TypeGen } from './typeGen';

export interface ChestItemModel extends DescItemModel {
    order: number,
    level: number
}
