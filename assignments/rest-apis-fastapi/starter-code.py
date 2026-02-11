"""
REST API with FastAPI - Starter Code

This starter code provides a basic structure for building a REST API
with FastAPI. You'll need to implement the missing functionality.

To run this API:
1. Install FastAPI: pip install fastapi uvicorn
2. Run the server: uvicorn starter-code:app --reload
3. Visit http://localhost:8000/docs for interactive API documentation
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Resource API", description="A simple REST API for managing resources")

# Define your data model here
class Item(BaseModel):
    """Model for an item/resource"""
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    completed: bool = False  # Example for todos


# Sample data storage (in-memory)
items_db: List[Item] = []


# TODO: Implement the following endpoints:

# GET all items
@app.get("/items", response_model=List[Item])
async def get_items():
    """Retrieve all items"""
    # TODO: Return all items from items_db
    pass


# GET a specific item by ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Retrieve a specific item by ID"""
    # TODO: Find and return item with matching ID
    # TODO: Raise HTTPException with status 404 if not found
    pass


# POST - Create a new item
@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    """Create a new item"""
    # TODO: Generate an ID and add item to items_db
    # TODO: Return the created item
    pass


# PUT - Update an existing item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """Update an existing item"""
    # TODO: Find the item by ID
    # TODO: Update its fields
    # TODO: Raise HTTPException with status 404 if not found
    pass


# DELETE - Remove an item
@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    """Delete an item by ID"""
    # TODO: Remove item from items_db
    # TODO: Raise HTTPException with status 404 if not found
    pass


# Optional: Add a search/filter endpoint
@app.get("/items/search/{query}", response_model=List[Item])
async def search_items(query: str):
    """Search for items by name or description"""
    # TODO: Filter items based on query string
    # TODO: Return matching items
    pass
