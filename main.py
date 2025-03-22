from collections import deque
import time
import random

def bfs(graph, start, goal):
    if start not in graph or goal not in graph:
        return None  # Handle invalid input
    
    queue = deque([(start, [start])])  # (current node, path taken)
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No path found

def generate_maze(size):
    maze = [['#' for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if random.random() > 0.3:  # 70% chance of open path
                maze[i][j] = '.'
    maze[0][0] = 'E'  # Entrance
    maze[size-1][size-1] = 'X'  # Exit
    return maze

def display_maze(maze):
    for row in maze:
        print(' '.join(row))

def find_store(graph, start, store_name):
    return bfs(graph, start, store_name)  # Using BFS for shortest path

def display_stores(graph, store_status):
    print("\nHere are all the available stores in the mall:")
    for store, status in store_status.items():
        print(f"- {store} ({'🟢 Open' if status else '🔴 Closed'})")

def recommend_store():
    recommendations = ["Store A", "Store B", "Store C", "Store D", "Food Court"]
    return random.choice(recommendations)

def chatbot():
    print("Hello! I'm your interactive mall navigation assistant. 🏬\n")
    
    mall_graph = {
        'Entrance': ['Store A', 'Store B'],
        'Store A': ['Entrance', 'Store C', 'Store D'],
        'Store B': ['Entrance', 'Store D'],
        'Store C': ['Store A', 'Food Court'],
        'Store D': ['Store A', 'Store B', 'Food Court'],
        'Food Court': ['Store C', 'Store D', 'Exit'],
        'Exit': ['Food Court']
    }
    
    store_status = {store: random.choice([True, False]) for store in mall_graph.keys()}  # Random open/closed status
    maze = generate_maze(5)  # Generate a 5x5 maze for mall layout
    
    while True:
        print("\nOptions:")
        print("1️⃣ Find a store")
        print("2️⃣ Display all stores")
        print("3️⃣ Get a store recommendation")
        print("4️⃣ View mall maze")
        print("5️⃣ Exit")
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            store_to_find = input("Enter the store name you want to find: ")
            if store_to_find in mall_graph:
                print("\nSearching for the best route... 🔍")
                time.sleep(1.5)
                path = find_store(mall_graph, 'Entrance', store_to_find)
                if path:
                    status = '🟢 Open' if store_status[store_to_find] else '🔴 Closed'
                    print(f"✅ Path to {store_to_find}: {' -> '.join(path)} ({status})")
                else:
                    print("❌ No path found to the store.")
            else:
                print("❌ Store not found in the mall directory. Please try again.")
        elif choice == '2':
            display_stores(mall_graph, store_status)
        elif choice == '3':
            recommendation = recommend_store()
            status = '🟢 Open' if store_status[recommendation] else '🔴 Closed'
            print(f"🛍️ How about visiting {recommendation}? {status}")
        elif choice == '4':
            print("\n🗺️ Here is the current mall maze layout:")
            display_maze(maze)
        elif choice == '5':
            print("\nThank you for using the mall navigation assistant. Have a great shopping experience! 🛍️")
            break
        else:
            print("⚠️ Invalid choice. Please select a valid option.")

# Start the chatbot
if __name__ == '__main__':
    chatbot()
