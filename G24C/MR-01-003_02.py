from pprint import pprint
from opentrons import protocol_api
import json
from pathlib import Path
from collections import defaultdict
from opentrons.types import Point

# metadata
metadata = {
    "protocolName": "MR-01-003-G24C-02",
    "author": "Manahill Rabbani <m.rabbani23@imperial.ac.uk>",
    "description": "MR-01-004-01",
    "apiLevel": "2.9",
}

move_commands = [
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "A1",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "A2",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "A3",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "A4",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "A5",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "A6",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "A7",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "A8",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "B1",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "B2",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "B3",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "B4",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "B5",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "B6",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "B7",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "B8",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "C1",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "C2",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "C3",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "C4",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "C5",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "C6",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "C7",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "C8",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "D1",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "D2",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "D3",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "D4",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "D5",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "D6",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "D7",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "D8",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "E1",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "E2",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "E3",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "E4",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "E5",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "E6",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "E7",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "E8",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "F1",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "F2",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "F3",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "F4",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "F5",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "F6",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "F7",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 256.9,
        "plate": 4,
        "location": [
            "F8",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "A1",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "A2",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "A3",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "A4",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "A5",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "A6",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "A7",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "A8",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "B1",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "B2",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "B3",
        ]
    },
    {
        "substance": "TriB",
        "amount": 53.9,
        "plate": 4,
        "location": [
            "B4",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "B5",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "B6",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "B7",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "B8",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "C1",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "C2",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "C3",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "C4",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "C5",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "C6",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "C7",
        ]
    },
    {
        "substance": "TriC",
        "amount": 38.0,
        "plate": 4,
        "location": [
            "C8",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "D1",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "D2",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "D3",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "D4",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "D5",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "D6",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "D7",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "D8",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "E1",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "E2",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "E3",
        ]
    },
    {
        "substance": "TriD",
        "amount": 64.8,
        "plate": 4,
        "location": [
            "E4",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "E5",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "E6",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "E7",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "E8",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "F1",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "F2",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "F3",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "F4",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "F5",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "F6",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "F7",
        ]
    },
    {
        "substance": "TriE",
        "amount": 49.0,
        "plate": 4,
        "location": [
            "F8",
        ]
    },
    {
        "substance": "Di17",
        "amount": 46.9,
        "plate": 4,
        "location": [
            "A1",
        ]
    },
    {
        "substance": "Di17",
        "amount": 46.9,
        "plate": 4,
        "location": [
            "B5",
        ]
    },
    {
        "substance": "Di17",
        "amount": 46.9,
        "plate": 4,
        "location": [
            "D1",
        ]
    },
    {
        "substance": "Di17",
        "amount": 46.9,
        "plate": 4,
        "location": [
            "E5",
        ]
    },
    {
        "substance": "Di18",
        "amount": 79.7,
        "plate": 4,
        "location": [
            "A2",
        ]
    },
    {
        "substance": "Di18",
        "amount": 79.7,
        "plate": 4,
        "location": [
            "B6",
        ]
    },
    {
        "substance": "Di18",
        "amount": 79.7,
        "plate": 4,
        "location": [
            "D2",
        ]
    },
    {
        "substance": "Di18",
        "amount": 79.7,
        "plate": 4,
        "location": [
            "E6",
        ]
    },
    {
        "substance": "Di23",
        "amount": 89.1,
        "plate": 4,
        "location": [
            "A3",
        ]
    },
    {
        "substance": "Di23",
        "amount": 89.1,
        "plate": 4,
        "location": [
            "B7",
        ]
    },
    {
        "substance": "Di23",
        "amount": 89.1,
        "plate": 4,
        "location": [
            "D3",
        ]
    },
    {
        "substance": "Di23",
        "amount": 89.1,
        "plate": 4,
        "location": [
            "E7",
        ]
    },
    {
        "substance": "Di24",
        "amount": 89.1,
        "plate": 4,
        "location": [
            "A4",
        ]
    },
    {
        "substance": "Di24",
        "amount": 89.1,
        "plate": 4,
        "location": [
            "B8",
        ]
    },
    {
        "substance": "Di24",
        "amount": 89.1,
        "plate": 4,
        "location": [
            "D4",
        ]
    },
    {
        "substance": "Di24",
        "amount": 89.1,
        "plate": 4,
        "location": [
            "E8",
        ]
    },
    {   
        "substance": "Di25",
        "amount": 168.0,
        "plate": "4",
        "location": [
            "A5",
            "C1",
            "D5",
            "F1"
        ]
    },
    {   
        "substance": "Di26",
        "amount": 90.6,
        "plate": "4",
        "location": [
            "A6",
            "C2",
            "D6",
            "F2"
        ]
    },
    {   
        "substance": "Di27",
        "amount": 106.2,
        "plate": "4",
        "location": [
            "A7",
            "C3",
            "D7",
            "F3"
        ]
    },
    {   
        "substance": "Di28",
        "amount": 111.0,
        "plate": "4",
        "location": [
            "A8",
            "C4",
            "D8",
            "F4"
        ]
    },
    {   
        "substance": "Di29",
        "amount": 113.3,
        "plate": "4",
        "location": [
            "B1",
            "C5",
            "E1",
            "F5"
        ]
    },
    {   
        "substance": "Di30",
        "amount": 81.2,
        "plate": "4",
        "location": [
            "B2",
            "C6",
            "E2",
            "F6"
        ]
    },
    {   
        "substance": "Di31",
        "amount": 106.2,
        "plate": "4",
        "location": [
            "B3",
            "C7",
            "E3",
            "F7"
        ]
    },
    {   
        "substance": "Di32",
        "amount": 70.3,
        "plate": "4",
        "location": [
            "B4",
            "C8",
            "E4",
            "F8"
        ]
    },
    {
        "substance": "Chloroform",
        "location": [
            "A1"
        ],
        "amount": 642.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A2"
        ],
        "amount": 609.5,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A3"
        ],
        "amount": 600.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A4"
        ],
        "amount": 600.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A5"
        ],
        "amount": 521.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A6"
        ],
        "amount": 598.6,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A7"
        ],
        "amount": 583.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A8"
        ],
        "amount": 578.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B1"
        ],
        "amount": 575.9,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B2"
        ],
        "amount": 608.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B3"
        ],
        "amount": 583.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B4"
        ],
        "amount": 618.9,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B5"
        ],
        "amount": 658.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B6"
        ],
        "amount": 625.4,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B7"
        ],
        "amount": 616.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B8"
        ],
        "amount": 616.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C1"
        ],
        "amount": 537.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C2"
        ],
        "amount": 614.4,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C3"
        ],
        "amount": 598.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C4"
        ],
        "amount": 594.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C5"
        ],
        "amount": 591.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C6"
        ],
        "amount": 623.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C7"
        ],
        "amount": 598.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C8"
        ],
        "amount": 634.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D1"
        ],
        "amount": 631.4,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D2"
        ],
        "amount": 598.6,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D3"
        ],
        "amount": 589.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D4"
        ],
        "amount": 589.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D5"
        ],
        "amount": 510.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D6"
        ],
        "amount": 587.6,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D7"
        ],
        "amount": 572.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D8"
        ],
        "amount": 567.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E1"
        ],
        "amount": 565.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E2"
        ],
        "amount": 597.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E3"
        ],
        "amount": 572.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E4"
        ],
        "amount": 608.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E5"
        ],
        "amount": 647.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E6"
        ],
        "amount": 614.4,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E7"
        ],
        "amount": 605.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E8"
        ],
        "amount": 605.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F1"
        ],
        "amount": 526.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F2"
        ],
        "amount": 603.5,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F3"
        ],
        "amount": 587.9,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F4"
        ],
        "amount": 583.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F5"
        ],
        "amount": 580.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F6"
        ],
        "amount": 612.9,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F7"
        ],
        "amount": 587.9,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F8"
        ],
        "amount": 623.8,
        "plate": "4"
    }
]

