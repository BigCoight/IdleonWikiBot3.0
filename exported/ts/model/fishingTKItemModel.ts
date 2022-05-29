import { FishingToolkitModel } from './fishingToolkitModel';
import { DescItemModel } from './descItemModel';
import { TypeGen } from './typeGen';

export interface FishingTKItemModel extends DescItemModel {
    fishingToolkit: FishingToolkitModel
}
