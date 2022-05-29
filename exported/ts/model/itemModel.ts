import { RecipeModel } from './recipeModel';
import { ItemVendorsModel } from './itemVendorsModel';
import { AnvilProduceModel } from './anvilProduceModel';
import { NoteModel } from './noteModel';
import { DetDropsModel } from './detDropsModel';
import { BaseItemModel } from './baseItemModel';
import { SourcesModel } from './sourcesModel';

export interface ItemModel {
    item: BaseItemModel,
    sources?: SourcesModel,
    notes?: NoteModel,
    recipe?: RecipeModel,
    vendors?: ItemVendorsModel,
    anvilProduction?: AnvilProduceModel,
    detDrops?: DetDropsModel
}
