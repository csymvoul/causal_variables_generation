from causallearn.search.ConstraintBased.FCI import fci 
from causallearn.utils.GraphUtils import GraphUtils
from sklearn.datasets import load_breast_cancer
import numpy as np

data = load_breast_cancer().data
target = load_breast_cancer().target
features = load_breast_cancer().feature_names
dataset_title = load_breast_cancer().filename.replace(".csv", "").replace(".gz", "")

class_used = True # Set True if class is used as feature, False otherwise
no_d_sep = True # Set True to remove no d-separation edges, False otherwise
remove_common_causes = False
independence_test = "fisherz" # Set "fisherz" or "chi2"

class_used_str = ""
no_d_sep_str = ""

if class_used:
    # dataset with class as feature
    data = np.column_stack((data, target))
    features = np.append(features, "class")
    class_used_str = "_with_class"
# Default is fisherz
G, edges = fci(data, independence_test)
pdy = GraphUtils.to_pydot(G)

# Convert nodes names to features names
nodes = G.nodes

# Remove no d-separation edges
if no_d_sep:
    for edge in edges:
        if str(edge.get_endpoint1()) == "CIRCLE" and str(edge.get_endpoint2()) == "CIRCLE":
            edges.remove(edge)
    no_d_sep = True
    no_d_sep_str = "_no_d_separation"

# Remove edges were one node is not an ancestor of the other
for edge in edges:
    if str(edge.get_endpoint1()) == "CIRCLE" or str(edge.get_endpoint2()) == "CIRCLE":
        edges.remove(edge)

for edge in edges:
    if str(edge.get_endpoint1()) == "CIRCLE":
        edges.remove(edge)

# Remove edges were latent common cause exists 
# (we need to do this step 4 times to remove all common causes for some reason)
if remove_common_causes:
    for edge in edges:
        if str(edge.get_endpoint1()) == "ARROW" and str(edge.get_endpoint2()) == "ARROW":
            edges.remove(edge)

for node in nodes:
    node.set_name(features[int(node.get_name().replace("X", "")) - 1])

# Create new graph replacing node IDs with features' names
pdy = GraphUtils.to_pydot(G, edges=edges)

# Save graph as png
pdy.write_png('figures/'+independence_test+'_'+dataset_title+class_used_str+no_d_sep_str+'.png')