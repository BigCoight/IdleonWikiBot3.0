from repositories.arcade.ArcadeBonusRepo import ArcadeBonusRepo
from repositories.collections.EnemyRepo import EnemyRepo
from repositories.dungeons.DungEnemyRepo import DungEnemyRepo
from repositories.dungeons.DungItemRepo import DungItemRepo
from repositories.enemies.BossDetailRepo import BossDetailRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.item.AnvilRepo import AnvilRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.RefineryCostRepo import RefineryCostRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.TrapBoxRepo import TrapBoxRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.misc.AchievementRepo import AchievementRepo
from repositories.misc.CardSetRepo import CardSetRepo
from repositories.misc.ColosseumRepo import ColosseumRepo
from repositories.misc.CompanionRepo import CompanionRepo
from repositories.misc.ConstellationsRepo import ConstellationsRepo
from repositories.misc.GemShopRepo import GemShopRepo
from repositories.misc.GrimoireUpgradeRepo import GrimoireUpgradeRepo
from repositories.misc.GuildBonusRepo import GuildBonusRepo
from repositories.misc.TaskDescriptionsRepo import TaskDescriptionRepo
from repositories.misc.TaskShopDescRepo import TaskShopDescRepo
from repositories.misc.TomeRepo import TomeRepo
from repositories.misc.UpgradeVaultRepo import UpgradeVaultRepo
from repositories.misc.equinox.DreamChallengeRepo import DreamChallengeRepo
from repositories.misc.equinox.DreamUpgradeRepo import DreamUpgradeRepo
from repositories.misc.weeklyboss.WeeklyActionRepo import WeeklyActionRepo
from repositories.misc.weeklyboss.WeeklyBossRepo import WeeklyBossRepo
from repositories.misc.weeklyboss.WeeklyShopRepo import WeeklyShopRepo
from repositories.misc.world1.BribeRepo import BribeRepo
from repositories.misc.world1.FeatherRepo import FeatherRepo
from repositories.misc.world2.BubbleRepo import BubbleRepo
from repositories.misc.world2.FishPoolRepo import FishPoolRepo
from repositories.misc.world2.PostOfficeRepo import PostOfficeRepo
from repositories.misc.world2.PostOfficeUpgradesRepo import PostOfficeUpgradesRepo
from repositories.misc.world2.SigilRepo import SigilRepo
from repositories.misc.world3.AtomColliderRepo import AtomColliderRepo
from repositories.misc.world3.BuildingRepo import BuildingRepo
from repositories.misc.world3.PrayerRepo import PrayerRepo
from repositories.misc.world3.ShrineRepo import ShrineRepo
from repositories.misc.world4.ArenaBonusRepo import ArenaBonusRepo
from repositories.misc.world4.ChipRepo import ChipRepo
from repositories.misc.world4.InfiniteTerritoryRepo import InfiniteTerritoryRepo
from repositories.misc.world4.JewelRepo import JewelRepo
from repositories.misc.world4.LabBonusRepo import LabBonusRepo
from repositories.misc.world4.MealRepo import MealRepo
from repositories.misc.world4.PetGeneRepo import PetGeneRepo
from repositories.misc.world4.PetStatRepo import PetStatRepo
from repositories.misc.world4.PetUpgradeRepo import PetUpgradeRepo
from repositories.misc.world4.TerritoryFightRepo import TerritoryFightRepo
from repositories.misc.world5.ArtifactRepo import ArtifactRepo
from repositories.misc.world5.CaptainBonusRepo import CaptainBonusRepo
from repositories.misc.world5.DivinityStyleRepo import DivinityStyleRepo
from repositories.misc.world5.GamingBoxRepo import GamingBoxRepo
from repositories.misc.world5.GamingSuperbitsRepo import GamingSuperbitsRepo
from repositories.misc.world5.GamingUpgradeRepo import GamingUpgradeRepo
from repositories.misc.world5.GodInfoRepo import GodInfoRepo
from repositories.misc.world5.IslandInfoRepo import IslandInfoRepo
from repositories.misc.world5.SlabItemSortRepo import SlabItemSortRepo
from repositories.misc.world5.hole.HoleBuildingRepo import HoleBuildingRepo
from repositories.misc.world6.JadeUpgradeRepo import JadeUpgradeRepo
from repositories.misc.world6.MarketInfoRepo import MarketInfoRepo
from repositories.misc.world6.NinjaItemRepo import NinjaItemRepo
from repositories.misc.world6.NinjaUpgradeRepo import NinjaUpgradeRepo
from repositories.misc.world6.SeedInfoRepo import SeedInfoRepo
from repositories.misc.world6.SummonEnemyRepo import SummonEnemyRepo
from repositories.misc.world6.SummonUnitRepo import SummonUnitRepo
from repositories.misc.world6.SummonUpgradeRepo import SummonUpgradeRepo
from repositories.npc.NpcRepo import NpcRepo
from repositories.talents.TalentTreeRepo import TalentTreeRepo

AllRepos = [SpecificItemRepo, EnemyRepo, DropTableRepo, NpcRepo, RecipeRepo, BubbleRepo, TalentTreeRepo,
            UpgradeVaultRepo, GrimoireUpgradeRepo, PostOfficeUpgradesRepo, PostOfficeRepo, VendorRepo, PrayerRepo, GemShopRepo, BuildingRepo, ShrineRepo,
            RefineryCostRepo, BribeRepo, ConstellationsRepo, DungEnemyRepo, DungItemRepo, AchievementRepo,
            GuildBonusRepo,
            AnvilRepo, ArenaBonusRepo, ChipRepo, InfiniteTerritoryRepo, JewelRepo, LabBonusRepo, MealRepo, PetGeneRepo,
            PetStatRepo, PetUpgradeRepo, TerritoryFightRepo, BossDetailRepo, CardSetRepo, FishPoolRepo, TrapBoxRepo,
            ArcadeBonusRepo, SigilRepo, TaskShopDescRepo, TaskDescriptionRepo, ColosseumRepo, ArtifactRepo,
            CaptainBonusRepo, DivinityStyleRepo, GamingBoxRepo, GamingUpgradeRepo, GodInfoRepo, IslandInfoRepo,
            SlabItemSortRepo, GamingSuperbitsRepo, CompanionRepo, AtomColliderRepo, WeeklyBossRepo, WeeklyActionRepo,
            WeeklyShopRepo, DreamChallengeRepo, DreamUpgradeRepo, SummonUpgradeRepo, NinjaUpgradeRepo, JadeUpgradeRepo,
            MarketInfoRepo, SeedInfoRepo, SummonEnemyRepo, SummonUnitRepo, NinjaItemRepo, FeatherRepo, TomeRepo,
            HoleBuildingRepo
            ]
