import streamlit as st
from utils.file_handler import safe_load_yaml
from core.rule_parser import SigmaRule

def render_rule_manager():
    st.title("Detection Rule Manager")
    
    if 'rules' not in st.session_state:
        st.session_state.rules = []

    uploaded_files = st.file_uploader("Upload Sigma YAML files", type=['yml', 'yaml'], accept_multiple_files=True)
    
    if st.button("Process Rules"):
        st.session_state.rules = []
        for file in uploaded_files:
            content = file.getvalue().decode("utf-8")
            raw_docs = safe_load_yaml(content)
            if raw_docs:
                for doc in raw_docs:
                    if doc:
                        rule = SigmaRule(doc, file.name)
                        st.session_state.rules.append(rule)
        st.success(f"Successfully processed {len(st.session_state.rules)} rules.")

    if st.session_state.rules:
        st.subheader("Loaded Rules")
        for rule in st.session_state.rules:
            with st.expander(f"{rule.title} ({rule.level})"):
                if not rule.is_valid:
                    st.error(f"Validation Errors: {', '.join(rule.errors)}")
                st.write(f"**ID:** {rule.id}")
                st.write(f"**File:** {rule.file_name}")
                st.write(f"**Logsource:** {rule.logsource}")
                st.write(f"**Tags:** {', '.join(rule.tags)}")
                st.code(rule.condition, language="text")