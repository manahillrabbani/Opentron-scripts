from pprint import pprint
from opentrons import protocol_api
import json
from pathlib import Path
from collections import defaultdict
from opentrons.types import Point

# metadata
metadata = {
    "protocolName": "MR-01-003-C14-04",
    "author": "Manahill Rabbani <m.rabbani23@imperial.ac.uk>",
    "description": "MR-01-003-12",
    "apiLevel": "2.9",
}

move_commands = [
    {
        "substance": "TriE",
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
            "B4",
            "B5",
            "B6",
            "B7",
            "B8",
            "C1",
            "C2",
            "C3",
            "C4",
            "C5",
            "C6",
            "C7",
            "C8",
            "D1",
            "D2",
            "D3",
            "D4",
            "D5",
            "D6",
            "D7",
            "D8",
            "E1",
            "E2",
            "E3",
            "E4",
            "E5",
            "E6",
            "E7",
            "E8",
            "F1",
            "F2",
            "F3",
            "F4",
            "F5"
        ],
        "amount": 138.6,
        "plate": "4"
    },
    
    {   
        "substance": "Di1",
        "amount": 74.0,
        "plate": "4",
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
            "B3"
        ]
    },
    {   
        "substance": "Di2",
        "amount": 113.8,
        "plate": "4",
        "location": [
            "B4",
            "B5",
            "B6",
            "B7",
            "B8",
            "C1",
            "C2",
            "C3",
            "C4",
            "C5"

        ]
    },
    {   
        "substance": "Di3",
        "amount": 108.3,
        "plate": "4",
        "location": [
            "C6",
            "C7",
            "C8",
            "D1",
            "D2",
            "D3",
            "D4",
            "D5",
            "D6"
        ]
    },
    {   
        "substance": "Di4",
        "amount": 74.0,
        "plate": "4",
        "location": [
            "D7",
            "D8",
            "E1",
            "E2",
            "E3",
            "E4",
            "E5",
            "E6"

        ]
    },
    {   
        "substance": "Di5",
        "amount": 113.8,
        "plate": "4",
        "location": [
            "E7",
            "E8",
            "F1",
            "F2",
            "F3",
            "F4",
            "F5",
        ]
    },


    {
        "substance": "Di2",
        "amount": 113.8,
        "plate": 4,
        "location": [
            "A1"
        ]
    },
    {
        "substance": "Di3",
        "amount": 108.3,
        "plate": 4,
        "location": [
            "A2",
            "B4"
        ]
    },
    {
        "substance": "Di4",
        "amount": 74.0,
        "plate": 4,
        "location": [
            "A3",
            "B5",
            "C6"

        ]
    },
    {
        "substance": "Di5",
        "amount": 113.8,
        "plate": 4,
        "location": [
            "A4",
            "B6",
            "C7",
            "D7"
        ]
    },
    {
        "substance": "Di6",
        "amount": 116.0,
        "plate": 4,
        "location": [
            "A5",
            "B7",
            "C8",
            "D8",
            "E7"
        ]
    },
    {
        "substance": "Di7",
        "amount": 129.3,
        "plate": 4,
        "location": [
            "A6",
            "B8",
            "D1",
            "E1",
            "E8"
        ]
    },
    {
        "substance": "Di8",
        "amount": 130.4,
        "plate": 4,
        "location": [
            "A7",
            "C1",
            "D2",
            "E2",
            "F1"
        ]
    },
    {
        "substance": "Di9",
        "amount": 77.4,
        "plate": 4,
        "location": [
            "A8",
            "C2",
            "D3",
            "E3",
            "F2"
        ]
    },
    {
        "substance": "Di10",
        "amount": 74.0,
        "plate": 4,
        "location": [
            "B1",
            "C3",
            "D4",
            "E4",
            "F3"
        ]
    },
    {
        "substance": "Di14",
        "amount": 103.9,
        "plate": 4,
        "location": [
            "B2",
            "C4",
            "D5",
            "E5",
            "F4"
        ]
    },
    {
        "substance": "Di15",
        "amount": 156.9,
        "plate": 4,
        "location": [
            "B3",
            "C5",
            "D6",
            "E6",
            "F5"
        ]
    },


    {
        "substance": "Chloroform",
        "location": [
            "A1"
        ],
        "amount": 673.5,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A2"
        ],
        "amount": 679.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A3"
        ],
        "amount": 713.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A4"
        ],
        "amount": 673.6,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A5"
        ],
        "amount": 671.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A6"
        ],
        "amount": 658.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A7"
        ],
        "amount": 657.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A8"
        ],
        "amount": 710.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B1"
        ],
        "amount": 713.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B2"
        ],
        "amount": 683.5,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B3"
        ],
        "amount": 630.4,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B4"
        ],
        "amount": 639.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B5"
        ],
        "amount": 673.5,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B6"
        ],
        "amount": 633.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B7"
        ],
        "amount": 631.5,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B8"
        ],
        "amount": 618.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C1"
        ],
        "amount": 617.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C2"
        ],
        "amount": 670.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C3"
        ],
        "amount": 673.5,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C4"
        ],
        "amount": 643.7,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C5"
        ],
        "amount": 590.6,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C6"
        ],
        "amount": 679.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C7"
        ],
        "amount": 639.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C8"
        ],
        "amount": 637.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D1"
        ],
        "amount": 623.8,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D2"
        ],
        "amount": 622.7,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D3"
        ],
        "amount": 675.7,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D4"
        ],
        "amount": 679.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D5"
        ],
        "amount": 649.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D6"
        ],
        "amount": 596.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D7"
        ],
        "amount": 673.6,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D8"
        ],
        "amount": 671.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E1"
        ],
        "amount": 658.1,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E2"
        ],
        "amount": 657.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E3"
        ],
        "amount": 710.0,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E4"
        ],
        "amount": 713.3,
        "plate": "4"
    },    {
        "substance": "Chloroform",
        "location": [
            "E5"
        ],
        "amount": 683.5,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E6"
        ],
        "amount": 630.4,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E7"
        ],
        "amount": 631.6,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E8"
        ],
        "amount": 618.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F1"
        ],
        "amount": 617.2,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F2"
        ],
        "amount": 670.3,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F3"
        ],
        "amount": 673.6,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F4"
        ],
        "amount": 643.7,
        "plate": "4"
    },    
    {
        "substance": "Chloroform",
        "location": [
            "F5"
        ],
        "amount": 590.7,
        "plate": "4"
    },

]

