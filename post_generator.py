from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length: str) -> str:
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"
    return "1 to 5 lines"  # default fallback


def get_prompt(length: str, language: str, tag: str, tone: str, audience: str | None = None) -> str:
    length_str = get_length_str(length)

    prompt = (
        "Generate a LinkedIn post using the below information. No preamble.\n\n"
        f"1) Topic: {tag}\n"
        f"2) Length: {length_str}\n"
        f"3) Language: {language}\n"
        f"4) Tone: {tone}\n"
        "If Language is Hinglish then it means it is a mix of Hindi and English.\n"
        "The script for the generated post should always be English.\n"
    )

    if audience:
        prompt += f"5) Target audience: {audience}\n"

    # Few-shot examples for writing style
    examples = few_shot.get_filtered_posts(length, language, tag)
    if len(examples) > 0:
        prompt += "\nUse the writing style as per the following examples."
        for i, post in enumerate(examples, start=1):
            post_text = post["text"]
            prompt += f"\n\nExample {i}:\n{post_text}"
            if i == 2:  # only first 2 examples
                break

    return prompt


def generate_post(length: str, language: str, tag: str, tone: str, audience: str | None = None) -> str:
    prompt = get_prompt(length, language, tag, tone, audience)
    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    post = generate_post("Medium", "English", "Job Search", "Professional", "early-career jobseekers in tech")
    print(post)
