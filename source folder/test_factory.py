# test_factory.py
import unittest
from animal_factory import AnimalFactory, Dog, Cat

class TestAnimalFactory(unittest.TestCase):

    def test_create_dog_successfully(self):
        """Test Case 1: Verify the factory correctly instantiates a Dog object."""
        animal = AnimalFactory.create_animal("dog")
        self.assertIsInstance(animal, Dog)
        self.assertEqual(animal.speak(), "Woof!")

    def test_create_cat_successfully(self):
        """Test Case 2: Verify the factory correctly instantiates a Cat object."""
        animal = AnimalFactory.create_animal("cat")
        self.assertIsInstance(animal, Cat)
        self.assertEqual(animal.speak(), "Meow!")

    def test_invalid_animal_raises_error(self):
        """Test Case 3: Verify the factory raises a ValueError for unknown types."""
        with self.assertRaises(ValueError) as context:
            AnimalFactory.create_animal("dragon")
        
        self.assertTrue("Unknown animal type: dragon" in str(context.exception))

if __name__ == '__main__':
    unittest.main()