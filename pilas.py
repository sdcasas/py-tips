from typing import Any, List, Optional


class Stack:
    """Class implementing a stack (LIFO) in Python."""

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self.items: List[Any] = []

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not self.items

    def add(self, item: Any) -> None:
        """Add an element to the stack.

        Args:
            item: The element to add to the stack.
        """
        self.items.append(item)

    def remove(self) -> None:
        """Remove and return the most recent element from the stack.

        Returns:
            The removed element from the stack, or None if the stack is empty.
        """
        if self.is_empty():
            print("The stack is empty")
            return None
        self.items.pop()

    def reset(self) -> None:
        """Clear the stack, removing all its elements."""
        self.items = []

    def items_show(self) -> None:
        """Show the current elements in the stack."""
        print(self.items)


# Create an instance of the Stack class
stack = Stack()

# Show the empty stack
stack.items_show()

# Add elements to the stack and show it after each operation
stack.add(3)
stack.items_show()
stack.add('Sergio Casas')
stack.items_show()
stack.add('mario bros')
stack.items_show()

# Remove elements from the stack and show it after each operation
stack.remove()
stack.items_show()
stack.remove()
stack.items_show()
stack.remove()
stack.items_show()
stack.remove()
stack.items_show()
