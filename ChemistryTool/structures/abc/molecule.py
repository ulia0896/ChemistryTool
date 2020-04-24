from abc import ABC, abstractmethod
from typing import Dict
from ...algorithms.abc import IsomorphismABC
from ...periodictable.element import Element
from collections import Counter


class MoleculeABC(IsomorphismABC, ABC):
    def __init__(self):
        self._atoms: Dict[int, str] = {}
        self._bonds: Dict[int, Dict[int, int]] = {}
        self._backup_atoms: Dict[int, str] = {}
        self._backup_bonds: Dict[int, Dict[int, int]] = {}
        self._neighbors: Dict[int, int] = {}

    @abstractmethod
    def get_atom(self, number: int) -> Element:
        ...

    @abstractmethod
    def get_bond(self, start_atom: int, end_atom: int) -> int:
        ...

    @abstractmethod
    def add_atom(self, element: Element, number: int):
        if number in self._atoms:
            raise IndexError('This atom has already been added!')
        else:
            self._atoms[number] = element
            self._bonds[number] = {}

    @abstractmethod
    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if start_atom == end_atom:
            raise ValueError('The atom cannot be bound to itself!')
        elif start_atom in self._bonds and end_atom in self._bonds[start_atom]:
            raise IndexError('The bond has already been added!')
        elif start_atom in self._bonds:




    @abstractmethod
    def delete_atom(self, number: int):
        ...

    @abstractmethod
    def delete_bond(self, start_atom: int, end_atom: int):
        old_bonds = self._bonds[number]
        try:
            old_bonds[start_atom][end_atom] = 0
            old_bonds[end_atom][start_atom] = 0
        except:
            print(("Could not delete bond between " + str(start_atom) +
                   " and " + str(end_atom) + "."))

    @abstractmethod
    def update_atom(self, element: Element, number: int):
        ...

    @abstractmethod
    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        ...

    @abstractmethod
    def __enter__(self):
        return self
        # todo: make backup of internal data
        ...

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        # todo: restore internal data in exception case.
        self._atoms = self._backup_atoms
        self._bonds = self._backup_bonds
        del self._backup_atoms
        del self._backup_bonds

    @abstractmethod
    def __str__(self):
        f = Counter(self._atoms)
        if isinstance (f, str):


        # todo:  brutto formula
        ...


__all__ = ['MoleculeABC']
