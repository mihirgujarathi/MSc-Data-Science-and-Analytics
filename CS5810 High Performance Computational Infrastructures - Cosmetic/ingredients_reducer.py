import sys
from collections import defaultdict
import heapq

def ingredient_reducer():
    current_count = defaultdict(int)

    # Parse input from standard input
    for line in sys.stdin:
        # Split the input line into ingredient, product type, and count
        parts = line.strip().split("\t")
        if len(parts) == 3:
            ingredient, product_type, count = parts
            key = (product_type, ingredient)
            current_count[key] += int(count)

    # Structure to hold the top 10 ingredients per product type
    top_ingredients = defaultdict(lambda: [])

    # Extract top 10 for each product type
    for (product_type, ingredient), count in current_count.items():
        heapq.heappush(top_ingredients[product_type], (count, ingredient))
        if len(top_ingredients[product_type]) > 10:
            heapq.heappop(top_ingredients[product_type])

    # Emit the sorted top 10 ingredients per product type
    for product_type, ingredients in top_ingredients.items():
        ingredients.sort(reverse=True)  # Sort descending by count
        print(f"\n===== Top 10 Ingredients for {product_type} =====")
        for count, ingredient in ingredients:
            print(f"{ingredient} --> {count}")
        print("\n")  # Add extra space after each product type list for clarity

if __name__ == "__main__":
    ingredient_reducer()
