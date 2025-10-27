# Inventory Management System

A Python inventory management system with input validation, error handling, and data persistence.

## Features

- Add/remove items with automatic quantity tracking
- Save/load inventory to JSON files
- Input validation and comprehensive error handling
- Low stock alerts
- Full logging for debugging

## Installation

```bash
git clone https://github.com/yourusername/inventory-system.git
cd inventory-system
python inventory_system.py
```

## Usage

```python
from inventory_system import InventorySystem

# Create inventory
inventory = InventorySystem()

# Add items
inventory.add_item("apple", 50)
inventory.add_item("banana", 30)

# Remove items
inventory.remove_item("apple", 12)

# Check quantity
qty = inventory.get_qty("apple")  # Returns 38

# Check low stock
low_items = inventory.check_low_items(threshold=25)

# Save/load
inventory.save_data("inventory.json")
inventory.load_data("inventory.json")

# Print report
inventory.print_data()
```

## API Reference

| Method | Description |
|--------|-------------|
| `add_item(item, qty)` | Add items to inventory |
| `remove_item(item, qty)` | Remove items from inventory |
| `get_qty(item)` | Get quantity of an item |
| `save_data(file)` | Save inventory to JSON |
| `load_data(file)` | Load inventory from JSON |
| `print_data()` | Print inventory report |
| `check_low_items(threshold)` | Find items below threshold |

## Code Quality

- **Pylint**: 10.00/10 
- **Bandit**: 0 issues 
- **Flake8**: 0 issues 

```bash
# Run static analysis
pylint inventory_system.py
flake8 inventory_system.py
bandit inventory_system.py
```

## License

MIT License
