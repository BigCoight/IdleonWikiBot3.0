import { DescItemModel } from './descItemModel';
import { FishingToolkitModel } from './fishingToolkitModel';
import { TypeGen } from './typeGen';

export interface FishingTKItemModel extends DescItemModel {
    fishingToolkit: FishingToolkitModel
}
