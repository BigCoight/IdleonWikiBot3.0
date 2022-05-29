import { DescItemModel } from './descItemModel';
import { TypeGen } from './typeGen';

export interface InvBagItemModel extends DescItemModel {
    order: number,
    level: number
}
