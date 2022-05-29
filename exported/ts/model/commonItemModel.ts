import { TypeGen } from './typeGen';

export interface CommonItemModel {
    internalID: string,
    displayName: string,
    sellPrice: number,
    typeGen: TypeGen,
    ID: number,
    Type: string,
    lvReqToCraft: number
}
