# Towards causal features generation using interaction variables


The steps are the following: 
1. __Identify the causal relationships:__ Analyze the edges of the causal graph obtained from the FCI algorithm to identify the causal relationships between variables. Each edge represents a causal relationship, where the tail variable influences the head variable.
2. __Determine the direction of causality:__ Determine the direction of causality based on the direction of the edges in the causal graph. For example, if there is an edge from variable A to variable B, it indicates that A causally influences B.
3. __Create new causal variables:__ Based on the identified causal relationships, you can create new variables by applying causal transformations to the existing variables. Here are a few examples:
    1. __Interaction variables:__ If variable A causally influences variable B and you want to capture the interaction effect, you can create an interaction variable by multiplying A and B. 
        - This approach is suitable when you suspect that the interaction between two variables is important and may have a causal effect. By multiplying the values of two causally related variables, you create a new variable that captures the combined effect of both variables. This can be useful in cases where the interaction effect is expected to play a significant role.
    2. __Derived variables:__ You can create derived variables by applying mathematical operations or transformations to the existing variables. For instance, if variable A causally influences variable B, you can create a derived variable C as the square or logarithm of B. 
        - Derived variables involve applying mathematical operations or transformations to existing variables to capture specific relationships. For example, taking the square or logarithm of a variable can help capture non-linear relationships that may have a causal effect. This approach can be beneficial when you have prior knowledge or hypotheses about the functional form of the causal relationship.
    3. __Lagged variables:__ If variable A causally influences variable B over time, you can create a lagged variable of B to capture the temporal effect. 
        - Lagged variables are relevant when you suspect a causal relationship between variables that operates over time. By creating lagged versions of variables, you capture the temporal effect and potential time lags in the causal relationship. This approach is suitable for studying phenomena where the effect of a variable in the past influences the outcome in the present or future.
    4. __Difference variables:__ If variable A causally influences variable B, you can create a difference variable by subtracting the lagged value of B from the current value of B. This can capture the change in B due to A. 
        - Difference variables involve subtracting the lagged value of a variable from its current value. This captures the change or difference in the variable over time, allowing you to examine the causal effect of an intervention or treatment. This approach is useful when you want to assess the impact of a specific change or manipulation in a variable on the outcome.
4. __Incorporate new variables into the analysis:__ Once you have created the new causal variables, you can incorporate them into your analysis or modeling pipeline. These variables can provide additional insights or improve the predictive performance of your models by capturing the causal relationships present in the data.

Remember that creating new causal variables requires domain knowledge and understanding of the underlying causal relationships. It is essential to carefully consider the causal mechanisms and interpret the new variables in the context of your specific problem domain.

If you are interested please consider citing our article:

@ARTICLE{SymvoulidisMobilityDataPlacement,
  author={Symvoulidis, Chrysostomos and Kiourtis, Athanasios and Marinos, George and Tom-Ata, Jean-Didier Totow and Manias, George and Mavrogiorgou, Argyro and Kyriazis, Dimosthenis},
  journal={IEEE Transactions on Computers}, 
  title={A User Mobility-based Data Placement Strategy in a Hybrid Cloud / Edge Environment using a Causal-aware Deep Learning Network}, 
  year={2023},
  volume={},
  number={},
  pages={1-14},
  publisher={IEEE},
  doi={10.1109/TC.2023.3311921}
}
