from decimal import Decimal

from django.utils.text import slugify

from apps.products.models import Category, Brand, Product


categories = {
    "Laptops": "laptops",
    "Smartphones": "smartphones",
    "Monitors": "monitors",
    "Gaming": "gaming",
    "Accessories": "accessories",
    "Headphones": "headphones",
    "Smartwatches": "smartwatches",
}

brands = {
    "Apple": "apple",
    "Samsung": "samsung",
    "Sony": "sony",
    "Logitech": "logitech",
    "ASUS": "asus",
    "Dell": "dell",
    "HP": "hp",
}


for name, slug in categories.items():
    Category.objects.get_or_create(
        name=name,
        defaults={"slug": slug},
    )


for name, slug in brands.items():
    Brand.objects.get_or_create(
        name=name,
        defaults={"slug": slug},
    )


products = [
    {
        "name": "MacBook Air M4",
        "description": "Lightweight Apple laptop with M4 chip, long battery life and high resolution display.",
        "price": Decimal("295000"),
        "category": "Laptops",
        "brand": "Apple",
        "tags": ["laptop", "apple", "m4", "productivity"],
        "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8",
    },
    {
        "name": "MacBook Pro M4",
        "description": "Powerful Apple professional laptop designed for developers, creators and demanding workloads.",
        "price": Decimal("450000"),
        "category": "Laptops",
        "brand": "Apple",
        "tags": ["laptop", "apple", "m4", "professional"],
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853",
    },
    {
        "name": "Dell XPS 15",
        "description": "Premium Dell laptop with powerful performance, high resolution display and professional design.",
        "price": Decimal("280000"),
        "category": "Laptops",
        "brand": "Dell",
        "tags": ["laptop", "dell", "premium", "professional"],
        "image": "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6",
    },
    {
        "name": "HP Spectre x360",
        "description": "Premium convertible laptop designed for productivity, portability and everyday professional work.",
        "price": Decimal("260000"),
        "category": "Laptops",
        "brand": "HP",
        "tags": ["laptop", "hp", "convertible", "productivity"],
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853",
    },
    {
        "name": "iPhone 17",
        "description": "Premium Apple smartphone with powerful processor, advanced camera and high quality display.",
        "price": Decimal("320000"),
        "category": "Smartphones",
        "brand": "Apple",
        "tags": ["smartphone", "apple", "iphone", "premium"],
        "image": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd",
    },
    {
        "name": "Samsung Galaxy S25",
        "description": "Flagship Samsung smartphone with advanced camera, powerful processor and premium display.",
        "price": Decimal("240000"),
        "category": "Smartphones",
        "brand": "Samsung",
        "tags": ["smartphone", "samsung", "android", "flagship"],
        "image": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf",
    },
    {
        "name": "Samsung Galaxy Ultra",
        "description": "Large premium Samsung smartphone built for photography, productivity and high performance.",
        "price": Decimal("310000"),
        "category": "Smartphones",
        "brand": "Samsung",
        "tags": ["smartphone", "samsung", "ultra", "camera"],
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9",
    },
    {
        "name": "Apple Watch Series",
        "description": "Smartwatch with fitness tracking, notifications and seamless Apple ecosystem integration.",
        "price": Decimal("120000"),
        "category": "Smartwatches",
        "brand": "Apple",
        "tags": ["smartwatch", "apple", "fitness", "wearable"],
        "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12",
    },
    {
        "name": "Samsung Galaxy Watch",
        "description": "Modern smartwatch with fitness tracking, health features and Android ecosystem integration.",
        "price": Decimal("95000"),
        "category": "Smartwatches",
        "brand": "Samsung",
        "tags": ["smartwatch", "samsung", "fitness", "wearable"],
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30",
    },
    {
        "name": "Sony WH-1000XM6",
        "description": "Premium wireless headphones with advanced noise cancellation and high quality audio.",
        "price": Decimal("95000"),
        "category": "Headphones",
        "brand": "Sony",
        "tags": ["headphones", "sony", "wireless", "noise cancelling"],
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e",
    },
    {
        "name": "Sony WH-CH720N",
        "description": "Affordable wireless noise cancelling headphones for everyday listening.",
        "price": Decimal("45000"),
        "category": "Headphones",
        "brand": "Sony",
        "tags": ["headphones", "sony", "wireless", "budget"],
        "image": "https://images.unsplash.com/photo-1484704849700-f032a568e944",
    },
    {
        "name": "Sony Wireless Headphones",
        "description": "Comfortable Sony wireless headphones designed for music, entertainment and daily use.",
        "price": Decimal("60000"),
        "category": "Headphones",
        "brand": "Sony",
        "tags": ["headphones", "sony", "wireless", "music"],
        "image": "https://images.unsplash.com/photo-1583394838336-acd977736f90",
    },
    {
        "name": "Logitech MX Master 4",
        "description": "Advanced wireless productivity mouse designed for developers and professionals.",
        "price": Decimal("35000"),
        "category": "Accessories",
        "brand": "Logitech",
        "tags": ["mouse", "logitech", "wireless", "productivity"],
        "image": "https://images.unsplash.com/photo-1527814050087-3793815479db",
    },
    {
        "name": "Logitech MX Mechanical",
        "description": "Premium wireless mechanical keyboard designed for productivity and programming.",
        "price": Decimal("38000"),
        "category": "Accessories",
        "brand": "Logitech",
        "tags": ["keyboard", "logitech", "mechanical", "productivity"],
        "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3",
    },
    {
        "name": "Logitech G Pro Keyboard",
        "description": "Mechanical gaming keyboard designed for competitive gaming and fast response time.",
        "price": Decimal("32000"),
        "category": "Gaming",
        "brand": "Logitech",
        "tags": ["keyboard", "logitech", "gaming", "mechanical"],
        "image": "https://images.unsplash.com/photo-1541140532154-b024d705b90a",
    },
    {
        "name": "ASUS TUF Gaming 27",
        "description": "Gaming monitor with high refresh rate and fast response time for competitive gaming.",
        "price": Decimal("85000"),
        "category": "Monitors",
        "brand": "ASUS",
        "tags": ["monitor", "asus", "gaming", "high refresh rate"],
        "image": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf",
    },
    {
        "name": "ASUS Gaming Laptop",
        "description": "High performance ASUS gaming laptop designed for gaming, development and demanding applications.",
        "price": Decimal("280000"),
        "category": "Gaming",
        "brand": "ASUS",
        "tags": ["laptop", "asus", "gaming", "performance"],
        "image": "https://images.unsplash.com/photo-1603302576837-37561b2e2302",
    },
    {
        "name": "Dell UltraSharp Monitor",
        "description": "Professional Dell monitor with high resolution display designed for developers and creators.",
        "price": Decimal("110000"),
        "category": "Monitors",
        "brand": "Dell",
        "tags": ["monitor", "dell", "professional", "4k"],
        "image": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf",
    },
    {
        "name": "Samsung Gaming Monitor",
        "description": "Fast Samsung gaming monitor with high refresh rate and immersive display.",
        "price": Decimal("90000"),
        "category": "Monitors",
        "brand": "Samsung",
        "tags": ["monitor", "samsung", "gaming", "display"],
        "image": "https://images.unsplash.com/photo-1593640408182-31c70c8268f5",
    },
    {
        "name": "Apple AirPods Pro",
        "description": "Premium wireless earbuds with active noise cancellation and seamless Apple device integration.",
        "price": Decimal("75000"),
        "category": "Accessories",
        "brand": "Apple",
        "tags": ["earbuds", "apple", "wireless", "noise cancelling"],
        "image": "https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1",
    },
]


for data in products:
    category = Category.objects.get(
        name=data["category"]
    )

    brand = Brand.objects.get(
        name=data["brand"]
    )

    Product.objects.update_or_create(
        slug=slugify(data["name"]),
        defaults={
            "name": data["name"],
            "description": data["description"],
            "price": data["price"],
            "category": category,
            "brand": brand,
            "tags": data["tags"],
            "image": data["image"],
            "is_active": True,
        },
    )


print(
    f"Seed complete. Total products: "
    f"{Product.objects.count()}"
)