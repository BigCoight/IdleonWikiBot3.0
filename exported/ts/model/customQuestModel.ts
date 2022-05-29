import { NoteModel } from './noteModel';
import { CustomReqModel } from './customReqModel';
import { QuestModel } from './questModel';
import { ComponentModel } from './componentModel';
import { QuestType } from './questType';

export interface CustomQuestModel extends QuestModel {
    CustomType: string,
    CustomArray: CustomReqModel[]
}
