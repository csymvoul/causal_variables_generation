# Towards causal features generation using interaction variables


The steps are the following: 
1. Identify the causal relationships: Analyze the edges of the causal graph obtained from the PC algorithm to identify the causal relationships between variables. Each edge represents a causal relationship, where the tail variable influences the head variable.
2. Determine the direction of causality: Determine the direction of causality based on the direction of the edges in the causal graph. For example, if there is an edge from variable A to variable B, it indicates that A causally influences B.
3. Create new causal variables: Based on the identified causal relationships, you can create new variables by applying causal transformations to the existing variables. Here are a few examples:
    1. Interaction variables: If variable A causally influences variable B and you want to capture the interaction effect, you can create an interaction variable by multiplying A and B.
    2. Derived variables: You can create derived variables by applying mathematical operations or transformations to the existing variables. For instance, if variable A causally influences variable B, you can create a derived variable C as the square or logarithm of B.
    3. Lagged variables: If variable A causally influences variable B over time, you can create a lagged variable of B to capture the temporal effect.
    4. Difference variables: If variable A causally influences variable B, you can create a difference variable by subtracting the lagged value of B from the current value of B. This can capture the change in B due to A.
4. Incorporate new variables into the analysis: Once you have created the new causal variables, you can incorporate them into your analysis or modeling pipeline. These variables can provide additional insights or improve the predictive performance of your models by capturing the causal relationships present in the data.

Remember that creating new causal variables requires domain knowledge and understanding of the underlying causal relationships. It is essential to carefully consider the causal mechanisms and interpret the new variables in the context of your specific problem domain.