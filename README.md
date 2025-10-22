# 🕹️ Sprite Collection and Interactive Demo (Pygame)

This project demonstrates object-oriented programming with inheritance in Python, integrating the Pygame library for graphical representation and sprite management. It includes unit tests, a sprite collection ADT, and an interactive demo where sprites can be displayed and randomized dynamically.

The focus is on modular design, equality checking, collection management, and interactive visuals.

# 🧱 Class Architecture

1️⃣ my_sprite

Represents the most basic game object:
- Loads and stores an image (image_fname) and its position (loc).
- Provides getters for the sprite’s image, width, and height.
- Implements an equality method (__eq__) to compare two sprites by width, height, and location (image content is not required).
- Implements __str__ and __repr__ for clear visualization in print statements and collections.
- Serves as the foundation for all drawable objects.

2️⃣ sprite_collection

A collection ADT for managing multiple my_sprite objects:
- Can store duplicates.
- Methods:
  - add(sprite) → adds a my_sprite to the collection, raises TypeError if not a sprite.
  - get_collection() → returns the underlying collection.
  - __getitem__ and __setitem__ → allow list-like indexing.
  - __len__ → returns the number of sprites.
  - __str__ → prints the collection in a clear, list-like format using repr().
  - search(target) → returns a list of unique sprites equal to the target.
- Fully compatible with Python list operations and easy to extend.

# 🧪 Unit Testing (sprite_test.py)

Unit tests ensure all features are working correctly using Python’s unittest framework:
- my_sprite tests:
    - Equality method with different images, same dimensions, different locations, and self-equality.
    - String representations.

- sprite_collection tests:
  - Adding sprites and type validation.
  - Collection indexing and length.
  - Search functionality (including empty collections, multiple matches, and same object references).
  - String representation of the collection.

# 🎮 Interactive Demo (demo.py)

demo.py is a visual showcase of the my_sprite and sprite_collection classes:
- Automatically creates colored demo images and spawns them at random locations.
- Displays all sprites in a Pygame window.
- Shows the current number of sprites in the top-left corner.
- Press Spacebar to add a new random sprite while the program is running.

This demo demonstrates how the classes can be used in a graphical, interactive setting — perfect for a small game framework or a teaching project.

# ⚙️ Core Features

- Object-Oriented Design: Clear separation between sprite objects and collections.
- Equality Checking: Compare sprites based on size and location without requiring identical images.
- Collection Management: Add, access, index, and search sprites efficiently.
- Interactive Demo: Dynamically adds sprites while displaying count and positions.
- Unit Tests: Comprehensive coverage for equality, collection methods, and search.
