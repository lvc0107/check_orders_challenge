import argparse


# small DB sample
class PluralMapping:
    WORDS = [
        {
            "singular": "soda",
            "plural": "sodas"
        },
        {
            "singular": "drink",
            "plural": "drinks"
        },
        {
            "singular": "pizza",
            "plural": "pizzas"
        }
    ]

    @classmethod
    def find_singular_word(cls, word):
        # TODO in next implemetation this search should be query against a DB
        for mapping in cls.WORDS:
            if word == mapping.get("singular"):
                return mapping

    @classmethod
    def find_plural_word(cls, word):
        # TODO in next implemetation this search should be query against a DB
        for mapping in cls.WORDS:
            if word == mapping.get("plural"):
                return mapping


class SinonymMapping:
    WORDS = {
        "soda": "drink",
        "drink": "soda",
    }

    @classmethod
    def find_synonym(cls, order):
        if order.is_plural:
            singular_word = cls.WORDS.get(order.item_singular)
            mapping = PluralMapping().find_singular_word(singular_word)
            return mapping.get("plural")
        else:
            return cls.WORDS.get(order.item_singular)


class Orders:
    def __init__(self, amount_items, item_singular, item_plural, description, is_plural):
        self.amount_items = int(amount_items)
        self.item_singular = item_singular
        self.item_plural = item_plural
        self.description = description
        if self.amount_items == 1:
            self.is_plural = False
        else:
            self.is_plural = is_plural

    def create_order(self):
        # TODO in a next implementation this object should be stored in a DB
        if self.is_plural:
            return f'{self.amount_items} {self.description} {self.item_plural}'
        else:
            return f'{self.amount_items} {self.description} {self.item_singular}'

    def __repr__(self):
        if self.is_plural:
            return f'Orders(amount_item={self.amount_items}, description={self.description}, item={self.item_plural}'
        else:
            return f'Orders(amount_item={self.amount_items}, description={self.description}, item={self.item_singular}'


def parse_orders(orders):
    order_objects = []
    for order in orders:
        parse_order = order.split(" ")  # list of token
        amount_item = parse_order.pop(0)
        for i, word in enumerate(parse_order):
            mapping = PluralMapping.find_singular_word(word)
            if mapping:
                parse_order.pop(i)
                description = " ".join(parse_order)
                order_objects.append(
                    Orders(amount_item, mapping.get("singular"), mapping.get("plural"), description, is_plural=False))
                break

            mapping = PluralMapping.find_plural_word(word)
            if mapping:
                parse_order.pop(i)
                description = " ".join(parse_order)
                order_objects.append(
                    Orders(amount_item, mapping.get("singular"), mapping.get("plural"), description, is_plural=True))
                break

    return order_objects


def update_existing_item(current_order_objects, current_item, new_item):
    if new_item.description == current_item.description:
        current_item.amount_items = new_item.amount_items
        return
    current_item.amount_items -= new_item.amount_items
    if current_item.amount_items == 1:
        current_item.is_plural = False
    if current_item.amount_items == 0:
        current_order_objects.remove(current_item)
    current_order_objects.append(new_item)


def update_orders(current_order_objects, new_order_objects):
    for new_item in new_order_objects:
        new_item_found = False
        for current_item in current_order_objects:
            if new_item.item_singular and new_item.item_singular in current_item.item_plural:
                new_item_found = True
                update_existing_item(current_order_objects, current_item, new_item)
                break
            elif new_item.item_plural and new_item.item_plural in current_item.item_plural:
                new_item_found = True
                update_existing_item(current_order_objects, current_item, new_item)
                break

            synonym = SinonymMapping.find_synonym(new_item)
            if synonym and synonym in current_item.item_plural:
                if new_item.is_plural:
                    new_item.item_plural = synonym
                else:
                    new_item.item_singular = synonym
                new_item_found = True
                update_existing_item(current_order_objects, current_item, new_item)
                break

        if not new_item_found:
            current_order_objects.append(new_item)


def serialize(current_order_objects):
    new_check = []
    for item in current_order_objects:
        new_check.append(item.create_order())
    return new_check


def change_check(current_order, new_order):
    new_order_objects = parse_orders(new_order)
    current_order_objects = parse_orders(current_order)

    update_orders(current_order_objects, new_order_objects)
    new_check = serialize(current_order_objects)

    return new_check


def test():
    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["1 soda regular"])
    print(new_check)
    assert new_check == ["2 large pepperoni pizzas", "2 sugar free sodas", "1 regular soda"]

    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["1 sodas regular"])
    print(new_check)
    assert new_check == ["2 large pepperoni pizzas", "2 sugar free sodas", "1 regular soda"]

    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["2 sodas regular"])
    print(new_check)
    assert new_check == ["2 large pepperoni pizzas", "1 sugar free soda", "2 regular sodas"]

    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["3 sodas regular"])
    print(new_check)
    assert new_check == ["2 large pepperoni pizzas", "3 regular sodas"]

    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["3 sugar free sodas"])
    print(new_check)
    assert new_check == ["2 large pepperoni pizzas", "3 sugar free sodas"]

    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["1 drink regular"])
    print(new_check)
    assert new_check == ["2 large pepperoni pizzas", "2 sugar free sodas", "1 regular soda"]

    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["1 drinks regular"])
    print(new_check)
    assert new_check == ["2 large pepperoni pizzas", "2 sugar free sodas", "1 regular soda"]

    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["1 regular soda"])
    print(new_check)
    assert new_check == ["2 large pepperoni pizzas", "2 sugar free sodas", "1 regular soda"]

    new_order = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["1 regular sodas"])
    print(new_check)
    assert new_order == ["2 large pepperoni pizzas", "2 sugar free sodas", "1 regular soda"]

    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["1 regular drink"])
    print(new_check)
    assert new_check == ["2 large pepperoni pizzas", "2 sugar free sodas", "1 regular soda"]

    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["1 regular drinks"])
    print(new_check)
    assert new_check == ["2 large pepperoni pizzas", "2 sugar free sodas", "1 regular soda"]

    new_check = change_check(["2 large pepperoni pizzas", "3 sugar free sodas"], ["1 regular drinks", "1 large pepperoni pizzas"])
    print(new_check)
    assert new_check == ["1 large pepperoni pizzas", "2 sugar free sodas", "1 regular soda"]


if __name__ == "__main__":
    CLI = argparse.ArgumentParser()
    CLI.add_argument(
        "--check",
        nargs="*",
        type=str,
        default=[],
    )
    CLI.add_argument(
        "--new_order",
        nargs="*",
        type=str,
        default=[],
    )
    args = CLI.parse_args()
    print(f"check: {args.check}")
    print(f"new_order: {args.new_order}")

    new_check = change_check(args.check, args.new_order)
    print(new_check)
    test()
