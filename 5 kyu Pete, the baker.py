recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}


def cakes(recipe):
    num_cakes = []
    try:
        for k, v in recipe.items():
            num_cakes.append(available.get(k) // v)
        return min(num_cakes)
    except TypeError:
        return 0
# return min(available.get(k, 0)/recipe[k] for k in recipe)


print(cakes(recipe))
