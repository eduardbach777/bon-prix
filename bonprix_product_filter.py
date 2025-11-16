
products = [
    {"id": 1, "name": "Schwarzes T-Shirt", "category": "Oberteile", "size": "M", "color": "Schwarz", "price": 19.99, "popularity": 85},
    {"id": 2, "name": "Blaue Jeans", "category": "Hosen", "size": "L", "color": "Blau", "price": 49.99, "popularity": 92},
    {"id": 3, "name": "Rotes Kleid", "category": "Kleider", "size": "S", "color": "Rot", "price": 39.99, "popularity": 78},
    {"id": 4, "name": "Weißes Hemd", "category": "Oberteile", "size": "M", "color": "Weiß", "price": 29.99, "popularity": 65},
    {"id": 5, "name": "Grüne Jacke", "category": "Jacken", "size": "L", "color": "Grün", "price": 89.99, "popularity": 71},
    {"id": 6, "name": "Schwarze Hose", "category": "Hosen", "size": "M", "color": "Schwarz", "price": 44.99, "popularity": 88},
    {"id": 7, "name": "Gelbes Top", "category": "Oberteile", "size": "S", "color": "Gelb", "price": 24.99, "popularity": 60},
    {"id": 8, "name": "Blaues Kleid", "category": "Kleider", "size": "M", "color": "Blau", "price": 54.99, "popularity": 95},
    {"id": 9, "name": "Graue Jacke", "category": "Jacken", "size": "XL", "color": "Grau", "price": 79.99, "popularity": 82},
    {"id": 10, "name": "Rosa T-Shirt", "category": "Oberteile", "size": "S", "color": "Rosa", "price": 17.99, "popularity": 73},
    {"id": 11, "name": "Schwarze Jacke", "category": "Jacken", "size": "L", "color": "Schwarz", "price": 99.99, "popularity": 90},
    {"id": 12, "name": "Weiße Jeans", "category": "Hosen", "size": "M", "color": "Weiß", "price": 39.99, "popularity": 68},
]


def search_products(search_term):
    """Search for products by name"""
    if not search_term:
        return products
    
    search_term = search_term.lower()
    results = []
    
    for product in products:
        if search_term in product["name"].lower() or search_term in product["category"].lower():
            results.append(product)
    
    return results


def filter_by_size(product_list, size):
    """Filter products by size"""
    if not size:
        return product_list
    
    filtered = []
    for product in product_list:
        if product["size"] == size:
            filtered.append(product)
    
    return filtered


def filter_by_color(product_list, color):
    """Filter products by color"""
    if not color:
        return product_list
    
    filtered = []
    for product in product_list:
        if product["color"].lower() == color.lower():
            filtered.append(product)
    
    return filtered


def filter_by_price_range(product_list, min_price=None, max_price=None):
    """Filter products by price range"""
    filtered = []
    
    for product in product_list:
        price = product["price"]
        
        # Check if price is within range
        if min_price is not None and price < min_price:
            continue
        if max_price is not None and price > max_price:
            continue
        
        filtered.append(product)
    
    return filtered


def sort_products(product_list, sort_by="name"):
    """Sort products by different criteria"""
    if sort_by == "price_low":
        return sorted(product_list, key=lambda x: x["price"])
    elif sort_by == "price_high":
        return sorted(product_list, key=lambda x: x["price"], reverse=True)
    elif sort_by == "popularity":
        return sorted(product_list, key=lambda x: x["popularity"], reverse=True)
    else:
        # Default: nach name
        return sorted(product_list, key=lambda x: x["name"])


def display_products(product_list):
    """Display products in a nice format"""
    if not product_list:
        print("\n❌ Keine Produkte gefunden.")
        return
    
    print(f"\n📦 {len(product_list)} Produkt(e) gefunden:\n")
    print("-" * 80)
    
    for product in product_list:
        print(f"ID: {product['id']:2d} | {product['name']:20s} | "
              f"Größe: {product['size']:3s} | Farbe: {product['color']:10s} | "
              f"€{product['price']:6.2f} | ⭐ {product['popularity']}")
    
    print("-" * 80)


def main():
    """Main program loop"""
    print("=" * 80)
    print("   🛍️  BON PRIX - Produktfilter System")
    print("=" * 80)
    
    # Alle Produkte
    filtered_products = products.copy()
    
    #  Search input
    search = input("\n🔍 Suchbegriff (Enter für alle): ").strip()
    if search:
        filtered_products = search_products(search)
        print(f"✓ Suche nach: '{search}'")
    
    # Größenfilter
    print("\nVerfügbare Größen: S, M, L, XL")
    size = input("📏 Größe filtern (Enter für alle): ").strip().upper()
    if size:
        filtered_products = filter_by_size(filtered_products, size)
        print(f"✓ Größe: {size}")
    
    # Farbenfilter
    print("\nVerfügbare Farben: Schwarz, Blau, Rot, Weiß, Grün, Gelb, Grau, Rosa")
    color = input("🎨 Farbe filtern (Enter für alle): ").strip()
    if color:
        filtered_products = filter_by_color(filtered_products, color)
        print(f"✓ Farbe: {color}")
    
    #  Preisfilter
    print("\nPreisbereich filtern:")
    min_price_input = input("  💰 Mindestpreis (Enter für keinen): ").strip()
    max_price_input = input("  💰 Maximalpreis (Enter für keinen): ").strip()
    
    min_price = float(min_price_input) if min_price_input else None
    max_price = float(max_price_input) if max_price_input else None
    
    if min_price is not None or max_price is not None:
        filtered_products = filter_by_price_range(filtered_products, min_price, max_price)
        price_range = f"€{min_price or 0} - €{max_price or '∞'}"
        print(f"✓ Preis: {price_range}")
    
    # Sort products
    print("\nSortierung: 1=Name, 2=Preis niedrig, 3=Preis hoch, 4=Beliebtheit")
    sort_choice = input("📊 Sortieren nach (Enter für Name): ").strip()
    
    sort_options = {
        "1": "name",
        "2": "price_low",
        "3": "price_high",
        "4": "popularity"
    }
    
    sort_by = sort_options.get(sort_choice, "name")
    filtered_products = sort_products(filtered_products, sort_by)
    
    #  Ergebnisse Anzeigen
    display_products(filtered_products)
    
    # Resetknopf
    print("\n")
    restart = input("Neue Suche? (j/n): ").strip().lower()
    if restart == "j":
        print("\n" * 2)
        main()
    else:
        print("\n👋 Vielen Dank! Auf Wiedersehen!")


if __name__ == "__main__":
    main()
