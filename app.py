# Flask Web App - Product Filter for Bon Prix
# Run with: python app.py

from flask import Flask, render_template, request

app = Flask(__name__)

# Product data - would normally be in a database
PRODUCTS = [
    {"id": 1, "name": "Schwarzes T-Shirt", "category": "Oberteile", "size": "M", "color": "Schwarz", "price": 19.99, "popularity": 85, "image": "tshirt.jpg"},
    {"id": 2, "name": "Blaue Jeans", "category": "Hosen", "size": "L", "color": "Blau", "price": 49.99, "popularity": 92, "image": "jeans.jpg"},
    {"id": 3, "name": "Rotes Kleid", "category": "Kleider", "size": "S", "color": "Rot", "price": 39.99, "popularity": 78, "image": "dress.jpg"},
    {"id": 4, "name": "Weißes Hemd", "category": "Oberteile", "size": "M", "color": "Weiß", "price": 29.99, "popularity": 65, "image": "shirt.jpg"},
    {"id": 5, "name": "Grüne Jacke", "category": "Jacken", "size": "L", "color": "Grün", "price": 89.99, "popularity": 71, "image": "jacket.jpg"},
    {"id": 6, "name": "Schwarze Hose", "category": "Hosen", "size": "M", "color": "Schwarz", "price": 44.99, "popularity": 88, "image": "pants.jpg"},
    {"id": 7, "name": "Gelbes Top", "category": "Oberteile", "size": "S", "color": "Gelb", "price": 24.99, "popularity": 60, "image": "top.jpg"},
    {"id": 8, "name": "Blaues Kleid", "category": "Kleider", "size": "M", "color": "Blau", "price": 54.99, "popularity": 95, "image": "dress2.jpg"},
    {"id": 9, "name": "Graue Jacke", "category": "Jacken", "size": "XL", "color": "Grau", "price": 79.99, "popularity": 82, "image": "jacket2.jpg"},
    {"id": 10, "name": "Rosa T-Shirt", "category": "Oberteile", "size": "S", "color": "Rosa", "price": 17.99, "popularity": 73, "image": "tshirt2.jpg"},
    {"id": 11, "name": "Schwarze Jacke", "category": "Jacken", "size": "L", "color": "Schwarz", "price": 99.99, "popularity": 90, "image": "jacket3.jpg"},
    {"id": 12, "name": "Weiße Jeans", "category": "Hosen", "size": "M", "color": "Weiß", "price": 39.99, "popularity": 68, "image": "jeans2.jpg"},
    {"id": 13, "name": "Blaues T-Shirt", "category": "Oberteile", "size": "L", "color": "Blau", "price": 22.99, "popularity": 77, "image": "tshirt3.jpg"},
    {"id": 14, "name": "Rote Jacke", "category": "Jacken", "size": "M", "color": "Rot", "price": 94.99, "popularity": 84, "image": "jacket4.jpg"},
    {"id": 15, "name": "Schwarzes Kleid", "category": "Kleider", "size": "L", "color": "Schwarz", "price": 59.99, "popularity": 91, "image": "dress3.jpg"},
]


def filter_products(search="", size="", color="", min_price=None, max_price=None, sort_by="name"):
    """Apply all filters and sorting to products"""
    
    # Start with all products
    results = PRODUCTS.copy()
    
    # Apply search filter
    if search:
        search = search.lower()
        results = [p for p in results if search in p["name"].lower() or search in p["category"].lower()]
    
    # Apply size filter
    if size:
        results = [p for p in results if p["size"] == size]
    
    # Apply color filter
    if color:
        results = [p for p in results if p["color"].lower() == color.lower()]
    
    # Apply price range filter
    if min_price is not None:
        results = [p for p in results if p["price"] >= min_price]
    
    if max_price is not None:
        results = [p for p in results if p["price"] <= max_price]
    
    # Apply sorting
    if sort_by == "price_low":
        results.sort(key=lambda x: x["price"])
    elif sort_by == "price_high":
        results.sort(key=lambda x: x["price"], reverse=True)
    elif sort_by == "popularity":
        results.sort(key=lambda x: x["popularity"], reverse=True)
    else:
        results.sort(key=lambda x: x["name"])
    
    return results


@app.route("/")
def index():
    """Main page with product filtering"""
    
    # Get filter parameters from URL
    search = request.args.get("search", "")
    size = request.args.get("size", "")
    color = request.args.get("color", "")
    sort_by = request.args.get("sort", "name")
    
    # Get price range
    min_price_str = request.args.get("min_price", "")
    max_price_str = request.args.get("max_price", "")
    
    min_price = float(min_price_str) if min_price_str else None
    max_price = float(max_price_str) if max_price_str else None
    
    # Filter products
    products = filter_products(search, size, color, min_price, max_price, sort_by)
    
    # Get unique sizes and colors for filter dropdowns
    all_sizes = sorted(set(p["size"] for p in PRODUCTS))
    all_colors = sorted(set(p["color"] for p in PRODUCTS))
    
    return render_template("index.html", 
                         products=products,
                         all_sizes=all_sizes,
                         all_colors=all_colors,
                         current_search=search,
                         current_size=size,
                         current_color=color,
                         current_sort=sort_by,
                         current_min_price=min_price_str,
                         current_max_price=max_price_str)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
