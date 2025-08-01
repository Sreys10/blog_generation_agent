from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
from src.states.blog_state import BlogState
from src.nodes.blog_node import BlogNode


class GraphBuilder:
    def __init__(self, llm):
        self.llm=llm
        self.graph= StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate blogs based on the topic"""
        
        self.blog_node_obj= BlogNode()

        ##nodes
        self.graph.add_node("title_creation",self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_node_obj.content_generation)

        ##edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph