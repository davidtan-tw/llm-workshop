from ctransformers import AutoModelForCausalLM
import json
import os
from pathlib import Path


def final_extract_json(resume):
    return (
        """
[INST] <<SYS>>
You are an assistant responsible for extracting attributes from unstructured
text and returning them as a valid JSON.
In your response, DO NOT include any text other than the JSON response.
Keys and values should be quoted with "". No trailing commas. Keys in lowercase snake_type.

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

This is just an example. Your response should not contain any fruits or vegetables, only applicant skills.

<</SYS>>"""
        + f"""

Extract technical skills from the given document using only information in
the following document:

{resume}

Only include the JSON response.
[/INST]
"""
    )


@given("I am evaluating a resume")
def step_impl(context):
    context.llm = AutoModelForCausalLM.from_pretrained(
        #"TheBloke/Llama-2-7B-Chat-GGML",
        Path("/Users/oege/.cache/huggingface/hub/models--TheBloke--Llama-2-7B-Chat-GGML/snapshots/76cd63c351ae389e1d4b91cab2cf470aab11864b/"),
        model_file="llama-2-7b-chat.ggmlv3.q4_0.bin",
        model_type="llama",
        # lib='avx2', for cpu use
        gpu_layers=110,  # 110 for 7b, 130 for 13b,
        context_length=4096,
        reset=True,
        top_k=20,
        top_p=0.95,
        max_new_tokens=1000,
        repetition_penalty=1.1,
        temperature=0.1,
        stream=False,
    )

@when("I evaluate the resume of {name}")
def step_impl(context, name):
    resume_file = name.lower().replace(" ", "_")+ ".txt"
    with open(Path().cwd()/"features"/"resources"/resume_file) as f:
        resume = f.read()
        
    context.json_resume = json.loads(context.llm(final_extract_json(resume)))
    print(context.json_resume)

@then("the applicant should have technical skills")
def step_impl(context):
    assert "technical_skills" in context.json_resume

@then("the applicant should know the {language} language")
def step_impl(context, language):
    assert "languages" in context.json_resume["technical_skills"]
    assert language in context.json_resume["technical_skills"]["languages"]

@then("the applicant should have {skill} experience")
def step_impl(context, skill):
    assert skill in context.json_resume["technical_skills"]
