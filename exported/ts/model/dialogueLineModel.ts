import { QuestTypeEnum } from '../enum/questTypeEnum';

export interface DialogueLineModel {
    Type: QuestType,
    DialogueText: string,
    NextIndex: number,
    Name?: string
}
