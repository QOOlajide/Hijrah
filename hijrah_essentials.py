# hijrah_essentials.py

# This script builds a Hijrah checklist by pairing categories with specific items
# and includes logic to extract important/essential items using list and dictionary comprehension.

def build_hijrah_pack(categories, items):
    """
    Creates a dictionary of Hijrah essentials from two aligned lists.
    Each category (e.g., 'documents') is matched to an item (e.g., 'passport').

    Args:
        categories (list): List of item categories.
        items (list): List of specific items.

    Returns:
        dict: Dictionary mapping categories to specific items.
    """
    if len(categories) != len(items):
        raise ValueError("The number of categories and items must be equal.")
    
    return {categories[i]: items[i] for i in range(len(categories))}


# Lists of categories and specific items for Hijrah preparation
categories = ["drink", "food", "shoes", "clothing", "documents", "currency", "medicine", "spiritual"]
items = ["water bottle", "dates", "comfortable sandals", "3 thobes", "passport", "USD and SAR", "first aid kit", "Qur’an"]

# Create the dictionary of Hijrah essentials
hijrah_pack = build_hijrah_pack(categories, items)

# Print the full packing list
print("🧳 Hijrah Packing List:")
# for category, item in hijrah_pack.items():
#     print(f"- {category.title()}: {item}")
print(hijrah_pack.items())

print("\n🛑 Critical Items Only:")

# Use dictionary comprehension to filter and display critical items
critical_categories = ["documents", "currency", "medicine", "spiritual"]
critical_items = {cat: hijrah_pack[cat] for cat in critical_categories if cat in hijrah_pack}

# Display only critical items
print(critical_items.items())
