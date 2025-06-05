def make_purchase(item_name:str):
    return {"message": f"Purchased item: {item_name}"}

def order_items(item_name: str, quantity: int):
    return {"message": f"{quantity} Ordered items are on the way: {item_name}"}

def check_order_status(order_id: str):
    return {"message": f"Order {order_id} is currently being processed."}

def cancel_order(order_id: str):
    return {"message": f"Order {order_id} has been canceled."}

def search_category(category_name: str):
    return {"message": f"Popular items in {category_name}: Item1, Item2, Item3."}

def apply_discount(code: str):
    return {"message": f"Discount code '{code}' applied successfully!"}

def get_shipping_info(zip_code: str):
    return {"message": f"Shipping to ZIP {zip_code} takes 3-5 business days."}