import { ClassType } from './classType';
import { BagType } from './bagType';
import { CommonItemModel } from './commonItemModel';
import { TypeGen } from './typeGen';

export interface EquipItemModel extends CommonItemModel {
    lvReqToEquip: number,
    Class: (ClassType | BagType),
    Speed: number,
    Reach: number,
    Weapon_Power: number,
    STR: number,
    AGI: number,
    WIS: number,
    LUK: number,
    Defence: number,
    UQ1txt: string,
    UQ1val: number,
    UQ2txt: string,
    UQ2val: number,
    Upgrade_Slots_Left: number
}
