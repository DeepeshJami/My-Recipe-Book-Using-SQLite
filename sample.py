import sqlite3

def add_sample_recipes():
    sample_recipes = [
        ("Chocolate Cake", "Rich and moist chocolate cake", "Mix ingredients, bake for 45 minutes.", 5, "45 mins", "Flour, sugar, cocoa, baking powder, eggs, milk"),
        ("Spaghetti Carbonara", "Creamy pasta with bacon and cheese", "Cook pasta, fry bacon, mix with egg and cheese.", 4, "30 mins", "Pasta, bacon, eggs, parmesan cheese"),
        ("Caesar Salad", "Classic salad with a creamy dressing", "Toss lettuce with dressing, croutons, and cheese.", 4, "20 mins", "Romaine lettuce, croutons, Caesar dressing, parmesan cheese"),
        ("Beef Stroganoff", "Rich and creamy beef and mushroom sauce", "Brown beef, add mushrooms and sauce, serve with pasta.", 4, "1 hour", "Beef, mushrooms, sour cream, onion, garlic, butter, pasta"),
        ("Chicken Tikka Masala", "Spicy and creamy Indian chicken dish", "Marinate and grill chicken, cook with masala sauce.", 5, "1 hour", "Chicken, yogurt, tomato sauce, spices"),
        ("Vegetable Stir Fry", "Quick and healthy stir-fried vegetables", "Stir-fry assorted vegetables, add sauce, serve with rice.", 3, "25 mins", "Bell peppers, broccoli, carrots, soy sauce, rice"),
        ("Lemon Drizzle Cake", "Light and zesty lemon cake", "Bake lemon-flavored cake, drizzle with lemon syrup.", 4, "50 mins", "Flour, sugar, lemon, eggs, butter"),
        ("Guacamole", "Fresh and creamy avocado dip", "Mash avocados, mix with lime, onion, and seasoning.", 5, "10 mins", "Avocado, lime, onion, cilantro, salt"),
        ("Banana Bread", "Moist bread with ripe bananas", "Mix ingredients, bake until golden brown.", 4, "1 hour 10 mins", "Bananas, flour, sugar, butter, eggs, baking soda"),
        ("Tomato Soup", "Classic and comforting tomato soup", "Simmer tomatoes with broth, blend until smooth.", 4, "45 mins", "Tomatoes, onion, garlic, vegetable broth, cream")
    ]

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.executemany('INSERT INTO recipes (title, description, procedure, rating, time_taken, ingredients) VALUES (?, ?, ?, ?, ?, ?)', sample_recipes)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_sample_recipes()
    print("Sample recipes added to the database.")
