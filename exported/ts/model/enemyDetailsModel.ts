import { EnemyType } from './enemyType';
import { AFKType } from './aFKType';

export interface EnemyDetailsModel {
    Name: string,
    AFKtype: AFKType,
    MonsterFace: number,
    MonsterOffsetX: number,
    MonsterOffsetY: number,
    HeightOfMonster: number,
    MonsterMoving: number,
    MovingFrame: number,
    RespawnTime: number,
    DeathFrame: number,
    MonsterHPTotal: number,
    Type: EnemyType,
    SpecialType: string,
    ExpGiven: number,
    ExpType: number,
    Defence: number,
    MoveSPEED: number,
    Damages: number,
    DefFor0?: number
}
