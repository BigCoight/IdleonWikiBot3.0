import { MapDataModel } from '../model/mapDataModel';

export class MapDataBase { constructor(public id: string, public data: MapDataModel) { } }



export const initMapDataRepo = () => {
    return [    
        new MapDataBase("Nothing", <MapDataModel>{
                "area": "Blunder Hills",
                "world": "Blunder Hills",
                "id": 0,
                "portalRequirements": [1, 0]
            }),
        new MapDataBase("mushG", <MapDataModel>{
                "area": "Spore Meadows",
                "world": "Blunder Hills",
                "id": 1,
                "portalRequirements": [20]
            }),
        new MapDataBase("frogG", <MapDataModel>{
                "area": "Froggy Fields",
                "world": "Blunder Hills",
                "id": 2,
                "portalRequirements": [30]
            }),
        new MapDataBase("JungleZ", <MapDataModel>{
                "area": "JungleZ",
                "world": "Blunder Hills",
                "id": 3,
                "portalRequirements": [150, 10]
            }),
        new MapDataBase("Copper", <MapDataModel>{
                "area": "Tunnels Entrance",
                "world": "Blunder Hills",
                "id": 6,
                "portalRequirements": [10]
            }),
        new MapDataBase("Iron", <MapDataModel>{
                "area": "Freefall Caverns",
                "world": "Blunder Hills",
                "id": 7,
                "portalRequirements": [25, 81]
            }),
        new MapDataBase("poopSmall", <MapDataModel>{
                "area": "Poopy Sewers",
                "world": "Blunder Hills",
                "id": 8,
                "portalRequirements": [20000]
            }),
        new MapDataBase("Plat", <MapDataModel>{
                "area": "The Ol' Straightaway",
                "world": "Blunder Hills",
                "id": 10,
                "portalRequirements": [40]
            }),
        new MapDataBase("Void", <MapDataModel>{
                "area": "Echoing Egress",
                "world": "Blunder Hills",
                "id": 11,
                "portalRequirements": [50, 60]
            }),
        new MapDataBase("Starfire", <MapDataModel>{
                "area": "Slip Slidy Ledges",
                "world": "Blunder Hills",
                "id": 12,
                "portalRequirements": [60]
            }),
        new MapDataBase("branch", <MapDataModel>{
                "area": "The Base Of The Bark",
                "world": "Blunder Hills",
                "id": 13,
                "portalRequirements": [2500, 50000]
            }),
        new MapDataBase("beanG", <MapDataModel>{
                "area": "Valley Of The Beans",
                "world": "Blunder Hills",
                "id": 14,
                "portalRequirements": [80, 1500]
            }),
        new MapDataBase("ratB", <MapDataModel>{
                "area": "Rats Nest",
                "world": "Blunder Hills",
                "id": 15,
                "portalRequirements": [35000]
            }),
        new MapDataBase("slimeG", <MapDataModel>{
                "area": "Jungle Perimeter",
                "world": "Blunder Hills",
                "id": 16,
                "portalRequirements": [200, 3000]
            }),
        new MapDataBase("mushR", <MapDataModel>{
                "area": "Birch Enclave",
                "world": "Blunder Hills",
                "id": 17,
                "portalRequirements": [0]
            }),
        new MapDataBase("acorn", <MapDataModel>{
                "area": "Hollowed Trunk",
                "world": "Blunder Hills",
                "id": 18,
                "portalRequirements": [5000]
            }),
        new MapDataBase("snakeG", <MapDataModel>{
                "area": "Winding Willows",
                "world": "Blunder Hills",
                "id": 19,
                "portalRequirements": [250]
            }),
        new MapDataBase("carrotO", <MapDataModel>{
                "area": "Vegetable Patch",
                "world": "Blunder Hills",
                "id": 24,
                "portalRequirements": [300, 2000]
            }),
        new MapDataBase("goblinG", <MapDataModel>{
                "area": "Forest Outskirts",
                "world": "Blunder Hills",
                "id": 26,
                "portalRequirements": [350]
            }),
        new MapDataBase("plank", <MapDataModel>{
                "area": "Encroaching Forest Villas",
                "world": "Blunder Hills",
                "id": 27,
                "portalRequirements": [30, 4200]
            }),
        new MapDataBase("frogBIG", <MapDataModel>{
                "area": "Tucked Away",
                "world": "Blunder Hills",
                "id": 28,
                "portalRequirements": [0]
            }),
        new MapDataBase("mushW", <MapDataModel>{
                "area": "Where the Branches End",
                "world": "Blunder Hills",
                "id": 31,
                "portalRequirements": [0]
            }),
        new MapDataBase("map32", <MapDataModel>{"area": "MininggF", "world": "Blunder Hills", "id": 32, "portalRequirements": [0]}),
        new MapDataBase("map33", <MapDataModel>{
                "area": "How Did u get here",
                "world": "Blunder Hills",
                "id": 33,
                "portalRequirements": [0]
            }),
        new MapDataBase("map34", <MapDataModel>{"area": "Miningg1", "world": "Blunder Hills", "id": 34, "portalRequirements": [0]}),
        new MapDataBase("map35", <MapDataModel>{"area": "Miningg2", "world": "Blunder Hills", "id": 35, "portalRequirements": [0]}),
        new MapDataBase("poopD", <MapDataModel>{
                "area": "Meel's Crypt",
                "world": "Blunder Hills",
                "id": 38,
                "portalRequirements": [0]
            }),
        new MapDataBase("Z", <MapDataModel>{"area": "Z", "world": "Blunder Hills", "id": 41, "portalRequirements": [0]}),
        new MapDataBase("jarSand", <MapDataModel>{
                "area": "Jar Bridge",
                "world": "Yum Yum Desert",
                "id": 51,
                "portalRequirements": [250]
            }),
        new MapDataBase("mimicA", <MapDataModel>{
                "area": "The Mimic Hole",
                "world": "Yum Yum Desert",
                "id": 52,
                "portalRequirements": [600, 1000]
            }),
        new MapDataBase("crabcake", <MapDataModel>{
                "area": "Dessert Dunes",
                "world": "Yum Yum Desert",
                "id": 53,
                "portalRequirements": [1000]
            }),
        new MapDataBase("FishSmall", <MapDataModel>{
                "area": "Salty Shores",
                "world": "Yum Yum Desert",
                "id": 54,
                "portalRequirements": [15]
            }),
        new MapDataBase("Filler", <MapDataModel>{"area": "Filler", "world": "Yum Yum Desert", "id": 56, "portalRequirements": [30]}),
        new MapDataBase("coconut", <MapDataModel>{
                "area": "The Grandioso Canyon",
                "world": "Yum Yum Desert",
                "id": 57,
                "portalRequirements": [1200]
            }),
        new MapDataBase("sandcastle", <MapDataModel>{
                "area": "Shifty Sandbox",
                "world": "Yum Yum Desert",
                "id": 58,
                "portalRequirements": [1600]
            }),
        new MapDataBase("pincermin", <MapDataModel>{
                "area": "Pincer Plateau",
                "world": "Yum Yum Desert",
                "id": 59,
                "portalRequirements": [2000]
            }),
        new MapDataBase("potato", <MapDataModel>{
                "area": "Slamabam Straightaway",
                "world": "Yum Yum Desert",
                "id": 60,
                "portalRequirements": [2500, 0]
            }),
        new MapDataBase("FishMed", <MapDataModel>{
                "area": "Deepwater Docks",
                "world": "Yum Yum Desert",
                "id": 61,
                "portalRequirements": [30]
            }),
        new MapDataBase("steak", <MapDataModel>{
                "area": "The Ring",
                "world": "Yum Yum Desert",
                "id": 62,
                "portalRequirements": [3000]
            }),
        new MapDataBase("moonman", <MapDataModel>{
                "area": "Up Up Down Down",
                "world": "Yum Yum Desert",
                "id": 63,
                "portalRequirements": [4000]
            }),
        new MapDataBase("sandgiant", <MapDataModel>{
                "area": "Sands of Time",
                "world": "Yum Yum Desert",
                "id": 64,
                "portalRequirements": [5000]
            }),
        new MapDataBase("snailZ", <MapDataModel>{
                "area": "Djonnuttown",
                "world": "Yum Yum Desert",
                "id": 65,
                "portalRequirements": [1]
            }),
        new MapDataBase("Bug2", <MapDataModel>{
                "area": "Bandit Bob's Hideout",
                "world": "Yum Yum Desert",
                "id": 67,
                "portalRequirements": [0]
            }),
        new MapDataBase("sheep", <MapDataModel>{
                "area": "Steep Sheep Ledge",
                "world": "Frostbite Tundra",
                "id": 101,
                "portalRequirements": [1000]
            }),
        new MapDataBase("flake", <MapDataModel>{
                "area": "Snowfield Outskirts",
                "world": "Frostbite Tundra",
                "id": 103,
                "portalRequirements": [2000]
            }),
        new MapDataBase("stache", <MapDataModel>{
                "area": "The Stache Split",
                "world": "Frostbite Tundra",
                "id": 104,
                "portalRequirements": [3000, 100000]
            }),
        new MapDataBase("bloque", <MapDataModel>{
                "area": "Refrigeration Station",
                "world": "Frostbite Tundra",
                "id": 105,
                "portalRequirements": [4000]
            }),
        new MapDataBase("mamoth", <MapDataModel>{
                "area": "Mamooooth Mountain",
                "world": "Frostbite Tundra",
                "id": 106,
                "portalRequirements": [6000]
            }),
        new MapDataBase("snowball", <MapDataModel>{
                "area": "Rollin' Tundra",
                "world": "Frostbite Tundra",
                "id": 107,
                "portalRequirements": [8000]
            }),
        new MapDataBase("penguin", <MapDataModel>{
                "area": "Signature Slopes",
                "world": "Frostbite Tundra",
                "id": 108,
                "portalRequirements": [11000]
            }),
        new MapDataBase("thermostat", <MapDataModel>{
                "area": "Thermonuclear Climb",
                "world": "Frostbite Tundra",
                "id": 109,
                "portalRequirements": [15000]
            }),
        new MapDataBase("glass", <MapDataModel>{
                "area": "Waterlogged Entrance",
                "world": "Frostbite Tundra",
                "id": 110,
                "portalRequirements": [18000]
            }),
        new MapDataBase("snakeB", <MapDataModel>{
                "area": "Cryo Catacombs",
                "world": "Frostbite Tundra",
                "id": 111,
                "portalRequirements": [22000]
            }),
        new MapDataBase("speaker", <MapDataModel>{
                "area": "Overpass of Sound",
                "world": "Frostbite Tundra",
                "id": 112,
                "portalRequirements": [35000]
            }),
        new MapDataBase("eye", <MapDataModel>{
                "area": "Crystal Basecamp",
                "world": "Frostbite Tundra",
                "id": 113,
                "portalRequirements": [120000]
            }),
        new MapDataBase("ram", <MapDataModel>{
                "area": "Wam Wonderland",
                "world": "Frostbite Tundra",
                "id": 116,
                "portalRequirements": [250000]
            }),
        new MapDataBase("skele2", <MapDataModel>{
                "area": "Hell Hath Frozen Over",
                "world": "Frostbite Tundra",
                "id": 117,
                "portalRequirements": [0]
            }),
        new MapDataBase("mushP", <MapDataModel>{
                "area": "Spaceway Raceway",
                "world": "Hyperion Nebula",
                "id": 151,
                "portalRequirements": [20000]
            }),
        new MapDataBase("w4a2", <MapDataModel>{
                "area": "TV Outpost",
                "world": "Hyperion Nebula",
                "id": 152,
                "portalRequirements": [30000]
            }),
        new MapDataBase("w4a3", <MapDataModel>{
                "area": "Donut Drive-In",
                "world": "Hyperion Nebula",
                "id": 153,
                "portalRequirements": [50000]
            }),
        new MapDataBase("demonP", <MapDataModel>{
                "area": "Outskirts of Fallstar Isle",
                "world": "Hyperion Nebula",
                "id": 154,
                "portalRequirements": [70000]
            }),
        new MapDataBase("w4b2", <MapDataModel>{
                "area": "Moutainous Deugh",
                "world": "Hyperion Nebula",
                "id": 155,
                "portalRequirements": [100000]
            }),
        new MapDataBase("w4b1", <MapDataModel>{
                "area": "Wurm Highway",
                "world": "Hyperion Nebula",
                "id": 156,
                "portalRequirements": [150000]
            }),
        new MapDataBase("w4b3", <MapDataModel>{
                "area": "Jelly Cube Bridge",
                "world": "Hyperion Nebula",
                "id": 157,
                "portalRequirements": [250000]
            }),
        new MapDataBase("w4b4", <MapDataModel>{
                "area": "Cocoa Tunnel",
                "world": "Hyperion Nebula",
                "id": 158,
                "portalRequirements": [500000]
            }),
        new MapDataBase("w4b5", <MapDataModel>{
                "area": "Standstill Plains",
                "world": "Hyperion Nebula",
                "id": 159,
                "portalRequirements": [700000]
            }),
        new MapDataBase("w4c1", <MapDataModel>{
                "area": "Shelled Shores",
                "world": "Hyperion Nebula",
                "id": 160,
                "portalRequirements": [1000000]
            }),
        new MapDataBase("w4c2", <MapDataModel>{
                "area": "The Untraveled Octopath",
                "world": "Hyperion Nebula",
                "id": 161,
                "portalRequirements": [2000000]
            }),
        new MapDataBase("w4c3", <MapDataModel>{
                "area": "Flamboyant Bayou",
                "world": "Hyperion Nebula",
                "id": 162,
                "portalRequirements": [3000000]
            }),
        new MapDataBase("w4c4", <MapDataModel>{
                "area": "Enclave of Eyes",
                "world": "Hyperion Nebula",
                "id": 163,
                "portalRequirements": [4000000]
            })    
]
}
