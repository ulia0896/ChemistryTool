from abc import ABC, abstractmethod
from ...algorithms.abc import IsomorphismABC
from ...periodictable.element import Element

class MoleculeABC(IsomorphismABC, ABC):
    def __init__(self):
       ...

    @abstractmethod
    def get_atom(self, number: int) -> Element:
        ...

    @abstractmethod
    def get_bond(self, start_atom: int, end_atom: int) -> int:
        ...

    @abstractmethod
    def add_atom(self, element: Element, number: int):
        ...

    @abstractmethod
    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        ...

    @abstractmethod
    def delete_atom(self, number: int):
        ...

    @abstractmethod
    def delete_bond(self, start_atom: int, end_atom: int):
        ...

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
        ...


__all__ = ['MoleculeABC']
