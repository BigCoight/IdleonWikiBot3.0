import { ClassType } from './classType';
import { StatItemModel } from './statItemModel';
import { TypeGen } from './typeGen';

export interface SkullItemModel extends StatItemModel {
    Skill: string,
    Skill_Power: number,
    Speed: number
}
