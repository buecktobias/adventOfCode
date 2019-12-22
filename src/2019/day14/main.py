# Created by Tobias Bück at 2019-12-14 18:58:42.987107
# Solution of day 14 of advent of Code 2019
#
import sys
from typing import List, Dict, Tuple
import utility  # helper methods
from math import ceil


class Molecule:
    molecules = set()

    def __init__(self, name):
        self.name = name
        self.molecules.add(self)

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class MoleculeSet:
    def __init__(self, molecule, amount):
        self.molecule = molecule
        self.amount = amount

    def __repr__(self):
        return f"{self.amount} {self.molecule}"


class Reaction:
    reactions = []

    def __init__(self, reaction_molecules: List[MoleculeSet], product: MoleculeSet):
        self.reaction_molecules = reaction_molecules
        self.product = product
        self.reactions.append(self)

    def has_product(self, product_name):
        return self.product.molecule.name == product_name

    def how_often_reaction_must_be_made_to_get(self, molecule, amount):
        assert self.product.molecule == molecule, f"Reaction can not produce {molecule}"
        return ceil(amount / self.product.amount)

    @classmethod
    def get_reactions_with_product(cls, product):
        return list(filter(lambda reaction: reaction.has_product(product), cls.reactions))

    def __repr__(self):
        return f"{self.reaction_molecules} => {self.product}"


def get_input_file():
    return open("../../../input/2019/test14")


def get_clean_data():
    with get_input_file() as input_file:
        lines_input_file = utility.get_lines_of_file(input_file)

    reactions = []
    for line in lines_input_file:
        in_molecules, out_molecule = line.split(" => ")
        in_molecules = in_molecules.split(", ")
        molecule_sets = []
        for molecule in in_molecules:
            amount, name = molecule.split(" ")
            amount = int(amount)
            molecule_sets.append(MoleculeSet(Molecule(name), amount))
        out_mol_amount, out_mol_name = out_molecule.split(" ")
        out_mol_amount = int(out_mol_amount)
        out_molecule = MoleculeSet(Molecule(out_mol_name), out_mol_amount)
        reaction = Reaction(molecule_sets, out_molecule)
        reactions.append(reaction)
    return reactions


def sum_dicts(dicts: List[Dict[Molecule, int]]):
    result_dict = dicts[0]
    for dict_ in dicts[1:]:
        for key in dict_:
            result_dict[key] += dict_[key]
    return result_dict


def make_reaction(reaction: Reaction, molecules_dict):
    for molecule_set in reaction.reaction_molecules:
        molecules_dict[molecule_set.molecule] -= molecule_set.amount

    molecules_dict[reaction.product.molecule] += reaction.product.amount
    return molecules_dict


def create_dictionary_with_zero_molecules():
    return {molecule: 0 for molecule in Molecule.molecules}


def calculate_cost_of_getting(molecule_set, reaction, leftovers):
    times = reaction.how_often_reaction_must_be_made_to_get(molecule_set.molecule, molecule_set.amount)
    return calculate_cost_of_making_reactions(reaction, leftovers, times=times), times


def calculate_cost_of_making_reactions(reaction, leftovers, times=1):
    # TODO times
    left_overs_copy = leftovers.copy()
    molecules_for_reaction = reaction.reaction_molecules
    dict_molecules = {}
    for molecule_set in molecules_for_reaction:
        dict_molecules[molecule_set.molecule] = molecule_set.amount

    total_cost = 0
    for key in dict_molecules.keys():
        amount_of_leftovers = leftovers[key]

        if amount_of_leftovers < dict_molecules[key]:
            tmp = dict_molecules[key]
            dict_molecules[key] -= amount_of_leftovers
            left_overs_copy[key] -= tmp
        else:
            tmp = dict_molecules[key]
            dict_molecules[key] = 0
            left_overs_copy[key] -= tmp

        molecule_set = MoleculeSet(key, dict_molecules[key])
        # really left overs copy ??? TODO
        cost, leftovers_of_molecule_set = amount_of_ore(molecule_set, left_overs_copy)
        total_cost += cost
        left_overs_copy = leftovers_of_molecule_set  # TODO not sure
    return total_cost


def amount_of_ore(molecule_set: MoleculeSet, leftovers: Dict[Molecule, int] = None) -> Tuple[int, Dict[Molecule, int]]:
    """
    @rtype: Tuple[int, Dict[Molecule, int]]
    @param molecule_set: The specific molecule of which the amount of ore should be find out.
    @param leftovers: All Molecules created
    @return: returns the amount of ore needed to create a specific molecule
    """
    if molecule_set.amount <= 0:
        return 0, leftovers

    if leftovers is None:
        leftovers = create_dictionary_with_zero_molecules()

    # Abbruchbedingung
    if molecule_set.molecule.name == "ORE":
        return molecule_set.amount, leftovers
    # ALle Reaktionen die dieses Molekül als Produkt haben.
    possible_reactions = Reaction.get_reactions_with_product(molecule_set.molecule.name)

    best_reaction_ore_consumption = sys.maxsize
    best_reaction = None
    best_reaction_leftovers = None
    for reaction in possible_reactions:

        reaction_tuple, times = calculate_cost_of_getting(molecule_set, reaction, leftovers)# DONE
        cost_of_reaction, leftovers_of_reaction = reaction_tuple
        if cost_of_reaction < best_reaction_ore_consumption:  # DONE
            best_reaction = reaction
            best_reaction_ore_consumption = cost_of_reaction
            best_reaction_leftovers = leftovers_of_reaction

    # TODO make reaction multiple times !!
    make_reaction(best_reaction, best_reaction_leftovers)
    return best_reaction_ore_consumption, leftovers


def part1():
    reactions = get_clean_data()
    print(reactions[0])
    molecules_dict = create_dictionary_with_zero_molecules()
    molecules_dict[Molecule("ORE")] = 5
    print(calculate_cost_of_making_reactions(reactions[0], molecules_dict))


def part2():
    lines = get_clean_data()


def main():
    part1()


if __name__ == '__main__':
    main()
