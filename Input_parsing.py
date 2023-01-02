import re

# Switch to this topic

#Provide relevant questions

# Answer -> Explanation

#Easy, Medium, Hard


def import_full_question_answer(text) -> tuple[str, str]:
    question_pattern = '(?<=Q:)(.*)(?=\\nA:)'
    question = re.findall(question_pattern, text)
    answer = text.split("A:")[-1]
    return (question[0],answer)

def import_question(text) -> str:
    question = text.split("Q:")[1]
    return question

def import_answer(text) -> str:
    answer = text.split("A:")[1]
    return answer

if __name__ == "__main__":
    import_full_question_answer("Q: What did Jennifer Arnold et al (2018) discover about individual differences in pronoun resolution?\nA: Individual differences in pronoun resolution may persist into adulthood, even for simple spoken sentences!\nDifferences may be driven by exposure to written language.")