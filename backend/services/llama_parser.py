from transformers import pipeline

# Mocked pipeline for demo; replace with actual local LLaMA2 path
parser_model = pipeline("text-generation", model="path/to/llama2")

def parse_constraints(constraints_list):
    parsed = {}
    for constraint in constraints_list:
        prompt = f"""
You are a scheduling assistant. Given this constraint:
"{constraint}"
Extract:
- staff name
- unavailable dates
- max_shifts
Return as a Python dictionary.
"""
        try:
            output = parser_model(prompt, max_new_tokens=100)[0]['generated_text']
            parsed.update(eval(output))  # Caution: Use safer parsing in prod
        except:
            continue
    return parsed