import { ComponentModel } from './componentModel';

export interface BuildingModel {
    name: string,
    description: string,
    bonus: string,
    lvlUpReq: ComponentModel[],
    maxLvl: number,
    costInc: number,
    bonusInc: number[],
    misc: number
}
