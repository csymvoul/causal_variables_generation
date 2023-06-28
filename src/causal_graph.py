from causallearn.search.ConstraintBased.FCI import fci 
from causallearn.utils.GraphUtils import GraphUtils
from causallearn.graph.Graph import Graph
from pandas import DataFrame
import numpy as np

class CausalGraph():
    def __init__(self, 
                 initial_data_array = None, 
                 class_used: bool = False, 
                 no_d_sep: bool = False, 
                 remove_common_causes: bool = False, 
                 independence_test: str = "fisherz"
                 ) -> None:
        self.initial_data_array = initial_data_array
        self.class_used = class_used
        self.no_d_sep = no_d_sep
        self.remove_common_causes = remove_common_causes
        self.independence_test = independence_test
        self.class_used_str = ""
        self.no_d_sep_str = ""
        self.data = initial_data_array.data
        self.target = initial_data_array.target
        self.dataset_title = initial_data_array.filename.replace(".csv", "").replace(".gz", "")
        self.features = initial_data_array.feature_names
        self.G = None
        self.edges = None
        self.nodes = None
        self.pdy = None
        self.path = "figures/"
        self.figure_file_extension = ".png"

    def set_data(self) -> None:
        self.data = self.initial_data_array.data

    def get_data(self) -> DataFrame:
        return self.data

    def set_target(self) -> None:
        self.target = self.initial_data_array.target

    def get_target(self) -> DataFrame:
        return self.target
    
    def set_dataset_title(self) -> None:
        self.dataset_title = self.initial_data_array.filename.replace(".csv", "").replace(".gz", "")

    def set_features(self) -> None:
        self.features = self.initial_data_array.feature_names

    def set_class_used(self, class_used) -> None:
        self.class_used = class_used
    
    def set_no_d_sep(self, no_d_sep) -> None:
        self.no_d_sep = no_d_sep
    
    def set_remove_common_causes(self, remove_common_causes) -> None:
        self.remove_common_causes = remove_common_causes
    
    def set_independence_test(self, independence_test) -> None:
        self.independence_test = independence_test
    
    def get_graph(self) -> Graph:
        return self.G

    def get_edges(self):
        return self.edges
    
    def get_nodes(self):
        return self.nodes

    def create_graph(self) -> None:
        # self.set_data()
        # self.set_target()
        # self.set_dataset_title()
        # self.set_features()

        if self.class_used:
            self.data = np.column_stack((self.initial_data_array.data, self.initial_data_array.target))
            self.features = np.append(self.features, "class")
            self.class_used_str = "_with_class"
        self.G, self.edges = fci(self.data, self.independence_test)
        self.pdy = GraphUtils.to_pydot(self.G)
        self.nodes = self.G.nodes

        if self.no_d_sep:
            for edge in self.edges:
                if str(edge.get_endpoint1()) == "CIRCLE" and str(edge.get_endpoint2()) == "CIRCLE":
                    self.edges.remove(edge)
            self.no_d_sep = True
            self.no_d_sep_str = "_no_d_separation"
        self.__remove_ancestor_edges()
        self.__remove_common_causal_effect_edges()
        self.__remove_cirle_edges()
    
    def __remove_cirle_edges(self) -> None:
        for edge in self.edges:
            if str(edge.get_endpoint1()) == "CIRCLE":
                self.edges.remove(edge)
        for edge in self.edges:
            if str(edge.get_endpoint2()) == "CIRCLE":
                self.edges.remove(edge)

    def __remove_ancestor_edges(self) -> None:
        for edge in self.edges:
            if str(edge.get_endpoint1()) == "CIRCLE" or str(edge.get_endpoint2()) == "CIRCLE":
                self.edges.remove(edge)
        for edge in self.edges:
            if str(edge.get_endpoint1()) == "CIRCLE":
                self.edges.remove(edge)
    
    def __remove_common_causal_effect_edges(self) -> None:
        for edge in self.edges:
            if str(edge.get_endpoint1()) == "ARROW" and str(edge.get_endpoint2()) == "ARROW":
                self.edges.remove(edge)
        for edge in self.edges:
            if str(edge.get_endpoint1()) == "ARROW" and str(edge.get_endpoint2()) == "ARROW":
                self.edges.remove(edge)
        for edge in self.edges:
            if str(edge.get_endpoint1()) == "ARROW" and str(edge.get_endpoint2()) == "ARROW":
                self.edges.remove(edge)
    
    def __replace_node_numbers_to_names(self) -> None:
        for i, node in enumerate(self.nodes):
            node.set_name(self.features[int(node.get_name().replace("X", "")) - 1])
            self.nodes[i] = node
        self.pdy = GraphUtils.to_pydot(self.G, edges=self.edges)

    def save_graph_as_figure(self) -> None:
        self.__replace_node_numbers_to_names()
        self.pdy.write_png(self.path + self.independence_test + "_" +self.dataset_title + self.class_used_str + self.no_d_sep_str + self.figure_file_extension)
        



