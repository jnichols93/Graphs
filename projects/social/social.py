import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # Add users
        # call addUser() until our number of users is numUsers
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        totalFriendships = avg_friendships * num_users // 2
        friendshipsCreated = 0
        collisions = 0
        while friendshipsCreated < totalFriendships:
            # pick a random number 1-n, pick another nu 1-n
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            # create a friendship between those two IDs
            if self.add_friendship(user_id, friend_id):
                friendshipsCreated +=2
            else:
                collisions += 1
        # Until you have friendship count = total friendships
        print(f"COLLISIONS: {collisions}")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # do a bft store paths as we go
        # create an empty queue
        q = Queue()
        visited = {}  # Note that this is a dictionary aka hastable, not a set
        # add PATH to the starting node to the queue
        q.enqueue( [user_id] )
        # while the queue is not empty...
        while q.size() > 0:
            # Dequeue the first Path from the Queue
            path = q.dequeue()
            v = path[-1]
            # check if its been visited
            if v not in visited:
                # when we reach an unvisited node, add the path to the dict
                visited[v] = path
                # add a path to each neighbor to the back of the queue
                for friendID in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(friendID)
                    q.enqueue(path_copy)
        # when we reach unvisited node, add path to visited dict.
        # return visited dictionary
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(200, 3)
    print("USERS:")
    print(sg.users)
    print("FRIENDSHIPS:")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
