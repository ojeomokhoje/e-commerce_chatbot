import requests
import json
from openai import OpenAI
from functions import ( 
    make_purchase, order_items, check_order_status,
    cancel_order, search_category, apply_discount, get_shipping_info
)
from tools import tools
from dotenv import load_dotenv
load_dotenv()

session = requests.Session()
FASTAPI_URL = os.getenv("FASTAPI_URL")

client = OpenAI(
    api_key= os.getenv("OPENAI_API_KEY"),
    base_url= os.getenv("base_url")
)

system_prompt = """
You are a helpful e-commerce assistant. Your job is to:

- Help users find products and place orders.
- Use function calls when needed:
    - order_items: Fetch details about products (e.g., price, availability).
    - make_purchase: Process a purchase after confirming with the user.
    - check_order_status: Provide updates on order status.
    - cancel_order: Cancel an existing order.
    - search_category: Help user explore product categories.
    - apply_discount: Apply available promo codes.
    - get_shipping_info: Provide estimated delivery times by ZIP.

Be clear and concise—ask for missing details (e.g., size, quantity) before acting.
Always confirm before charging (e.g., "Ready to buy [Product] for $X?").
"""

conversation = [{"role": "system", "content": system_prompt}]

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat. Goodbye!")
        break

    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=conversation,
        model="granite3.3:8b",
        tools=tools,
        tool_choice="auto"
    )

    assistant_reply = response.choices[0].message.content
    if assistant_reply:
        print(f"Assistant: {assistant_reply}")
        conversation.append({"role": "assistant", "content": assistant_reply})

    if response.choices[0].message.tool_calls:
        for tool_call in response.choices[0].message.tool_calls:
            tool_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            # Dispatch to correct function
            tool_result = None
            if tool_name == "make_purchase":
                tool_result = make_purchase(**args)
            elif tool_name == "order_items":
                tool_result = order_items(**args)
            elif tool_name == "check_order_status":
                tool_result = check_order_status(**args)
            elif tool_name == "cancel_order":
                tool_result = cancel_order(**args)
            elif tool_name == "search_category":
                tool_result = search_category(**args)
            elif tool_name == "apply_discount":
                tool_result = apply_discount(**args)
            elif tool_name == "get_shipping_info":
                tool_result = get_shipping_info(**args)

            if tool_result:
                print(f"Tool result for {tool_name}: {tool_result}")
                conversation.append({"role": "function", "name": tool_name, "content": json.dumps(tool_result)})
