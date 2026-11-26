from html import escape

import streamlit as st


def get_grade(mark: int) -> str:
    """Return a letter grade for a mark from 0 to 100."""
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "F"


st.set_page_config(page_title="Student Grade Manager", page_icon="🎓")
st.title("Student Grade Manager")
st.caption("Add students and track class results.")
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap');

    .stApp {
        background:
            radial-gradient(ellipse at 12% 0%, rgba(99, 102, 241, .12), transparent 34%),
            #f6f7fb;
        color: #182230;
        font-family: 'DM Sans', sans-serif;
    }
    .block-container { max-width: 980px; padding-top: 3rem; padding-bottom: 4rem; }
    h1, h2, h3 { font-family: 'Manrope', sans-serif !important; color: #172033; }
    h1 { letter-spacing: -1.5px; }
    [data-testid="stCaptionContainer"] p { color: #687386; font-size: 1rem; }
    [data-testid="stForm"] {
        background: rgba(255, 255, 255, .92);
        border: 1px solid #e7eaf1;
        border-radius: 18px;
        padding: 1.35rem 1.5rem 1rem;
        box-shadow: 0 10px 30px rgba(30, 41, 59, .06);
    }
    [data-testid="stTextInput"] input, [data-testid="stNumberInput"] input {
        border-radius: 10px;
        background: #fbfcfe;
    }
    [data-testid="stFormSubmitButton"] button {
        border: 0;
        border-radius: 10px;
        background: linear-gradient(135deg, #5b5ce2, #7c5ce7);
        color: white;
        font-weight: 700;
        min-height: 2.7rem;
        transition: transform .15s ease, box-shadow .15s ease;
    }
    [data-testid="stFormSubmitButton"] button:hover {
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 7px 16px rgba(91, 92, 226, .25);
    }
    [data-testid="stMetric"] {
        background: white;
        border: 1px solid #e7eaf1;
        border-radius: 16px;
        padding: 1rem 1.2rem;
        box-shadow: 0 7px 20px rgba(30, 41, 59, .045);
    }
    [data-testid="stMetricLabel"] p { color: #687386; font-weight: 600; }
    [data-testid="stMetricValue"] { color: #5148c8; font-family: 'Manrope', sans-serif; }
    .grade-table-wrap {
        border: 1px solid #e7eaf1;
        border-radius: 14px;
        overflow: hidden;
        background: white;
        box-shadow: 0 7px 20px rgba(30, 41, 59, .045);
    }
    table.grade-table { width: 100%; border-collapse: collapse; }
    .grade-table th {
        background: #f1f2fc;
        color: #5148c8;
        font-size: .82rem;
        font-weight: 700;
        letter-spacing: .04em;
        text-align: left;
        padding: .9rem 1rem;
    }
    .grade-table td { color: #344054; padding: .85rem 1rem; border-top: 1px solid #edf0f5; }
    .grade-table tbody tr:hover { background: #fafaff; }
    .grade-badge {
        display: inline-block;
        min-width: 1.8rem;
        border-radius: 999px;
        padding: .2rem .55rem;
        background: #eeedff;
        color: #5148c8;
        font-weight: 700;
        text-align: center;
    }
    [data-testid="stAlert"] { border-radius: 12px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("# 🎓 Student Grade Manager")
st.caption("A clear view of every student’s progress and your class results.")

# Streamlit reruns this script after each interaction, so session state keeps
# the list alive between reruns.
if "students" not in st.session_state:
    st.session_state.students = []

with st.form("add_student", clear_on_submit=True):
    name = st.text_input("Name")
    mark = st.number_input("Mark", min_value=0, max_value=100, step=1)
    submitted = st.form_submit_button("Add student")

if submitted:
    clean_name = name.strip()
    if not clean_name:
        st.error("Enter a student name.")
    elif not 0 <= mark <= 100:
        # The number input enforces these bounds too; keep validation here as
        # a guard in case the input constraints are changed later.
        st.error("Mark must be between 0 and 100.")
    else:
        st.session_state.students.append({"Name": clean_name, "Mark": int(mark)})
        st.success(f"Added {clean_name}.")

students = st.session_state.students
if students:
    results = [
        {"Name": student["Name"], "Mark": student["Mark"], "Grade": get_grade(student["Mark"])}
        for student in students
    ]
    marks = [student["Mark"] for student in students]

    st.subheader("Class results")
    st.subheader("📊 Class results")
    average_col, highest_col, lowest_col = st.columns(3)
    average_col.metric("Class average", f"{sum(marks) / len(marks):.1f}")
    highest_col.metric("Highest mark", max(marks))
    lowest_col.metric("Lowest mark", min(marks))
    st.dataframe(results, use_container_width=True, hide_index=True)
    table_rows = "".join(
        "<tr>"
        f"<td>{escape(str(student['Name']))}</td>"
        f"<td>{student['Mark']}</td>"
        f"<td><span class='grade-badge'>{get_grade(student['Mark'])}</span></td>"
        "</tr>"
        for student in students
    )
    st.markdown(
        "<div class='grade-table-wrap'><table class='grade-table'>"
        "<thead><tr><th>Name</th><th>Mark</th><th>Grade</th></tr></thead>"
        f"<tbody>{table_rows}</tbody></table></div>",
        unsafe_allow_html=True,
    )
else:
    st.info("Add a student to see the class results and metrics.")