class TechFestExpenses:
    def __init__(self):
        self.num_people = 0
        self.registration_total = 0

    def registration_expenses(self):
        self.num_people = int(input("Enter the number of registered participants: "))
        fee_per_person = float(input("Enter the registration fee per participant: "))
        self.registration_total = self.num_people * fee_per_person
        print(f"Registration Expenses: {self.registration_total}")
        return self.registration_total

    def misc_expenses(self):
        other_costs = float(input("Enter the miscellaneous expenses: "))
        print(f"Miscellaneous Expenses: {other_costs}")
        return other_costs

    def setup_expenses(self):
        lighting_cost = float(input("Enter the lighting and sound costs: "))
        stage_cost = float(input("Enter the stage setup costs: "))
        setup_total = lighting_cost + stage_cost
        print(f"Setup Committee Expenses: {setup_total}")
        return setup_total

    def food_expenses(self):
        meal_cost = float(input("Enter the cost per meal: "))
        meals_count = int(input("Enter the number of meals per day: "))
        fest_days = int(input("Enter the number of fest days: "))
        total_food_cost = self.num_people * meal_cost * meals_count * fest_days
        print(f"Food Expenses: {total_food_cost}")
        return total_food_cost

    def media_expenses(self):
        ad_costs = float(input("Enter the advertisement costs: "))
        promo_cost = float(input("Enter the social media promotion costs: "))
        photo_video_cost = float(input("Enter the photography and videography costs: "))
        media_total = ad_costs + promo_cost + photo_video_cost
        print(f"Media Committee Expenses: {media_total}")
        return media_total

    def green_protocol_expenses(self):
        waste_cost = float(input("Enter waste management costs: "))
        print(f"Green Protocol Expenses: {waste_cost}")
        return waste_cost

    def program_expenses(self):
        concert_count = int(input("Enter the number of concerts: "))
        concert_expense_total = 0

        for concert in range(1, concert_count + 1):
            single_concert_cost = float(input(f"Enter cost for concert {concert}: "))
            concert_expense_total += single_concert_cost

        print(f"Program Committee Expenses: {concert_expense_total} (for {concert_count} concerts)")
        return concert_expense_total

    def calculate_total_expenses(self):
        reg_exp = self.registration_expenses()
        food_total = self.food_expenses()
        setup_total = self.setup_expenses()
        media_total = self.media_expenses()
        green_protocol_total = self.green_protocol_expenses()
        program_total = self.program_expenses()
        misc_total = self.misc_expenses()

        final_total_expense = (reg_exp + food_total + setup_total + media_total + green_protocol_total + program_total + misc_total)
        print(f"Total Tech Fest Expenditure: {final_total_expense}")


tech_fest = TechFestExpenses()
tech_fest.calculate_total_expenses()
