from src.states.blog_state import BlogState

class BlogNode:
    """
    A class to represent the blog node"""

    def __init__(self, llm):
        self.llm= llm

    def title_creation(self,state:BlogState):
        """
        create the title for the blog
        
        """
        if "topic" in state and state["topic"]:
            prompt="""
                You are an expert blog content wroter. Use Markdown Formatting. Generate a blog title for the {topic}. This title should be creative and SEO Friendly 
                """
            
            system_messages= prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_messages)

            return {"blog": {"title":response.content}}     
        
    
    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt = """You are expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the {topic}"""
            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']['title'], "content": response.content}}