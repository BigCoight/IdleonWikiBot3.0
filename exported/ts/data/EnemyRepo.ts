import { AFKType } from '../model/aFKType';
import { BossAttackModel } from '../model/bossAttackModel';
import { BossDetailsModel } from '../model/bossDetailsModel';
import { CardDropModel } from '../model/cardDropModel';
import { CoinDropModel } from '../model/coinDropModel';
import { EnemyDetailsModel } from '../model/enemyDetailsModel';
import { EnemyModel } from '../model/enemyModel';
import { EnemyNavModel } from '../model/enemyNavModel';
import { EnemyTableModel } from '../model/enemyTableModel';
import { EnemyType } from '../model/enemyType';
import { ItemDropModel } from '../model/itemDropModel';
import { MapDataModel } from '../model/mapDataModel';
import { RecipeDropModel } from '../model/recipeDropModel';
import { SubTableDropModel } from '../model/subTableDropModel';
import { TalentDropModel } from '../model/talentDropModel';

export class EnemyBase { constructor(public id: string, public data: EnemyModel) { } }



export const initEnemyRepo = () => {
    return [    
        new EnemyBase("ForgeA", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Fire Forge",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "CopperBar", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "IronBar", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GoldBar", "quantity": 69, "chance": 0.5, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ForgeB", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Cinder Forge",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PlatBar", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DementiaBar", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "VoidBar", "quantity": 69, "chance": 0.5, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Bandit_Bob", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bandit Bob",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest19", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest19", "quantity": 69, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest19", "quantity": 69, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest19", "quantity": 69, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest19", "quantity": 69, "chance": 0.01, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest19", "quantity": 69, "chance": 0.07, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "Crystal1",
                    "next": "Blank",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("SoulCard1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Forest Soul",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC11", "quantity": 1, "chance": 0.00022, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul1", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul1", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul1", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul1", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("SoulCard2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dune Soul",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC12", "quantity": 1, "chance": 0.00018, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul2", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul2", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul2", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul2", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("SoulCard3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Rooted Soul",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD10", "quantity": 1, "chance": 0.00016, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul3", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul3", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul3", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul3", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("SoulCard4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Frigid Soul",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD9", "quantity": 1, "chance": 0.00014, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable12", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("SoulCard5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Squiddy Soul",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD9", "quantity": 1, "chance": 0.00014, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable12", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("SoulCard6", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bandit Bob",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD9", "quantity": 1, "chance": 0.00014, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable12", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("CritterCard1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Froge",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC11", "quantity": 1, "chance": 0.00022, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter1", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("CritterCard2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Crabbo",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC12", "quantity": 1, "chance": 0.00018, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter2", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("CritterCard3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Scorpie",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD10", "quantity": 1, "chance": 0.00016, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter3", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("CritterCard4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Mousey",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD9", "quantity": 1, "chance": 0.00014, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter4", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("CritterCard5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Owlio",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD9", "quantity": 1, "chance": 0.00014, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter5", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("CritterCard6", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Pingy",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD9", "quantity": 1, "chance": 0.00014, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter6", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("CritterCard7", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bunny",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD9", "quantity": 1, "chance": 0.00014, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter7", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("CritterCard8", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dung Beat",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD9", "quantity": 1, "chance": 0.00014, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter8", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("CritterCard9", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Honker",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD9", "quantity": 1, "chance": 0.00014, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter9", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("CritterCard10", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Blobfish",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 420,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD10", "quantity": 1, "chance": 0.00014, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter10", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Cooking", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Cooking",
                    "AFKtype": AFKType.Cooking,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 180,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 100,
                    "ExpType": 10,
                    "Defence": 100,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Laboratory", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Laboratory",
                    "AFKtype": AFKType.Laboratory,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 180,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 25,
                    "ExpType": 12,
                    "Defence": 100,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogP", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Poisonic Frog",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 14,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 43,
                    "HeightOfMonster": 32,
                    "MonsterMoving": 1,
                    "MovingFrame": 5,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 50,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 7,
                    "ExpType": 0,
                    "Defence": 2,
                    "MoveSPEED": 4,
                    "Damages": [5, 1],
                    "DefFor0": 2
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.012, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.0014, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogNest", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Frog Nest",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 13,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 38,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 55,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 3000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 150,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [50, 1],
                    "DefFor0": 40.66
                },
                "drops": <EnemyTableModel>{"drops": []},
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogD", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Globohopper",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 75,
                    "HeightOfMonster": 67,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 10,
                    "MonsterHPTotal": 10000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 4,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.014, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.004, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogY", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "King Frog",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 13,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 72,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 55,
                    "DeathFrame": 14,
                    "MonsterHPTotal": 2500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 95,
                    "ExpType": 0,
                    "Defence": 110,
                    "MoveSPEED": 3,
                    "Damages": [45, 1],
                    "DefFor0": 35.69
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.017, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.006, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogR", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Lava Slimer",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 13,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 55,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 2500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 95,
                    "ExpType": 0,
                    "Defence": 110,
                    "MoveSPEED": 3,
                    "Damages": [45, 1],
                    "DefFor0": 35.69
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogW", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chromatium Frog",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 75,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 7,
                    "MonsterHPTotal": 10000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 0,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.03, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.02, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogGG", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Eldritch Croaker",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 75,
                    "HeightOfMonster": 82,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 45,
                    "DeathFrame": 19,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 6,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.025, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogGR", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Grandfrogger",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 107,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 7,
                    "MonsterHPTotal": 700,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 4,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.8, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogGR2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Rotting Grandfrogger",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 17500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.8, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogGR3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Forlorn Grandfrogger",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 350000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.8, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("frogGR4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Vengeful Grandfrogger",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 1400000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.8, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("rocky", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Grumblo",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 46,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 10,
                    "MonsterHPTotal": 10000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 0,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.016, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.0025, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("cactus", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Cactopunk",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 75,
                    "HeightOfMonster": 61,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 10,
                    "MonsterHPTotal": 10000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 4,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.022, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.005, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("totem", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Lazlo",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 75,
                    "HeightOfMonster": 75,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 7,
                    "MonsterHPTotal": 10000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 4,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.016, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.002, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("target", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Target",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 21,
                    "MonsterOffsetX": 50,
                    "MonsterOffsetY": 34,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 40,
                    "DeathFrame": 10,
                    "MonsterHPTotal": 18500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 310,
                    "ExpType": 0,
                    "Defence": 260,
                    "MoveSPEED": 2,
                    "Damages": [125, 1],
                    "DefFor0": 123.37
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.012, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.0017, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("steakR", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Beefie",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 31,
                    "MonsterOffsetX": 50,
                    "MonsterOffsetY": 72,
                    "HeightOfMonster": 64,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 40,
                    "DeathFrame": 14,
                    "MonsterHPTotal": 23000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 350,
                    "ExpType": 0,
                    "Defence": 300,
                    "MoveSPEED": 5,
                    "Damages": [150, 1],
                    "DefFor0": 152.99
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.018, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.0025, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("potatoB", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Crescent Spud",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 21,
                    "MonsterOffsetX": 50,
                    "MonsterOffsetY": 34,
                    "HeightOfMonster": 89,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 40,
                    "DeathFrame": 17,
                    "MonsterHPTotal": 18500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 310,
                    "ExpType": 0,
                    "Defence": 260,
                    "MoveSPEED": 4,
                    "Damages": [125, 1],
                    "DefFor0": 123.37
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.03, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.005, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("snakeZ", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Snakenhotep",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 90,
                    "HeightOfMonster": 156,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 9,
                    "MonsterHPTotal": 1750,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 4,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.8, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("snakeZ2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Enraged Snakenhotep",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 12250,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.8, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("snakeZ3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Inevitable Snakenhotep",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 1750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.8, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("iceknight", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Ice Guard",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 90,
                    "HeightOfMonster": 76,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 10,
                    "MonsterHPTotal": 10000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 4,
                    "Damages": [50, 1],
                    "DefFor0": 40.66
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.08, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("iceBossZ", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Glaciaxus",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 90,
                    "HeightOfMonster": 141,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 6,
                    "MonsterHPTotal": 2800,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 4,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.8, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("iceBossZ2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Golden Glaciaxus",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 90,
                    "HeightOfMonster": 141,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 6,
                    "MonsterHPTotal": 66000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 4,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.8, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("iceBossZ3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Caustic Glaciaxus",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 90,
                    "HeightOfMonster": 141,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 6,
                    "MonsterHPTotal": 4480000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 3400,
                    "MoveSPEED": 4,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits1", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DungCredits2", "quantity": 1, "chance": 0.8, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Crystal0", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Crystal Carrot",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 1,
                    "MonsterOffsetX": 23,
                    "MonsterOffsetY": 23,
                    "HeightOfMonster": 68,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 35,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 1,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 0,
                    "Defence": 150,
                    "MoveSPEED": 4,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA14", "quantity": 1, "chance": 0.01, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampC3", "quantity": 1, "chance": 0.1, "questLink": "Papua_Piggea2"},
                        <TalentDropModel>{"item": "TalentBook1", "quantity": 3618100, "chance": 0.005, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable1", "quantity": 1, "chance": 0.6, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable2", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3", "quantity": 1, "chance": 0.4, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable4", "quantity": 1, "chance": 0.6, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5b", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "acorn",
                    "next": "mushW",
                    "hasCrystal": false,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("Crystal1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Crystal Crabal",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 11,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 64,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 7500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 210,
                    "ExpType": 0,
                    "Defence": 180,
                    "MoveSPEED": 4,
                    "Damages": [1, 1],
                    "DefFor0": 0
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsB13", "quantity": 1, "chance": 0.008, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampC3", "quantity": 1, "chance": 0.1, "questLink": "Papua_Piggea2"},
                        <TalentDropModel>{"item": "TalentBook1", "quantity": 3618100, "chance": 0.005, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable6", "quantity": 1, "chance": 0.6, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable7", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable8", "quantity": 1, "chance": 0.4, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.6, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable12", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5b", "quantity": 3, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "shovelR",
                    "next": "Bandit_Bob",
                    "hasCrystal": false,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("Crystal2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Crystal Cattle",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 47,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 47,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 252000,
                    "DeathFrame": 17,
                    "MonsterHPTotal": 1000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 210,
                    "ExpType": 0,
                    "Defence": 180,
                    "MoveSPEED": 5,
                    "Damages": [1, 1],
                    "DefFor0": 0
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE15", "quantity": 1, "chance": 0.008, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampC3", "quantity": 1, "chance": 0.1, "questLink": "Papua_Piggea2"},
                        <TalentDropModel>{"item": "TalentBook1", "quantity": 3618100, "chance": 0.005, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable14", "quantity": 1, "chance": 0.6, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable15", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable16", "quantity": 1, "chance": 0.4, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable17", "quantity": 1, "chance": 0.6, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable18", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5b", "quantity": 3, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "skele2",
                    "next": null,
                    "hasCrystal": false,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("Crystal3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Crystal Custard",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 47,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 60,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 252000,
                    "DeathFrame": 14,
                    "MonsterHPTotal": 1000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 210,
                    "ExpType": 0,
                    "Defence": 180,
                    "MoveSPEED": 5,
                    "Damages": [1, 1],
                    "DefFor0": 0
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG14", "quantity": 1, "chance": 0.008, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampC3", "quantity": 1, "chance": 0.1, "questLink": "Papua_Piggea2"},
                        <TalentDropModel>{"item": "TalentBook1", "quantity": 3618100, "chance": 0.005, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable19", "quantity": 1, "chance": 0.6, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable20", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable21", "quantity": 1, "chance": 0.4, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "w4c4",
                    "next": "Blank",
                    "hasCrystal": false,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("mushG", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Green Mushroom",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 1,
                    "MonsterOffsetX": 23,
                    "MonsterOffsetY": 23,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 35,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 10,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [1, 1],
                    "DefFor0": 0
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands1", "quantity": 1, "chance": 0.22, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA0", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodHealth1", "quantity": 3, "chance": 0.005, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentShirts16", "quantity": 1, "chance": 0.00035, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneW2", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Cutter", "quantity": 1, "chance": 1e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable1", "quantity": 1, "chance": 0.003, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Spore Meadows",
                    "world": "Blunder Hills",
                    "id": 1,
                    "portalRequirements": [20]
                },
                "navigation": <EnemyNavModel>{
                    "prev": null,
                    "next": "mushR",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("frogG", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Frog",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 14,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 43,
                    "HeightOfMonster": 30,
                    "MonsterMoving": 1,
                    "MovingFrame": 5,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 50,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 7,
                    "ExpType": 0,
                    "Defence": 2,
                    "MoveSPEED": 4,
                    "Damages": [5, 1],
                    "DefFor0": 2
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 3, "chance": 0.48, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 1, "chance": 0.21, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA2", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest3", "quantity": 1, "chance": 0.15, "questLink": "Picnic_Stowaway2"},
                        <ItemDropModel>{"item": "Quest4", "quantity": 1, "chance": 0.15, "questLink": "Picnic_Stowaway2"},
                        <ItemDropModel>{"item": "FoodPotMana1", "quantity": 1, "chance": 0.002, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats6", "quantity": 1, "chance": 0.00025, "questLink": "N/A"},
                        <ItemDropModel>{"item": "InvStorageF", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable1", "quantity": 1, "chance": 0.0038, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Froggy Fields",
                    "world": "Blunder Hills",
                    "id": 2,
                    "portalRequirements": [30]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "mushR",
                    "next": "beanG",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("beanG", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bored Bean",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 7,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 50,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 150,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 15,
                    "ExpType": 0,
                    "Defence": 4,
                    "MoveSPEED": 4,
                    "Damages": [11, 1],
                    "DefFor0": 5.97
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 5, "chance": 0.46, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands3", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA3", "quantity": 1, "chance": 9.7e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA2", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats25", "quantity": 1, "chance": 3.5e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable1", "quantity": 1, "chance": 0.0045, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Valley Of The Beans",
                    "world": "Blunder Hills",
                    "id": 14,
                    "portalRequirements": [80, 1500]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "frogG",
                    "next": "slimeG",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("slimeG", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Slime",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 24,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 42,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 250,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 23,
                    "ExpType": 0,
                    "Defence": 9,
                    "MoveSPEED": 4,
                    "Damages": [15, 1],
                    "DefFor0": 8.9
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 8, "chance": 0.44, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Jungle1", "quantity": 1, "chance": 0.19, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA4", "quantity": 1, "chance": 9.5e-05, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes1", "quantity": 43, "chance": 3e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "OilBarrel2", "quantity": 10, "chance": 0.0003, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes1", "quantity": 47, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable2", "quantity": 1, "chance": 0.004, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Jungle Perimeter",
                    "world": "Blunder Hills",
                    "id": 16,
                    "portalRequirements": [200, 3000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "beanG",
                    "next": "snakeG",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("snakeG", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Baby Boa",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 25,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 36,
                    "HeightOfMonster": 32,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 45,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 450,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 34,
                    "ExpType": 0,
                    "Defence": 18,
                    "MoveSPEED": 8,
                    "Damages": [18, 1],
                    "DefFor0": 11.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 11, "chance": 0.43, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Jungle2", "quantity": 1, "chance": 0.18, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA5", "quantity": 1, "chance": 9.4e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodHealth2", "quantity": 3, "chance": 0.005, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest7", "quantity": 1, "chance": 0.2, "questLink": "Stiltzcho2"},
                        <ItemDropModel>{"item": "StampA7", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "InvBag100", "quantity": 1, "chance": 8e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable2", "quantity": 1, "chance": 0.005, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Winding Willows",
                    "world": "Blunder Hills",
                    "id": 19,
                    "portalRequirements": [250]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "slimeG",
                    "next": "carrotO",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("carrotO", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Carrotman",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 9,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 45,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 50,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 800,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 45,
                    "ExpType": 0,
                    "Defence": 30,
                    "MoveSPEED": 6,
                    "Damages": [22, 1],
                    "DefFor0": 14.57
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 15, "chance": 0.41, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Jungle3", "quantity": 1, "chance": 0.17, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA6", "quantity": 1, "chance": 9e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodHealth2", "quantity": 4, "chance": 0.006, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentBows4", "quantity": 1, "chance": 4e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable2", "quantity": 1, "chance": 0.006, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Vegetable Patch",
                    "world": "Blunder Hills",
                    "id": 24,
                    "portalRequirements": [300, 2000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "snakeG",
                    "next": "goblinG",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("goblinG", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Glublin",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 15,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 52,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 1250,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 60,
                    "ExpType": 0,
                    "Defence": 52,
                    "MoveSPEED": 4,
                    "Damages": [30, 1],
                    "DefFor0": 21.54
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 19, "chance": 0.39, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Forest1", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA7", "quantity": 1, "chance": 8.6e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneHelm1", "quantity": 1, "chance": 0.00015, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes1", "quantity": 44, "chance": 3e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3", "quantity": 1, "chance": 0.004, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Forest Outskirts",
                    "world": "Blunder Hills",
                    "id": 26,
                    "portalRequirements": [350]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "carrotO",
                    "next": "plank",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("plank", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Wode Board",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 3,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 58,
                    "HeightOfMonster": 46,
                    "MonsterMoving": 1,
                    "MovingFrame": 5,
                    "RespawnTime": 45,
                    "DeathFrame": 19,
                    "MonsterHPTotal": 1800,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 75,
                    "ExpType": 0,
                    "Defence": 70,
                    "MoveSPEED": 3,
                    "Damages": [35, 1],
                    "DefFor0": 26.12
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 23, "chance": 0.37, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Forest2", "quantity": 1, "chance": 0.15, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA8", "quantity": 1, "chance": 8e-05, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes1", "quantity": 48, "chance": 3e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest12", "quantity": 1, "chance": 0.1, "questLink": "Dog_Bone1"},
                        <ItemDropModel>{"item": "EquipmentShirts19", "quantity": 1, "chance": 1e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3", "quantity": 1, "chance": 0.0045, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Encroaching Forest Villas",
                    "world": "Blunder Hills",
                    "id": 27,
                    "portalRequirements": [30, 4200]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "goblinG",
                    "next": "frogBIG",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("frogBIG", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Gigafrog",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 13,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 26,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 55,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 2500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 95,
                    "ExpType": 0,
                    "Defence": 110,
                    "MoveSPEED": 3,
                    "Damages": [45, 1],
                    "DefFor0": 35.69
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 28, "chance": 0.35, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Forest3", "quantity": 1, "chance": 0.14, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA9", "quantity": 1, "chance": 7e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampA10", "quantity": 1, "chance": 3e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodPotRe2", "quantity": 5, "chance": 0.001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampA8", "quantity": 1, "chance": 0.0003, "questLink": "Papua_Piggea1"},
                        <ItemDropModel>{"item": "ObolBronzePop", "quantity": 1, "chance": 1e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3", "quantity": 1, "chance": 0.005, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Tucked Away",
                    "world": "Blunder Hills",
                    "id": 28,
                    "portalRequirements": [0]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "plank",
                    "next": "poopSmall",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("branch", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Walking Stick",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 8,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 20,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 60,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 1500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 120,
                    "ExpType": 0,
                    "Defence": 150,
                    "MoveSPEED": 4,
                    "Damages": [20, 1],
                    "DefFor0": 12.82
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 90, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "TreeInterior1", "quantity": 1, "chance": 0.21, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA12", "quantity": 1, "chance": 6e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "TreeInterior1b", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes1", "quantity": 68, "chance": 0.0002, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3c", "quantity": 1, "chance": 0.0057, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "The Base Of The Bark",
                    "world": "Blunder Hills",
                    "id": 13,
                    "portalRequirements": [2500, 50000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "ratB",
                    "next": "acorn",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("acorn", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Nutto",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 5,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 42,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 60,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 4000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 190,
                    "ExpType": 0,
                    "Defence": 200,
                    "MoveSPEED": 5,
                    "Damages": [40, 1],
                    "DefFor0": 30.84
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 110, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "TreeInterior2", "quantity": 1, "chance": 0.23, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA13", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3c", "quantity": 1, "chance": 0.0065, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Hollowed Trunk",
                    "world": "Blunder Hills",
                    "id": 18,
                    "portalRequirements": [5000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "branch",
                    "next": "Crystal0",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("mushW", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Wood Mushroom",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 34,
                    "MonsterOffsetX": 23,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 50,
                    "DeathFrame": 14,
                    "MonsterHPTotal": 10000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 300,
                    "ExpType": 0,
                    "Defence": 500,
                    "MoveSPEED": 4,
                    "Damages": [75, 1],
                    "DefFor0": 66.8
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 40, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest15", "quantity": 1, "chance": 1e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "TreeInterior1b", "quantity": 1, "chance": 7.5e-05, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA16", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3c", "quantity": 1, "chance": 0.007, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5b", "quantity": 1, "chance": 0.002, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Where the Branches End",
                    "world": "Blunder Hills",
                    "id": 31,
                    "portalRequirements": [0]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "Crystal0",
                    "next": null,
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("poopSmall", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Poop",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 20,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 30,
                    "HeightOfMonster": 32,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 60,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 9000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 220,
                    "ExpType": 0,
                    "Defence": 100,
                    "MoveSPEED": 4,
                    "Damages": [150, 1],
                    "DefFor0": 152.99
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 80, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Sewers1", "quantity": 1, "chance": 0.24, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA10", "quantity": 1, "chance": 6e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Sewers1b", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes1", "quantity": 69, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest22", "quantity": 1, "chance": 0.23, "questLink": "Mutton2"},
                        <ItemDropModel>{"item": "Quest22", "quantity": 1, "chance": 0.23, "questLink": "Mutton3"},
                        <ItemDropModel>{"item": "Quest22", "quantity": 1, "chance": 0.23, "questLink": "Mutton4"},
                        <SubTableDropModel>{"item": "DropTable3b", "quantity": 1, "chance": 0.006, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Poopy Sewers",
                    "world": "Blunder Hills",
                    "id": 8,
                    "portalRequirements": [20000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "frogBIG",
                    "next": "ratB",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("ratB", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Rat",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 22,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 32,
                    "MonsterMoving": 1,
                    "MovingFrame": 9,
                    "RespawnTime": 60,
                    "DeathFrame": 18,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 330,
                    "ExpType": 0,
                    "Defence": 180,
                    "MoveSPEED": 8,
                    "Damages": [220, 1],
                    "DefFor0": 238.55
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 105, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Sewers2", "quantity": 1, "chance": 0.19, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA11", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest14", "quantity": 1, "chance": 0.1, "questLink": "TP_Pete2"},
                        <ItemDropModel>{"item": "Quest23", "quantity": 1, "chance": 0.16, "questLink": "Mutton3"},
                        <ItemDropModel>{"item": "Quest23", "quantity": 1, "chance": 0.16, "questLink": "Mutton4"},
                        <SubTableDropModel>{"item": "DropTable3b", "quantity": 1, "chance": 0.006, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Rats Nest",
                    "world": "Blunder Hills",
                    "id": 15,
                    "portalRequirements": [35000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "poopSmall",
                    "next": "branch",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("poopD", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Boop",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 33,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 30,
                    "HeightOfMonster": 34,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 745000,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 200000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 1000,
                    "ExpType": 0,
                    "Defence": 120,
                    "MoveSPEED": 3,
                    "Damages": [250, 1],
                    "DefFor0": 275.97
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1, "chance": 0.99, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Sewers3", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA15", "quantity": 1, "chance": 0.0015, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Meel's Crypt",
                    "world": "Blunder Hills",
                    "id": 38,
                    "portalRequirements": [0]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "poopBig",
                    "next": "wolfA",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("rockG", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Healing Rune",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 13,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 42,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 55,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 3000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 150,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [50, 1],
                    "DefFor0": 40.66
                },
                "drops": <EnemyTableModel>{"drops": []},
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("rockB", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Shielding Rune",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 13,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 42,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 55,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 3000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 150,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [50, 1],
                    "DefFor0": 40.66
                },
                "drops": <EnemyTableModel>{"drops": []},
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("rockS", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Skeleton Rune",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 13,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 42,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 6000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 10,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [50, 1],
                    "DefFor0": 40.66
                },
                "drops": <EnemyTableModel>{"drops": []},
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("jarSand", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sandy Pot",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 16,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 32,
                    "MonsterMoving": 1,
                    "MovingFrame": 5,
                    "RespawnTime": 50,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 4000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 150,
                    "ExpType": 0,
                    "Defence": 115,
                    "MoveSPEED": 5,
                    "Damages": [55, 1],
                    "DefFor0": 45.72
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 40, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertA1", "quantity": 1, "chance": 0.22, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsB1", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats9", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertA1b", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable6", "quantity": 1, "chance": 0.003, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Jar Bridge",
                    "world": "Yum Yum Desert",
                    "id": 51,
                    "portalRequirements": [250]
                },
                "navigation": <EnemyNavModel>{
                    "prev": null,
                    "next": "mimicA",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("mimicA", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Mimic",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 17,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 48,
                    "MonsterMoving": 1,
                    "MovingFrame": 9,
                    "RespawnTime": 50,
                    "DeathFrame": 19,
                    "MonsterHPTotal": 5500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 180,
                    "ExpType": 0,
                    "Defence": 132,
                    "MoveSPEED": 4,
                    "Damages": [62, 1],
                    "DefFor0": 52.96
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 47, "chance": 0.47, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertA2", "quantity": 1, "chance": 0.212, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GoldricP1", "quantity": 1, "chance": 0.1, "questLink": "Goldric3"},
                        <CardDropModel>{"item": "CardsB2", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "InvBag101", "quantity": 1, "chance": 2.5e-05, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes2", "quantity": 16, "chance": 5e-06, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable6", "quantity": 1, "chance": 0.0032, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "The Mimic Hole",
                    "world": "Yum Yum Desert",
                    "id": 52,
                    "portalRequirements": [600, 1000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "jarSand",
                    "next": "crabcake",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("crabcake", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Crabcake",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 11,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 64,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 7500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 210,
                    "ExpType": 0,
                    "Defence": 150,
                    "MoveSPEED": 4,
                    "Damages": [70, 1],
                    "DefFor0": 61.42
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 55, "chance": 0.45, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertA3", "quantity": 1, "chance": 0.205, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsB3", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertA3b", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes2", "quantity": 41, "chance": 2.5e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable6", "quantity": 1, "chance": 0.0036, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Dessert Dunes",
                    "world": "Yum Yum Desert",
                    "id": 53,
                    "portalRequirements": [1000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "mimicA",
                    "next": "coconut",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("coconut", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Mafioso",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 10,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 55,
                    "HeightOfMonster": 44,
                    "MonsterMoving": 1,
                    "MovingFrame": 15,
                    "RespawnTime": 40,
                    "DeathFrame": 26,
                    "MonsterHPTotal": 11000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 240,
                    "ExpType": 0,
                    "Defence": 180,
                    "MoveSPEED": 4,
                    "Damages": [90, 1],
                    "DefFor0": 83.29
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 67, "chance": 0.43, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertB1", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GoldricP2", "quantity": 1, "chance": 0.075, "questLink": "Goldric3"},
                        <CardDropModel>{"item": "CardsB4", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes2", "quantity": 17, "chance": 2e-06, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable7", "quantity": 1, "chance": 0.0032, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "The Grandioso Canyon",
                    "world": "Yum Yum Desert",
                    "id": 57,
                    "portalRequirements": [1200]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "crabcake",
                    "next": "sandcastle",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("sandcastle", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sand Castle",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 28,
                    "MonsterOffsetX": 50,
                    "MonsterOffsetY": 59,
                    "HeightOfMonster": 34,
                    "MonsterMoving": 1,
                    "MovingFrame": 9,
                    "RespawnTime": 40,
                    "DeathFrame": 19,
                    "MonsterHPTotal": 13000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 265,
                    "ExpType": 0,
                    "Defence": 205,
                    "MoveSPEED": 3,
                    "Damages": [99, 1],
                    "DefFor0": 93.41
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 80, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertB2", "quantity": 1, "chance": 0.19, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GoldricP3", "quantity": 1, "chance": 0.05, "questLink": "Goldric3"},
                        <CardDropModel>{"item": "CardsB5", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable7", "quantity": 1, "chance": 0.0035, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Shifty Sandbox",
                    "world": "Yum Yum Desert",
                    "id": 58,
                    "portalRequirements": [1600]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "coconut",
                    "next": "pincermin",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("pincermin", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Pincermin",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 2,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 42,
                    "HeightOfMonster": 82,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 50,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 15500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 290,
                    "ExpType": 0,
                    "Defence": 240,
                    "MoveSPEED": 5,
                    "Damages": [112, 1],
                    "DefFor0": 108.27
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 90, "chance": 0.38, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertB3", "quantity": 1, "chance": 0.18, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsB6", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <RecipeDropModel>{
                            "item": "SmithingRecipes4",
                            "quantity": 53,
                            "chance": 3e-06,
                            "questLink": "(Enter World 4)"
                        },
                        <SubTableDropModel>{"item": "DropTable7", "quantity": 1, "chance": 0.0037, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Pincer Plateau",
                    "world": "Yum Yum Desert",
                    "id": 59,
                    "portalRequirements": [2000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "sandcastle",
                    "next": "potato",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("potato", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Mashed Potato",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 21,
                    "MonsterOffsetX": 50,
                    "MonsterOffsetY": 34,
                    "HeightOfMonster": 89,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 40,
                    "DeathFrame": 17,
                    "MonsterHPTotal": 18500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 310,
                    "ExpType": 0,
                    "Defence": 260,
                    "MoveSPEED": 6,
                    "Damages": [125, 1],
                    "DefFor0": 123.37
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 100, "chance": 0.37, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertB4", "quantity": 1, "chance": 0.17, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsB7", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable7", "quantity": 1, "chance": 0.0039, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Slamabam Straightaway",
                    "world": "Yum Yum Desert",
                    "id": 60,
                    "portalRequirements": [2500, 0]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "pincermin",
                    "next": "steak",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("steak", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Tyson",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 31,
                    "MonsterOffsetX": 50,
                    "MonsterOffsetY": 72,
                    "HeightOfMonster": 62,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 40,
                    "DeathFrame": 14,
                    "MonsterHPTotal": 23000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 350,
                    "ExpType": 0,
                    "Defence": 300,
                    "MoveSPEED": 5,
                    "Damages": [150, 1],
                    "DefFor0": 152.99
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 112, "chance": 0.36, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertC1", "quantity": 1, "chance": 0.18, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsB8", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable8", "quantity": 1, "chance": 0.0032, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "The Ring",
                    "world": "Yum Yum Desert",
                    "id": 62,
                    "portalRequirements": [3000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "potato",
                    "next": "moonman",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("moonman", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Moonmoon",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 30,
                    "MonsterOffsetX": 50,
                    "MonsterOffsetY": 66,
                    "HeightOfMonster": 54,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 40,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 26500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 380,
                    "ExpType": 0,
                    "Defence": 330,
                    "MoveSPEED": 4,
                    "Damages": [170, 1],
                    "DefFor0": 177.1
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 125, "chance": 0.35, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertC2", "quantity": 1, "chance": 0.165, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertC2b", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsB9", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest18", "quantity": 1, "chance": 0.0001, "questLink": "Loominadi1"},
                        <SubTableDropModel>{"item": "DropTable8", "quantity": 1, "chance": 0.0035, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Up Up Down Down",
                    "world": "Yum Yum Desert",
                    "id": 63,
                    "portalRequirements": [4000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "steak",
                    "next": "sandgiant",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("sandgiant", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sand Giant",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 29,
                    "MonsterOffsetX": 50,
                    "MonsterOffsetY": 72,
                    "HeightOfMonster": 44,
                    "MonsterMoving": 1,
                    "MovingFrame": 9,
                    "RespawnTime": 40,
                    "DeathFrame": 20,
                    "MonsterHPTotal": 30000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 410,
                    "ExpType": 0,
                    "Defence": 365,
                    "MoveSPEED": 3,
                    "Damages": [195, 1],
                    "DefFor0": 207.65
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 140, "chance": 0.34, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertC3", "quantity": 1, "chance": 0.152, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsB10", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes2", "quantity": 58, "chance": 1.7e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable8", "quantity": 1, "chance": 0.0037, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Sands of Time",
                    "world": "Yum Yum Desert",
                    "id": 64,
                    "portalRequirements": [5000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "moonman",
                    "next": "snailZ",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("snailZ", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Snelbie",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 27,
                    "MonsterOffsetX": 50,
                    "MonsterOffsetY": 72,
                    "HeightOfMonster": 54,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 40,
                    "DeathFrame": 18,
                    "MonsterHPTotal": 35000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 460,
                    "ExpType": 0,
                    "Defence": 400,
                    "MoveSPEED": 4,
                    "Damages": [225, 1],
                    "DefFor0": 244.76
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 160, "chance": 0.35, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DesertC4", "quantity": 1, "chance": 0.14, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsB11", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentPendant14", "quantity": 1, "chance": 2e-06, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable8", "quantity": 1, "chance": 0.0039, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Djonnuttown",
                    "world": "Yum Yum Desert",
                    "id": 65,
                    "portalRequirements": [1]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "sandgiant",
                    "next": "shovelR",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("sheep", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sheepie",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 35,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 47,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 17,
                    "MonsterHPTotal": 55000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 620,
                    "ExpType": 0,
                    "Defence": 550,
                    "MoveSPEED": 4,
                    "Damages": [300, 1],
                    "DefFor0": 338.94
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 180, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowA1", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE0", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentStatues16", "quantity": 1, "chance": 0.0002, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampB5", "quantity": 1, "chance": 8e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable14", "quantity": 1, "chance": 0.0025, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Steep Sheep Ledge",
                    "world": "Frostbite Tundra",
                    "id": 101,
                    "portalRequirements": [1000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": null,
                    "next": "flake",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("flake", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Frost Flake",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 36,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 44,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 40,
                    "DeathFrame": 10,
                    "MonsterHPTotal": 67000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 700,
                    "ExpType": 0,
                    "Defence": 650,
                    "MoveSPEED": 4,
                    "Damages": [360, 1],
                    "DefFor0": 415.1
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 190, "chance": 0.46, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowA2", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE1", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampB7", "quantity": 1, "chance": 6e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowA2a", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable14", "quantity": 1, "chance": 0.0028, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Snowfield Outskirts",
                    "world": "Frostbite Tundra",
                    "id": 103,
                    "portalRequirements": [2000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "sheep",
                    "next": "stache",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("stache", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sir Stache",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 37,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 70,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 40,
                    "DeathFrame": 10,
                    "MonsterHPTotal": 81000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 800,
                    "ExpType": 0,
                    "Defence": 775,
                    "MoveSPEED": 4,
                    "Damages": [420, 1],
                    "DefFor0": 491.48
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 205, "chance": 0.43, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowA3", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE2", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodPotGr3", "quantity": 1, "chance": 0.002, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentStatues17", "quantity": 1, "chance": 0.0002, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable14", "quantity": 1, "chance": 0.0031, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "The Stache Split",
                    "world": "Frostbite Tundra",
                    "id": 104,
                    "portalRequirements": [3000, 100000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "flake",
                    "next": "bloque",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("ram", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dedotated Ram",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 46,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 62,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 35,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 1250000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 3500,
                    "ExpType": 0,
                    "Defence": 1500,
                    "MoveSPEED": 6,
                    "Damages": [3000, 1],
                    "DefFor0": 3563.92
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 520, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowA4", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE14", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentRings23", "quantity": 1, "chance": 1e-06, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable16", "quantity": 1, "chance": 0.0034, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Wam Wonderland",
                    "world": "Frostbite Tundra",
                    "id": 116,
                    "portalRequirements": [250000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "eye",
                    "next": "skele",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("bloque", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bloque",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 32,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 42,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 40,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 100000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 940,
                    "ExpType": 0,
                    "Defence": 900,
                    "MoveSPEED": 4,
                    "Damages": [500, 1],
                    "DefFor0": 593.5
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 240, "chance": 0.41, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowB1", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE3", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentStatues19", "quantity": 1, "chance": 0.0002, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodPotMana3", "quantity": 1, "chance": 0.0025, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable15", "quantity": 1, "chance": 0.0025, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Refrigeration Station",
                    "world": "Frostbite Tundra",
                    "id": 105,
                    "portalRequirements": [4000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "stache",
                    "next": "mamoth",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("mamoth", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Mamooth",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 38,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 40,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 115000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1030,
                    "ExpType": 0,
                    "Defence": 1050,
                    "MoveSPEED": 3,
                    "Damages": [580, 1],
                    "DefFor0": 695.37
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 260, "chance": 0.39, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowB2", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE4", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowB2a", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "InvBag110", "quantity": 1, "chance": 8e-06, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest63", "quantity": 1, "chance": 1, "questLink": "Shuvelle5"},
                        <SubTableDropModel>{"item": "DropTable15", "quantity": 1, "chance": 0.0027, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Mamooooth Mountain",
                    "world": "Frostbite Tundra",
                    "id": 106,
                    "portalRequirements": [6000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "bloque",
                    "next": "snowball",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("snowball", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Snowman",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 39,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 135000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1130,
                    "ExpType": 0,
                    "Defence": 1200,
                    "MoveSPEED": 6,
                    "Damages": [690, 1],
                    "DefFor0": 834.89
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 285, "chance": 0.37, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowB5", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE5", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampB10", "quantity": 1, "chance": 2.5e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodHealth10", "quantity": 1, "chance": 0.009, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest63", "quantity": 1, "chance": 1, "questLink": "Shuvelle6"},
                        <SubTableDropModel>{"item": "DropTable15", "quantity": 1, "chance": 0.0029, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Rollin' Tundra",
                    "world": "Frostbite Tundra",
                    "id": 107,
                    "portalRequirements": [8000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "mamoth",
                    "next": "penguin",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("penguin", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Penguin",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 40,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 48,
                    "MonsterMoving": 1,
                    "MovingFrame": 14,
                    "RespawnTime": 40,
                    "DeathFrame": 25,
                    "MonsterHPTotal": 160000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1250,
                    "ExpType": 0,
                    "Defence": 1350,
                    "MoveSPEED": 4,
                    "Damages": [800, 1],
                    "DefFor0": 973.57
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 310, "chance": 0.36, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowB3", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE6", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentStatues16", "quantity": 1, "chance": 0.0003, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable15", "quantity": 1, "chance": 0.0031, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Signature Slopes",
                    "world": "Frostbite Tundra",
                    "id": 108,
                    "portalRequirements": [11000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "snowball",
                    "next": "thermostat",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("thermostat", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Thermister",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 41,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 68,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 20,
                    "MonsterHPTotal": 185000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1370,
                    "ExpType": 0,
                    "Defence": 1500,
                    "MoveSPEED": 4,
                    "Damages": [950, 1],
                    "DefFor0": 1161.15
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 340, "chance": 0.35, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowB4", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE7", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampB12", "quantity": 1, "chance": 1e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest63", "quantity": 1, "chance": 1, "questLink": "Shuvelle7"},
                        <RecipeDropModel>{
                            "item": "SmithingRecipes4",
                            "quantity": 54,
                            "chance": 8e-07,
                            "questLink": "(Enter World 4)"
                        },
                        <SubTableDropModel>{"item": "DropTable15", "quantity": 1, "chance": 0.0033, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Thermonuclear Climb",
                    "world": "Frostbite Tundra",
                    "id": 109,
                    "portalRequirements": [15000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "penguin",
                    "next": "glass",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("glass", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Quenchie",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 42,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 44,
                    "MonsterMoving": 1,
                    "MovingFrame": 10,
                    "RespawnTime": 45,
                    "DeathFrame": 23,
                    "MonsterHPTotal": 225000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1570,
                    "ExpType": 0,
                    "Defence": 1700,
                    "MoveSPEED": 4,
                    "Damages": [1150, 1],
                    "DefFor0": 1408.37
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 370, "chance": 0.34, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowC1", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE8", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentStatues17", "quantity": 1, "chance": 0.0003, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable16", "quantity": 1, "chance": 0.0025, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Waterlogged Entrance",
                    "world": "Frostbite Tundra",
                    "id": 110,
                    "portalRequirements": [18000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "thermostat",
                    "next": "snakeB",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("snakeB", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Cryosnake",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 43,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 36,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 45,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 260000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1690,
                    "ExpType": 0,
                    "Defence": 1900,
                    "MoveSPEED": 6,
                    "Damages": [1425, 1],
                    "DefFor0": 1743.06
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 400, "chance": 0.32, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowC2", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE9", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentStatues19", "quantity": 1, "chance": 0.0003, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable16", "quantity": 1, "chance": 0.0028, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Cryo Catacombs",
                    "world": "Frostbite Tundra",
                    "id": 111,
                    "portalRequirements": [22000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "glass",
                    "next": "speaker",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("speaker", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bop Box",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 44,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 12,
                    "RespawnTime": 45,
                    "DeathFrame": 23,
                    "MonsterHPTotal": 310000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1780,
                    "ExpType": 0,
                    "Defence": 2150,
                    "MoveSPEED": 4,
                    "Damages": [1700, 1],
                    "DefFor0": 2072.08
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 440, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowC3", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE10", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodHealth9", "quantity": 1, "chance": 0.007, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable16", "quantity": 1, "chance": 0.003, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Overpass of Sound",
                    "world": "Frostbite Tundra",
                    "id": 112,
                    "portalRequirements": [35000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "snakeB",
                    "next": "eye",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("eye", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Neyeptune",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 63,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 43,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 350000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1900,
                    "ExpType": 0,
                    "Defence": 2400,
                    "MoveSPEED": 4,
                    "Damages": [2000, 1],
                    "DefFor0": 2424.95
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 490, "chance": 0.28, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowC4", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE11", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowC4a", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable16", "quantity": 1, "chance": 0.0032, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Crystal Basecamp",
                    "world": "Frostbite Tundra",
                    "id": 113,
                    "portalRequirements": [120000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "speaker",
                    "next": "ram",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("Iceball", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Ice Ball",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 45,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 70,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 45,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 200000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1500,
                    "ExpType": 0,
                    "Defence": 100,
                    "MoveSPEED": 4,
                    "Damages": [1, 1],
                    "DefFor0": 0
                },
                "drops": <EnemyTableModel>{"drops": []},
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("mushP", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Purp Mushroom",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 49,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 38,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 520000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2350,
                    "ExpType": 0,
                    "Defence": 2800,
                    "MoveSPEED": 4,
                    "Damages": [2100, 1],
                    "DefFor0": 2541.34
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 550, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyA1", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentShoes30", "quantity": 1, "chance": 6e-06, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG1", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable19", "quantity": 1, "chance": 0.0025, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Spaceway Raceway",
                    "world": "Hyperion Nebula",
                    "id": 151,
                    "portalRequirements": [20000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": null,
                    "next": "w4a2",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4a2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "TV",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 50,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 55,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 40,
                    "DeathFrame": 18,
                    "MonsterHPTotal": 700000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 3000,
                    "ExpType": 0,
                    "Defence": 3300,
                    "MoveSPEED": 4,
                    "Damages": [2300, 1],
                    "DefFor0": 2772.33
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 630, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyA2", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyA2b", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Line12", "quantity": 1, "chance": 2.2e-06, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG2", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable19", "quantity": 1, "chance": 0.0028, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "TV Outpost",
                    "world": "Hyperion Nebula",
                    "id": 152,
                    "portalRequirements": [30000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "mushP",
                    "next": "w4a3",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4a3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Donut",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 51,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 60,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 40,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 925000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 4000,
                    "ExpType": 0,
                    "Defence": 3800,
                    "MoveSPEED": 4,
                    "Damages": [2550, 1],
                    "DefFor0": 3057.91
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 730, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyA3", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentShoes32", "quantity": 1, "chance": 6e-06, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG3", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable19", "quantity": 1, "chance": 0.0031, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Donut Drive-In",
                    "world": "Hyperion Nebula",
                    "id": 153,
                    "portalRequirements": [50000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "w4a2",
                    "next": "demonP",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("demonP", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Demon Genie",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 52,
                    "MonsterOffsetX": 50,
                    "MonsterOffsetY": 69,
                    "HeightOfMonster": 68,
                    "MonsterMoving": 1,
                    "MovingFrame": 13,
                    "RespawnTime": 40,
                    "DeathFrame": 24,
                    "MonsterHPTotal": 1250000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 4800,
                    "ExpType": 0,
                    "Defence": 4325,
                    "MoveSPEED": 3,
                    "Damages": [2750, 1],
                    "DefFor0": 3284.02
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 860, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyA4", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentRings24", "quantity": 1, "chance": 4e-06, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG4", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable19", "quantity": 1, "chance": 0.0034, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Outskirts of Fallstar Isle",
                    "world": "Hyperion Nebula",
                    "id": 154,
                    "portalRequirements": [70000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "w4a3",
                    "next": "w4b2",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4b2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Soda Can",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 54,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 38,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 2000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 7600,
                    "ExpType": 0,
                    "Defence": 5150,
                    "MoveSPEED": 6,
                    "Damages": [3000, 1],
                    "DefFor0": 3563.92
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1050, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyB1", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Weight3", "quantity": 1, "chance": 1.9e-06, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG6", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable20", "quantity": 1, "chance": 0.0027, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Moutainous Deugh",
                    "world": "Hyperion Nebula",
                    "id": 155,
                    "portalRequirements": [100000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "demonP",
                    "next": "w4b1",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4b1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Flying Worm",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 53,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 55,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 40,
                    "DeathFrame": 18,
                    "MonsterHPTotal": 2500000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 8750,
                    "ExpType": 0,
                    "Defence": 5650,
                    "MoveSPEED": 7,
                    "Damages": [3400, 1],
                    "DefFor0": 4005.88
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1300, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyB2", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StampA29", "quantity": 1, "chance": 3.8e-06, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG5", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable20", "quantity": 1, "chance": 0.0025, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Wurm Highway",
                    "world": "Hyperion Nebula",
                    "id": 156,
                    "portalRequirements": [150000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "w4b2",
                    "next": "w4b3",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4b3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Gelatinous Cuboid",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 55,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 60,
                    "MonsterMoving": 1,
                    "MovingFrame": 12,
                    "RespawnTime": 40,
                    "DeathFrame": 19,
                    "MonsterHPTotal": 3300000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 10800,
                    "ExpType": 0,
                    "Defence": 6200,
                    "MoveSPEED": 4,
                    "Damages": [3900, 1],
                    "DefFor0": 4549.15
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1600, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyB3", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG7", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "InvStorageS", "quantity": 1, "chance": 3.8e-06, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable20", "quantity": 1, "chance": 0.0029, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Jelly Cube Bridge",
                    "world": "Hyperion Nebula",
                    "id": 157,
                    "portalRequirements": [250000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "w4b1",
                    "next": "w4b4",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4b4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Choccie",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 56,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 60,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 40,
                    "DeathFrame": 17,
                    "MonsterHPTotal": 4500000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 14000,
                    "ExpType": 0,
                    "Defence": 6900,
                    "MoveSPEED": 4,
                    "Damages": [4500, 1],
                    "DefFor0": 5189.1
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 2000, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyB4", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentRings25", "quantity": 1, "chance": 4e-06, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG8", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable20", "quantity": 1, "chance": 0.0031, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Cocoa Tunnel",
                    "world": "Hyperion Nebula",
                    "id": 158,
                    "portalRequirements": [500000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "w4b3",
                    "next": "w4b5",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4b5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Biggole Wurm",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 57,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 55,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 40,
                    "DeathFrame": 10,
                    "MonsterHPTotal": 6500000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 17500,
                    "ExpType": 0,
                    "Defence": 7700,
                    "MoveSPEED": 6,
                    "Damages": [5200, 1],
                    "DefFor0": 5921.21
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 2500, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyB5", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG9", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable20", "quantity": 1, "chance": 0.0033, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Standstill Plains",
                    "world": "Hyperion Nebula",
                    "id": 159,
                    "portalRequirements": [700000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "w4b4",
                    "next": "w4c1",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4c1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Clammie",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 58,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 40,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 9000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 23400,
                    "ExpType": 0,
                    "Defence": 8700,
                    "MoveSPEED": 4,
                    "Damages": [6000, 1],
                    "DefFor0": 6741.2
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 3100, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyC1", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyC1b", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG10", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable21", "quantity": 1, "chance": 0.0025, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Shelled Shores",
                    "world": "Hyperion Nebula",
                    "id": 160,
                    "portalRequirements": [1000000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "w4b5",
                    "next": "w4c2",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4c2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Octodar",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 59,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 36,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 14,
                    "MonsterHPTotal": 12000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 27600,
                    "ExpType": 0,
                    "Defence": 9600,
                    "MoveSPEED": 4,
                    "Damages": [7000, 1],
                    "DefFor0": 7744.43
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 3500, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyC2", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG11", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes4", "quantity": 55, "chance": 3e-07, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable21", "quantity": 1, "chance": 0.0028, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "The Untraveled Octopath",
                    "world": "Hyperion Nebula",
                    "id": 161,
                    "portalRequirements": [2000000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "w4c1",
                    "next": "w4c3",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4c3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Flombeige",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 60,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 60,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 45,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 16000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 30000,
                    "ExpType": 0,
                    "Defence": 10500,
                    "MoveSPEED": 4,
                    "Damages": [8200, 1],
                    "DefFor0": 8920.83
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 4500, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyC3", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Line3", "quantity": 1, "chance": 1e-06, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG12", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable21", "quantity": 1, "chance": 0.003, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Flamboyant Bayou",
                    "world": "Hyperion Nebula",
                    "id": 162,
                    "portalRequirements": [3000000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "w4c2",
                    "next": "w4c4",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("w4c4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Stilted Seeker",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 61,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 76,
                    "MonsterMoving": 1,
                    "MovingFrame": 9,
                    "RespawnTime": 45,
                    "DeathFrame": 20,
                    "MonsterHPTotal": 20000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 33000,
                    "ExpType": 0,
                    "Defence": 11000,
                    "MoveSPEED": 6,
                    "Damages": [10000, 1],
                    "DefFor0": 10638.1
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 5000, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyC4", "quantity": 1, "chance": 0.16, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsG13", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable21", "quantity": 1, "chance": 0.0032, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Enclave of Eyes",
                    "world": "Hyperion Nebula",
                    "id": 163,
                    "portalRequirements": [4000000]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "w4c3",
                    "next": "Crystal3",
                    "hasCrystal": true,
                    "crystalName": "Crystal3",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("mushR", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Red Mushroom",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 19,
                    "MonsterOffsetX": 23,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 50,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 45,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 1000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 47,
                    "ExpType": 0,
                    "Defence": 25,
                    "MoveSPEED": 4,
                    "Damages": [30, 1],
                    "DefFor0": 21.54
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 6, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands4", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsA1", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable1", "quantity": 1, "chance": 0.0052, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Birch Enclave",
                    "world": "Blunder Hills",
                    "id": 17,
                    "portalRequirements": [0]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "mushG",
                    "next": "frogG",
                    "hasCrystal": true,
                    "crystalName": "Crystal0",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("shovelR", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dig Doug",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 56,
                    "MonsterMoving": 1,
                    "MovingFrame": 5,
                    "RespawnTime": 40,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 228,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 60, "chance": 0.43, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsB12", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable7", "quantity": 1, "chance": 0.0032, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "snailZ",
                    "next": "Crystal1",
                    "hasCrystal": true,
                    "crystalName": "Crystal1",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("skele", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Xylobone",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 56,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 40,
                    "DeathFrame": 20,
                    "MonsterHPTotal": 200000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2000,
                    "ExpType": 0,
                    "Defence": 100,
                    "MoveSPEED": 4,
                    "Damages": [200, 1],
                    "DefFor0": 213.8
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 100, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE12", "quantity": 1, "chance": 0.01, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable14", "quantity": 1, "chance": 0.01, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "ram",
                    "next": "skele2",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("skele2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bloodbone",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 48,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 56,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 60,
                    "DeathFrame": 20,
                    "MonsterHPTotal": 10000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 6000,
                    "ExpType": 0,
                    "Defence": 100,
                    "MoveSPEED": 4,
                    "Damages": [3000, 1],
                    "DefFor0": 3563.92
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 800, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowC5", "quantity": 1, "chance": 0.01, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsE13", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable16", "quantity": 1, "chance": 0.005, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Hell Hath Frozen Over",
                    "world": "Frostbite Tundra",
                    "id": 117,
                    "portalRequirements": [0]
                },
                "navigation": <EnemyNavModel>{
                    "prev": "skele",
                    "next": "Crystal2",
                    "hasCrystal": true,
                    "crystalName": "Crystal2",
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("wolfA", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Amarok",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 25000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 105,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <ItemDropModel>{"item": "Crystal1", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <CoinDropModel>{"item": "COIN", "quantity": 500, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Meatloaf", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ2", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats39", "quantity": 1, "chance": 0.001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ObolAmarokA", "quantity": 1, "chance": 0.0007, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest17", "quantity": 1, "chance": 0.3, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable1", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable2", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "poopD",
                    "next": "wolfB",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": <BossDetailsModel>{
                    "health": 25000,
                    "defence": 105,
                    "exp": 4000,
                    "keys": 1,
                    "attacks": [
                        <BossAttackModel>{"name": "Fireball", "damage": 50},
                        <BossAttackModel>{"name": "Stomp", "damage": 120},
                        <BossAttackModel>{"name": "Rock Spikes", "damage": 70},
                        <BossAttackModel>{"name": "Spike Traps", "damage": 68},
                        <BossAttackModel>{"name": "Sword Swing", "damage": 100},
                        <BossAttackModel>{"name": "Uppercut", "damage": 200},
                        <BossAttackModel>{"name": "Rocketfist", "damage": 100}
                    ]
                }
            }),
        new EnemyBase("wolfB", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chaotic Amarok",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 8000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 1750,
                    "MoveSPEED": 3,
                    "Damages": [1200, 1],
                    "DefFor0": 1469.66
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 500, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Meatloaf", "quantity": 3, "chance": 0.1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ4", "quantity": 1, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats39", "quantity": 1, "chance": 0.004, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ObolAmarokA", "quantity": 1, "chance": 0.0033, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest17", "quantity": 3, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest29", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable1", "quantity": 4, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable2", "quantity": 4, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3", "quantity": 4, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "wolfA",
                    "next": "wolfC",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": <BossDetailsModel>{
                    "health": 8000000,
                    "defence": 1750,
                    "exp": 400000,
                    "keys": 5,
                    "attacks": [
                        <BossAttackModel>{"name": "Fireball", "damage": 650},
                        <BossAttackModel>{"name": "Stomp", "damage": 1500},
                        <BossAttackModel>{"name": "Rock Spikes", "damage": 800},
                        <BossAttackModel>{"name": "Spike Traps", "damage": 675},
                        <BossAttackModel>{"name": "Sword Swing", "damage": 1500},
                        <BossAttackModel>{"name": "Uppercut", "damage": 3000},
                        <BossAttackModel>{"name": "Rocketfist", "damage": 1000}
                    ]
                }
            }),
        new EnemyBase("wolfC", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Radiant Amarok",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 100000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 8000,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 500, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Meatloaf", "quantity": 10, "chance": 0.05, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ14", "quantity": 1, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats39", "quantity": 1, "chance": 0.012, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ObolAmarokA", "quantity": 1, "chance": 0.0085, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentCape3", "quantity": 1, "chance": 0.001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneZ1", "quantity": 1, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest17", "quantity": 6, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest29", "quantity": 2, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "wolfB",
                    "next": "babaHour",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": <BossDetailsModel>{
                    "health": 100000000,
                    "defence": 8000,
                    "exp": 50000000,
                    "keys": 30,
                    "attacks": [
                        <BossAttackModel>{"name": "Fireball", "damage": 3650},
                        <BossAttackModel>{"name": "Stomp", "damage": 5500},
                        <BossAttackModel>{"name": "Rock Spikes", "damage": 3800},
                        <BossAttackModel>{"name": "Spike Traps", "damage": 3675},
                        <BossAttackModel>{"name": "Sword Swing", "damage": 5500},
                        <BossAttackModel>{"name": "Uppercut", "damage": 8000},
                        <BossAttackModel>{"name": "Rocketfist", "damage": 5000}
                    ]
                }
            }),
        new EnemyBase("Boss2A", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Efaunt",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 1000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 550,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <ItemDropModel>{"item": "Crystal2", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <CoinDropModel>{"item": "COIN", "quantity": 4000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ3", "quantity": 1, "chance": 0.025, "questLink": "N/A"},
                        <ItemDropModel>{"item": "MidnightCookie", "quantity": 1, "chance": 0.07, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ObolEfauntA", "quantity": 1, "chance": 0.001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats2", "quantity": 1, "chance": 0.000667, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes2", "quantity": 75, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EfauntDrop1", "quantity": 1, "chance": 0.3, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable6", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable7", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable8", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "babaMummy",
                    "next": "Boss2B",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": <BossDetailsModel>{
                    "health": 1000000,
                    "defence": 550,
                    "exp": 100000,
                    "keys": 1,
                    "attacks": [
                        <BossAttackModel>{"name": "Hammer", "damage": 1250},
                        <BossAttackModel>{"name": "Scimitar", "damage": 300},
                        <BossAttackModel>{"name": "Fire Column", "damage": 350},
                        <BossAttackModel>{"name": "Purple Psionic Hoops", "damage": 450},
                        <BossAttackModel>{"name": "Finger Gun", "damage": 5000},
                        <BossAttackModel>{"name": "Headpat", "damage": 10000},
                        <BossAttackModel>{"name": "Blue Psionic", "damage": 400}
                    ]
                }
            }),
        new EnemyBase("Boss2B", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chaotic Efaunt",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 30000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 3500,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 4000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ7", "quantity": 1, "chance": 0.016, "questLink": "N/A"},
                        <ItemDropModel>{"item": "MidnightCookie", "quantity": 1, "chance": 0.07, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ObolEfauntA", "quantity": 1, "chance": 0.003, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats2", "quantity": 1, "chance": 0.002, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EfauntDrop1", "quantity": 3, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EfauntDrop2", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable7", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable8", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "Boss2A",
                    "next": "Boss2C",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": <BossDetailsModel>{
                    "health": 30000000,
                    "defence": 3500,
                    "exp": 2000000,
                    "keys": 5,
                    "attacks": [
                        <BossAttackModel>{"name": "Hammer", "damage": 1800},
                        <BossAttackModel>{"name": "Scimitar", "damage": 4000},
                        <BossAttackModel>{"name": "Fire Column", "damage": 2000},
                        <BossAttackModel>{"name": "Purple Psionic Hoops", "damage": 1500},
                        <BossAttackModel>{"name": "Finger Gun", "damage": 2500},
                        <BossAttackModel>{"name": "Headpat", "damage": 5000},
                        <BossAttackModel>{"name": "Blue Psionic", "damage": 3300}
                    ]
                }
            }),
        new EnemyBase("Boss2C", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Gilded Efaunt",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 400000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 15000,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 4000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ15", "quantity": 1, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "MidnightCookie", "quantity": 1, "chance": 0.07, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ObolEfauntA", "quantity": 1, "chance": 0.018, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats2", "quantity": 1, "chance": 0.015, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EfauntDrop1", "quantity": 12, "chance": 0.9, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EfauntDrop2", "quantity": 4, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentCape4", "quantity": 1, "chance": 0.0007, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable8", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "Boss2B",
                    "next": "mini3a",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": <BossDetailsModel>{
                    "health": 400000000,
                    "defence": 15000,
                    "exp": 100000000,
                    "keys": 40,
                    "attacks": [
                        <BossAttackModel>{"name": "Hammer", "damage": 18000},
                        <BossAttackModel>{"name": "Scimitar", "damage": 40000},
                        <BossAttackModel>{"name": "Fire Column", "damage": 20000},
                        <BossAttackModel>{"name": "Purple Psionic Hoops", "damage": 15000},
                        <BossAttackModel>{"name": "Finger Gun", "damage": 25000},
                        <BossAttackModel>{"name": "Headpat", "damage": 50000},
                        <BossAttackModel>{"name": "Blue Psionic", "damage": 33000}
                    ]
                }
            }),
        new EnemyBase("Boss3A", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chizoar",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 20000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 2250,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 4000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ8", "quantity": 1, "chance": 0.007, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ObolChizoarA", "quantity": 1, "chance": 0.0008, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentPendant24", "quantity": 1, "chance": 0.001, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Chiz0", "quantity": 1, "chance": 0.3, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable14", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable15", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable16", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "mini3a",
                    "next": "Boss3B",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": <BossDetailsModel>{
                    "health": 20000000,
                    "defence": 2250,
                    "exp": 750000,
                    "keys": 1,
                    "attacks": [
                        <BossAttackModel>{"name": "Front Stomp", "damage": 3200},
                        <BossAttackModel>{"name": "Back Stomp", "damage": 3600},
                        <BossAttackModel>{"name": "Frozen Spikes", "damage": 2500},
                        <BossAttackModel>{"name": "Falling Icicles", "damage": 2100},
                        <BossAttackModel>{"name": "Tusk Swipe", "damage": 3500}
                    ]
                }
            }),
        new EnemyBase("Boss3B", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chaotic Chizoar",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 250000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 7500,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 4000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ9", "quantity": 1, "chance": 0.004, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ObolChizoarA", "quantity": 1, "chance": 0.002, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentPendant24", "quantity": 1, "chance": 0.0032, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Chiz0", "quantity": 3, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Chiz1", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable15", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable16", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "Boss3A",
                    "next": "Boss3C",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": <BossDetailsModel>{
                    "health": 250000000,
                    "defence": 7500,
                    "exp": 10000000,
                    "keys": 5,
                    "attacks": [
                        <BossAttackModel>{"name": "Front Stomp", "damage": 6000},
                        <BossAttackModel>{"name": "Back Stomp", "damage": 9000},
                        <BossAttackModel>{"name": "Frozen Spikes", "damage": 5000},
                        <BossAttackModel>{"name": "Falling Icicles", "damage": 4000},
                        <BossAttackModel>{"name": "Tusk Swipe", "damage": 6000}
                    ]
                }
            }),
        new EnemyBase("Boss3C", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Blighted Chizoar",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 2000000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 25000,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 4000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ16", "quantity": 1, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ObolChizoarA", "quantity": 1, "chance": 0.01, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentPendant24", "quantity": 1, "chance": 0.014, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentCape5", "quantity": 1, "chance": 0.0003, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Chiz0", "quantity": 7, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Chiz1", "quantity": 2, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneZ1", "quantity": 1, "chance": 0.03, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable8", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "Boss3B",
                    "next": "mini4a",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": <BossDetailsModel>{
                    "health": 2000000000,
                    "defence": 25000,
                    "exp": 500000000,
                    "keys": 50,
                    "attacks": [
                        <BossAttackModel>{"name": "Front Stomp", "damage": 18000},
                        <BossAttackModel>{"name": "Back Stomp", "damage": 40000},
                        <BossAttackModel>{"name": "Frozen Spikes", "damage": 20000},
                        <BossAttackModel>{"name": "Falling Icicles", "damage": 15000},
                        <BossAttackModel>{"name": "Tusk Swipe", "damage": 25000},
                        <BossAttackModel>{"name": "filler", "damage": 33000}
                    ]
                }
            }),
        new EnemyBase("Boss4A", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Troll",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 400000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 4000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ10", "quantity": 1, "chance": 0.007, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FillerMaterial", "quantity": 2, "chance": 0.3, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable19", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable20", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable21", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "mini4a",
                    "next": "Boss4B",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("Boss4B", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chaotic Troll",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 2000000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 4000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ11", "quantity": 1, "chance": 0.004, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FillerMaterial", "quantity": 2, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FillerMaterial", "quantity": 2, "chance": 0.002, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable19", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable20", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable21", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "Boss4A",
                    "next": "Blank",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("poopBig", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dr Defecaus",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 745000,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ1", "quantity": 1, "chance": 0.03, "questLink": "N/A"},
                        <ItemDropModel>{"item": "JobApplication", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes2", "quantity": 24, "chance": 0.06, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Sewers1", "quantity": 150, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{
                            "item": "EquipmentToolsHatchet2b",
                            "quantity": 1,
                            "chance": 0.02,
                            "questLink": "N/A"
                        },
                        <ItemDropModel>{"item": "EquipmentTools10", "quantity": 1, "chance": 0.01, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Sewers1b", "quantity": 1, "chance": 0.1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3", "quantity": 2, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "babayaga",
                    "next": "poopD",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("babayaga", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Baba Yaga",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 6,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 92,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 86400,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 150000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 1750,
                    "ExpType": 0,
                    "Defence": 300,
                    "MoveSPEED": 4,
                    "Damages": [400, 20],
                    "DefFor0": 466.07
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 800, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ0", "quantity": 1, "chance": 0.03, "questLink": "N/A"},
                        <ItemDropModel>{"item": "BabaYagaETC", "quantity": 1, "chance": 0.006, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes1", "quantity": 63, "chance": 0.06, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest41", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable1", "quantity": 2, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable2", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3", "quantity": 0.5, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": null,
                    "next": "poopBig",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("babaHour", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Biggie Hours",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 6,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 86,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 86400,
                    "DeathFrame": 20,
                    "MonsterHPTotal": 800000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12500,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 5,
                    "Damages": [500, 20],
                    "DefFor0": 593.5
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 7000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Hgg", "quantity": 1, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneZ1", "quantity": 2, "chance": 0.4, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes2", "quantity": 66, "chance": 0.06, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA3b", "quantity": 1, "chance": 0.008, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ5", "quantity": 1, "chance": 0.024, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes2", "quantity": 75, "chance": 0.06, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable6", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable13", "quantity": 1, "chance": 0.4, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "wolfC",
                    "next": "babaMummy",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("babaMummy", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "King Doot",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 6,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 102,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 86400,
                    "DeathFrame": 17,
                    "MonsterHPTotal": 3000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 50000,
                    "ExpType": 0,
                    "Defence": 1000,
                    "MoveSPEED": 4,
                    "Damages": [800, 450],
                    "DefFor0": 973.57
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ6", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key2", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes2", "quantity": 65, "chance": 0.06, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 5, "chance": 0.75, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneZ1", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA3b", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentPants19", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "MidnightCookie", "quantity": 2, "chance": 0.2, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable13", "quantity": 1, "chance": 0.5, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "babaHour",
                    "next": "Boss2A",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("mini3a", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dilapidated Slush",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 6,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 60,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 86400,
                    "DeathFrame": 7,
                    "MonsterHPTotal": 12500000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 250000,
                    "ExpType": 0,
                    "Defence": 2000,
                    "MoveSPEED": 0,
                    "Damages": [20000, 450],
                    "DefFor0": 19482
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ12", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "WorshipSkull8", "quantity": 1, "chance": 0.009, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ObolSlush", "quantity": 1, "chance": 0.004, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key3", "quantity": 2, "chance": 0.8, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes3", "quantity": 20, "chance": 0.06, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA3b", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA3b", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable13", "quantity": 1, "chance": 0.5, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "Boss2C",
                    "next": "Boss3A",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("mini4a", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Mutated Mush",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 6,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 78,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 86400,
                    "DeathFrame": 9,
                    "MonsterHPTotal": 120000000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 2000000,
                    "ExpType": 0,
                    "Defence": 4500,
                    "MoveSPEED": 3,
                    "Damages": [3000, 450],
                    "DefFor0": 3563.92
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 25000, "chance": 1, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsZ13", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes3", "quantity": 21, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA3b", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PetEgg", "quantity": 1, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Ladle", "quantity": 3, "chance": 1, "questLink": "N/A"},
                        <RecipeDropModel>{"item": "SmithingRecipes4", "quantity": 56, "chance": 0.008, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable13", "quantity": 1, "chance": 0.5, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": <EnemyNavModel>{
                    "prev": "Boss3C",
                    "next": "Boss4A",
                    "hasCrystal": true,
                    "crystalName": null,
                    "hasCard": true
                },
                "bossData": null
            }),
        new EnemyBase("xmasEvent", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Giftmas Blobulyte",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 10, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY0", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest30", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent1", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent2", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent3", "quantity": 2, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent4", "quantity": 2, "chance": 0.25, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("xmasEvent2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Meaning of Giftmas",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 10, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY0", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest30", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent1", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent2", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent3", "quantity": 2, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent4", "quantity": 2, "chance": 0.25, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("xmasEvent3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Golden Giftmas Box",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 10, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY0", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest30", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent1", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent2", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent3", "quantity": 2, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent4", "quantity": 2, "chance": 0.25, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("loveEvent", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Loveulyte",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY3", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest40", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent5", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent6", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent7", "quantity": 2, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent8", "quantity": 2, "chance": 0.25, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("loveEvent2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chocco Box",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY3", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest40", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent5", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent6", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent7", "quantity": 2, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent8", "quantity": 2, "chance": 0.25, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("EasterEvent1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Egggulyte",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY6", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest42", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneTe", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneAe", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneWe", "quantity": 2, "chance": 0.25, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("EasterEvent2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Egg Capsule",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY6", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest42", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest44", "quantity": 1, "chance": 0.13, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneTe", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneAe", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneWe", "quantity": 2, "chance": 0.25, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("SummerEvent1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Coastiolyte",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY11", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest49", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest50", "quantity": 1, "chance": 0.13, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("SummerEvent2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Summer Spirit",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY2", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Timecandy1", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Timecandy2", "quantity": 3, "chance": 0.01, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneWeb", "quantity": 1, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneT1eb", "quantity": 3, "chance": 0.03, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneAeB", "quantity": 3, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest50", "quantity": 1, "chance": 0.1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Blank0ramaFiller", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Nightmare Amarok",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 85,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ghost", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Ghost (Event)",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 6,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 52,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 100,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 1000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "a",
                    "ExpGiven": 1,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 5,
                    "Damages": [5, 5],
                    "DefFor0": 2
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 10, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY0", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest30", "quantity": 1, "chance": 0.15, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent1", "quantity": 2, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent2", "quantity": 2, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent3", "quantity": 2, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent4", "quantity": 2, "chance": 0.3, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("slimeR", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Valentslime",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 24,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 32,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 42,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 20,
                    "ExpType": 0,
                    "Defence": 9,
                    "MoveSPEED": 4,
                    "Damages": [1, 1],
                    "DefFor0": 0
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY3", "quantity": 1, "chance": 0.085, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest40", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent5", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent6", "quantity": 3, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent7", "quantity": 2, "chance": 0.25, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodEvent8", "quantity": 2, "chance": 0.25, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("sheepB", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Floofie",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 35,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 47,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 17,
                    "MonsterHPTotal": 300,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 1,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 5,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY6", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Timecandy1", "quantity": 3, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Timecandy2", "quantity": 3, "chance": 0.15, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Timecandy4", "quantity": 2, "chance": 0.01, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneTe", "quantity": 2, "chance": 0.07, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneAe", "quantity": 2, "chance": 0.08, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneWe", "quantity": 2, "chance": 0.04, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("snakeY", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Shell Snake",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 25,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 36,
                    "HeightOfMonster": 32,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 45,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 170,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 34,
                    "ExpType": 0,
                    "Defence": 18,
                    "MoveSPEED": 8,
                    "Damages": [22, 1],
                    "DefFor0": 14.57
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY7", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Timecandy1", "quantity": 3, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Timecandy2", "quantity": 3, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneTe", "quantity": 2, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneAe", "quantity": 2, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneWe", "quantity": 2, "chance": 0.02, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("crabcakeB", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Mr Blueberry",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 11,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 40,
                    "HeightOfMonster": 64,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 20,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [22, 1],
                    "DefFor0": 14.57
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY10", "quantity": 1, "chance": 0.03, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest49", "quantity": 1, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneT1eb", "quantity": 3, "chance": 0.012, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneAeB", "quantity": 3, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneWeb", "quantity": 2, "chance": 0.01, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("shovelY", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Plasti Doug",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 56,
                    "MonsterMoving": 1,
                    "MovingFrame": 5,
                    "RespawnTime": 40,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 69, "chance": 0.5, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsY13", "quantity": 1, "chance": 0.03, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Quest49", "quantity": 1, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneT1eb", "quantity": 3, "chance": 0.012, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneAeB", "quantity": 3, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneWeb", "quantity": 2, "chance": 0.01, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("pghost", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Ghost (Event)",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 40,
                    "DeathFrame": 9,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 7,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet0", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Squirrel",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 36,
                    "MonsterMoving": 1,
                    "MovingFrame": 7,
                    "RespawnTime": 40,
                    "DeathFrame": 15,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Piggo",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 38,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 16,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Wild Boar",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 1,
                    "MovingFrame": 5,
                    "RespawnTime": 40,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 5,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Mallay",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 44,
                    "MonsterMoving": 1,
                    "MovingFrame": 5,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Whale",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 45,
                    "MonsterMoving": 1,
                    "MovingFrame": 5,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chippy",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 44,
                    "MonsterMoving": 1,
                    "MovingFrame": 8,
                    "RespawnTime": 40,
                    "DeathFrame": 7,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet6", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bunny",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 13,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet7", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Mecho Mouse",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 1,
                    "MovingFrame": 0,
                    "RespawnTime": 40,
                    "DeathFrame": 10,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet8", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Panda",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 47,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet9", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Panda",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 47,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet10", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Panda",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 47,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Pet11", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Panda",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 23,
                    "MonsterOffsetX": 38,
                    "MonsterOffsetY": 47,
                    "HeightOfMonster": 47,
                    "MonsterMoving": 1,
                    "MovingFrame": 6,
                    "RespawnTime": 40,
                    "DeathFrame": 12,
                    "MonsterHPTotal": 14000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 420,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 4,
                    "Damages": [2, 1],
                    "DefFor0": 0.5
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Copper", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Copper",
                    "AFKtype": AFKType.Mining,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 120,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 1,
                    "Defence": 30,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC1", "quantity": 1, "chance": 0.0002, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable4", "quantity": 1, "chance": 0.0065, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Tunnels Entrance",
                    "world": "Blunder Hills",
                    "id": 6,
                    "portalRequirements": [10]
                },
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Iron", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Iron",
                    "AFKtype": AFKType.Mining,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 120,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 5,
                    "ExpType": 1,
                    "Defence": 180,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC2", "quantity": 1, "chance": 0.00013, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable4", "quantity": 1, "chance": 0.007, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Freefall Caverns",
                    "world": "Blunder Hills",
                    "id": 7,
                    "portalRequirements": [25, 81]
                },
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Gold", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Gold",
                    "AFKtype": AFKType.Mining,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 120,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 10,
                    "ExpType": 1,
                    "Defence": 1250,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC3", "quantity": 1, "chance": 0.00011, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable4", "quantity": 1, "chance": 0.0075, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Plat", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Plat",
                    "AFKtype": AFKType.Mining,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 180,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 30,
                    "ExpType": 1,
                    "Defence": 16000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD2", "quantity": 1, "chance": 8e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable4", "quantity": 1, "chance": 0.0077, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "The Ol' Straightaway",
                    "world": "Blunder Hills",
                    "id": 10,
                    "portalRequirements": [40]
                },
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Dementia", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dementia",
                    "AFKtype": AFKType.Mining,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 180,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 55,
                    "ExpType": 1,
                    "Defence": 150000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD1", "quantity": 1, "chance": 6e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable4", "quantity": 1, "chance": 0.0082, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Void", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Void",
                    "AFKtype": AFKType.Mining,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 240,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 185,
                    "ExpType": 1,
                    "Defence": 600000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD3", "quantity": 1, "chance": 6e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable4", "quantity": 2, "chance": 0.009, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Echoing Egress",
                    "world": "Blunder Hills",
                    "id": 11,
                    "portalRequirements": [50, 60]
                },
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Lustre", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Lustre",
                    "AFKtype": AFKType.Mining,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 240,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 250,
                    "ExpType": 1,
                    "Defence": 2000000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD4", "quantity": 1, "chance": 6e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable4", "quantity": 2, "chance": 0.0095, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Starfire", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Starfire",
                    "AFKtype": AFKType.Mining,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 240,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 500,
                    "ExpType": 1,
                    "Defence": 5000000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsF16", "quantity": 1, "chance": 3e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable4", "quantity": 2, "chance": 0.011, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Slip Slidy Ledges",
                    "world": "Blunder Hills",
                    "id": 12,
                    "portalRequirements": [60]
                },
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Dreadlo", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dreadlo",
                    "AFKtype": AFKType.Mining,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 300,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 850,
                    "ExpType": 1,
                    "Defence": 25000000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 2, "chance": 0.4, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Godshard", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Godshard",
                    "AFKtype": AFKType.Mining,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 38,
                    "HeightOfMonster": 25,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 600,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.oreType,
                    "SpecialType": "",
                    "ExpGiven": 1250,
                    "ExpType": 1,
                    "Defence": 100000000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 2, "chance": 0.4, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("OakTree", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Oak Tree",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 2,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 3,
                    "Defence": 20,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC4", "quantity": 1, "chance": 0.0004, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5", "quantity": 1, "chance": 0.008, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("BirchTree", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Birch Tree",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 5,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 6,
                    "ExpType": 3,
                    "Defence": 80,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC5", "quantity": 1, "chance": 0.00029, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5", "quantity": 1, "chance": 0.0085, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("JungleTree", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Jungle Tree",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 112,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 5000000,
                    "DeathFrame": 7,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 12,
                    "ExpType": 3,
                    "Defence": 250,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC6", "quantity": 1, "chance": 0.00021, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5", "quantity": 1, "chance": 0.009, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ForestTree", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Forest Tree",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 8,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 20,
                    "ExpType": 3,
                    "Defence": 600,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC7", "quantity": 1, "chance": 0.00017, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5", "quantity": 1, "chance": 0.0095, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("PalmTree", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Palm Tree",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 2,
                    "RespawnTime": 0,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 32,
                    "ExpType": 3,
                    "Defence": 1250,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD7", "quantity": 1, "chance": 0.00011, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable11", "quantity": 2, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ToiletTree", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Toilet Tree",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 3,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 50,
                    "ExpType": 3,
                    "Defence": 3500,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD5", "quantity": 1, "chance": 0.00012, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5", "quantity": 1, "chance": 0.0106, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("StumpTree", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Stump Tree",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 4,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 90,
                    "ExpType": 3,
                    "Defence": 10000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD6", "quantity": 1, "chance": 0.00013, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable5", "quantity": 1, "chance": 0.0102, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("SaharanFoal", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Saharan Foal",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 3,
                    "RespawnTime": 0,
                    "DeathFrame": 0,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 150,
                    "ExpType": 3,
                    "Defence": 20000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD8", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable17", "quantity": 1, "chance": 0.0089, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Tree7", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Wispy Tree",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 3,
                    "RespawnTime": 0,
                    "DeathFrame": 9,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 275,
                    "ExpType": 3,
                    "Defence": 50000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsF2", "quantity": 1, "chance": 0.0001, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable17", "quantity": 1, "chance": 0.0089, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("AlienTree", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Alien Tree",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 4,
                    "RespawnTime": 0,
                    "DeathFrame": 6,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 500,
                    "ExpType": 3,
                    "Defence": 100000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsF13", "quantity": 1, "chance": 1e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable22", "quantity": 2, "chance": 0.00815, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Tree8", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Cubed Tree",
                    "AFKtype": AFKType.Choppin,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 0,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 4,
                    "RespawnTime": 0,
                    "DeathFrame": 10,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.treeType,
                    "SpecialType": "",
                    "ExpGiven": 1250,
                    "ExpType": 3,
                    "Defence": 250000,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsF12", "quantity": 1, "chance": 4e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable22", "quantity": 1, "chance": 0.0089, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("FishSmall", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Small Fish",
                    "AFKtype": AFKType.Fishing,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 50,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 2,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.fishType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 4,
                    "Defence": 40,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Salty Shores",
                    "world": "Yum Yum Desert",
                    "id": 54,
                    "portalRequirements": [15]
                },
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("FishMed", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Medium Fish",
                    "AFKtype": AFKType.Fishing,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 50,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 2,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.fishType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 4,
                    "Defence": 20000,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Deepwater Docks",
                    "world": "Yum Yum Desert",
                    "id": 61,
                    "portalRequirements": [30]
                },
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Fish1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Goldfish",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 48,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 0,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.fishType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Fish2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Hermit Can",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 48,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.fishType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Fish3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Jellyfish",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 48,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 2,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.fishType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Fish4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bloach",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 48,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 3,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.fishType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Fish5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Skelefish",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 48,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 4,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.fishType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Fish6", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Shark",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 48,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 5,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.fishType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Fish7", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Manta Ray",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 48,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 6,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.fishType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Fish8", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Kraken",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 4,
                    "MonsterOffsetX": 42,
                    "MonsterOffsetY": 28,
                    "HeightOfMonster": 48,
                    "MonsterMoving": 1,
                    "MovingFrame": 4,
                    "RespawnTime": 86400,
                    "DeathFrame": 7,
                    "MonsterHPTotal": 750000,
                    "Type": EnemyType.fishType,
                    "SpecialType": "a",
                    "ExpGiven": 12000,
                    "ExpType": 0,
                    "Defence": 600,
                    "MoveSPEED": 3,
                    "Damages": [1000, 1],
                    "DefFor0": 1223.26
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable9", "quantity": 1, "chance": 0.012, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("BugNest1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Fly Nest",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 30,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 51,
                    "RespawnTime": 86400,
                    "DeathFrame": 0,
                    "MonsterHPTotal": 999999999,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 6,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 2, "chance": 0, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("BugNest2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Butterfly Bar",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 30,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 67,
                    "RespawnTime": 86400,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 999999999,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 6,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 2, "chance": 0, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("BugNest3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sentient Bowl",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 30,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 59,
                    "RespawnTime": 86400,
                    "DeathFrame": 2,
                    "MonsterHPTotal": 999999999,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 6,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 2, "chance": 0, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("BugNest4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Grocery Bag",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 30,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 63,
                    "RespawnTime": 86400,
                    "DeathFrame": 3,
                    "MonsterHPTotal": 999999999,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 6,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 2, "chance": 0, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("BugNest5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Snowden",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 30,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 106,
                    "RespawnTime": 86400,
                    "DeathFrame": 4,
                    "MonsterHPTotal": 999999999,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 6,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 2, "chance": 0, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("BugNest6", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Icicle Nest",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 30,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 112,
                    "RespawnTime": 86400,
                    "DeathFrame": 5,
                    "MonsterHPTotal": 999999999,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 6,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 2, "chance": 0, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("BugNest7", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bee Hive",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 30,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 157,
                    "RespawnTime": 86400,
                    "DeathFrame": 6,
                    "MonsterHPTotal": 999999999,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 6,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 2, "chance": 0, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("BugNest8", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Fairy Hovel",
                    "AFKtype": AFKType.Fighting,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 30,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 112,
                    "RespawnTime": 86400,
                    "DeathFrame": 7,
                    "MonsterHPTotal": 999999999,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 6,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Grasslands2", "quantity": 2, "chance": 0, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Bug1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Flies",
                    "AFKtype": AFKType.Catching,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 50,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 0,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.bugType,
                    "SpecialType": "",
                    "ExpGiven": 2,
                    "ExpType": 6,
                    "Defence": 50,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC11", "quantity": 1, "chance": 0.00042, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable12", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Bug2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Butterflies",
                    "AFKtype": AFKType.Catching,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 50,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.bugType,
                    "SpecialType": "",
                    "ExpGiven": 6,
                    "ExpType": 6,
                    "Defence": 600,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsC12", "quantity": 1, "chance": 0.0003, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ButterBar", "quantity": 1, "chance": 0.01, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable12", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": <MapDataModel>{
                    "area": "Bandit Bob's Hideout",
                    "world": "Yum Yum Desert",
                    "id": 67,
                    "portalRequirements": [0]
                },
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Bug3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sentient Cereal",
                    "AFKtype": AFKType.Catching,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 50,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 2,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.bugType,
                    "SpecialType": "",
                    "ExpGiven": 10,
                    "ExpType": 6,
                    "Defence": 2500,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD10", "quantity": 1, "chance": 0.00028, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable12", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Bug4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Fruitflies",
                    "AFKtype": AFKType.Catching,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 50,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 3,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.bugType,
                    "SpecialType": "",
                    "ExpGiven": 20,
                    "ExpType": 6,
                    "Defence": 7000,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsD9", "quantity": 1, "chance": 0.00025, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable12", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Bug5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Mosquisnow",
                    "AFKtype": AFKType.Catching,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 50,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 4,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.bugType,
                    "SpecialType": "",
                    "ExpGiven": 40,
                    "ExpType": 6,
                    "Defence": 18000,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsF8", "quantity": 1, "chance": 0.00025, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable18", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Bug6", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Flycicle",
                    "AFKtype": AFKType.Catching,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 50,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 5,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.bugType,
                    "SpecialType": "",
                    "ExpGiven": 75,
                    "ExpType": 6,
                    "Defence": 40000,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsF9", "quantity": 1, "chance": 0.00025, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable18", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Bug7", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Bumble Bee",
                    "AFKtype": AFKType.Catching,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 50,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 6,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.bugType,
                    "SpecialType": "",
                    "ExpGiven": 150,
                    "ExpType": 6,
                    "Defence": 100000,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsF14", "quantity": 1, "chance": 5e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable23", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Bug8", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Fairy",
                    "AFKtype": AFKType.Catching,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 32,
                    "MonsterOffsetY": 50,
                    "HeightOfMonster": 100,
                    "MonsterMoving": 0,
                    "MovingFrame": 1,
                    "RespawnTime": 0,
                    "DeathFrame": 7,
                    "MonsterHPTotal": 5,
                    "Type": EnemyType.bugType,
                    "SpecialType": "",
                    "ExpGiven": 300,
                    "ExpType": 6,
                    "Defence": 250000,
                    "MoveSPEED": 0,
                    "Damages": [6, 1],
                    "DefFor0": 2.67
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 0, "chance": 0, "questLink": "N/A"},
                        <CardDropModel>{"item": "CardsF15", "quantity": 1, "chance": 2e-05, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable23", "quantity": 1, "chance": 0.015, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestA1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dewdrop Bronze Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 18000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 10,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 100, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneW1", "quantity": 1, "chance": 0.025, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA1", "quantity": 1, "chance": 0.09, "questLink": "N/A"},
                        <ItemDropModel>{"item": "OakTree", "quantity": 40, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Copper", "quantity": 30, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "CopperBar", "quantity": 20, "chance": 0.2, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable1", "quantity": 1, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key1", "quantity": 1, "chance": 0.04, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestB1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dewdrop Silver Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 36000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 400, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.12, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats17", "quantity": 1, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneW2", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA2", "quantity": 1, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodG4", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Iron", "quantity": 50, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "CopperBar", "quantity": 50, "chance": 0.35, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key1", "quantity": 1, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "JungleTree", "quantity": 15, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "BirchTree", "quantity": 25, "chance": 0.1, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable2", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestC1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dewdrop Golden Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 86400,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1250, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.8, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodG1", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "IronBar", "quantity": 15, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Gold", "quantity": 20, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "ToiletTree", "quantity": 50, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key1", "quantity": 1, "chance": 0.18, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StumpTree", "quantity": 50, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentShirts12", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable3", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestD1", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Dewdrop Legendary Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 345600,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 100000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{"drops": []},
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestA2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sandstone Bronze Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 18000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 10,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 1000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneW2", "quantity": 1, "chance": 0.025, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA2", "quantity": 1, "chance": 0.09, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Fish1", "quantity": 50, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Fish2", "quantity": 50, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Bug1", "quantity": 65, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Gold", "quantity": 75, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key2", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GoldBar", "quantity": 20, "chance": 0.2, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable6", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestB2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sandstone Silver Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 36000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 4000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats18", "quantity": 1, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneW3", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA3", "quantity": 1, "chance": 0.09, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Fish3", "quantity": 100, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Bug3", "quantity": 125, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key2", "quantity": 1, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodG2", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Plat", "quantity": 50, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GoldBar", "quantity": 60, "chance": 0.35, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PalmTree", "quantity": 100, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable7", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestC2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sandstone Golden Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 86400,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 10000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodG3", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PlatBar", "quantity": 20, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Dementia", "quantity": 80, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Fish4", "quantity": 150, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Bug4", "quantity": 169, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentPants4", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key2", "quantity": 1, "chance": 0.18, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable8", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestD2", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Sandstone Legendary Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 345600,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 100000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{"drops": []},
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestA3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chillsnap Bronze Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 18000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 10,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 10000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.12, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneW3", "quantity": 1, "chance": 0.025, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SnowA2a", "quantity": 1, "chance": 0.01, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA3", "quantity": 1, "chance": 0.09, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul1", "quantity": 50, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter1", "quantity": 65, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PlatBar", "quantity": 60, "chance": 0.35, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key3", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PlatBar", "quantity": 20, "chance": 0.2, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable14", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestB3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chillsnap Silver Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 36000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 40000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.23, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentHats28", "quantity": 1, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneW3", "quantity": 1, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA3", "quantity": 1, "chance": 0.3, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter2", "quantity": 350, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Bug5", "quantity": 150, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key3", "quantity": 1, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodG5", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Dementia", "quantity": 100, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "SaharanFoal", "quantity": 100, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable15", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestC3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chillsnap Golden Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 86400,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 100000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.45, "questLink": "N/A"},
                        <ItemDropModel>{"item": "DementiaBar", "quantity": 80, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul2", "quantity": 400, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Void", "quantity": 120, "chance": 0.1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Bug6", "quantity": 150, "chance": 0.2, "questLink": "N/A"},
                        <ItemDropModel>{"item": "EquipmentPants5", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key3", "quantity": 1, "chance": 0.18, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodG6", "quantity": 1, "chance": 0.3, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable16", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestD3", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Chillsnap Legendary Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 345600,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 100000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{"drops": []},
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestA4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Astro Bronze Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 18000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 10,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 8000000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.12, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneW4", "quantity": 1, "chance": 0.015, "questLink": "N/A"},
                        <ItemDropModel>{"item": "GalaxyA2b", "quantity": 1, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA4", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Soul1", "quantity": 50, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter6", "quantity": 200, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "VoidBar", "quantity": 100, "chance": 0.35, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key1", "quantity": 1, "chance": 0.006, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable19", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestB4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Astro Silver Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 36000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 30000000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.23, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneW4", "quantity": 1, "chance": 0.04, "questLink": "N/A"},
                        <ItemDropModel>{"item": "StoneA4", "quantity": 1, "chance": 0.07, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Critter8", "quantity": 600, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Bug7", "quantity": 1500, "chance": 0.4, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key2", "quantity": 1, "chance": 0.012, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodG7", "quantity": 1, "chance": 0.5, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Lustre", "quantity": 1000, "chance": 0.6, "questLink": "N/A"},
                        <ItemDropModel>{"item": "AlienTree", "quantity": 750, "chance": 0.5, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable20", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestC4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Astro Golden Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 86400,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{
                    "drops": [
                        <CoinDropModel>{"item": "COIN", "quantity": 60000000, "chance": 1, "questLink": "N/A"},
                        <ItemDropModel>{"item": "PremiumGem", "quantity": 1, "chance": 0.45, "questLink": "N/A"},
                        <ItemDropModel>{"item": "LustreBar", "quantity": 150, "chance": 0.05, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Starfire", "quantity": 2000, "chance": 0.03, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Bug8", "quantity": 1500, "chance": 0.02, "questLink": "N/A"},
                        <ItemDropModel>{"item": "Key3", "quantity": 1, "chance": 0.01, "questLink": "N/A"},
                        <ItemDropModel>{"item": "FoodG7", "quantity": 2, "chance": 0.03, "questLink": "N/A"},
                        <SubTableDropModel>{"item": "DropTable21", "quantity": 1, "chance": 1, "questLink": "N/A"}
                    ]
                },
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestD4", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "Astro Legendary Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 345600,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 100000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": <EnemyTableModel>{"drops": []},
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestA5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Bronze Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 18000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 10,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestB5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Silver Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 36000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestC5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Golden Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 86400,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestD5", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Legendary Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 345600,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 100000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestA6", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Bronze Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 18000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 10,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestB6", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Silver Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 36000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestC6", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Golden Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 86400,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestD6", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Legendary Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 345600,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 100000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestA7", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Bronze Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 18000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 10,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestB7", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Silver Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 36000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestC7", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Golden Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 86400,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestD7", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Legendary Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 345600,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 100000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestA8", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Bronze Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 18000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 10,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestB8", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Silver Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 36000,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 500,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestC8", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Golden Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 86400,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 20000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("ChestD8", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "NYI Legendary Chest",
                    "AFKtype": AFKType.Error,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 34,
                    "MonsterOffsetY": 25,
                    "HeightOfMonster": 40,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 345600,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 100000,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 0,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 1],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": null,
                "navigation": null,
                "bossData": null
            }),
        new EnemyBase("Nothing", <EnemyModel>{
                "details": <EnemyDetailsModel>{
                    "Name": "",
                    "AFKtype": AFKType.Nothing,
                    "MonsterFace": 0,
                    "MonsterOffsetX": 22,
                    "MonsterOffsetY": 32,
                    "HeightOfMonster": 180,
                    "MonsterMoving": 0,
                    "MovingFrame": 0,
                    "RespawnTime": 1,
                    "DeathFrame": 1,
                    "MonsterHPTotal": 42,
                    "Type": EnemyType.monsterType,
                    "SpecialType": "",
                    "ExpGiven": 69,
                    "ExpType": 0,
                    "Defence": 1,
                    "MoveSPEED": 0,
                    "Damages": [0, 0],
                    "DefFor0": 0.22
                },
                "drops": null,
                "mapData": <MapDataModel>{
                    "area": "Blunder Hills",
                    "world": "Blunder Hills",
                    "id": 0,
                    "portalRequirements": [1, 0]
                },
                "navigation": null,
                "bossData": null
            })    
]
}
