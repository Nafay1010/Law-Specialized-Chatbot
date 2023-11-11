import wolframalpha

# Function to compute a mathematical problem using Wolfram Alpha
def compute_formula_with_wolfram(formula, **parameters):
    # Your Wolfram Alpha App ID
    app_id = '44X2XG-T5K5ULARUK'
    client = wolframalpha.Client(app_id)

    # Construct the query by substituting the parameters into the formula
    query = formula
    for param, value in parameters.items():
        query = query.replace(str(param), str(value))

    try:
        # Making the query to Wolfram Alpha
        res = client.query(query)

        # Initialize an empty list to collect the plaintext results
        results = []

        # Processing the response
        for pod in res.pods:
            for sub in pod.subpods:
                if hasattr(sub, 'plaintext') and sub.plaintext:
                    results.append(sub.plaintext)

        # Join all the results into a single string
        response_string = '\n'.join(results)
        return response_string

    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
formula = "2x^2+y+Sin(α)"
parameters = {
    'x': "3",
    'y': "4",
    'α': "90"
}

# formula = "n ≥ ((Cxy - μ × Cz)×m×g)/(2 × μ × sin(α)× Ft)× fs"
# parameters = {
#     'Cxy': '0.8',
#     'μ': '0.6',
#     'Cz': '1',
#     'm': '1000',
#     'g': '9.81',
#     'α': '65',
#     'Ft' : '5000',
#     'fs': '1.25'
# }

# formula = "n ≥ (m×g× (Cx×h-Cz×1))/(2× sin(α)× Ft×1)×fs"
# parameters = {
#     'm': '1000',
#     'g': '9.81',
#     'Cx' : '0.8',
#     'h': '1.2',
#     'Cz': '1',
#     'α': '65',
#     'Ft': '5000',
#     'fs': '1.25'
# }

result = compute_formula_with_wolfram(formula, **parameters)
print(result)
