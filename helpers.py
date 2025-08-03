from cs50 import SQL

# Connect to the database
db = SQL("sqlite:///database/climatelens.db")

def lookup_emissions(product):
    print("Query received:", product)

    try:
        rows = db.execute("SELECT * FROM products WHERE LOWER(name) = ?", product.lower())
        print("SQL Results:", rows)
    except Exception as e:
        print("SQL Error:", e)
        return {
            "extraction": 0,
            "manufacturing": 0,
            "transport": 0,
            "packaging": 0,
            "distribution": 0
        }

    if not rows:
        return {
            "extraction": 0,
            "manufacturing": 0,
            "transport": 0,
            "packaging": 0,
            "distribution": 0
        }

    # Map the emission_score into arbitrary breakdown for now
    total = rows[0]["emission_score"]
    return {
        "extraction": round(total * 0.25, 2),
        "manufacturing": round(total * 0.30, 2),
        "transport": round(total * 0.15, 2),
        "packaging": round(total * 0.20, 2),
        "distribution": round(total * 0.10, 2)
    }

def generate_report(data):
    # Placeholder for future report generation
    pass
