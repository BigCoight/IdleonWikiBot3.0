import { NoteModel } from './noteModel';
import { ComponentModel } from './componentModel';
import { QuestModel } from './questModel';
import { QuestType } from './questType';

export interface ItemQuestModel extends QuestModel {
    ItemReq: ComponentModel[]
}
