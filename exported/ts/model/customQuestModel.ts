import { ComponentModel } from './componentModel';
import { CustomReqModel } from './customReqModel';
import { NoteModel } from './noteModel';
import { QuestModel } from './questModel';
import { QuestType } from './questType';

export interface CustomQuestModel extends QuestModel {
    CustomType: string,
    CustomArray: CustomReqModel[]
}
