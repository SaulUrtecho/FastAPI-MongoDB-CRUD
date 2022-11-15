

def car_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "url": item["url"],
        "model": item["model"],
        "color": item["color"],
        "year": item["year"]
    }

def cars_entity(entity) -> list:
    return [car_entity(item) for item in entity]