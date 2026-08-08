import streamlit as st
from analyzer import analyze_message


# Page configuration
st.set_page_config(
    page_title="PhishGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Custom styling
st.markdown(
    """
    <style>
    .main-title {
        font-size: 46px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 18px;
        color: #8f96a3;
        margin-bottom: 25px;
    }

    .section-header {
        font-size: 24px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 12px;
    }

    .footer {
        text-align: center;
        color: #777f8c;
        padding: 20px;
        font-size: 13px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Application header
st.markdown(
    '<div class="main-title">🛡️ PhishGuard</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "Phishing Awareness & Threat Analysis Tool"
    "</div>",
    unsafe_allow_html=True,
)


# Application introduction
st.info(
    "Analyze suspicious emails and messages using "
    "rule-based phishing indicators such as suspicious "
    "keywords, urgency, credential requests, URLs, "
    "financial requests, threats, and potentially "
    "dangerous attachments."
)


# Sidebar
with st.sidebar:

    st.header("🛡️ PhishGuard")

    st.write("Cybersecurity Project 3")

    st.divider()

    st.subheader("Detection Categories")

    st.write("🔎 Suspicious Keywords")
    st.write("⏱️ Urgency Indicators")
    st.write("🔑 Credential Requests")
    st.write("💳 Financial Requests")
    st.write("⚠️ Threat Language")
    st.write("📎 Suspicious Attachments")
    st.write("🔗 URL Analysis")

    st.divider()

    st.caption(
        "Educational cybersecurity analysis tool."
    )

    st.caption(
        "Results are rule-based indicators and "
        "should not be treated as definitive proof "
        "that a message is malicious."
    )


# Message analysis section
st.markdown(
    '<div class="section-header">'
    "📩 Message Analysis"
    "</div>",
    unsafe_allow_html=True,
)


message = st.text_area(
    "Suspicious Email / Message",
    height=280,
    placeholder="Paste a suspicious email or message here...",
)


analyze_button = st.button(
    "🔍 Analyze Message",
    use_container_width=True,
)


# Analyze submitted message
if analyze_button:

    if not message.strip():

        st.warning(
            "Please enter an email or message before "
            "starting the analysis."
        )

    else:

        result = analyze_message(message)

        st.divider()

        # Risk assessment
        st.markdown(
            '<div class="section-header">'
            "🎯 Risk Assessment"
            "</div>",
            unsafe_allow_html=True,
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Risk Score",
                f"{result['risk_score']}/100",
            )

        with col2:
            st.metric(
                "Risk Level",
                result["risk_level"],
            )

        with col3:
            st.metric(
                "URLs Detected",
                len(result["urls"]),
            )

        # Risk alert
        if result["risk_level"] == "CRITICAL":

            st.error(
                "🚨 CRITICAL RISK — Multiple phishing "
                "indicators were detected."
            )

        elif result["risk_level"] == "HIGH":

            st.error(
                "⚠️ HIGH RISK — Several phishing "
                "indicators were detected."
            )

        elif result["risk_level"] == "MEDIUM":

            st.warning(
                "⚠️ MEDIUM RISK — The message contains "
                "some suspicious characteristics."
            )

        else:

            st.success(
                "✅ LOW RISK — No major phishing "
                "indicators were detected."
            )

        # Risk score interpretation
        st.markdown(
            '<div class="section-header">'
            "📈 Risk Score Interpretation"
            "</div>",
            unsafe_allow_html=True,
        )

        score = result["risk_score"]

        if score >= 75:

            st.write(
                "🔴 **75–100: CRITICAL** — "
                "Multiple strong phishing indicators were detected. "
                "The message should be treated as highly suspicious."
            )

        elif score >= 50:

            st.write(
                "🟠 **50–74: HIGH** — "
                "Several suspicious characteristics were detected. "
                "The message requires careful verification."
            )

        elif score >= 25:

            st.write(
                "🟡 **25–49: MEDIUM** — "
                "Some suspicious indicators were detected. "
                "Additional verification is recommended."
            )

        else:

            st.write(
                "🟢 **0–24: LOW** — "
                "The analyzer did not detect significant phishing "
                "indicators."
            )

        # Detection summary
        st.markdown(
            '<div class="section-header">'
            "📊 Detection Summary"
            "</div>",
            unsafe_allow_html=True,
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Keywords",
                len(result["keywords"]),
            )

        with col2:

            st.metric(
                "Urgency",
                len(result["urgency"]),
            )

        with col3:

            st.metric(
                "Credential Indicators",
                len(result["credentials"]),
            )

        with col4:

            st.metric(
                "URL Findings",
                len(result["url_findings"]),
            )

        # Suspicious keywords
        st.markdown(
            '<div class="section-header">'
            "🔎 Suspicious Keywords"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["keywords"]:

            cols = st.columns(3)

            for index, keyword in enumerate(
                result["keywords"]
            ):

                with cols[index % 3]:

                    st.warning(
                        f"**{keyword}**"
                    )

        else:

            st.success(
                "No suspicious keywords detected."
            )

        # Urgency indicators
        st.markdown(
            '<div class="section-header">'
            "⏱️ Urgency Indicators"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["urgency"]:

            for item in result["urgency"]:

                st.write(
                    f"• **{item}**"
                )

        else:

            st.write(
                "No urgency indicators detected."
            )

        # Credential indicators
        st.markdown(
            '<div class="section-header">'
            "🔑 Credential Indicators"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["credentials"]:

            for item in result["credentials"]:

                st.write(
                    f"• **{item}**"
                )

        else:

            st.write(
                "No credential-related indicators detected."
            )

        # Financial indicators
        st.markdown(
            '<div class="section-header">'
            "💳 Financial Indicators"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["financial"]:

            for item in result["financial"]:

                st.write(
                    f"• **{item}**"
                )

        else:

            st.write(
                "No financial indicators detected."
            )

        # Threat indicators
        st.markdown(
            '<div class="section-header">'
            "⚠️ Threat Indicators"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["threats"]:

            for item in result["threats"]:

                st.write(
                    f"• **{item}**"
                )

        else:

            st.write(
                "No threatening language detected."
            )

        # Attachment analysis
        st.markdown(
            '<div class="section-header">'
            "📎 Attachment Analysis"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["attachments"]:

            for item in result["attachments"]:

                st.warning(
                    f"Potentially dangerous attachment "
                    f"extension detected: **{item}**"
                )

        else:

            st.write(
                "No potentially dangerous attachment "
                "extensions detected."
            )

        # Email address analysis
        st.markdown(
            '<div class="section-header">'
            "📧 Email Addresses"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["email_addresses"]:

            for address in result["email_addresses"]:

                st.code(address)

        else:

            st.write(
                "No email addresses detected."
            )

        # URL analysis
        st.markdown(
            '<div class="section-header">'
            "🔗 URL Analysis"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["urls"]:

            for url in result["urls"]:

                st.code(
                    url,
                    language="text",
                )

        else:

            st.success(
                "No URLs detected."
            )

        # URL red flags
        if result["url_findings"]:

            st.markdown(
                '<div class="section-header">'
                "🚩 URL Red Flags"
                "</div>",
                unsafe_allow_html=True,
            )

            for finding in result["url_findings"]:

                st.warning(
                    f"**Finding:** {finding['finding']}\n\n"
                    f"**URL:** {finding['url']}"
                )

        # Phishing red flags
        st.markdown(
            '<div class="section-header">'
            "🚩 Phishing Red Flags"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["red_flags"]:

            for flag in result["red_flags"]:

                st.write(
                    f"🚩 {flag}"
                )

        else:

            st.success(
                "No major phishing red flags detected."
            )

        # Red flag checklist
        st.markdown(
            '<div class="section-header">'
            "🛡️ Red Flag Checklist"
            "</div>",
            unsafe_allow_html=True,
        )

        checklist = [
            (
                "Urgency / pressure",
                len(result["urgency"]) > 0,
            ),
            (
                "Credential request",
                len(result["credentials"]) > 0,
            ),
            (
                "Financial request",
                len(result["financial"]) > 0,
            ),
            (
                "Threatening language",
                len(result["threats"]) > 0,
            ),
            (
                "Suspicious attachment",
                len(result["attachments"]) > 0,
            ),
            (
                "URL detected",
                len(result["urls"]) > 0,
            ),
            (
                "Suspicious URL characteristics",
                len(result["url_findings"]) > 0,
            ),
            (
                "Suspicious keywords",
                len(result["keywords"]) > 0,
            ),
        ]

        for label, detected in checklist:

            if detected:

                st.error(
                    f"🚨 {label}: DETECTED"
                )

            else:

                st.success(
                    f"✅ {label}: NOT DETECTED"
                )

        # Safety explanation
        st.markdown(
            '<div class="section-header">'
            "🧠 Why Could This Message Be Unsafe?"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["explanations"]:

            for explanation in result["explanations"]:

                st.write(
                    f"• {explanation}"
                )

        else:

            st.write(
                "No major safety concerns were identified "
                "by the analyzer."
            )

        # Recommended action
        st.markdown(
            '<div class="section-header">'
            "🛡️ Recommended Action"
            "</div>",
            unsafe_allow_html=True,
        )

        if result["risk_level"] in [
            "HIGH",
            "CRITICAL",
        ]:

            st.error(
                "Do not click suspicious links, open "
                "unexpected attachments, or provide "
                "passwords and other sensitive information. "
                "Verify the request through an official "
                "communication channel."
            )

        elif result["risk_level"] == "MEDIUM":

            st.warning(
                "Review the sender, links, attachments, "
                "and context carefully before taking action."
            )

        else:

            st.success(
                "No major indicators were detected. "
                "Continue following normal security practices."
            )


# Footer
st.divider()

st.markdown(
    '<div class="footer">'
    "PhishGuard | Cybersecurity Project 3 | "
    "Phishing Awareness Analysis"
    "</div>",
    unsafe_allow_html=True,
)