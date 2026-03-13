import webbrowser
import random

# Meal options categorized by dietary restrictions
meal_options = {
    "Vegetarian": {
        "Breakfast": [
            ("Avocado Toast with Eggs", "https://youtube.com/shorts/M8N5lZGTW5w"),
            ("Oatmeal with Almonds and Berries", "https://youtube.com/shorts/yEUYT6XFUBE"),
            ("Green Smoothie with Nuts", "https://youtu.be/RFgwlrVu7Ok")
        ],
        "Lunch": [
            ("Chickpea Salad", "https://youtube.com/shorts/GKi2-gQ02LU"),
            ("Quinoa Bowl with Veggies", "https://youtu.be/QJkEs9B34X8"),
            ("Vegetable Stir Fry", "https://youtube.com/shorts/EkQN0xNlFmI")
        ],
        "Dinner": [
            ("Lentil Soup", "https://youtu.be/BR67V-U72s8"),
            ("Grilled Vegetable Wrap", "https://youtube.com/shorts/PZitxXOFcR0"),
            ("Stuffed Bell Peppers", "https://youtube.com/shorts/lTh2gGrLE_E")
        ]
    },
    "Diabetic-Friendly": {
        "Breakfast": [
            ("Greek Yogurt with Nuts", "https://youtube.com/shorts/90c52vcW90o"),
            ("Scrambled Eggs with Spinach", "https://youtube.com/shorts/wbkxtxVLKN0"),
            ("Oatmeal with Berries", "https://youtube.com/shorts/JQpVTS-Mpwg")
        ],
        "Lunch": [
            ("Grilled Chicken Salad", "https://youtube.com/shorts/vNCQLSzFxG0"),
            ("Quinoa and Black Beans", "https://youtu.be/ZJXSgR77l7M"),
            ("Steamed Salmon with Veggies", "https://youtube.com/shorts/aVXTx6gfU8o")
        ],
        "Dinner": [
            ("Baked Salmon with Broccoli", "https://youtube.com/shorts/v9LDBDrsgik"),
            ("Zucchini Noodles with Avocado Pesto", "https://youtu.be/NgPJVJDsySM"),
            ("Tofu Stir-Fry with Steamed Rice", "https://youtube.com/shorts/1mKyIjY1lGA")
        ]
    }
}

# Days of the week
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def generate_weekly_plan(diet):
    """Generate a weekly meal plan and a grocery list."""
    weekly_plan = {}
    grocery_list = set()
    
    print("\n📅 Your Weekly Meal Plan:")
    with open("weekly_meal_plan.txt", "w") as file:
        file.write("Weekly Meal Plan:\n")
        for i, day in enumerate(week_days, start=1):
            breakfast, lunch, dinner = (
                random.choice(meal_options[diet]["Breakfast"]),
                random.choice(meal_options[diet]["Lunch"]),
                random.choice(meal_options[diet]["Dinner"])
            )
            
            weekly_plan[day] = {"Breakfast": breakfast, "Lunch": lunch, "Dinner": dinner}
            
            print(f"\n📅 Day {i} ({day}):")
            print(f"  🍽 Breakfast: {breakfast[0]}")
            print(f"  🍽 Lunch: {lunch[0]}")
            print(f"  🍽 Dinner: {dinner[0]}")
            
            file.write(f"Day {i} ({day}):\n")
            file.write(f"  Breakfast: {breakfast[0]}\n  Lunch: {lunch[0]}\n  Dinner: {dinner[0]}\n\n")
            
            grocery_list.update([breakfast[0], lunch[0], dinner[0]])
    
    print("\n🛒 Your Grocery List:")
    with open("grocery_list.txt", "w") as file:
        file.write("Grocery List:\n")
        for item in grocery_list:
            print(f"  ✅ {item}")
            file.write(f"{item}\n")
    
    print("\n✅ Weekly meal plan saved as 'weekly_meal_plan.txt'!")
    print("✅ Grocery list saved as 'grocery_list.txt'!")
    
    return weekly_plan

# User selects dietary restriction
print("Select your dietary restriction:")
dietary_choices = list(meal_options.keys())
for index, diet in enumerate(dietary_choices, start=1):
    print(f"{index}. {diet}")
choice = int(input("Enter the number of your choice: "))
selected_diet = dietary_choices[choice - 1]

# Ask if user wants a weekly meal plan
weekly_plan_choice = input("\nDo you want a weekly meal plan? (yes/no): ").strip().lower()
if weekly_plan_choice == "yes":
    generate_weekly_plan(selected_diet)
else:
    print("\nWhich meal do you want to select?")
    meal_types = ["Breakfast", "Lunch", "Dinner"]
    for index, meal in enumerate(meal_types, start=1):
        print(f"{index}. {meal}")
    meal_choice = int(input("Enter the number of your choice: "))
    selected_meal_type = meal_types[meal_choice - 1]
    
    meal_list = meal_options[selected_diet].get(selected_meal_type, [])
    print(f"\nAvailable {selected_meal_type} options for {selected_diet}:")
    for index, (meal, _) in enumerate(meal_list, start=1):
        print(f"{index}. {meal}")
    meal_selection = int(input("Enter the number of the meal you want: "))
    selected_meal, selected_meal_link = meal_list[meal_selection - 1]
    
    print(f"\n🍽 Selected {selected_meal_type}: {selected_meal}")
    print(f"📺 Watch here: {selected_meal_link}")
    
    watch_video = input("\nDo you want to watch the YouTube video? (yes/no): ").strip().lower()
    if watch_video == "yes":
        webbrowser.open(selected_meal_link)
        print("\n🎬 Opening YouTube video...")
    else:
        print("\n✅ Skipping video.")