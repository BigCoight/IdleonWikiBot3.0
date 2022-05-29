import { QuestType } from './questType';

export interface DialogueLineModel {
    Type: QuestType,
    DialogueText: string,
    NextIndex: number,
    Name?: string
}
