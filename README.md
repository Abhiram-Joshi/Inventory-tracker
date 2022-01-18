# Inventory-tracker

This project is an implementation of an inventory tracking web application for a logistics company with the following features:-
- Basic CRUD functionality
    - Create inventory items
    - Edit inventory items
    - Delete inventory items
    - View a list of all inventory items
- Ability to create “shipments” and assign inventory to the shipment, and adjust inventory appropriately
    - Create shipment from items in the inventory
        - If a shipment is successfully created, the quantity of the corresponding item in the inventory is reduced by the quantity used in the shipment
    - Cancel shipment
        - Cannot be done if the shipment is already marked as delivered
        - If the shipment is cancelled, the items in the shipment are added to back to the inventory
    - Deliver shipment
        - Cannot be done if the shipment is already marked as cancelled

## Installation

In the cloned repository deirectory, use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## Usage

In the cloned repository directory(after installation of the dependencies), write the following commands

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


These commands will start a development server on your system.

<br>

With the development server running, in the frontend folder, open the `index.html` file in your browser. This file provides a basic UI to demonstrate the implementation of the backend routes.

The steps below would explain the working of the User interface:-

- In the `index.html` file

    -  `Fetch all items` button will fetch all the items in the inventory which are stored in the database. The button will be disabled once pressed to avoid repitition of the list.

    - `Click here to add an item to the inventory` button will lead you to the `add_item.html` page where the user will be asked to fill out a form to add a new item to the inventory in the database.

    - The `Buy item` button enables you to buy items from the inventory. To use this feature, add enter the `Item ID` and the `quantity` of that item to be bought in the corresponding text boxes and press the `Buy Item` button. Press the `Fetch all items` button to check the remaining quantity of the item.

    - The `Remove Item` button enables you to remove an item from the inventory. To use this feature, enter the `Item ID` of the item you need to remove and press the `Remove Item` button. Press the `Fetch all items` button to see the remaining items.

    - The `Go to shipment` button leads you to the shipment portal(`shipment.html` file)

<br>

- In the `shipment.html` file

    - `Fetch all shipments` buttonn will fetch all the shipments which have been created and stored in the database. The button will be disabled once pressed to avoid repitition of the list.

    - `Create shipment` button will lead you to the `create_shipment.html` page where the user will be asked to fill out a form to create a new shipment from the items already present in the database. If a shipment is successfully created, the quantity of the corresponding item in the inventory is reduced by the quantity used in the shipment. The page also has a `Fetch all items` button, which will list all the items in the inventory for the user's reference.

    - `Mark as cancelled` button enables the user to mark a shipment as cancelled if it has not been delivered yet. To use this feature, enter the `Shipment ID` of the shipment to be marked as cancelled and press the `Mark as cancelled` button. If the shipment is successfully cancelled, the quantity of items in the shipment are added back to the inventory. Press the `Fetch all shipments` button to see the status of the shipment.

    - `Mark as delivered` button enables the user to mark a shipment as delivered if it has not been cancelled yet. To use this feature, enter the `Shipment ID` of the shipment to be marked as delivered and press the `Mark as delivered` button. `Fetch all shipments` button to see the status of the shipment.

<br>

The documentation for the API routes can be obtained from [this link](https://documenter.getpostman.com/view/14681434/UVXjKw54). The API routes in the documentation have been written for a local development setup. The routes can be tested by using the `Run in Postman` button on the top-right of the page. If you don't want to run a development server for testing those routes, replace the host `http://127.0.0.1:8000/` with `https://shopify-iinventory.herokuapp.com/` in the API routes. This would call the same routes hosted on Heroku.