substance_locations = {
    "3": {
        "name": "Stock",
        "type": "analyticalsales_24_wellplate_80000ul",
        "A1": {
            "substance": "TriB",
            "amount": 10000
        },
        "A2": {
            "substance": "TriC",
            "amount": 5000
        },
        "A3": {
            "substance": "TriD",
            "amount": 5000
        },
        "A4": {
            "substance": "TriE",
            "amount": 8000
        },
        "A5": {
            "substance": "Di1",
            "amount": 2000
        },
        "A6": {
            "substance": "Di2",
            "amount": 2000
        },
        "B1": {
            "substance": "Di3",
            "amount": 2000
        },
        "B2": {
            "substance": "Di4",
            "amount": 2000
        },
        "B3": {
            "substance": "Di5",
            "amount": 2000
        },
        "B4": {
            "substance": "Di6",
            "amount": 2000
        },
        "B5": {
            "substance": "Di7",
            "amount": 2000
        },
        "B6": {
            "substance": "Di8",
            "amount": 2000
        },
        "C1": {
            "substance": "Di9",
            "amount": 2000
        },
        "C2": {
            "substance": "Di10",
            "amount": 2000
        },
        "C3": {
            "substance": "Di14",
            "amount": 2000
        },
        "C4": {
            "substance": "Di15",
            "amount": 2000
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
        # self.left_pipette = self.protocol.load_instrument(
            # "p1000_single_gen2", "left", tip_racks=[self.tiprack1000]
        # )
        self.left_pipette = protocol.load_instrument(
            "p300_single_gen2", "left", tip_racks=[self.tiprack300]
        )
        # self.left_pipette.flow_rate.aspirate = 40
        # self.left_pipette.flow_rate.dispense = 40
        self.left_pipette.flow_rate.aspirate = 60
        self.left_pipette.flow_rate.dispense = 60
        self.left_pipette.swelled = False
        # self.left_pipette.swelled = False
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
