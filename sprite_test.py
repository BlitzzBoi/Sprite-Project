import unittest
import pygame
from my_sprite import my_sprite
from sprite_collection import sprite_collection

class TestMySprite(unittest.TestCase):
    def setUp(self):
        pygame.init()
        surf = pygame.Surface((50,100))
        pygame.image.save(surf, "test_img.png")
    
    def tearDown(self):
        pygame.quit()

    # EQUALITY TESTS

    #Two sprites with same image, location, and size should be equal.
    def test_equality_same_image_true(self):
        s1 = my_sprite("test_img.png", (10, 20))
        s2 = my_sprite("test_img.png", (10, 20))
        self.assertTrue(s1 == s2)
    
    #Two sprites with different locations shouldn't be equal
    def test_equality_different_location_false(self):
        s1 = my_sprite("test_img.png", (10, 20))
        s2 = my_sprite("test_img.png", (0, 0))
        self.assertFalse(s1 == s2)
    
    #The same object should equal itself
    def test_equality_itself(self):
        s1 = my_sprite("test_img.png", (5, 5))
        self.assertTrue(s1 == s1)

    #Two sprites with different images but same location and size are equal
    def test_equality_diff_images_same_loc_size(self):
        surf1 = pygame.Surface((50, 100))
        surf2 = pygame.Surface((50, 100))

        pygame.image.save(surf1, "img1.png")
        pygame.image.save(surf2, "img2.png")

        s1 = my_sprite("img1.png", (10, 20))
        s2 = my_sprite("img2.png", (10, 20))
        self.assertTrue(s1 == s2)

    #Check if my_sprite prints correctly
    def test_str_representation(self):
        s = my_sprite("test_img.png", (10, 20))
        out = str(s)
        self.assertIn("Sprite at", out)
        self.assertIn("(", out)
        self.assertIn("x", out)
        

class TestSpriteCollection(unittest.TestCase):
    def setUp(self):
        pygame.init()
        surf = pygame.Surface((20, 20))
        pygame.image.save(surf, "img.png")
        self.s1 = my_sprite("img.png", (0, 0))
        self.s2 = my_sprite("img.png", (1, 1))
        self.collection = sprite_collection()

    def tearDown(self):
        pygame.quit()

    # ADD & GET_COLLECTION TESTS

    def test_add_and_len(self):
        self.collection.add(self.s1)
        self.collection.add(self.s2)
        self.assertEqual(len(self.collection), 2)

    def test_add_invalid_type(self):
        with self.assertRaises(TypeError):
            self.collection.add("not a sprite")

    def test_get_collection(self):
        self.collection.add(self.s1)
        self.assertIn(self.s1, self.collection.get_collection())

    def test_get_set_item(self):
        self.collection.add(self.s1)
        self.collection[0] = self.s2
        self.assertEqual(self.collection[0], self.s2)

    def test_len_functionality(self):
        self.collection.add(self.s1)
        self.collection.add(self.s2)
        self.assertEqual(len(self.collection), 2)

    # SEARCH TESTS

    def test_search_found_multiple(self):
        self.collection.add(self.s1)
        self.collection.add(self.s2)
        self.collection.add(my_sprite("img.png", (0, 0)))
        result = self.collection.search(self.s1)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(isinstance(s, my_sprite) for s in result))

    def test_search_not_found(self):
        self.collection.add(self.s2)
        result = self.collection.search(self.s1)
        self.assertEqual(result, [])

    def test_search_empty_collection(self):
        result = self.collection.search(self.s1)
        self.assertEqual(result, [])

    def test_search_same_object_reference(self):
        self.collection.add(self.s1)
        result = self.collection.search(self.s1)
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.s1)

    def test_str_representation_collection(self):
        self.collection.add(self.s1)
        self.collection.add(self.s2)
        out = str(self.collection)
        self.assertTrue(out.startswith("["))
        self.assertIn("my_sprite", out)
        self.assertTrue(out.endswith("]"))


if __name__ == "__main__":
    unittest.main()