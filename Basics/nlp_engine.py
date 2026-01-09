import spacy
import re
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Pattern: "marks of Abin"
matcher.add("MARKS_OF", [
    [{"LOWER": {"IN": ["mark", "marks", "score", "result", "grade"]}},
     {"LOWER": "of"},
     {"ENT_TYPE": "PERSON"}]
])

# Pattern: "Abin marks"
matcher.add("NAME_MARKS", [
    [{"ENT_TYPE": "PERSON"},
     {"LOWER": {"IN": ["mark", "marks", "score", "result", "grade"]}}]
])


def parse_query(text):
    doc = nlp(text)

    # ==== 1. Student name extraction ====
    student = None

    # a) SpaCy PERSON entities
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            student = ent.text.title()
    print(student)

    # b) Pattern matching (more accurate)
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        for token in span:
            if token.ent_type_ == "PERSON":
                student = token.text.title()

    # c) Fallback regex
    fallback = re.search(r"(?:of|for)\s+([A-Za-z]+)", text.lower())
    if fallback and not student:
        student = fallback.group(1).title()

    # d) Fallback first-word assumption
    first = text.split()[0]
    if student is None and first.isalpha():
        student = first.title()

    # ==== 2. Semester extraction ====
    sem = None
    sem_re = re.search(r"(?:sem|semester)\s*([0-9]+)", text.lower())
    if sem_re:
        sem = sem_re.group(1)

    # ==== 3. Department extraction ====
    dept_map = {
        "computer science": "Computer Science",
        "cs": "Computer Science",
        "cse": "Computer Science",
        "mechanical": "Mechanical",
        "me": "Mechanical",
        "civil": "Civil",
        "ce": "Civil",
        "electronics": "Electronics",
        "ece": "Electronics",
        "eee": "Electronics"
    }

    dept = None
    text_low = text.lower()
    for key, val in dept_map.items():
        if key in text_low:
            dept = val

    # ==== 4. Intent classification ====
    mark_keywords = ["mark", "marks", "result", "score", "grade"]
    detail_keywords = ["detail", "info", "information"]
    dept_keywords = ["department", "dept"]

    if any(k in text_low for k in mark_keywords):
        intent = "get_marks"
    elif any(k in text_low for k in detail_keywords):
        intent = "get_student"
    elif any(k in text_low for k in dept_keywords):
        intent = "get_department"
    else:
        intent = "unknown"

    return {
        "intent": intent,
        "student": student,
        "semester": sem,
        "department": dept
    }
