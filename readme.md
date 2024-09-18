# Coffee Shop Python Project

## Project Overview

This project involves creating a Python application to model a Coffee Shop domain using object-oriented programming principles. The objective is to design a domain model consisting of three main entities: `Customer`, `Coffee`, and `Order`, and to establish the relationships between them.

### Scenario

You are tasked with building a domain model for a Coffee Shop. The relationships between entities are as follows:
- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

The `Customer` and `Coffee` entities have a many-to-many relationship through the `Order` entity.

## Instructions

### 1. Setup and Preparation

1. **Create a New Directory:**
   - Create a directory named `coffee_shop` for your project.
   - Navigate to this directory.

2. **Set Up Virtual Environment:**
   - Use `pipenv` to set up a virtual environment:
     ```bash
     pipenv install
     pipenv shell
     ```

3. **Install Dependencies:**
   - Install necessary packages such as `pytest` for testing:
     ```bash
     pipenv install pytest
     ```

### 2. Domain Model Design

- Sketch your domain model, identifying the classes `Customer`, `Coffee`, and `Order`.
- Establish the relationships between these classes.
- Determine the attributes and methods for each class.

### 3. Create Class Files

1. Create three Python files in the `coffee_shop` directory:
   - `customer.py`
   - `coffee.py`
   - `order.py`

2. Define a class in each file corresponding to the file name.

### 4. Implement Initializers and Properties

- **Customer Class (`customer.py`):**
  - Initialize with a `name` (string between 1 and 15 characters).
  - Implement property `name` with validation.

- **Coffee Class (`coffee.py`):**
  - Initialize with a `name` (string, at least 3 characters long).
  - Implement property `name` with validation.

- **Order Class (`order.py`):**
  - Initialize with a `Customer` instance, a `Coffee` instance, and a `price` (float between 1.0 and 10.0).
  - Implement properties `customer`, `coffee`, and `price` with validation.

### 5. Define Object Relationship Methods and Properties

- **Order Class (`order.py`):**
  - `customer` property returns the `Customer` instance for the order.
  - `coffee` property returns the `Coffee` instance for the order.

- **Coffee Class (`coffee.py`):**
  - `orders()` method returns a list of all `Order` instances for that coffee.
  - `customers()` method returns a unique list of `Customer` instances who have ordered that coffee.

- **Customer Class (`customer.py`):**
  - `orders()` method returns a list of all `Order` instances for that customer.
  - `coffees()` method returns a unique list of `Coffee` instances that the customer has ordered.

### 6. Implement Aggregate and Association Methods

- **Customer Class (`customer.py`):**
  - `create_order(coffee, price)` method: Creates a new `Order` instance associated with the customer and the coffee.

- **Coffee Class (`coffee.py`):**
  - `num_orders()` method: Returns the total number of times a coffee has been ordered.
  - `average_price()` method: Returns the average price for a coffee based on its orders.

## Dependencies

- Python 3.x
- `pipenv`
- `pytest`

## Usage

1. To run the application, ensure the virtual environment is activated:
   ```bash
   pipenv shell

## Contributing
Feel free to fork the repository, make improvements, and submit pull requests. Ensure that your changes are well-documented and tested.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or feedback, please contact [Rono Peter]
 at [peter.rono@student.moringaschool.com].