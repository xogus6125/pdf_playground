import streamlit as st
st.markdown(
    """
    <style>
    .footer {
        padding: 15px;
        background-color: #f2f2f2;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        text-align: center;
    }
    .footer a {
        text-decoration: none;
        color: #0073e6;
        font-weight: bold;
    }
    .footer a:hover {
        color: #005bb5;
    }
    .footer .icon {
        margin-right: 8px;
    }
    </style>
    <div class="footer">
        <p>
            Created by 
            <a href="https://share.streamlit.io/user/desolatetraveller" target="_blank">
                <span class="icon"></span>Avijit Chakraborty
            </a> |
            <a href="mailto:avijit.mba18@gmail.com" target="_blank">
                <span class="icon">✉️</span>Email
            </a> |
            <a href="https://www.linkedin.com/in/avijit2403/" target="_blank">
                <span class="icon">👤</span>LinkedIn
            </a> |
            <a href="https://github.com/DesolateTraveller" target="_blank">
                <span class="icon">💻</span>GitHub
            </a>
        </p>
        <p style="margin-top: 10px; font-size: 14px;">
            For the best view of the app, please <strong>zoom-out</strong> your browser to <strong>75%</strong>.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
