import heapq
import itertools

# ---------- Graph (from Part 1) ----------
graph = {
    "Nairobi": {"Naivasha": 90, "Narok": 142, "Thika": 40},
    "Naivasha": {"Nakuru": 71},
    "Narok": {"Bomet": 81},
    "Thika": {"Nyeri": 110},
    "Nyeri": {"Nyahururu": 103},
    "Nyahururu": {"Nakuru": 75},
    "Nakuru": {"Kericho": 108},
    "Bomet": {"Kericho": 79},
    "Kericho": {"Kisumu": 84},
    "Kisumu": {},
}

start = "Nairobi"
goal = "Kisumu"


# ---------- Uniform Cost Search ----------
def uniform_cost_search(graph, start, goal, verbose=True):
    """
    Uniform Cost Search on a weighted, directed graph.

    Returns: (path, total_cost, expanded_nodes)
             path is None and total_cost is float('inf') if no route exists.
    """
    counter = itertools.count()              # tie-breaker so heapq never compares nodes
    frontier = [(0, next(counter), start)]   # priority queue of (g(n), tie, node)
    best_cost = {start: 0}                   # cheapest g(n) found so far for each node
    parent = {start: None}                   # for path reconstruction
    explored = set()                         # nodes already expanded
    expanded_order = []                      # nodes expanded, in order

    step = 0
    while frontier:
        g, _, node = heapq.heappop(frontier)  # lowest cumulative cost

        # Skip stale entries (a cheaper route to this node was already expanded)
        if node in explored:
            continue

        step += 1
        explored.add(node)
        expanded_order.append(node)

        if verbose:
            print(f"Step {step}: expand {node} (g = {g} km)")

        # Goal test when a node is POPPED, which guarantees optimality
        if node == goal:
            path = []
            current = node
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            if verbose:
                print(f"\nGoal '{goal}' reached.")
            return path, g, expanded_order

        # Generate successors
        for neighbor, step_cost in graph[node].items():
            new_cost = g + step_cost
            if neighbor not in explored and new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(frontier, (new_cost, next(counter), neighbor))

        if verbose:
            # Live frontier, skipping stale entries, sorted by cost
            live = sorted(
                (c, n) for c, _, n in frontier
                if n not in explored and c == best_cost[n]
            )
            print("   Frontier:", [(n, c) for c, n in live])

    return None, float("inf"), expanded_order


# ---------- Run the search ----------
path, total_cost, expanded = uniform_cost_search(graph, start, goal)

print("\n" + "=" * 50)
print("Nodes expanded (in order):", expanded)
print("Number of nodes expanded: ", len(expanded))
print("Optimal path:", " -> ".join(path))
print("Total path cost:", total_cost, "km")

# ---------- Validate against the Part 1 expected result ----------
expected_path = ["Nairobi", "Naivasha", "Nakuru", "Kericho", "Kisumu"]
expected_cost = 353

assert path == expected_path, f"Path mismatch: {path}"
assert total_cost == expected_cost, f"Cost mismatch: {total_cost}"
print("\nValidation passed: matches the expected Part 1 path and 353 km cost.")