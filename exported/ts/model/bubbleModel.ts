import { LiquidComponentModel } from './liquidComponentModel';
import { ComponentModel } from './componentModel';

export interface BubbleModel {
    cauldron: string,
    x1: number,
    x2: number,
    func: string,
    description: string,
    requirements: (LiquidComponentModel | ComponentModel)[]
}
