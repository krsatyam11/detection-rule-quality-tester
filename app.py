import streamlit as st
from modules.dashboard import render_dashboard
from modules.rule_manager import render_rule_manager
from modules.log_analyzer import render_log_analyzer
from modules.test_runner import render_test_runner
from modules.results import render_results
from modules.reporting import render_reporting

# Professional, generic page configuration (No emojis, standard layout)
st.set_page_config(page_title="Detection Rule Quality Tester", layout="wide")

def main():
    st.sidebar.title("Detection Engineering")
    st.sidebar.markdown("Sigma Rule Validation Utility")
    st.sidebar.divider()
    
    menu = [
        "Dashboard", 
        "Rule Manager", 
        "Log Analyzer", 
        "Execution Engine", 
        "Detection Results", 
        "Export Reports"
    ]
    
    choice = st.sidebar.radio("Navigation", menu, label_visibility="collapsed")
    
    if choice == "Dashboard":
        render_dashboard()
    elif choice == "Rule Manager":
        render_rule_manager()
    elif choice == "Log Analyzer":
        render_log_analyzer()
    elif choice == "Execution Engine":
        render_test_runner()
    elif choice == "Detection Results":
        render_results()
    elif choice == "Export Reports":
        render_reporting()

    st.sidebar.divider()
    st.sidebar.caption("Build Version: 1.0.0 | Local Environment")

if __name__ == "__main__":
    main()