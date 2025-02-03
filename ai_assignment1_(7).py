class RestaurantRecommendationAgent:
    def __init__(self):
        self.available_restaurants = [
            {"name": "Spicy Delight", "cuisine": "Indian", "location": "Downtown", "budget": "Medium"},
            {"name": "Sushi Zen", "cuisine": "Japanese", "location": "Uptown", "budget": "High"},
            {"name": "Pasta Paradise", "cuisine": "Italian", "location": "Midtown", "budget": "Medium"},
            {"name": "Taco Fiesta", "cuisine": "Mexican", "location": "Downtown", "budget": "Low"},
            {"name": "Green Bowl", "cuisine": "Vegan", "location": "Uptown", "budget": "Medium"},
            {"name": "BBQ Haven", "cuisine": "American", "location": "Midtown", "budget": "High"}
        ]
        self.recommended_restaurants = []

    def display_available_restaurants(self):
        print("\nAvailable Restaurants:")
        for idx, restaurant in enumerate(self.available_restaurants, start=1):
            print(f"{idx}. {restaurant['name']} ({restaurant['cuisine']}, {restaurant['location']}, {restaurant['budget']} Budget)")

    def recommend_restaurant(self, criterion, value):
        self.recommended_restaurants = [
            r for r in self.available_restaurants if r[criterion].lower() == value.lower()
        ]

        if self.recommended_restaurants:
            print("\nRecommended Restaurants:")
            for idx, restaurant in enumerate(self.recommended_restaurants, start=1):
                print(f"{idx}. {restaurant['name']} ({restaurant['cuisine']}, {restaurant['location']}, {restaurant['budget']} Budget)")
        else:
            print("\nNo matching restaurants found.")

    def select_recommendation(self, index):
        if 1 <= index <= len(self.recommended_restaurants):
            selected = self.recommended_restaurants[index - 1]
            print(f"\nYou selected: {selected['name']} ({selected['cuisine']}, {selected['location']}, {selected['budget']} Budget)")
        else:
            print("Invalid selection.")

agent = RestaurantRecommendationAgent()

while True:
    print("\nWhat would you like to do?")
    print("1. Display all available restaurants")
    print("2. Get restaurant recommendations")
    print("3. Select a recommended restaurant")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        agent.display_available_restaurants()
    elif choice == '2':
        print("\nWould you like recommendations based on:")
        print("1. Cuisine")
        print("2. Location")
        print("3. Budget")
        filter_choice = input("Enter your choice: ")

        if filter_choice == '1':
            value = input("Enter preferred cuisine (Indian, Japanese, Italian, Mexican, Vegan, American): ")
            agent.recommend_restaurant("cuisine", value)
        elif filter_choice == '2':
            value = input("Enter preferred location (Downtown, Uptown, Midtown): ")
            agent.recommend_restaurant("location", value)
        elif filter_choice == '3':
            value = input("Enter budget (Low, Medium, High): ")
            agent.recommend_restaurant("budget", value)
        else:
            print("Invalid choice.")

    elif choice == '3':
        if agent.recommended_restaurants:
            index = int(input("Enter the number of the restaurant you want to select: "))
            agent.select_recommendation(index)
        else:
            print("No recommendations available. Please get recommendations first.")
    elif choice == '4':
        print("Thank you for using the restaurant recommendation agent!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
