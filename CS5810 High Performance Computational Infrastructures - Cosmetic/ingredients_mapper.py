import sys
import csv
import string

def ingredient_mapper():
    # Parse input from standard input
    reader = csv.reader(sys.stdin)
    next(reader)  # Skip header row

    # Emit (ingredient, product type, 1) for each non-blank ingredient in specified products
    for row in reader:
        product_type = row[0]
        # Check if the product is a Cleanser, Moisturizer, or Sun protect
        if "Cleanser" in product_type or "Moisturizer" in product_type or "Sun protect" in product_type:
            # Extract ingredients column
            ingredients = row[5].split(',')
            # Emit (ingredient, product type, 1) for each non-blank ingredient
            for ingredient in ingredients:
                ingredient = ingredient.strip().translate(str.maketrans('', '', string.punctuation))
                if ingredient:  # Check if ingredient is not blank
                    print(f"{ingredient}\t{product_type}\t1")

if __name__ == "__main__":
    ingredient_mapper()
