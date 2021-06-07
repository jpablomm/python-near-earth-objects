"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    # def __init__(self, designation: str, name: str = None, diameter='nan', hazardous: bool = False):
    with open(neo_csv_path) as infile:
        reader = csv.DictReader(infile)
        neo_list = []
        for approach in reader:
            neo = NearEarthObject(
                designation=approach['pdes'],
                name=(approach['name'] if approach['name'] else None),
                diameter=(approach['diameter'] if approach['diameter'] else 'nan'),
                hazardous=(True if approach['pha']=='Y' else False))
            neo_list.append(neo)
    return neo_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    # def __init__(self, designation: str, time: str = None, distance: float = 0.0, velocity: float = 0.0, neo=None):
    with open(cad_json_path) as infile:
        data = json.load(infile)
        cad_list = []
        for cad in data['data']:
            cad = CloseApproach(cad[0], cad[3], float(cad[4]), float(cad[7]))
            cad_list.append(cad)
    return cad_list
