import os

# 🔹 Try importing Groq safely
try:
    from groq import Groq
    USE_LLM = True
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
except Exception:
    USE_LLM = False


# 🔹 Rule-based mapping (PRIMARY)
def rule_based_mapping(df):
    mapping = []

    for col in df.columns:
        col_lower = col.lower()

        if any(k in col_lower for k in ["temp", "temperature"]):
            mapping.append((col, "TEMP", "Temperature", "F"))

        elif any(k in col_lower for k in ["sys", "systolic"]):
            mapping.append((col, "SYSBP", "Systolic Blood Pressure", "mmHg"))

        elif any(k in col_lower for k in ["dia", "diastolic"]):
            mapping.append((col, "DIABP", "Diastolic Blood Pressure", "mmHg"))

        elif any(k in col_lower for k in ["pulse", "heart", "rate"]):
            mapping.append((col, "PULSE", "Pulse Rate", "beats/min"))

    return mapping


# 🔹 LLM fallback (SECONDARY)
def llm_mapping(columns):
    if not USE_LLM:
        return None

    try:
        prompt = f"""
You are a clinical data expert.

Map these columns to SDTM Vital Signs (VS domain).
Return ONLY Python list of tuples like:
[("column_name", "TESTCD", "TEST", "UNIT")]

Columns:
{columns}
"""

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
        )

        content = response.choices[0].message.content

        # ⚠️ risky but acceptable for controlled output
        mapping = eval(content)

        return mapping

    except Exception as e:
        print("LLM failed:", e)
        return None


# 🔹 MAIN AGENT FUNCTION
def infer_mapping(df):
    # Step 1: rule-based
    mapping = rule_based_mapping(df)

    if mapping:
        return mapping, "rule-based"

    # Step 2: fallback to LLM
    mapping = llm_mapping(df.columns.tolist())

    if mapping:
        return mapping, "llm"

    # Step 3: fail gracefully
    return [], "none"