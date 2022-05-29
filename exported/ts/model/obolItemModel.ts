import { ClassType } from './classType';
import { StatItemModel } from './statItemModel';
import { TypeGen } from './typeGen';

export interface ObolItemModel extends StatItemModel {
    family: string,
    rarity: string,
    Skill: string,
    Skill_Power: number
}
