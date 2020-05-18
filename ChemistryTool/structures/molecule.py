from typing import Dict
from ..algorithms.abc import IsomorphismABC
from ..periodictable.element import Element
from collections import Counter
from .abc import MoleculeABC


class Molecule(IsomorphismABC, MoleculeABC):
    def __init__(self):
        self._atoms: Dict[int, Element] = {}
        self._bonds: Dict[int, Dict[int, int]] = {}
        self._backup_atoms: Dict[int, str] = {}
        self._backup_bonds: Dict[int, Dict[int, int]] = {}
        self._neighbors: Dict[int, int] = {}

    def get_atom(self, number: int) -> Element:
        return self._atoms[number]

    def get_bond(self, start_atom: int, end_atom: int) -> int:
        return self._bonds[start_atom][end_atom]

    def add_atom(self, element: Element, number: int):
        if isinstance(element, Element):
            if number in self._atoms:
                raise IndexError('This atom has already been added!')
            else:
                self._atoms[number] = element
                self._bonds[number] = {}
        else:
            raise TypeError('Object must be the element!')

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
            if start_atom == end_atom:
                raise ValueError('The atom cannot be bound to itself!')
            elif start_atom in self._bonds and end_atom in self._bonds[start_atom]:
                raise IndexError('The bond has already been added!')
            elif start_atom in self._bonds:
                self._bonds[start_atom][end_atom] = bond_type
                self._bonds[end_atom][start_atom] = bond_type
            else:
                self._bonds[start_atom] = {end_atom: bond_type}
                self._bonds[end_atom] = {start_atom: bond_type}

    def delete_atom(self, number: int):
        del self._atoms[number], self._bonds[number]
        for k, v in self._bonds.items():
            if number in v:
                del self._bonds[k][number]

    def delete_bond(self, start_atom: int, end_atom: int):
        try:
            del self._bonds[start_atom][end_atom]
            del self._bonds[end_atom][start_atom]
        except:
            print(("Could not delete bond between " + str(start_atom) +
                   " and " + str(end_atom) + "."))

    def update_atom(self, element: Element, number: int):
        if isinstance(element, Element):
            if number in self._atoms:
                self._atoms[number] = element
            else:
                print("This atom does not exist!")
        else:
            raise TypeError('Object must be the element!')

    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if start_atom in self._bonds and end_atom in self._bonds:
            self._bonds[start_atom][end_atom] = bond_type
            self._bonds[end_atom][start_atom] = bond_type
        else:
            print("This bond does not exist!")

    def plane_graph(self):
        atoms = self._atoms
        bonds = self._bonds
        start = 1
        seen = {start}
        freq = {'C': 8 / 3, 'O': 1}
        stack = [(m, start, b) for m, b in sorted(bonds[start].items(), reverse=True,
                                                  key=lambda k: (freq[atoms[k[0]]], -k[1]))]
        path = []
        closures = []

        while stack:
            current, previous, _ = move = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            path.append(move)

            for m, b in sorted(bonds[current].items(), reverse=True,
                               key=lambda k: (freq[atoms[k[0]]], -k[1])):
                if m == previous:
                    continue
                elif m in seen:
                    closures.append((current, m, b))
                else:
                    stack.append((m, current, b))
        return start, path, closures  # (3, [(2, 3, 2), (1, 2, 1), (4, 1, 1)], [(4, 3, 1)])

    def __enter__(self):
        self._backup_atoms = self._atoms.copy()
        self._backup_bonds = {}
        for k, v in self._bonds.items():
            self._backup_bonds[k] = v.copy()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is None:
            del self._backup_atoms
            del self._backup_bonds
        else:
            self._atoms = self._backup_atoms
            self._bonds = self._backup_bonds
            del self._backup_atoms
            del self._backup_bonds

    def __str__(self):
        f = dict(Counter(self._atoms))
        print('Gross formula: ')
        return ''.join(['{0}{1}'.format(k, v) for k, v in f.items()])

    def __repr__(self):
        return 'Molecule: atoms{}, bonds{}'.format(self._atoms, self._bonds)

__all__ = ['MoleculeABC']
