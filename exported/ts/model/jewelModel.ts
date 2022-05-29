import { ComponentModel } from './componentModel';

export interface JewelModel {
    x: number,
    y: number,
    range: number,
    effect: string,
    description: string,
    requirements: ComponentModel[],
    name: string,
    bonusGiven: number
}
