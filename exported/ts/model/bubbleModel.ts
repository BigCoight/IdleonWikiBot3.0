import { ComponentModel } from './componentModel';
import { LiquidComponentModel } from './liquidComponentModel';

export interface BubbleModel {
    cauldron: string,
    x1: number,
    x2: number,
    func: string,
    description: string,
    requirements: (LiquidComponentModel | ComponentModel)[]
}
