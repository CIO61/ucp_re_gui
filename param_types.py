param_fields = {
    "FarmBuilding": [
        "Farm1",
        "Farm2",
        "Farm3",
        "Farm4",
        "Farm5",
        "Farm6",
        "Farm7",
        "Farm8"
    ],
    "Resource": [
        "SellResource01",
        "SellResource02",
        "SellResource03",
        "SellResource04",
        "SellResource05",
        "SellResource06",
        "SellResource07",
        "SellResource08",
        "SellResource09",
        "SellResource10",
        "SellResource11",
        "SellResource12",
        "SellResource13",
        "SellResource14",
        "SellResource15"
    ],
    "Unit": [
        "SortieUnitRanged",
        "SortieUnitMelee",
        "DefUnit1",
        "DefUnit2",
        "DefUnit3",
        "DefUnit4",
        "DefUnit5",
        "DefUnit6",
        "DefUnit7",
        "DefUnit8",
        "RaidUnit1",
        "RaidUnit2",
        "RaidUnit3",
        "RaidUnit4",
        "RaidUnit5",
        "RaidUnit6",
        "RaidUnit7",
        "RaidUnit8",
        "AttUnitPatrol",
        "AttUnitBackup",
        "AttUnitEngage",
        "AttUnitSiegeDef",
        "AttUnitMain1",
        "AttUnitMain2",
        "AttUnitMain3",
        "AttUnitMain4",
        "AttUnitVanguard"

    ],
    "DiggingUnit": [
        "DefDiggingUnit",
        "AttDiggingUnit"
    ],
    "SiegeEngine": [
        "SiegeEngine1",
        "SiegeEngine2",
        "SiegeEngine3",
        "SiegeEngine4",
        "SiegeEngine5",
        "SiegeEngine6",
        "SiegeEngine7",
        "SiegeEngine8",
        "HarassingSiegeEngine1",
        "HarassingSiegeEngine2",
        "HarassingSiegeEngine3",
        "HarassingSiegeEngine4",
        "HarassingSiegeEngine5",
        "HarassingSiegeEngine6",
        "HarassingSiegeEngine7",
        "HarassingSiegeEngine8"
    ],
    "BlacksmithSetting": ["BlacksmithSetting"],
    "FletcherSetting": ["FletcherSetting"],
    "PoleturnerSetting": ["PoleturnerSetting"],
    "TargetChoice": ["TargetChoice"]
}

not_personal = [  # unused
    "Name",
    "Description",  # deprecated
    "CustomName"
]

