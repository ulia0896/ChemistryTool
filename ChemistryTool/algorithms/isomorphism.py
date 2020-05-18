from typing import Dict
from .abc import IsomorphismABC


class Isomorphism(IsomorphismABC):
    __slots__ = ()

    def get_mapping(self, other) -> Dict[int, int]:
        seen = set()
        o_atoms = other._atoms
        o_bonds = other._bonds
        pass

    def isomorphism(self, other):
        start, plane_graph, c = other.plane_graph()
        # start = plane_graph(other)[0]
        path = []
        seen = set()
        starts = [(x, y) for x, y in self._atoms.items() if y == other._atoms[start]]
        procedure = []

        for start in starts:
            stack = []
            while stack:
                 start, back = atom = stack.pop()






__all__ = ['Isomorphism']
