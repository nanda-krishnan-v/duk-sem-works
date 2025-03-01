class RiverCrossing:
    def __init__(self, initial_state=(3, 3, 1)):
        self.initial_state = initial_state
        self.visited = set()

    def is_safe(self, state):
        m, c, boat = state
        return not (m < c and m > 0) and not ((3 - m) < (3 - c) and (3 - m) > 0)

    def get_next_states(self, state):
        m, c, boat = state
        next_states = []
        if boat == 1:
            if m > 0:
                next_states.append((m - 1, c, 0))
            if m > 1:
                next_states.append((m - 2, c, 0))
            if c > 0:
                next_states.append((m, c - 1, 0))
            if c > 1:
                next_states.append((m, c - 2, 0))
            if m > 0 and c > 0:
                next_states.append((m - 1, c - 1, 0))
        else:
            if m < 3:
                next_states.append((m + 1, c, 1))
            if m < 2:
                next_states.append((m + 2, c, 1))
            if c < 3:
                next_states.append((m, c + 1, 1))
            if c < 2:
                next_states.append((m, c + 2, 1))
            if m < 3 and c < 3:
                next_states.append((m + 1, c + 1, 1))
        return [next_state for next_state in next_states if self.is_safe(next_state)]

    def solve(self):
        queue = [(self.initial_state, [])]
        while queue:
            state, path = queue.pop(0)
            if state in self.visited:
                continue
            self.visited.add(state)
            if state == (0, 0, 0):
                return path + [state]
            for next_state in self.get_next_states(state):
                queue.append((next_state, path + [state]))
        return None

river_crossing = RiverCrossing()

solution = river_crossing.solve()
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")