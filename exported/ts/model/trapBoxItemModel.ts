import { ClassType } from './classType';
import { ToolItemModel } from './toolItemModel';
import { TrapBoxModel } from './trapBoxModel';
import { TypeGen } from './typeGen';

export interface TrapBoxItemModel extends ToolItemModel {
    trapBoxData: TrapBoxModel
}
