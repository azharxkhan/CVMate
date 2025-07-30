from utils.db_access import get_section_content, get_all_sections

def get_chatbot_response(user_input):
    user_input = user_input.lower()
    matched = []

    for section in get_all_sections():
        if section.lower() in user_input:
            matched.append(section)

    if matched:
        return "\n\n".join([f"[{m}]\n{get_section_content(m)}" for m in matched])
    
    return "I couldn't find a direct match. Try asking about: " + ", ".join(get_all_sections())
