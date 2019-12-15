# Created by Tobias Bück at 2019-12-14 18:58:42.987107
# Solution of day 14 of advent of Code 2019
# 
# INPUTS
from typing import List

import utility     # helper methods


class Molecule:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


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
        Reaction.reactions.append(self)

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


def has_reaction_product(reaction, product):
    return reaction.product.molecule.name == product


def get_reactions_with_product(product):
    return list(filter(lambda reaction: has_reaction_product(reaction, product), Reaction.reactions))


def amount_of_ore(reaction):
    if len(reaction.reaction_molecules) == 1 and reaction.reaction_molecules[0].molecule.name == "ORE":
        return reaction.reaction_molecules[0].amount / reaction.product.amount  # TODO product amount

    result = 0
    for molecule_set in reaction.reaction_molecules:
        molecule_reactions = get_reactions_with_product(molecule_set.molecule.name)
        cheapest_ore_reaction = min(molecule_reactions, key=lambda _reaction: amount_of_ore(_reaction))
        result += molecule_set.amount * amount_of_ore(cheapest_ore_reaction)
    return result


def part1():
    reactions = get_clean_data()
    fuel_reactions = get_reactions_with_product("FUEL")
    print(fuel_reactions)
    print(amount_of_ore(fuel_reactions[0]))


def part2():
    lines = get_clean_data()


def main():
    part1()


if __name__ == '__main__':
    main()
