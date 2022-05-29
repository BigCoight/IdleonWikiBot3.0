import { ClassType } from './classType';
import { StatItemModel } from './statItemModel';
import { TypeGen } from './typeGen';

export interface WeaponItemModel extends StatItemModel {
    Speed: number,
    Reach: number
}
