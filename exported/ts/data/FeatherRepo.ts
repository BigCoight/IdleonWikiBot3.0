import { FeatherModel } from '../model/featherModel';

export class FeatherBase { constructor(public index: number, public data: FeatherModel) { } }



export const initFeatherRepo = () => {
    return [    
        new FeatherBase(0, <FeatherModel>{
                "name": "Feather Generation",
                "x1": 5,
                "x2": 1.1,
                "x3": 100,
                "bonus1": "{/sec",
                "bonus2": "Generates +1 feather per second"
            }),
        new FeatherBase(1, <FeatherModel>{
                "name": "Bonuses of Orion",
                "x1": 350,
                "x2": 25,
                "x3": 1000,
                "bonus1": "+{% Class XP",
                "bonus2": "Gain a permanent bonus for outside this map! This upgrade never resets..."
            }),
        new FeatherBase(2, <FeatherModel>{
                "name": "Feather Multiplier",
                "x1": 500,
                "x2": 1.11,
                "x3": 2500,
                "bonus1": "+{ Base DMG",
                "bonus2": "Boosts feather generation by +5%"
            }),
        new FeatherBase(3, <FeatherModel>{
                "name": "Feather Cheapener",
                "x1": 3000,
                "x2": 1.16,
                "x3": 30000,
                "bonus1": "+{% Total DMG",
                "bonus2": "All feather upgrades are 10% cheaper"
            }),
        new FeatherBase(4, <FeatherModel>{
                "name": "Feather Restart",
                "x1": 1e+06,
                "x2": 14,
                "x3": 750000,
                "bonus1": "+{% Skill XP",
                "bonus2": "Reset almost all Upgrades and Feathers. Generate {x Feathers"
            }),
        new FeatherBase(5, <FeatherModel>{
                "name": "Super Feather Production",
                "x1": 2e+06,
                "x2": 1.12,
                "x3": 1e+07,
                "bonus1": "+{% Drop Rate",
                "bonus2": "Generates +5 feathers per second"
            }),
        new FeatherBase(6, <FeatherModel>{
                "name": "Shiny Feathers",
                "x1": 5e+06,
                "x2": 1.4,
                "x3": 2.5e+08,
                "bonus1": "+{ All Stat",
                "bonus2": "Rare chance for a Shiny Feather, each one gives +1% feather generation"
            }),
        new FeatherBase(7, <FeatherModel>{
                "name": "Super Feather Cheapener",
                "x1": 5e+07,
                "x2": 1.27,
                "x3": 5e+09,
                "bonus1": "{",
                "bonus2": "All feather upgrades are 20% cheaper"
            }),
        new FeatherBase(8, <FeatherModel>{
                "name": "The Great Mega Reset",
                "x1": 2.5e+11,
                "x2": 20,
                "x3": 1e+11,
                "bonus1": "Nah",
                "bonus2": "Reset almost everything. Gain a permanent Megafeather"
            })    
]
}
