from pprint import pprint
from opentrons import protocol_api
import json
from pathlib import Path
from collections import defaultdict
from opentrons.types import Point

# metadata
metadata = {
    "protocolName": "MR-01-003-G24J-01",
    "author": "Manahill Rabbani <m.rabbani23@imperial.ac.uk>",
    "description": "MR-01-003-G24J",
    "apiLevel": "2.9",
}

move_commands = [
    {
        "substance": "TriG",
        "location": [
            "A1",
            "A2",
            "A3",
            "A4",
            "A5",
            "A6",
            "A7",
            "A8",
            "B1",
            "B2",
            "B3",
            "B4"
        ],
        "amount": 59.7,
        "plate": "4"
    },
    {
        "substance": "TriJ",
        "location": [
            "A1",
            "A2",
            "A3",
            "A4",
            "A5",
            "A6",
            "A7",
            "A8",
            "B1",
            "B2",
            "B3",
            "B4"
        ],
        "amount": 121.2,
        "plate": "4"
    },
    {   
        "substance": "Di17",
        "amount": 66.4,
        "plate": "4",
        "location": [
            "A1"
        ]
    },
    {
        "substance": "Di18",
        "amount": 112.8,
        "plate": 4,
        "location": [
            "A2"
        ]
    },
    {   
        "substance": "Di23",
        "amount": 126.1,
        "plate": "4",
        "location": [
            "A3"
        ]
    },
    {   
        "substance": "Di24",
        "amount": 126.1,
        "plate": "4",
        "location": [
            "A4"
        ]
    },
    {   
        "substance": "Di25",
        "amount": 237.8,
        "plate": "4",
        "location": [
            "A5"
        ]
    },
    {   
        "substance": "Di26",
        "amount": 128.3,
        "plate": "4",
        "location": [
            "A6"
        ]
    },
    {   
        "substance": "Di27",
        "amount": 150.4,
        "plate": "4",
        "location": [
            "A7"
        ]
    },
    {   
        "substance": "Di28",
        "amount": 157.0,
        "plate": "4",
        "location": [
            "A8"
        ]
    },
    {   
        "substance": "Di29",
        "amount": 160.4,
        "plate": "4",
        "location": [
            "B1"
        ]
    },
    {   
        "substance": "Di30",
        "amount": 115.0,
        "plate": "4",
        "location": [
            "B2"
        ]
    },
    {   
        "substance": "Di31",
        "amount": 150.4,
        "plate": "4",
        "location": [
            "B3"
        ]
    },
    {   
        "substance": "Di32",
        "amount": 99.5,
        "plate": "4",
        "location": [
            "B4"
        ]
    },
    {
        "substance": "Chloroform",
        "location": [
            "A1"
        ],
        "amount": 752.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A2"
        ],
        "amount": 706.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A3"
        ],
        "amount": 693.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A4"
        ],
        "amount": 693.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A5"
        ],
        "amount": 581.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A6"
        ],
        "amount": 690.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A7"
        ],
        "amount": 668.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A8"
        ],
        "amount": 662.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B1"
        ],
        "amount": 658.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B2"
        ],
        "amount": 704.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B3"
        ],
        "amount": 668.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B4"
        ],
        "amount": 719.6,
        "plate": "4"
    }
]

substance_locations = {
    "3": {
        "name": "Stock",
        "type": "analyticalsales_24_wellplate_80000ul",
        "A1": {
            "substance": "TriG",
            "amount": 3000
        },
        "A2": {
            "substance": "Di17",
            "amount": 2000
        },
        "A3": {
            "substance": "Di18",
            "amount": 2000
        },
        "A4": {
            "substance": "Di23",
            "amount": 2000
        },
        "A5": {
            "substance": "Di24",
            "amount": 2000
        },
        "A6": {
            "substance": "Di25",
            "amount": 2000
        },
        "B1": {
            "substance": "Di26",
            "amount": 2000
        },
        "B2": {
            "substance": "Di27",
            "amount": 2000
        },
        "B3": {
            "substance": "Di28",
            "amount": 2000
        },
        "B4": {
            "substance": "Di29",
            "amount": 2000
        },
        "B5": {
            "substance": "Di30",
            "amount": 2000
        },
        "B6": {
            "substance": "Di31",
            "amount": 2000
        },
        "C1": {
            "substance": "Di32",
            "amount": 2000
        },
        "C2": {
            "substance": "TriJ",
            "amount": 3000
        },
    },
    "5": {
        "name": "Solvent",
        "type": "fisher_6_wellplate_25000ul",
        "A1": {
            "substance": "Chloroform",
            "amount": 20000
        },
        "A2": {
            "substance":"Chloroform",
            "amount": 20000
        },
        "A3": {
            "substance":"Chloroform",
            "amount": 20000
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
