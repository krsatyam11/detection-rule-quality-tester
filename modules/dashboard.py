import streamlit as st

def render_dashboard():
    st.title("SOC Dashboard")
    st.markdown("Overview of actual imported data and test results.")
    
    has_rules = 'rules' in st.session_state and st.session_state.rules
    has_logs = 'log_df' in st.session_state and st.session_state.log_df is not None
    has_results = 'results' in st.session_state and st.session_state.results
    
    if not (has_rules or has_logs or has_results):
        st.info("Upload detection rules and log files to begin testing.")
        return

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Rules Loaded", len(st.session_state.rules) if has_rules else 0)
    with col2:
        st.metric("Total Log Records", len(st.session_state.log_df) if has_logs else 0)
    with col3:
        if has_results:
            matches = sum(r["match_count"] for r in st.session_state.results)
            st.metric("Total Detections", matches)
        else:
            st.metric("Total Detections", "Not run")

    st.divider()
    if has_results:
        rules_hit = sum(1 for r in st.session_state.results if r["match_count"] > 0)
        st.write("### Last Test Execution")
        st.write(f"**Execution Time:** {st.session_state.execution_time:.2f} seconds")
        st.write(f"**Rule Match Coverage:** {rules_hit} / {len(st.session_state.rules)} rules generated alerts.")