substance_locations = {
    "3": {
        "name": "Stock",
        "type": "analyticalsales_24_wellplate_80000ul",
        "A1": {
            "substance": "TriJ",
            "amount": 13000
        },
        "A2": {
            "substance": "TriB",
            "amount": 2000
        },
        "A3": {
            "substance": "TriC",
            "amount": 2000
        },
        "A4": {
            "substance": "TriD",
            "amount": 2000
        },
        "A5": {
            "substance": "TriE",
            "amount": 2000
        },
        "A6": {
            "substance": "Di17",
            "amount": 2000
        },
        "B1": {
            "substance": "Di18",
            "amount": 2000
        },
        "B2": {
            "substance": "Di23",
            "amount": 2000
        },
        "B3": {
            "substance": "Di24",
            "amount": 2000
        },
        "B4": {
            "substance": "Di25",
            "amount": 2000
        },
        "B5": {
            "substance": "Di26",
            "amount": 2000
        },
        "B6": {
            "substance": "Di27",
            "amount": 2000
        },
        "C1": {
            "substance": "Di28",
            "amount": 2000
        },
        "C2": {
            "substance": "Di29",
            "amount": 2000
        },
        "C3": {
            "substance": "Di30",
            "amount": 2000
        },
        "C4": {
            "substance": "Di31",
            "amount": 2000
        },
        "C5": {
            "substance": "Di32",
            "amount": 2000
        },
    },
    "5": {
        "name": "Solvent",
        "type": "fisher_6_wellplate_25000ul",
        "A1": {
            "substance": "Chloroform",
            "amount": 25000
        },
        "A2": {
            "substance":"Chloroform",
            "amount": 30000
        }
        }
}

