from causallearn.search.ConstraintBased.FCI import fci 
from causallearn.utils.GraphUtils import GraphUtils
from sklearn.datasets import load_breast_cancer
import numpy as np
from src.causal_graph import CausalGraph

initial_data = load_breast_cancer()

causal_graph = CausalGraph(initial_data_array=initial_data, 
                           class_used=True, 
                           no_d_sep=False, 
                           remove_common_causes=False, 
                           independence_test="fisherz")
causal_graph.create_graph()
causal_graph.save_graph_as_figure()
causal_graph.save_graph_as_dot()

causal_graph.get_causal_relations()
# causal_dataset = causal_graph.get_data_with_causal_variables()
print(f"Initial DataFrame shape: {causal_graph.get_df().shape}")
print(f"Causal DataFrame shape:  {causal_graph.get_causal_df().shape}")
causal_graph.save_causal_df_as_csv()