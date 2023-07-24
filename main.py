from causallearn.search.ConstraintBased.FCI import fci 
from causallearn.utils.GraphUtils import GraphUtils
from sklearn.datasets import load_breast_cancer
import numpy as np
from src.causal_graph import CausalGraph
from src.model import Model

initial_data = load_breast_cancer()

# Causal variables generation
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
causal_graph.save_df_as_csv()

# Dataset selection
causal_df = causal_graph.get_causal_df()
df = causal_graph.get_df()

selected_df = causal_df

# Model training and evaluation
model = Model(data=selected_df)
model.preprocess_data()
model.split_data()
model.fit()
model.predict()
predictions = model.get_predictions()
y_test = model.get_y_test()
print("------------------------------------\n")
print("Model predictions:\n")
print(f"Predictions: \n{predictions}\n")
print(f"y_test: \n{y_test.to_numpy()}")
print("------------------------------------\n")
print("Model metrics:\n")
model.calculate_accuracy()
accuracy = model.get_accuracy()
print(f"Accuracy: \t{accuracy}")

model.calculate_precision()
precision = model.get_precision()
print(f"Precision: \t{precision}")

model.calculate_recall()
recall = model.get_recall()
print(f"Recall: \t{recall}")

model.calculate_f1()
f1 = model.get_f1()
print(f"F1: \t{f1}")

model.calculate_confusion_matrix()
confusion_matrix = model.get_confusion_matrix()
print(f"Confusion matrix: \n{confusion_matrix}")

model.calculate_roc_auc()
roc_auc = model.get_roc_auc()
print(f"ROC AUC: \t{roc_auc}")
print("------------------------------------")