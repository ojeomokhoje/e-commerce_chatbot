tools = [{
        "type": "function",
        "function": {
            "name": "make_purchase",
            "description": "This function is meant to make purchase of items ",
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {"type": "string"}
                },
                "required": ["item_name"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "order_items",
            "description": "This function is meant to make order of items ",
            "parameters": {
                "type": "object",
                "properties": {
                    "item_name": {"type": "string"},
                    "quantity": {"type": "integer"},

                },
                "required": ["item_name", "quantity"]
            }
        }
    },
          {
        "type": "function",
        "function": {
            "name": "check_order_status",
            "description": "This function is meant to check the current status of a customer's order.",
            "parameters": {
            "type": "object",
            "properties": {
                "order_id": { "type": "string" }
            },
            "required": ["order_id"]
        }
    }
},
    {
        "type": "function",
        "function": {
            "name": "cancel_order",
            "description": "This function is meant to cancel an existing order.",
            "parameters": {
            "type": "object",
            "properties": {
                "order_id": { "type": "string" }
            },
            "required": ["order_id"]
        }
    }
    },
    {
        "type": "function",
        "function": {
            "name": "search_category",
            "description": "This function is meant to return popular items in a specific category.",
            "parameters": {
            "type": "object",
            "properties": {
                "category_name": { "type": "string" }
            },
            "required": ["category_name"]
        }
    }
},
    {
        "type": "function",
        "function": {
            "name": "apply_discount",
            "description": "This function is meant to apply a discount code to the customer's order.",
            "parameters": {
            "type": "object",
            "properties": {
                "code": { "type": "string" }
            },
            "required": ["code"]
        }
    }
    },
    {
        "type": "function",
        "function": {
            "name": "get_shipping_info",
            "description": "This function is meant to provide shipping time estimates based on ZIP code.",
            "parameters": {
            "type": "object",
            "properties": {
                "zip_code": { "type": "string" }
            },
            "required": ["zip_code"]
        }
    }
}
]
