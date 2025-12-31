import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]
tone_options = ["Professional", "Casual", "Motivational", "Funny"]


def main():
    st.set_page_config(
        page_title="LinkedIn Post Generator",
        page_icon="💼",
        layout="centered",
    )

    # ---------- CUSTOM STYLING ----------
    st.markdown(
        """
        <style>
        /* Overall background: dark with subtle gradient */
        .stApp {
            background: radial-gradient(circle at top, #111827 0, #020617 45%, #000000 100%);
            color: #f9fafb;
        }

        /* Title */
        .app-title {
            text-align: center;
            font-size: 2.4rem;
            font-weight: 800;
            letter-spacing: 0.04em;
            margin: 2rem 0 1.5rem 0;
            color: #f97316; /* orange */
        }

        /* Labels */
        label {
            font-weight: 600 !important;
            color: #e5e7eb !important;
        }

        /* Selectboxes & text inputs */
        .stSelectbox div[data-baseweb="select"],
        .stTextInput input {
            background-color: #020617 !important;
            color: #f9fafb !important;
            border-radius: 0.75rem !important;
            border: 1px solid rgba(148, 163, 184, 0.6) !important;
        }
        .stTextInput input:focus {
            border-color: #f97316 !important;
            box-shadow: 0 0 0 1px #f97316 !important;
        }

        /* Generate button */
        .stButton>button {
            background: linear-gradient(90deg, #f97316, #fb923c);
            color: #111827;
            border-radius: 999px;
            border: none;
            padding: 0.6rem 1.8rem;
            font-weight: 700;
            letter-spacing: 0.04em;
            box-shadow: 0 14px 35px rgba(248, 113, 22, 0.55);
        }
        .stButton>button:hover {
            filter: brightness(1.05);
            box-shadow: 0 16px 40px rgba(248, 113, 22, 0.8);
        }

        /* Generated post card */
        .post-card {
            margin-top: 1.5rem;
            padding: 1.5rem 1.75rem;
            border-radius: 1.25rem;
            background: #020617;
            border: 1px solid rgba(148, 163, 184, 0.6);
        }

        .section-title {
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 0.3rem;
            color: #f97316;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ---------- APP LAYOUT ----------
    fs = FewShotPosts()

    # Title (no empty wrapper div)
    st.markdown('<div class="app-title">LinkedIn Post Generator</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        selected_tag = st.selectbox("Title", options=sorted(fs.get_tags()))
    with col2:
        selected_length = st.selectbox("Length", options=length_options)
    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    tone = st.selectbox("Tone / Style", options=tone_options, index=0)

    audience = st.text_input(
        "Target audience (optional)",
        placeholder="e.g. fresh graduates, hiring managers in tech, mid-level product managers",
    )

    post = None
    if st.button("Generate"):
        post = generate_post(
            selected_length,
            selected_language,
            selected_tag,
            tone,
            audience if audience.strip() else None,
        )

    if post:
        st.markdown('<div class="post-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Generated Post</div>', unsafe_allow_html=True)
        st.write(post)

        st.markdown('<div class="section-title" style="margin-top:1rem;">Copy / Export</div>', unsafe_allow_html=True)
        st.code(post, language="markdown")

        st.download_button(
            label="Download as .txt",
            data=post,
            file_name="linkedin_post.txt",
            mime="text/plain",
        )
        st.markdown("</div>", unsafe_allow_html=True)  # close post-card


if __name__ == "__main__":
    main()
