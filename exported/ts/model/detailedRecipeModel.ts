import { DetRecipeComponentModel } from './detRecipeComponentModel';
import { ComponentModel } from './componentModel';

export interface DetailedRecipeModel {
    detRecipe: DetRecipeComponentModel[],
    detRecipeTotals?: ComponentModel[]
}