class Opentrons:
    def __init__(
        self,
        protocol: protocol_api.ProtocolContext,
        deck_info: dict,
    ):
        """
        Initialise the Opentrons object.

        Parameters
        ----------
        protocol : protocol_api.ProtocolContext
            The protocol context for the current protocol.
        deck_info : dict
            Dictionary of deck information.
            Contains information of substances and their quantities on the deck.

        Returns
        -------
        None
        """
        # Set gantry speeds
        self.protocol = protocol
        self.protocol.max_speeds["X"] = 220
        self.protocol.max_speeds["Y"] = 220
        self.protocol.max_speeds["Z"] = 220

        # TODO: Add dynamic loading of labware
        # self.tiprack1000 = self.protocol.load_labware(
        #     "opentrons_96_tiprack_1000ul", 1
        # )
        self.tiprack300 = self.protocol.load_labware(
            "opentrons_96_tiprack_300ul", 2
        )
        self.plate = self.protocol.load_labware(
            "analyticalsales_48_wellplate_2000ul", 4
        )
        self.labware = {}
        self.labware[4] = self.plate
        # self.labware[1] = self.tiprack1000
        self.labware[2] = self.tiprack300
        # Add substances to the deck
        for deck_number in deck_info:
            self.labware[int(deck_number)] = self.protocol.load_labware(
                deck_info[deck_number]["type"], int(deck_number)
            )
        # Delete name and type from deck_info
        for deck_number in deck_info:
            del deck_info[deck_number]["type"]
            del deck_info[deck_number]["name"]
        # Loading pipettes
        # self.right_pipette = self.protocol.load_instrument(
            # "p1000_single_gen2", "right", tip_racks=[self.tiprack1000]
        # )
        self.left_pipette = protocol.load_instrument(
            "p300_single_gen2", "left", tip_racks=[self.tiprack300]
        )
        # self.right_pipette.flow_rate.aspirate = 40
        # self.right_pipette.flow_rate.dispense = 40
        self.left_pipette.flow_rate.aspirate = 60
        self.left_pipette.flow_rate.dispense = 60
        self.left_pipette.swelled = False
        # self.right_pipette.swelled = False
        # For tracking substance amounts
        self.substances = defaultdict(list)
        for position in deck_info:
            position_int = int(position)
            for well_plate in deck_info[position]:
                substance_position = self.labware[position_int][well_plate]
                substance = deck_info[position][well_plate]
                substance_name = substance["substance"]
                amount = substance["amount"]
                self.substances[substance_name].append(
                    {
                        "position": substance_position,
                        "amount": amount,
                    }
                )

    def swell_tip(self, pipette, position):
        """
        Swells the tip in the `stock` labware location at a specified location.

        Notes
        -----
        Perform before a pipette is used for transfer.

        Parameters
        ----------
        pipette : pipette
            The pipette to be used.

        position:
            Position to swell the tip in.

        Returns
        -------
        None

        """
        for i in range(1):
            pipette.aspirate(100, position)
            self.protocol.delay(10)
            pipette.move_to(position.top())
            pipette.dispense(100, location=position)
        pipette.swelled = True

    def move_without_drip(self, position_to, position_from, pipette, amount):
        """
        Transfers substance from one location to another without dripping (hopefully).

        Notes
        -----
        Ideally, the swell function will be used before this function is called to reduce the
        probability of drips.

        Parameters
        ----------
        position_to: position
            Location of the target well plates to move substance to.
        position_from: position
            Location of the source well plates to move substance from.
        amount: float or int
            Amount of substance to be moved. (in uL)


        Returns
        -------
        None

        """
        # Check if pipette swelled before movement
        pipette.aspirate(amount, position_from)
        pipette.air_gap(15)
        pipette.dispense(location=position_to.top(z=2))

    def move_substance(self, amount, substance_name, position_to, pipette):
        """
        Moves a specified amount of substance from one location to another.

        Parameters
        ----------
        amount : float or int
            Amount of substance to be moved. (in mL)
        substance_name : str
            Name of the substance to be moved.
        position_to: position
            Location of the target well plates to move substance to.
        pipette: pipette
            The pipette to be used.
        value:

        Returns
        -------
        None

        """
        # Find the deck location of the substance
        try:
            substance_position = self.substances[substance_name][0]["position"]
        except:
            pprint(self.substances)
            print(f"Substance {substance_name} not found.")
            raise RuntimeError(
                f"Substance not found in deck. This could be due to the deck being empty, or the amount of {substance_name} needed exceeding the amount placed on the deck."
            )

        # Perform swelling
        if pipette.swelled != substance_name:
            self.swell_tip(
                pipette=pipette,
                position=substance_position,
            )
            pipette.swelled = substance_name
            # Check to see if amount of substance is greater than the amount on the deck
        minimum_volume = 400
        if amount > (
            self.substances[substance_name][0]["amount"] - minimum_volume
        ):
            print(
                f"Amount of {substance_name} needed is greater than the amount on the deck.\n"
                f"Trying again to move after changing the well plate to movw from of {substance_name}."
            )
            # Change the well plate to move from
            self.substances[substance_name].pop(0)
            if len(self.substances[substance_name]) == 0:
                raise RuntimeError(
                    f"No more {substance_name} left on the deck. Please check the deck and try again."
                )
            self.move_substance(
                amount=amount,
                substance_name=substance_name,
                position_to=position_to,
                pipette=pipette,
            )

        assert pipette.swelled == substance_name
        # Get amount left on deck
        # amount_left = self.substances[substance_name][0]["amount"]
        # Change well bottom clearance to prevent pipette touching the solvent
        # aspirate_loc = substance_position.bottom()
        # aspirate_loc = aspirate_loc.move(
        #     Point(0, 0, -aspirate_loc.point.z + 1)
        # )
        self.move_without_drip(
            pipette=pipette,
            position_to=position_to,
            position_from=substance_position,
            amount=amount,
        )
        self.substances[substance_name][0]["amount"] -= amount


