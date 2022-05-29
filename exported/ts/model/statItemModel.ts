import { ClassType } from './classType';
import { BaseItemModel } from './baseItemModel';
import { TypeGen } from './typeGen';

export interface StatItemModel extends BaseItemModel {
    lvReqToCraft: number,
    lvReqToEquip: number,
    Class: ClassType,
    Weapon_Power: number,
    STR: number,
    AGI: number,
    WIS: number,
    LUK: number,
    Defence: number,
    miscUp1: string,
    miscUp2: string,
    Upgrade_Slots_Left: number
}
