import { ComponentModel } from './componentModel';
import { NoteModel } from './noteModel';
import { QuestModel } from './questModel';
import { QuestType } from './questType';

export interface ItemQuestModel extends QuestModel {
    ItemReq: ComponentModel[]
}
