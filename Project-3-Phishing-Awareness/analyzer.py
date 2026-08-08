import re
from urllib.parse import urlparse


# PHISHING KEYWORD DATABASE

SUSPICIOUS_KEYWORDS = [
    "urgent",
    "immediately",
    "verify",
    "verification",
    "suspended",
    "suspension",
    "password",
    "login",
    "account",
    "click here",
    "confirm",
    "security alert",
    "winner",
    "claim",
    "payment",
    "invoice",
    "refund",
    "unusual activity",
    "unauthorized activity",
    "security warning",
    "update your account",
]


# URGENCY / PRESSURE INDICATORS

URGENCY_KEYWORDS = [
    "urgent",
    "immediately",
    "act now",
    "within 24 hours",
    "within 48 hours",
    "last chance",
    "expires today",
    "final warning",
    "do not delay",
    "respond immediately",
    "action required",
]


# CREDENTIAL REQUEST INDICATORS

CREDENTIAL_KEYWORDS = [
    "password",
    "username",
    "login",
    "credentials",
    "verify your account",
    "confirm your identity",
    "enter your password",
    "enter your username",
    "sign in",
]


# FINANCIAL REQUEST INDICATORS

FINANCIAL_KEYWORDS = [
    "payment",
    "bank account",
    "credit card",
    "debit card",
    "transfer money",
    "send money",
    "invoice",
    "refund",
    "billing",
    "transaction",
    "financial information",
]


# THREAT INDICATORS

THREAT_KEYWORDS = [
    "account will be closed",
    "account will be suspended",
    "account will be deleted",
    "legal action",
    "penalty",
    "blocked",
    "terminated",
    "lose access",
    "failure to comply",
]


# SUSPICIOUS FILE EXTENSIONS

SUSPICIOUS_EXTENSIONS = [
    ".exe",
    ".scr",
    ".bat",
    ".cmd",
    ".vbs",
    ".js",
    ".jar",
    ".msi",
    ".ps1",
    ".hta",
]


# URL SHORTENERS

URL_SHORTENERS = [
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "ow.ly",
    "is.gd",
    "buff.ly",
]


# SUSPICIOUS TLDs

SUSPICIOUS_TLDS = [
    ".tk",
    ".ml",
    ".ga",
    ".cf",
    ".gq",
    ".top",
    ".xyz",
    ".click",
    ".download",
]


# URL EXTRACTION

def extract_urls(text):
    """
    Extract HTTP/HTTPS URLs from a message.

    Handles:
    - Normal URLs
    - Markdown-style links
    - Duplicate URLs
    """

    url_pattern = r"https?://[^\s<>\])\"']+"

    urls = re.findall(url_pattern, text)

    cleaned_urls = []

    for url in urls:

        # Remove common punctuation from the end.
        url = url.rstrip(".,!?;:")

        if url not in cleaned_urls:
            cleaned_urls.append(url)

    return cleaned_urls


# EMAIL ADDRESS EXTRACTION


def extract_email_addresses(text):
    """
    Extract email addresses from a message.
    """

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    return re.findall(email_pattern, text)


# KEYWORD DETECTION

def detect_keywords(text):
    """
    Detect suspicious phishing-related keywords.
    """

    text_lower = text.lower()

    found = []

    for keyword in SUSPICIOUS_KEYWORDS:

        if keyword in text_lower:
            found.append(keyword)

    return found


# URGENCY DETECTION

def detect_urgency(text):
    """
    Detect urgency and pressure tactics.
    """

    text_lower = text.lower()

    found = []

    for keyword in URGENCY_KEYWORDS:

        if keyword in text_lower:
            found.append(keyword)

    return found


# CREDENTIAL DETECTION

def detect_credential_request(text):
    """
    Detect requests for usernames, passwords,
    logins, or identity verification.
    """

    text_lower = text.lower()

    found = []

    for keyword in CREDENTIAL_KEYWORDS:

        if keyword in text_lower:
            found.append(keyword)

    return found


# FINANCIAL REQUEST DETECTION

def detect_financial_request(text):
    """
    Detect financial-related requests.
    """

    text_lower = text.lower()

    found = []

    for keyword in FINANCIAL_KEYWORDS:

        if keyword in text_lower:
            found.append(keyword)

    return found


# THREAT DETECTION

def detect_threats(text):
    """
    Detect threatening or intimidating language.
    """

    text_lower = text.lower()

    found = []

    for keyword in THREAT_KEYWORDS:

        if keyword in text_lower:
            found.append(keyword)

    return found



# ATTACHMENT DETECTION

def detect_attachments(text):
    """
    Detect potentially dangerous attachment filenames.
    """

    text_lower = text.lower()

    found = []

    for extension in SUSPICIOUS_EXTENSIONS:

        if extension in text_lower:
            found.append(extension)

    return found


# URL ANALYSIS

