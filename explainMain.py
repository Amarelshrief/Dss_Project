# Business and Logic Explanation:
# Start
# |
# |---> Enter number of alternatives and market states
# |
# |---> For each alternative
# |      |
# |      |---> Enter alternative name
# |      |
# |      |---> For each market state
# |             |
# |             |---> Enter expected value
# |
# |---> Maximize based on different criteria
# |
# |---> Display selected alternative for each criterion
# |
# End

# This console app assists decision-making by evaluating various alternatives based on user-inputted expected values.

# The app considers different decision criteria, each providing a unique perspective on selecting the most favorable alternative.

# Function to collect user input:
# - Users input the number of alternatives and market states.
# - For each alternative, users provide the name and expected values for each market state.
# - The app stores this information in a table for analysis.

# Functions implementing decision-making criteria:
# - Maximax: Selects the alternative with the highest maximum payoff, providing an optimistic approach.
# - Maximin: Chooses the alternative with the highest minimum payoff, focusing on risk aversion.
# - Hurwicz: Offers a compromise between optimism and risk aversion, allowing users to specify their optimism coefficient.
# - Equally Likely: Assumes equal likelihood of market states and selects the alternative with the highest average payoff.
# - Minimax Regret: Identifies the alternative with the smallest maximum regret, considering missed opportunities.

# Main function:
# - Gathers user input and displays the results for each decision criterion.
# - Users can make informed decisions based on their risk preferences and the nature of the decision-making scenario.

# Entry point of the program:
# - The main function is executed when the script is run.

# Overall, the app provides a versatile tool for decision-makers, allowing them to explore multiple decision criteria and make informed choices based on their preferences and the nature of the decision context.

# Technical Breakdown Explanation:

# Import necessary modules for colored console output
from colorama import Fore, Style

# Function to collect user input for decision-making
def get_user_input():
    # Prompt the user to enter the number of alternatives and market states
    num_alternatives = int(input(f"{Fore.YELLOW}Enter the number of alternatives: {Style.RESET_ALL}"))
    num_states = int(input(f"{Fore.YELLOW}Enter the number of market states: {Style.RESET_ALL}"))

    # Initialize a table to store user input for alternatives and their expected values in different states
    table = []
    for i in range(num_alternatives):
        # Prompt the user to enter the name of each alternative
        alternative = [input(f"{Fore.CYAN}Enter the name of Alternative {i + 1}: {Style.RESET_ALL}")]
        for j in range(num_states):
            # Prompt the user to enter the expected value for the alternative in the current market state
            value = input(f"{Fore.CYAN}Enter the expected value for Alternative {i + 1} in State {j + 1}: {Style.RESET_ALL}")
            # Convert input to float and handle empty values
            value = parse_value(value)
            # Append the alternative name and its value for the current market state to the table
            alternative.append(value)
        # Append the alternative information to the overall table
        table.append(alternative)

    # Return the completed table containing user input
    return table

# Function to parse user input value and convert it to a float
def parse_value(value):
    # Check if the input value is empty
    if value.strip() == "":
        # If empty, return 0.0
        return 0.0
    else:
        # Replace special characters and convert to float
        value = value.replace('–', '-').replace(',', '')
        # Return the converted float value
        return float(value)

# Functions implementing decision-making criteria:

# Maximax: Choose the alternative with the highest maximum payoff
def maximax(alternatives):
    # Find the maximum payoff for each alternative
    max_values = [max(alt[1:]) for alt in alternatives]
    # Find the index of the alternative with the highest maximum payoff
    max_index = max_values.index(max(max_values))
    # Return the alternative index with 1 added (for 1-based indexing)
    return max_index + 1

# Maximin: Choose the alternative with the highest minimum payoff
def maximin(alternatives):
    # Find the minimum payoff for each alternative
    min_values = [min(alt[1:]) for alt in alternatives]
    # Find the index of the alternative with the highest minimum payoff
    max_index = min_values.index(max(min_values))
    # Return the alternative index with 1 added (for 1-based indexing)
    return max_index + 1

# Hurwicz: A compromise between Maximax and Maximin criteria
def hurwicz(alternatives, alpha):
    # Calculate a weighted average of maximum and minimum payoffs for each alternative
    weighted_values = [(alpha * max(alt[1:]) + (1 - alpha) * min(alt[1:])) for alt in alternatives]
    # Find the index of the alternative with the highest weighted average payoff
    max_index = weighted_values.index(max(weighted_values))
    # Return the alternative index with 1 added (for 1-based indexing)
    return max_index + 1

# Equally Likely: Choose the alternative with the highest average payoff, assuming equal likelihood of market states
def equally_likely(alternatives):
    # Calculate the average payoff for each alternative
    avg_values = [sum(alt[1:]) / len(alt[1:]) for alt in alternatives]
    # Find the index of the alternative with the highest average payoff
    max_index = avg_values.index(max(avg_values))
    # Return the alternative index with 1 added (for 1-based indexing)
    return max_index + 1

# Minimax Regret: Choose the alternative with the smallest maximum regret
def minimax_regret(alternatives):
    # Find the maximum payoff for each alternative
    max_values = [max(alt[1:]) for alt in alternatives]
    # Create a regret table by subtracting each alternative's payoff from the maximum payoff
    regret_table = [[max_value - value for value in alt[1:]] for alt, max_value in zip(alternatives, max_values)]
    # Find the maximum regret for each alternative
    max_regrets = [max(regret) for regret in regret_table]
    # Find the index of the alternative with the smallest maximum regret
    max_index = max_regrets.index(min(max_regrets))
    # Return the alternative index with 1 added (for 1-based indexing)
    return max_index + 1

# Main function to execute the decision-making process
def main():
    # Get user input table for alternatives and expected values
    user_table = get_user_input()

    # Print results for each decision criterion
    print(f"{Fore.GREEN}Maximax choice: {Fore.RED}Alternative {maximax(user_table)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Maximin choice: {Fore.RED}Alternative {maximin(user_table)}{Style.RESET_ALL}")
    # Prompt the user to enter the coefficient of optimism for the Hurwicz criterion
    alpha = float(input(f"{Fore.YELLOW}Enter the coefficient of optimism (alpha) for the Hurwicz criterion: {Style.RESET_ALL}"))
    # Print result for the Hurwicz criterion with the specified coefficient of optimism
    print(f"{Fore.GREEN}Hurwicz choice (alpha={alpha}): Alternative {hurwicz(user_table, alpha)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Equally likely choice: {Fore.RED}Alternative {equally_likely(user_table)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Minimax regret choice: {Fore.RED}Alternative {minimax_regret(user_table)}{Style.RESET_ALL}")

# Entry point of the program
if __name__ == "__main__":
    # Execute the main function
    main()