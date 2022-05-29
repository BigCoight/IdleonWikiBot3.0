import { EnemyTableModel } from './enemyTableModel';
import { EnemyDetailsModel } from './enemyDetailsModel';
import { EnemyNavModel } from './enemyNavModel';
import { BossDetailsModel } from './bossDetailsModel';
import { MapDataModel } from './mapDataModel';

export interface EnemyModel {
    details: EnemyDetailsModel,
    drops?: EnemyTableModel,
    mapData?: MapDataModel,
    navigation?: EnemyNavModel,
    bossData?: BossDetailsModel
}
