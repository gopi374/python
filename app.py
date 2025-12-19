import google.generativeai as genai

# Configure with your API key
genai.configure(api_key="")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content
response = model.generate_content("Explain how AI works")
print(response.text)
