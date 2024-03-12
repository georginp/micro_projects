from typing import List, Dict


def calculate_bmi(
    weight: float,
    height: float
) -> float:

    """
    Calculate the Body Mass Index (BMI) given weight in kilograms
    and height in meters.
    """

    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive values.")
    bmi = weight / (height ** 2)
    return bmi


def calculate_calories_burned(
    duration: float
) -> float:

    """
    Calculate the estimated number of calories burned during exercise.
    """

    calories_per_minute = 5
    calories_burnt = duration * calories_per_minute
    return calories_burnt


def filter_overweight_people(
    people_data: List[Dict[str, any]]
) -> List[Dict[str, any]]:

    """
    Filter overweight people based on BMI.
    """

    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 25:
            overweight_people.append(person)
    return overweight_people


def main():
    people_data = []

    print("Enter fitness data for each person (Enter a blank name to finish):")
    while True:
        name = input("Enter person's name(Enter End to finish the program): ").strip()
        if not name or name.lower() == "end":
            break
        weight = float(input("Enter person's weight in kilograms: "))
        if weight <= 0:
            print("Weight must be a positive value. Please enter a valid weight.")
            continue
        height = float(input("Enter person's height in meters: "))
        if height <= 0:
            print("Height must be a positive value. Please enter a valid height.")
            continue
        duration = float(input("Enter exercise duration in minutes: "))
        if duration <= 0:
            print("Duration must be a positive value. Please enter a valid duration.")
            continue
        person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
        people_data.append(person)

    print("\nFitness Analysis:")
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        calories_burned = calculate_calories_burned(person['duration'])
        print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned}")

    overweight_people = filter_overweight_people(people_data)
    print("\nOverweight People:")
    for person in overweight_people:
        bmi = calculate_bmi(person['weight'], person['height'])
        print(f"{person['name']}: BMI = {bmi:.2f}")


if __name__ == "__main__":
    main()
