"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        return node

    def search(self, value):
        """
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Implement recursive BST search.
        """
        #Node not found
        if node is None:
            return False

        #Node found
        if value == node.value:
            return True

        #Value is smaller than current node
        if value < node.value:
            return self._search_recursive(node.left, value)

        #Value is larger than current node
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """
        vals = []

        self._inorder_recursive(self.root, vals)

        return vals

    def _inorder_recursive(self, node, values):
        """
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:

            #Gets lower values
            self._inorder_recursive(node.left, values)

            #Gets current value
            values.append(node.value)

            #Gets larger values
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===\n")

    # ===============================
    # BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    bst = BST()

    vals_for_inserting = [2, 16, 1, 30, 25, 4, 3, 20]

    for val in vals_for_inserting:
        bst.insert(val)

    print(f"Inserted Values: {", ".join(map(str, vals_for_inserting))}\n")
    print(f"In-Order Sorted Values: {", ".join(map(str, bst.inorder()))}\n")

    print("\n=== TREE CONSTRUCTION ===\n")

    tree = BST()

    new_for_inserting = [60, 20, 65, 2, 48, 15, 100, 6]

    for val in new_for_inserting:
        tree.insert(val)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    sorted_vals = tree.inorder()
    print("\n=== IN-ORDER TRAVERSAL ===\n")
    print(f"In-Order Traversal Results: {", ".join(map(str, sorted_vals))}\n")


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===\n")

    print(f"Searching Tree for 65\n")
    first_search = tree.search(65)
    if first_search == True:
        print("65 Found!\n")
    else:
        print("65 Not Found!\n")

    print(f"Searching Tree for 6\n")
    second_search = tree.search(6)
    if second_search == True:
        print("6 Found!\n")
    else:
        print("6 Not Found!\n")

    print(f"Searching Tree for 600\n")
    third_search = tree.search(600)
    if third_search == True:
        print("600 Found!\n")
    else:
        print("600 Not Found!\n")

    print(f"Searching Tree for 1\n")
    fourth_search = tree.search(1)
    if fourth_search == True:
        print("1 Found!\n")
    else:
        print("1 Not Found!\n")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")



if __name__ == "__main__":
    main()