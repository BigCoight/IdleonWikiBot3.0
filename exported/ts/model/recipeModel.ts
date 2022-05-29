import { SourceModel } from './sourceModel';
import { DetailedRecipeModel } from './detailedRecipeModel';
import { ComponentModel } from './componentModel';

export interface RecipeModel {
    intID: string,
    recipe: ComponentModel[],
    levelReqToCraft: number,
    expGiven: number,
    no: number,
    tab: number,
    sellPrice?: number,
    recipeFrom?: SourceModel[],
    detailedRecipe?: DetailedRecipeModel
}
