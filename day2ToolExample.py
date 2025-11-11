from google import genai
from google.genai.types import Tool, GenerateContentConfig, HttpOptions, UrlContext

client = genai.Client(http_options=HttpOptions(api_version="v1"))
model_id = "gemini-2.5-flash"

url_context_tool = Tool(url_context = UrlContext)
url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/70679/simple-whole-roasted-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=(f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}"),
    config=GenerateContentConfig(
        tools=[url_context_tool],
        response_modalities=["TEXT"],
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# For verification, you can inspect the metadata to see which URLs the
# model retrieved
    print(response.candidates[0].url_context_metadata)