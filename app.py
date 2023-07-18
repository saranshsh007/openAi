import openai

openai.api_type = "azure"

openai.api_version = "2023-05-15"

openai.api_base = "https://ai-training0.openai.azure.com/" 

openai.api_key = "ad32fb199aab424f8ccc264b8ac08bec"

class LLM:
    def __init__(self) :
        self.keywords = None
        self.description = None
        self.product = None
    def generate_keywords(self,product):
        query1 = f"""Generate keywords for the properties of a product:\n{product}\n\nSome sample keywords are product type, weight, cost, dimensions, color whereas other keywords may vary depending on what the product is."""
        
        response1 = openai.Completion.create(
            engine="GPT3-5",
            prompt=query1,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        return response1.choices[0].text.strip()

    def create_keyword_value_dictionary(self,keywords, description):
        query2 = f"""use the keywords:\n{keywords}\ngenerated to create a dictionary for keywords and values where values can be found in the description:\n{description}\n\nIf there are no values for the specification of the product show null against the specification."""
        
        response2 = openai.Completion.create(
            engine="GPT3-5",
            prompt=query2,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        return response2.choices[0].text.strip()

if __name__ == "__main__":

    product = input("Enter product: ")
    analyzer = LLM()
    res = analyzer.generate_keywords(product)
    print(res)
    description = input("Enter description of product: ")
    output = analyzer.create_keyword_value_dictionary(res,description)
    print(output)