import { PoolType } from './poolType';

export interface FishPoolModel {
    fish: string,
    expGiven: number,
    damageDelt: number,
    efficiency: number,
    cardDrop: string,
    cardChance: number,
    pool: PoolType
}
