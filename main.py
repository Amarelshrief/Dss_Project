# Import necessary modules for colored console output
from colorama import Fore, Style

# Function to collect user input for alternatives and market states
def get_user_input():
    # Prompt the user to enter the number of alternatives
    num_alternatives = int(input(f"{Fore.YELLOW}Enter the number of alternatives: {Style.RESET_ALL}"))
    # Prompt the user to enter the number of market states
    num_states = int(input(f"{Fore.YELLOW}Enter the number of market states: {Style.RESET_ALL}"))

    # Initialize an empty table to store user input
    table = []
    # Loop through each alternative
    for i in range(num_alternatives):
        # Prompt the user to enter the name of each alternative
        alternative = [input(f"{Fore.CYAN}Enter the name of Alternative {i + 1}: {Style.RESET_ALL}")]
        # Loop through each market state for the current alternative
        for j in range(num_states):
            # Prompt the user to enter the expected value for the alternative in the current market state
            value = input(f"{Fore.CYAN}Enter the expected value for Alternative {i + 1} in State {j + 1}: {Style.RESET_ALL}")
            # Call parse_value to convert input to float and handle empty values
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

# Function implementing Maximax criterion
def maximax(alternatives):
    # Find the maximum payoff for each alternative
    max_values = [max(alt[1:]) for alt in alternatives]
    # Find the index of the alternative with the highest maximum payoff
    max_index = max_values.index(max(max_values))
    # Print the reasoning behind the decision
    print(f"{'#' * 5} {Fore.YELLOW}Maximax criterion: Selecting the alternative with the highest maximum payoff. {'#' * 5}")
    print(f"{'#' * 5} {Fore.CYAN}Reasoning: Maximax criterion assumes the best-case scenario by selecting the alternative with the highest potential payoff. {'#' * 5}")
    # Return the alternative index with 1 added (for 1-based indexing)
    return max_index + 1

# Function implementing Maximin criterion
def maximin(alternatives):
    # Find the minimum payoff for each alternative
    min_values = [min(alt[1:]) for alt in alternatives]
    # Find the index of the alternative with the highest minimum payoff
    max_index = min_values.index(max(min_values))
    # Print the reasoning behind the decision
    print(f"{'#' * 5} {Fore.YELLOW}Maximin criterion: Selecting the alternative with the highest minimum payoff. {'#' * 5}")
    print(f"{'#' * 5} {Fore.CYAN}Reasoning: Maximin criterion assumes the worst-case scenario by selecting the alternative with the highest guaranteed minimum payoff. {'#' * 5}")
    # Return the alternative index with 1 added (for 1-based indexing)
    return max_index + 1

# Function implementing Hurwicz criterion
def hurwicz(alternatives, alpha):
    # Calculate a weighted average of maximum and minimum payoffs for each alternative
    weighted_values = [(alpha * max(alt[1:]) + (1 - alpha) * min(alt[1:])) for alt in alternatives]
    # Find the index of the alternative with the highest weighted average payoff
    max_index = weighted_values.index(max(weighted_values))
    # Print the reasoning behind the decision
    print(f"{'#' * 5} {Fore.YELLOW}Hurwicz criterion (alpha={alpha}): Selecting the alternative with the highest weighted average payoff. {'#' * 5}")
    print(f"{'#' * 5} {Fore.CYAN}Reasoning: Hurwicz criterion balances between optimism and pessimism by considering a weighted average of maximum and minimum payoffs. {'#' * 5}")
    # Return the alternative index with 1 added (for 1-based indexing)
    return max_index + 1

# Function implementing Equally Likely criterion
def equally_likely(alternatives):
    # Calculate the average payoff for each alternative
    avg_values = [sum(alt[1:]) / len(alt[1:]) for alt in alternatives]
    # Find the index of the alternative with the highest average payoff
    max_index = avg_values.index(max(avg_values))
    # Print the reasoning behind the decision
    print(f"{'#' * 5} {Fore.YELLOW}Equally Likely criterion: Selecting the alternative with the highest average payoff. {'#' * 5}")
    print(f"{'#' * 5} {Fore.CYAN}Reasoning: Equally Likely criterion assumes equal probabilities for each market state and selects the alternative with the highest average payoff. {'#' * 5}")
    # Return the alternative index with 1 added (for 1-based indexing)
    return max_index + 1

# Function implementing Minimax Regret criterion
def minimax_regret(alternatives):
    # Find the maximum payoff for each alternative
    max_values = [max(alt[1:]) for alt in alternatives]
    # Create a regret table by subtracting each alternative's payoff from the maximum payoff
    regret_table = [[max_value - value for value in alt[1:]] for alt, max_value in zip(alternatives, max_values)]
    # Find the maximum regret for each alternative
    max_regrets = [max(regret) for regret in regret_table]
    # Find the index of the alternative with the smallest maximum regret
    max_index = max_regrets.index(min(max_regrets))
    # Print the reasoning behind the decision
    print(f"{'#' * 5} {Fore.YELLOW}Minimax Regret criterion: Selecting the alternative with the smallest maximum regret. {'#' * 5}")
    print(f"{'#' * 5} {Fore.CYAN}Reasoning: Minimax Regret criterion minimizes the maximum regret by considering the difference between each alternative's payoff and the maximum payoff in each market state. {'#' * 5}")
    # Return the alternative index with 1 added (for 1-based indexing)
    return max_index + 1

# Main function
def main():
    # Get user input table
    user_table = get_user_input()

    # Print results for each decision criterion
    print(f"{'#' * 5} {Fore.GREEN}Maximax choice: {Fore.RED}Alternative {maximax(user_table)}{Style.RESET_ALL} {'#' * 5}")
    print(f"{'#' * 5} {Fore.GREEN}Maximin choice: {Fore.RED}Alternative {maximin(user_table)}{Style.RESET_ALL} {'#' * 5}")
    # Prompt the user to enter the coefficient of optimism for the Hurwicz criterion
    alpha = float(input(f"{Fore.YELLOW}Enter the coefficient of optimism (alpha) for the Hurwicz criterion: {Style.RESET_ALL}"))
    # Print result for the Hurwicz criterion with the specified coefficient of optimism
    print(f"{'#' * 5} {Fore.GREEN}Hurwicz choice (alpha={alpha}): Alternative {hurwicz(user_table, alpha)}{Style.RESET_ALL} {'#' * 5}")
    print(f"{'#' * 5} {Fore.GREEN}Equally likely choice: {Fore.RED}Alternative {equally_likely(user_table)}{Style.RESET_ALL} {'#' * 5}")
    print(f"{'#' * 5} {Fore.GREEN}Minimax regret choice: {Fore.RED}Alternative {minimax_regret(user_table)}{Style.RESET_ALL} {'#' * 5}")

# Entry point of the program
if __name__ == "__main__":
    main()