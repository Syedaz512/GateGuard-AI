
import json
import streamlit as st
from pathlib import Path
from crew import verify_student

def get_student_record(mis_id):
    file_path = Path(__file__).parent / "data" / "students.json"

    with open(file_path, "r", encoding="utf-8") as file:
        students = json.load(file)

    for student in students:
        if student["mis_id"] == str(mis_id).strip():
            return student

    return None


st.set_page_config(
    page_title="GateGuard AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background: #050b14;
        color: #f8fafc;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 35px;
        padding-bottom: 40px;
    }

    .status-container {
        text-align: center;
        margin-bottom: 25px;
    }

    .status-badge {
        display: inline-block;
        padding: 8px 18px;
        border-radius: 25px;
        background: #06251f;
        border: 1px solid #10b981;
        color: #34d399;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .hero {
        text-align: center;
        margin-bottom: 35px;
    }

    .hero-title {
        font-size: 52px;
        font-weight: 800;
        color: white;
        margin-bottom: 8px;
    }

    .hero-title span {
        color: #22d3ee;
    }

    .hero-subtitle {
        color: #cbd5e1;
        font-size: 20px;
        font-weight: 500;
        margin-bottom: 8px;
    }

    .hero-description {
        color: #64748b;
        font-size: 14px;
    }

    .metric-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 16px;
        padding: 22px;
        text-align: center;
        margin-bottom: 30px;
    }

    .metric-number {
        color: #22d3ee;
        font-size: 28px;
        font-weight: 800;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 13px;
        margin-top: 5px;
    }

    .verify-card {
        background: #0f172a;
        border: 1px solid #164e63;
        border-radius: 20px;
        padding: 28px;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .verify-title {
        color: white;
        font-size: 25px;
        font-weight: 800;
        margin-bottom: 7px;
    }

    .verify-description {
        color: #94a3b8;
        font-size: 14px;
    }

    .result-success {
        background: #06251f;
        border: 1px solid #10b981;
        border-radius: 20px;
        padding: 28px;
        margin-top: 25px;
    }

    .result-failed {
        background: #2a1015;
        border: 1px solid #ef4444;
        border-radius: 20px;
        padding: 28px;
        margin-top: 25px;
    }

    .success-title {
        color: #34d399;
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .failed-title {
        color: #f87171;
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .badge-success {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.3);
        color: #34d399;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 18px;
    }

    .badge-failed {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        background: rgba(239, 68, 68, 0.12);
        border: 1px solid rgba(239, 68, 68, 0.3);
        color: #f87171;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 18px;
    }

    .detail-box {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(148, 163, 184, 0.12);
        border-radius: 14px;
        padding: 5px 20px;
    }

    .detail-row {
        display: flex;
        justify-content: space-between;
        padding: 14px 0;
        border-bottom: 1px solid rgba(148, 163, 184, 0.1);
    }

    .detail-row:last-child {
        border-bottom: none;
    }

    .detail-label {
        color: #94a3b8;
        font-size: 14px;
        font-weight: 600;
    }

    .detail-value {
        color: white;
        font-size: 14px;
        font-weight: 700;
    }

    .verified-value {
        color: #34d399;
    }

    .gate-message {
        margin-top: 18px;
        padding: 14px 16px;
        border-radius: 12px;
        background: rgba(16, 185, 129, 0.08);
        border: 1px solid rgba(16, 185, 129, 0.2);
        color: #a7f3d0;
        font-size: 14px;
        font-weight: 600;
    }

    .failed-message {
        padding: 17px;
        border-radius: 12px;
        background: rgba(127, 29, 29, 0.18);
        color: #fecaca;
        font-size: 15px;
        line-height: 1.7;
    }

    .security-note {
        margin-top: 30px;
        padding: 15px;
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 12px;
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
    }

    .footer {
        text-align: center;
        color: #475569;
        font-size: 12px;
        margin-top: 30px;
    }

    .stTextInput label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
    }

    .stTextInput input {
        background: #08111f !important;
        color: white !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        height: 48px !important;
    }

    .stTextInput input:focus {
        border-color: #22d3ee !important;
        box-shadow: 0 0 0 1px #22d3ee !important;
    }

    .stButton button {
        width: 100%;
        height: 48px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(90deg, #0891b2, #4f46e5);
        color: white;
        font-size: 16px;
        font-weight: 700;
    }

    .stButton button:hover {
        background: linear-gradient(90deg, #0e7490, #4338ca);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="status-container">
        <div class="status-badge">● SYSTEM ONLINE</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🛡️ GateGuard <span>AI</span></div>
        <div class="hero-subtitle">AI-Powered University Gate Verification</div>
        <div class="hero-description">Fast and intelligent student record verification powered by CrewAI and Groq.</div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-number">AI</div>
            <div class="metric-label">Powered Verification</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-number">50+</div>
            <div class="metric-label">Demo Student Records</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-number">24/7</div>
            <div class="metric-label">Verification Concept</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <div class="verify-card">
        <div class="verify-title">🎓 Student Verification</div>
        <div class="verify-description">Enter a numeric MIS ID to search the university student records.</div>
    </div>
    """,
    unsafe_allow_html=True
)

mis_id = st.text_input(
    "Student MIS ID",
    placeholder="Enter MIS ID — Example: 1001"
)

verify_button = st.button("🔐 Verify Student")

if verify_button:

    if not mis_id.strip():
        st.warning("Please enter a Student MIS ID.")

    elif not mis_id.strip().isdigit():
        st.error("MIS ID must contain numbers only.")

    else:

        with st.spinner("🔎 Searching student records..."):

            try:
                result = verify_student(mis_id.strip())
                result_text = str(result)
                result_lower = result_text.lower()

                failed = (
                    "not verified" in result_lower
                    or "no student record" in result_lower
                    or "does not exist" in result_lower
                    or "could not be verified" in result_lower
                )

                
                if failed:

                    st.error("❌ Verification Failed")

                    st.markdown("### RECORD NOT FOUND")

                    st.write(
                        f"The MIS ID **{mis_id.strip()}** could not be verified "
                        "in the university student records."
                    )

                    st.warning(
                        "Please contact the university security office "
                        "for further verification."
                    )

                
                else:

                    student = get_student_record(mis_id.strip())

                    if student:

                        st.success("✅ Student Verified")

                        st.markdown("### VERIFICATION SUCCESSFUL")

                        col1, col2 = st.columns(2)

                        with col1:
                            st.caption("MIS ID")
                            st.markdown(f"**{student['mis_id']}**")

                            st.caption("Student Name")
                            st.markdown(f"**{student['name']}**")

                            st.caption("Program")
                            st.markdown(f"**{student['program']}**")

                        with col2:
                            st.caption("Semester")
                            st.markdown(f"**{student['semester']}**")

                            st.caption("Status")
                            st.markdown(f"**🟢 {student['status']}**")

                        st.success(
                            "🟢 Gate Status: Student record verified successfully."
                        )

                    else:

                        st.error("Student record could not be loaded.")


            except Exception as e:
                st.error(f"Verification error: {e}")

st.markdown(
    """
    <div class="security-note">
        🔒 Demo Environment • Fictional student records are used.
        Final gate decisions should be made by authorized university security staff.
    </div>

    <div class="footer">
        GateGuard AI • CrewAI + Groq • University Security Demo
    </div>
    """,
    unsafe_allow_html=True
)

