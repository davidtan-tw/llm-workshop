from ctransformers import AutoModelForCausalLM
import json


def extract_json3(resume):
    return (
        """
[INST] <<SYS>>
You are an assistant responsible for extracting attributes from unstructured
text and returning them as a valid JSON.
In your response, DO NOT include any text other than the JSON response.
Keys and values should be quoted with "". No trailing commas.

Example: This is a resume, and I'm listing my technical skills:
- Fruits: Apple, Banana, Coconut
- Raw Vegetables: Lettuce, Cabbage, Zucchini, Carrots (Diced, Sliced)

The response should then be in the format:
{
    "technical_skills":
      {
        {
            "fruits": ["Apple", "Banana", "Coconut"],
            "raw_vegetables": ["Lettuce", "Cabbage", "Zucchini", "Carrots (Diced, Sliced)"]
        }
    }
}

<</SYS>>"""
        + f"""

Extract technical skills from the given document using only information in
the following document:

{resume}

Only include the JSON response.
[/INST]
"""
    )


@given("I am looking for a Java developer")
def step_impl(context):
    context.llm = AutoModelForCausalLM.from_pretrained(
        "TheBloke/Llama-2-7B-Chat-GGML",
        model_file="llama-2-7b-chat.ggmlv3.q4_0.bin",
        model_type="llama",
        # lib='avx2', for cpu use
        gpu_layers=110,  # 110 for 7b, 130 for 13b,
        context_length=2048,
        reset=True,
        threads=8,
        top_k=20,
        top_p=0.95,
        max_new_tokens=1000,
        repetition_penalty=1.1,
        temperature=0.1,
        stream=False,
    )

    context.expected_skills = {
    "technical_skills": {
        "languages": ["Java", "Python", "JavaScript", "C#"],
        "web": ["HTML5", "CSS3", "Bootstrap", "React", "Angular", "Node.js"],
        "mobile": ["Android (Java, Kotlin)", "iOS (Swift)"],
    }
}

@when("I evaluate the resume of {name}")
def step_impl(context, name):
    resume_file_name = name.lower().replace(" ", "_")+ ".txt"
    with open(resume_file_name, "r") as f:
        resume = f.read()
        
    context.actual_skills = json.loads(context.llm(extract_json3(resume)))

    print(context.actual_skills)

@then("the resume needs to have the Java language")
def step_impl(context):
    assert "Java" in context.actual_skills["technical_skills"]["languages"]

@then("the resume needs to have web experience")
def step_impl(context):
    assert "web" in context.actual_skills["technical_skills"].keys()
    
