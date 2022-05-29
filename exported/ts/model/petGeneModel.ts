import { AbilityType } from './abilityType';

export interface PetGeneModel {
    name: string,
    abilityType: AbilityType,
    x2: number,
    lowerLetter: string,
    upperLetter: string,
    description: string,
    combatDescription: string
}
