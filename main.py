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