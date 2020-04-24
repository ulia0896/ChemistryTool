from typing import Dict
from .abc import IsomorphismABC
from abc import abstractmethod


class Isomorphism(IsomorphismABC):
    def __init__(self):
        self._atoms: Dict[int, str] = {}

    @abstractmethod
    def get_mapping(self, other) -> Dict[int, int]:
        seen = set()
        o_atoms = other._atoms
        o_bonds = other._bonds
        pass

    def plane_graph(self, other):
        atoms, bonds = other
        start = 1
        seen = {start}
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

    def isomorphism(self, other):
        start, plane_graph, c = self.plane_graph(other)
        # start = plane_graph(other)[0]
        path = []
        seen = set()
        starts = [(x, y) for x, y in self._atoms.items() if y == other._atoms[start]]
        procedure =

        for start in starts:
            stack = []
            while stack:
                 start, back = atom = stack.pop()






__all__ = ['Isomorphism']
