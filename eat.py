#!/usr/bin/env python3
"""
🍽️  What Should I Eat?
A fun little picker for when you can't decide what to eat.

Usage:
    python3 eat.py            # pick from everything
    python3 eat.py breakfast  # pick from a specific meal
    python3 eat.py list       # show all categories
    python3 eat.py add        # add your own food (interactive)
"""

import json
import os
import random
import sys
import time

# Where we store your custom foods
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "foods.json")

DEFAULT_FOODS = {
    "breakfast": [
        "Pancakes 🥞", "Omelette 🍳", "Cereal 🥣", "Avocado toast 🥑",
        "French toast 🍞", "Smoothie bowl 🥤", "Paratha + chai ☕",
    ],
    "lunch": [
        "Chicken biryani 🍛", "Burger & fries 🍔", "Caesar salad 🥗",
        "Sushi 🍣", "Tacos 🌮", "Pasta 🍝", "Shawarma wrap 🌯",
    ],
    "dinner": [
        "Steak 🥩", "Pizza 🍕", "Ramen 🍜", "Grilled fish 🐟",
        "Butter chicken 🍛", "Stir-fry noodles 🥢", "BBQ platter 🍢",
    ],
    "snack": [
        "Popcorn 🍿", "Fruit bowl 🍓", "Chips & dip 🥔", "Nuts 🥜",
        "Ice cream 🍦", "Chocolate 🍫", "Samosa 🥟",
    ],
}


def load_foods():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return DEFAULT_FOODS


def save_foods(foods):
    with open(DATA_FILE, "w") as f:
        json.dump(foods, f, indent=2)


def drumroll(final, options):
    """Cute slot-machine effect before revealing the pick."""
    for _ in range(12):
        print(f"\r  🎰  {random.choice(options):<28}", end="", flush=True)
        time.sleep(0.08)
    print(f"\r  ✨  {final:<28}")


def pick(foods, category=None):
    if category:
        if category not in foods:
            print(f"❌ No category '{category}'. Try: {', '.join(foods)}")
            return
        options = foods[category]
        label = category
    else:
        options = [item for items in foods.values() for item in items]
        label = "anything"

    print(f"\n🤔 Deciding what to eat ({label})...\n")
    choice = random.choice(options)
    drumroll(choice, options)
    print(f"\n👉 You should eat: {choice}\n")


def add_food(foods):
    print("\n➕ Add your own food!")
    cat = input("   Category (e.g. lunch): ").strip().lower()
    item = input("   Food name: ").strip()
    if not cat or not item:
        print("   Skipped (empty input).")
        return
    foods.setdefault(cat, []).append(item)
    save_foods(foods)
    print(f"   ✅ Added '{item}' to '{cat}'!")


def list_all(foods):
    print("\n📋 All foods:\n")
    for cat, items in foods.items():
        print(f"  {cat.title()}:")
        for it in items:
            print(f"    • {it}")
        print()


def main():
    foods = load_foods()
    arg = sys.argv[1].lower() if len(sys.argv) > 1 else None

    if arg == "list":
        list_all(foods)
    elif arg == "add":
        add_food(foods)
    else:
        pick(foods, arg)


if __name__ == "__main__":
    main()