param_names = [
  "WallDecoration",
  "Unknown001",
  "Unknown002",
  "Unknown003",
  "Unknown004",
  "Unknown005",
  "CriticalPopularity",
  "LowestPopularity",
  "HighestPopularity",
  "TaxesMin",
  "TaxesMax",
  "Unknown011",
  "Farm1",
  "Farm2",
  "Farm3",
  "Farm4",
  "Farm5",
  "Farm6",
  "Farm7",
  "Farm8",
  "PopulationPerFarm",
  "PopulationPerWoodcutter",
  "PopulationPerQuarry",
  "PopulationPerIronmine",
  "PopulationPerPitchrig",
  "MaxQuarries",
  "MaxIronmines",
  "MaxWoodcutters",
  "MaxPitchrigs",
  "MaxFarms",
  "BuildInterval",
  "ResourceRebuildDelay",
  "MaxFood",
  "MinimumApples",
  "MinimumCheese",
  "MinimumBread",
  "MinimumWheat",
  "MinimumHop",
  "TradeAmountFood",
  "TradeAmountEquipment",
  "AIRequestDelay",
  "MinimumGoodsRequiredAfterTrade",
  "DoubleRationsFoodThreshold",
  "MaxWood",
  "MaxStone",
  "MaxResourceOther",
  "MaxEquipment",
  "MaxBeer",
  "MaxResourceVariance",
  "RecruitGoldThreshold",
  "BlacksmithSetting",
  "FletcherSetting",
  "PoleturnerSetting",
  "SellResource01",
  "SellResource02",
  "SellResource03",
  "SellResource04",
  "SellResource05",
  "SellResource06",
  "SellResource07",
  "SellResource08",
  "SellResource09",
  "SellResource10",
  "SellResource11",
  "SellResource12",
  "SellResource13",
  "SellResource14",
  "SellResource15",
  "DefWallPatrolRallyTime",
  "DefWallPatrolGroups",
  "DefSiegeEngineGoldThreshold",
  "DefSiegeEngineBuildDelay",
  "Unknown072",
  "Unknown073",
  "RecruitProbDefDefault",
  "RecruitProbDefWeak",
  "RecruitProbDefStrong",
  "RecruitProbRaidDefault",
  "RecruitProbRaidWeak",
  "RecruitProbRaidStrong",
  "RecruitProbAttackDefault",
  "RecruitProbAttackWeak",
  "RecruitProbAttackStrong",
  "SortieUnitRangedMin",
  "SortieUnitRanged",
  "SortieUnitMeleeMin",
  "SortieUnitMelee",
  "DefDiggingUnitMax",
  "DefDiggingUnit",
  "RecruitInterval",
  "RecruitIntervalWeak",
  "RecruitIntervalStrong",
  "DefTotal",
  "OuterPatrolGroupsCount",
  "OuterPatrolGroupsMove",
  "OuterPatrolRallyDelay",
  "DefWalls",
  "DefUnit1",
  "DefUnit2",
  "DefUnit3",
  "DefUnit4",
  "DefUnit5",
  "DefUnit6",
  "DefUnit7",
  "DefUnit8",
  "RaidUnitsBase",
  "RaidUnitsRandom",
  "RaidUnit1",
  "RaidUnit2",
  "RaidUnit3",
  "RaidUnit4",
  "RaidUnit5",
  "RaidUnit6",
  "RaidUnit7",
  "RaidUnit8",
  "HarassingSiegeEngine1",
  "HarassingSiegeEngine2",
  "HarassingSiegeEngine3",
  "HarassingSiegeEngine4",
  "HarassingSiegeEngine5",
  "HarassingSiegeEngine6",
  "HarassingSiegeEngine7",
  "HarassingSiegeEngine8",
  "HarassingSiegeEnginesMax",
  "RaidRetargetDelay",
  "AttForceBase",
  "AttForceRandom",
  "AttForceSupportAllyThreshold",
  "AttForceRallyPercentage",
  "Unknown129",
  "AttAssaultDelay",
  "AttUnitPatrolRecommandDelay",
  "Unknown132",
  "SiegeEngine1",
  "SiegeEngine2",
  "SiegeEngine3",
  "SiegeEngine4",
  "SiegeEngine5",
  "SiegeEngine6",
  "SiegeEngine7",
  "SiegeEngine8",
  "CowThrowInterval",
  "Unknown142",
  "AttMaxEngineers",
  "AttDiggingUnit",
  "AttDiggingUnitMax",
  "AttUnitVanguard",
  "AttUnitVanguardMax",
  "AttMaxAssassins",
  "AttMaxLaddermen",
  "AttMaxTunnelers",
  "AttUnitPatrol",
  "AttUnitPatrolMax",
  "AttUnitPatrolGroupsCount",
  "AttUnitBackup",
  "AttUnitBackupMax",
  "AttUnitBackupGroupsCount",
  "AttUnitEngage",
  "AttUnitEngageMax",
  "AttUnitSiegeDef",
  "AttUnitSiegeDefMax",
  "AttUnitSiegeDefGroupsCount",
  "AttUnitMain1",
  "AttUnitMain2",
  "AttUnitMain3",
  "AttUnitMain4",
  "AttMaxDefault",
  "AttMainGroupsCount",
  "TargetChoice"
]

Popularity = [
    "CriticalPopularity",
    "LowestPopularity"
    "HighestPopularity"]

FarmBuilding = [
    "None",
    "WheatFarm",
    "HopFarm",
    "AppleFarm",
    "DairyFarm"
]

Resource = [
    "None",
    "Wood",
    "Hop",
    "Stone",
    "Iron",
    "Pitch",
    "Wheat",
    "Bread",
    "Cheese",
    "Meat",
    "Apples",
    "Beer",
    "Flour",
    "Bows",
    "Crossbows",
    "Spears",
    "Pikes",
    "Maces",
    "Swords",
    "LeatherArmors",
    "IronArmors"
]

Unit = [
    "None",
    "Tunneler",
    "EuropArcher",
    "Crossbowman",
    "Spearman",
    "Pikeman",
    "Maceman",
    "Swordsman",
    "Knight",
    "Ladderman",
    "Engineer",
    "Monk",
    "ArabArcher",
    "Slave",
    "Slinger",
    "Assassin",
    "HorseArcher",
    "ArabSwordsman",
    "FireThrower"
]

DiggingUnit = [
    "None",
    "EuropArcher",
    "Spearman",
    "Pikeman",
    "Maceman",
    "Engineer",
    "Slave"
]

SiegeEngine = [
    "None",
    "Catapult",
    "Trebuchet",
    "Mangonel",
    "Tent",
    "SiegeTower",
    "BatteringRam",
    "Shield",
    "TowerBallista",
    "FireBallista"
]

BlacksmithSetting = [
    "Both",
    "Swords",
    "Maces"
]

PoleturnerSetting = [
    "Both",
    "Pikes",
    "Spears"
]

FletcherSetting = [
    "Both",
    "Bows",
    "Crossbows"
]

TargetChoice = [
    "Gold",
    "Balanced",
    "Any",
    "Closest",
    "Player"
]

