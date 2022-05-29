import { FishPoolModel } from '../model/fishPoolModel';
import { PoolType } from '../model/poolType';

export class FishPoolBase { constructor(public index: number, public data: FishPoolModel) { } }



export const initFishPoolRepo = () => {
    return [    
        new FishPoolBase(0, <FishPoolModel>{
                "fish": "Fish1",
                "expGiven": 4,
                "damageDelt": 25,
                "efficiency": 0,
                "cardDrop": "CardsC8",
                "cardChance": 0.002,
                "pool": PoolType.FishSmall
            }),
        new FishPoolBase(1, <FishPoolModel>{
                "fish": "Fish2",
                "expGiven": 7,
                "damageDelt": 70,
                "efficiency": 50,
                "cardDrop": "CardsC9",
                "cardChance": 0.0018,
                "pool": PoolType.FishSmall
            }),
        new FishPoolBase(2, <FishPoolModel>{
                "fish": "Fish3",
                "expGiven": 12,
                "damageDelt": 120,
                "efficiency": 200,
                "cardDrop": "CardsC10",
                "cardChance": 0.0016,
                "pool": PoolType.FishSmall
            }),
        new FishPoolBase(3, <FishPoolModel>{
                "fish": "Fish4",
                "expGiven": 21,
                "damageDelt": 200,
                "efficiency": 400,
                "cardDrop": "CardsD11",
                "cardChance": 0.0014,
                "pool": PoolType.FishSmall
            }),
        new FishPoolBase(4, <FishPoolModel>{
                "fish": "Fish5",
                "expGiven": 35,
                "damageDelt": 300,
                "efficiency": 0,
                "cardDrop": "CardsF20",
                "cardChance": 0.001,
                "pool": PoolType.FishMed
            }),
        new FishPoolBase(5, <FishPoolModel>{
                "fish": "Fish6",
                "expGiven": 60,
                "damageDelt": 750,
                "efficiency": 10000,
                "cardDrop": "CardsF21",
                "cardChance": 0.0004,
                "pool": PoolType.FishMed
            }),
        new FishPoolBase(6, <FishPoolModel>{
                "fish": "Fish7",
                "expGiven": 92,
                "damageDelt": 1500,
                "efficiency": 50000,
                "cardDrop": "CardsF22",
                "cardChance": 0.0001,
                "pool": PoolType.FishMed
            }),
        new FishPoolBase(7, <FishPoolModel>{
                "fish": "Fish8",
                "expGiven": 150,
                "damageDelt": 5000,
                "efficiency": 200000,
                "cardDrop": "CardsF23",
                "cardChance": 2.5e-05,
                "pool": PoolType.FishMed
            })    
]
}
