from __future__ import annotations

from copy import copy
from dataclasses import dataclass

from lib import dijkstra


@dataclass
class Room:
    index: int
    _size: int
    _content: list[int]

    def __str__(self) -> str:
        return ''.join(str(a) for a in self._content)

    def __copy__(self) -> Room:
        return Room(self.index, self._size, self._content[:])

    @property
    def first(self) -> int:
        return self._content[-1]

    def get(self, i: int) -> int:
        try:
            return self._content[i]
        except IndexError:
            return 0

    @property
    def is_clean(self) -> bool:
        return all(a == self.index for a in self._content)

    @property
    def is_empty(self) -> bool:
        return len(self._content) == 0

    @property
    def is_full(self) -> bool:
        return len(self._content) == self._size

    @property
    def spots_left(self) -> int:
        return self._size - len(self._content)

    @property
    def is_finished(self) -> bool:
        return self.is_full and self.is_clean

    def can_add(self, amphipod: int) -> bool:
        return amphipod == self.index and not self.is_full and self.is_clean

    def add(self, amphipod: int) -> None:
        self._content.append(amphipod)

    def remove(self) -> int:
        return self._content.pop()


class AmphipodState(dijkstra.State):
    def __init__(
        self,
        room_size: int,
        rooms: list[Room],
        hallway: list[int] = None,
        cost: int = 0,
    ):
        super().__init__(cost)
        self._room_size = room_size
        self._rooms = rooms
        self._hallway = hallway or [0] * 7

    @classmethod
    def from_input(cls, input_lines: list[str]) -> AmphipodState:
        room_size = len(input_lines)
        return AmphipodState(room_size, rooms=[
            Room(name, room_size, [{'A': 1, 'B': 2, 'C': 3, 'D': 4}[c] for c in content])
            for name, content in zip(
                [1, 2, 3, 4],
                list(zip(*[line[3:10:2] for line in input_lines])),
            )
        ])

    def __hash__(self) -> int:
        return hash(''.join(str(r) for r in self._rooms) + ''.join(str(h) for h in self._hallway))

    @property
    def is_finished(self) -> bool:
        return all(r.is_finished for r in self._rooms)

    def _can_move(self, room: int, hall: int) -> bool:
        return not (
            hall < room + 1 and any(self._hallway[hall + 1:room + 2]) or
            hall > room + 2 and any(self._hallway[room + 2:hall])
        )

    def move(self, amphipod: int, r: int, h: int, into_room: bool) -> AmphipodState:
        rooms = [copy(room) for room in self._rooms]
        hallway = self._hallway[:]
        if into_room:
            rooms[r].add(hallway[h])
            hallway[h] = 0
        else:
            hallway[h] = rooms[r].remove()
        return AmphipodState(self._room_size, rooms, hallway, self.cost + ([
             [3, 2, 2, 4, 6, 8, 9],
             [5, 4, 2, 2, 4, 6, 7],
             [7, 6, 4, 2, 2, 4, 5],
             [9, 8, 6, 4, 2, 2, 3],
        ][r][h] + rooms[r].spots_left - int(into_room)) * 10 ** (amphipod - 1))

    @property
    def next_states(self) -> list[AmphipodState]:
        return [
            # all states that move an amphipod out of a room
            self.move(room.first, r, h, into_room=False)
            for r, room in enumerate(self._rooms) if not room.is_clean and not room.is_empty
            for h, amphipod in enumerate(self._hallway) if not amphipod and self._can_move(r, h)
        ] + [
            # all states that move an amphipod into a room
            self.move(amphipod, r, h, into_room=True)
            for h, amphipod in enumerate(self._hallway) if amphipod
            for r, room in enumerate(self._rooms) if room.can_add(amphipod) and self._can_move(r, h)
        ]

    def __repr__(self) -> str:
        s = '.ABCD'
        return '\n'.join([
            '#############',
            '#' + s[self._hallway[0]] + '.'.join(s[a] for a in self._hallway[1:-1]) + s[self._hallway[-1]] + '#',
        ] + [
            ('#' if i == self._room_size - 1 else ' ') * 2 +
            '#' + '#'.join(s[r.get(i)] for r in self._rooms) + '#' +
            ('#' if i == self._room_size - 1 else ' ') * 2
            for i in range(self._room_size - 1, -1, -1)
        ] + ['  #########'])


def part1(input_lines: list[str]) -> int:
    path = dijkstra.shortest_path(AmphipodState.from_input(input_lines[5:1:-3]))
    dijkstra.print_path(path)
    return path[-1].cost


def part2(input_lines: list[str]) -> int:
    path = dijkstra.shortest_path(AmphipodState.from_input(input_lines[5:1:-1]))
    dijkstra.print_path(path)
    return path[-1].cost



input1 = """\
#############
#...........#
###B#C#B#D###
  #A#D#C#A#  
  #########  """

input2 = """\
#############
#...........#
###A#D#B#C###
  #B#C#D#A#
  #########"""

cost = part1(input1.split('\n'))
print(cost)
