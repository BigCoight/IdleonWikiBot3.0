import { NpcHeadModel } from './npcHeadModel';
import { DialogueLineModel } from './dialogueLineModel';
import { QuestModel } from './questModel';

export interface NpcModel {
    head?: NpcHeadModel,
    quests: Record<string, QuestModel>,
    dialogue: DialogueLineModel[]
}
