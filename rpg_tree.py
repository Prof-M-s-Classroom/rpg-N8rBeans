class StoryNode:
    """Represents a node in the decision tree."""
    def __init__(self, event_number, description, left=None, right=None):
        self.event_number = event_number
        self.description = description
        self.left = left
        self.right = right

class GameDecisionTree:
    """Binary decision tree for the RPG."""
    def __init__(self):
        # stores StoryNode elements
        self.nodes = {}
        # start with no root
        self.root = None

    def insert(self, event_number, description, left_event, right_event):
        """Insert a new story node into the tree."""
        # check if current node exists
        if event_number not in self.nodes:
            # if node does not exist, create it
            self.nodes[event_number] = StoryNode(event_number, description)
        else:
            # if node does exist, update it
            # check if description is blank
            if self.nodes[event_number].description == "":
                # if it is, update it
                self.nodes[event_number].description = description

        current_node = self.nodes[event_number]

        # check if left event number is -1
        if left_event != -1:
            # if it is not -1, then generate the left node
            if left_event not in self.nodes:
                self.nodes[left_event] = StoryNode(left_event, "")
            current_node.left = self.nodes[left_event]
        else:
            # otherwise set no left node
            current_node.left = None

        # check if right event number is -1
        if right_event != -1:
            # if it is not -1, then generate the right node
            if right_event not in self.nodes:
                self.nodes[right_event] = StoryNode(right_event, "")
            current_node.right = self.nodes[right_event]
        else:
            # otherwise set no right node
            current_node.right = None

        # set root to current node
        if self.root is None:
            self.root = current_node

    def play_game(self):
        """Interactive function that plays the RPG."""
        if self.root is None:
            print("Story tree empty")
            return

        # begin at root node
        current_node = self.root

        # traverse all nodes
        while current_node:
            # print story option
            print("\n" + current_node.description)

            # if there is no next node at all then the story is over
            if current_node.left is None and current_node.right is None:
                print("\nCongratulations! The story ends here! Thank you for playing!")
                break

            # get player choice to traverse story
            while True:
                choice = input("Decide 1 or 2: ")
                if choice == '1':
                    next_node = current_node.left
                elif choice == '2':
                    next_node = current_node.right
                else:
                    print("Invalid choice. Please enter 1 or 2.")
                    continue
                break

            # if there is no next node for the chosen story direction then the story is over
            if next_node is None:
                print("\nCongratulations! The story ends here! Thank you for playing!")
                break

            # set current node to next node to continue the story
            current_node = next_node

def load_story(filename, game_tree):
    """Load story from a file and construct the decision tree."""
    try:
        # open the file in read format
        with open(filename, 'r') as file:
            # traverse all lines in the file
            for line in file:
                line = line.strip()
                if not line:
                    continue

                # parse the line using the '|' separator
                parts = line.split(' | ')
                # line number
                event_number = int(parts[0])
                # story description and prompt
                description = parts[1]
                # left node number
                left_event = int(parts[2])
                # right node number
                right_event = int(parts[3])

                # insert node into tree to initialize story
                game_tree.insert(event_number, description, left_event, right_event)

    # if file cannot be located
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# main program
if __name__ == "__main__":
    # generate decision tree
    game_tree = GameDecisionTree()

    # load story into decision tree (from AI generated text file)
    load_story("story.txt", game_tree)

    # run the game
    game_tree.play_game()