def analyze_url(url):
    """
    Analyze a URL for common suspicious characteristics.
    """

    findings = []

    try:

        parsed = urlparse(url)

        scheme = parsed.scheme.lower()

        hostname = parsed.hostname

        # HTTPS CHECK

        if scheme == "http":

            findings.append(
                "URL does not use HTTPS"
            )

        # INVALID HOSTNAME

        if not hostname:

            findings.append(
                "URL has no valid hostname"
            )

            return findings

        hostname_lower = hostname.lower()

         # IP ADDRESS CHECK

        ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

        if re.match(ip_pattern, hostname_lower):

            findings.append(
                "URL uses an IP address instead of a domain name"
            )

        # URL SHORTENER CHECK

        if hostname_lower in URL_SHORTENERS:

            findings.append(
                "URL uses a URL shortening service"
            )

        # SUSPICIOUS TLD CHECK

        for tld in SUSPICIOUS_TLDS:

            if hostname_lower.endswith(tld):

                findings.append(
                    f"Domain uses potentially suspicious TLD: {tld}"
                )

                break

     
        # @ SYMBOL CHECK
       

        if "@" in url:

            findings.append(
                "URL contains an @ symbol that may obscure the destination"
            )

        
        # EXCESSIVE SUBDOMAIN CHECK
        

        parts = hostname_lower.split(".")

        if len(parts) >= 5:

            findings.append(
                "URL contains an unusually large number of subdomains"
            )

        
        # SUSPICIOUS KEYWORDS IN DOMAIN
    

        suspicious_domain_words = [
            "login",
            "verify",
            "secure",
            "account",
            "update",
            "password",
            "bank",
            "support",
        ]

        for word in suspicious_domain_words:

            if word in hostname_lower:

                findings.append(
                    f"Domain contains sensitive keyword: {word}"
                )

                break

    except Exception:

        findings.append(
            "Unable to safely parse URL"
        )

    return findings


# RISK SCORE


def calculate_risk(
    keyword_count,
    urgency_count,
    credential_count,
    financial_count,
    threat_count,
    attachment_count,
    url_count,
    suspicious_url_count,
):
    """
    Calculate a 0-100 phishing risk score.

    This is a rule-based educational scoring system.
    """

    score = 0

    # Suspicious keywords
    score += min(keyword_count * 2, 16)

    # Urgency
    score += min(urgency_count * 5, 15)

    # Credential requests
    score += min(credential_count * 7, 21)

    # Financial requests
    score += min(financial_count * 6, 18)

    # Threat language
    score += min(threat_count * 5, 15)

    # Suspicious attachments
    score += min(attachment_count * 5, 10)

    # Presence of URL
    if url_count > 0:
        score += 5

    # Suspicious URL characteristics
    score += min(suspicious_url_count * 5, 20)

    # Keep score between 0 and 100.
    score = min(score, 100)

    # Determine risk level.
    if score >= 75:

        risk_level = "CRITICAL"

    elif score >= 50:

        risk_level = "HIGH"

    elif score >= 25:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    return score, risk_level


# COMPLETE MESSAGE ANALYSIS


def analyze_message(text):
    """
    Perform complete phishing-awareness analysis.
    """

    keywords = detect_keywords(text)

    urgency = detect_urgency(text)

    credentials = detect_credential_request(text)

    financial = detect_financial_request(text)

    threats = detect_threats(text)

    attachments = detect_attachments(text)

    urls = extract_urls(text)

    email_addresses = extract_email_addresses(text)

  
    # Analyze every URL


    url_findings = []

    for url in urls:

        findings = analyze_url(url)

        for finding in findings:

            url_findings.append(
                {
                    "url": url,
                    "finding": finding,
                }
            )


    # Generate red flags
 

    red_flags = []

    if urgency:

        red_flags.append(
            "Urgency or pressure to act quickly"
        )

    if credentials:

        red_flags.append(
            "Possible request for account credentials"
        )

    if financial:

        red_flags.append(
            "Possible financial or payment request"
        )

    if threats:

        red_flags.append(
            "Threatening or intimidating language"
        )

    if attachments:

        red_flags.append(
            "Potentially dangerous attachment detected"
        )

    if urls:

        red_flags.append(
            "Message contains a URL"
        )

    if url_findings:

        red_flags.append(
            "URL contains potentially suspicious characteristics"
        )

  
    # Calculate score
  

    risk_score, risk_level = calculate_risk(
        keyword_count=len(keywords),
        urgency_count=len(urgency),
        credential_count=len(credentials),
        financial_count=len(financial),
        threat_count=len(threats),
        attachment_count=len(attachments),
        url_count=len(urls),
        suspicious_url_count=len(url_findings),
    )

  
    # Generate explanation
  

    explanations = []

    if urgency:

        explanations.append(
            "The message uses urgency or pressure to encourage "
            "the recipient to act quickly."
        )

    if credentials:

        explanations.append(
            "The message contains language associated with "
            "requests for credentials or account verification."
        )

    if financial:

        explanations.append(
            "The message contains financial or payment-related "
            "language that may attempt to obtain sensitive information."
        )

    if threats:

        explanations.append(
            "The message uses threats or consequences to pressure "
            "the recipient."
        )

    if attachments:

        explanations.append(
            "The message references potentially dangerous file "
            "extensions that should be treated cautiously."
        )

    if url_findings:

        explanations.append(
            "One or more URLs contain characteristics that "
            "warrant additional verification."
        )

    if not explanations:

        explanations.append(
            "No major phishing indicators were identified by "
            "the rule-based analyzer."
        )


    # Return complete analysis
 

    return {
        "keywords": keywords,
        "urgency": urgency,
        "credentials": credentials,
        "financial": financial,
        "threats": threats,
        "attachments": attachments,
        "urls": urls,
        "email_addresses": email_addresses,
        "url_findings": url_findings,
        "red_flags": red_flags,
        "explanations": explanations,
        "risk_score": risk_score,
        "risk_level": risk_level,
    }