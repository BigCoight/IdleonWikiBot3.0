import { ComponentModel } from './componentModel';

export interface ChipModel {
    name: string,
    bonus: string,
    description: string,
    requirements: ComponentModel[],
    bool1: boolean,
    stat: string,
    baseVal: number
}
