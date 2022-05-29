import { TypeGen } from './typeGen';

export interface BaseItemModel {
    internalName: string,
    displayName: string,
    sellPrice: number,
    typeGen: TypeGen,
    Type: string
}
