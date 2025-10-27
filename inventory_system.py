"""
Inventory Management System
A simple system for managing stock items with add, remove,
and reporting capabilities.
"""
import json
import logging
from datetime import datetime


class InventorySystem:
    """
    A class to manage inventory operations.
    """

    def __init__(self):
        """Initialize the inventory system with empty stock data."""
        self.stock_data = {}

    def add_item(self, item="default", qty=0, logs=None):
        """
        Add an item to the inventory.

        Args:
            item: Item name (must be a string)
            qty: Quantity to add (must be a non-negative integer)
            logs: List to store operation logs

        Returns:
            bool: True if successful, False otherwise
        """
        if logs is None:
            logs = []

        # Input validation
        if not isinstance(item, str) or not item:
            logging.warning("Invalid item name: %s", item)
            return False

        if not isinstance(qty, int) or qty < 0:
            logging.warning("Invalid quantity for %s: %s", item, qty)
            return False

        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        log_message = f"{datetime.now()}: Added {qty} of {item}"
        logs.append(log_message)
        logging.info(log_message)
        return True

    def remove_item(self, item, qty):
        """
        Remove an item from the inventory.

        Args:
            item: Item name (must be a string)
            qty: Quantity to remove (must be a positive integer)

        Returns:
            bool: True if successful, False otherwise
        """
        # Input validation
        if not isinstance(item, str) or not item:
            logging.warning("Invalid item name: %s", item)
            return False

        if not isinstance(qty, int) or qty <= 0:
            logging.warning("Invalid quantity for %s: %s", item, qty)
            return False

        try:
            if item not in self.stock_data:
                logging.warning("Item '%s' not found in inventory", item)
                return False

            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
                logging.info(
                    "Item '%s' removed from inventory (quantity reached 0)",
                    item
                )
            else:
                logging.info("Removed %d of %s", qty, item)
            return True
        except KeyError as e:
            logging.error("Key error while removing item: %s", e)
            return False

    def get_qty(self, item):
        """
        Get the quantity of an item in inventory.

        Args:
            item: Item name

        Returns:
            int: Quantity of the item, or 0 if not found
        """
        if not isinstance(item, str) or not item:
            logging.warning("Invalid item name: %s", item)
            return 0

        return self.stock_data.get(item, 0)

    def load_data(self, file="inventory.json"):
        """
        Load inventory data from a JSON file.

        Args:
            file: Path to the JSON file

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(file, "r", encoding="utf-8") as f:
                self.stock_data = json.load(f)
            logging.info("Data loaded successfully from %s", file)
            return True
        except FileNotFoundError:
            logging.warning(
                "File %s not found. Starting with empty inventory.",
                file
            )
            self.stock_data = {}
            return False
        except json.JSONDecodeError as e:
            logging.error("Error decoding JSON from %s: %s", file, e)
            return False
        except IOError as e:
            logging.error("IO error while loading data: %s", e)
            return False

    def save_data(self, file="inventory.json"):
        """
        Save inventory data to a JSON file.

        Args:
            file: Path to the JSON file

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(file, "w", encoding="utf-8") as f:
                json.dump(self.stock_data, f, indent=2)
            logging.info("Data saved successfully to %s", file)
            return True
        except IOError as e:
            logging.error("Error saving data to %s: %s", file, e)
            return False

    def print_data(self):
        """
        Print the current inventory to console.
        """
        print("Items Report")
        print("-" * 30)
        if not self.stock_data:
            print("No items in inventory")
        else:
            for item, quantity in self.stock_data.items():
                print(f"{item} -> {quantity}")

    def check_low_items(self, threshold=5):
        """
        Check for items below a certain quantity threshold.

        Args:
            threshold: Minimum quantity threshold (default: 5)

        Returns:
            list: List of items below the threshold
        """
        if not isinstance(threshold, int) or threshold < 0:
            logging.warning(
                "Invalid threshold: %s. Using default value of 5.",
                threshold
            )
            threshold = 5

        result = [item for item, qty in self.stock_data.items()
                  if qty < threshold]
        return result


def main():
    """
    Main function to demonstrate the inventory system.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    logging.info("Starting inventory system...")

    # Create inventory system instance
    inventory = InventorySystem()

    # Valid operations
    inventory.add_item("apple", 10)
    inventory.add_item("banana", 5)

    # Invalid operations (will be caught and logged)
    inventory.add_item("banana", -2)  # Invalid: negative quantity
    inventory.add_item(123, "ten")  # Invalid: wrong types

    # Remove operations
    inventory.remove_item("apple", 3)
    inventory.remove_item("orange", 1)  # Item doesn't exist

    # Query operations
    apple_qty = inventory.get_qty("apple")
    print(f"Apple stock: {apple_qty}")

    low_items = inventory.check_low_items()
    print(f"Low items: {low_items}")

    # Save and load
    inventory.save_data()
    inventory.load_data()
    inventory.print_data()

    # Removed dangerous eval() call
    logging.info("Inventory system operations completed")


if __name__ == "__main__":
    main()
