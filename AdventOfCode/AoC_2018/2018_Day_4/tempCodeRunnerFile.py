    if sleepiest_guard in sleepiest_min_dict:
        # Find the highest value in the inner dictionary for the sleepiest guard
        highest_value_sleepiest_guard = max(sleepiest_min_dict[sleepiest_guard].values())  # Get the maximum value in the inner dictionary
        # Find the minute(s) associated with the highest value
        minutes_with_highest_value_sleepiest_guard = [minute for minute, value in sleepiest_min_dict[sleepiest_guard].items() if value == highest_value_sleepiest_guard]
        
        # Convert list of minutes into a space-separated string
        minutes_str = ' '.join(map(str, minutes_with_highest_value_sleepiest_guard))

        # Print the results
        print(f"Guard {sleepiest_guard} was asleep most during minute(s) {minutes_str} on {highest_value_sleepiest_guard} days")