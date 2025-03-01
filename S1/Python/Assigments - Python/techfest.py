def registration_expenses():
    people_registered = int(input("Enter the number of registered participants: "))
    fee_per_person = float(input("Enter the registration fee per participant: "))
    registration_total = people_registered * fee_per_person
    print(f"Registration Expenses: {registration_total}")
    return registration_total, people_registered

def misc_expenses():
    other_costs = float(input("Enter the miscellaneous expenses: "))
    print(f"Miscellaneous Expenses: {other_costs}")
    return other_costs


def setup_expenses():
    lighting_cost = float(input("Enter the lighting and sound costs: "))
    stage_cost = float(input("Enter the stage setup costs: "))
    setup_total = lighting_cost + stage_cost
    print(f"Setup Committee Expenses: {setup_total}")
    return setup_total


def food_expenses(num_people):
    meal_cost = float(input("Enter the cost per meal: "))
    meals_count = int(input("Enter the number of meals per day: "))
    fest_days = int(input("Enter the number of fest days: "))
    total_food_cost = num_people * meal_cost * meals_count * fest_days
    print(f"Food Expenses: {total_food_cost}")
    return total_food_cost


def media_expenses():
    ad_costs = float(input("Enter the advertisement costs: "))
    promo_cost = float(input("Enter the social media promotion costs: "))
    photo_video_cost = float(input("Enter the photography and videography costs: "))
    media_total = ad_costs + promo_cost + photo_video_cost
    print(f"Media Committee Expenses: {media_total}")
    return media_total


def green_protocol_expenses():
    waste_cost = float(input("Enter waste management costs: "))
    print(f"Green Protocol Expenses: {waste_cost}")
    return waste_cost


def program_expenses():
    concert_count = int(input("Enter the number of concerts: "))
    concert_expense_total = 0  

    for concert in range(1, concert_count + 1):
        single_concert_cost = float(input(f"Enter cost for concert {concert}: "))
        concert_expense_total += single_concert_cost

    print(f"Program Committee Expenses: {concert_expense_total} (for {concert_count} concerts)")
    return concert_expense_total



def main():
    reg_exp, num_people = registration_expenses()
    food_total = food_expenses(num_people)
    setup_total = setup_expenses()
    media_total = media_expenses()
    green_protocol_total = green_protocol_expenses()
    program_total = program_expenses()
    misc_total = misc_expenses()

    final_total_expense = reg_exp + food_total + setup_total + media_total + green_protocol_total + program_total + misc_total
    print(f"Total Tech Fest Expenditure: {final_total_expense}")


main()