def run(protocol: protocol_api.ProtocolContext):
    """
    Run the protocol.
    """

    amount_added = defaultdict(lambda: 0)
    substance_path = substance_locations
    move_path = move_commands
    # Check if root in the directory
    #if not substance_path.is_file():
    #    substance_path = Path("/root/Opentrons_Code/AB-02-007/Plate2/substance_locations.json")
    #    move_path = Path("/root/Opentrons_Code/AB-02-007/Plate2/move_commands.json")

    #with open(str(substance_path)) as f:
    #    deck_info = json.load(f)
    ot = Opentrons(protocol=protocol, deck_info=substance_locations)

    #with open(str(move_path)) as f:
    #    move_info = json.load(f)

    # Extract list of moves from the move information
    moves = []
    for substance in move_commands:
        for location in substance["location"]:
            moves.append(
                {
                    "substance": substance["substance"],
                    "location": location,
                    "amount": substance["amount"],
                    "plate": substance["plate"],
                }
            )
    added_substances = []
    positions_added = defaultdict(str)
    pipette_max_volume = 220
    for move in moves:
        location = move["location"]
        amount = int(move["amount"])
        plate = int(move["plate"])
        substance = move["substance"]
        # Get target well location
        target_well = ot.labware[plate].wells(location)[0]
        # Add the first substance to the list
        num_moves = amount // pipette_max_volume
        added = 0
        if len(added_substances) == 0:
            ot.left_pipette.pick_up_tip()
            added_substances.append(substance)
        # Check if substance matches the last substance added
        elif substance != added_substances[-1]:
            # Get a new tip
            ot.left_pipette.drop_tip()
            ot.left_pipette.pick_up_tip()
            added_substances.append(substance)
        for i in range(num_moves + 1):
            # Check if move is the last move
            if i == num_moves:
                amount_to_add = amount - added
            else:
                amount_to_add = pipette_max_volume
            if amount_to_add == 0:
                continue
            ot.move_substance(
                amount=amount_to_add,
                substance_name=substance,
                position_to=target_well,
                pipette=ot.left_pipette,
            )
            added += amount_to_add
            amount_added[location] += amount_to_add
        positions_added[location] += substance + " "
    for line in protocol.commands():
        continue
    pprint(amount_added)
    pprint(positions_added)
