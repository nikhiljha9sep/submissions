def multiply_matrix(input_matrix):
    # Create a copy of the input matrix to avoid modifying the original DataFrame
    modified_matrix = input_matrix.copy()

    # Apply the specified logic to each value in the DataFrame
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round the values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

# Example usage:
# Assuming result_matrix is the DataFrame obtained from Question 1
modified_result_matrix = mu
