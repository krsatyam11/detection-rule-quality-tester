import streamlit as st
from core.detection_engine import DetectionEngine

def render_test_runner():
    st.title("Execution Engine")
    
    has_rules = 'rules' in st.session_state and st.session_state.rules
    has_logs = 'log_df' in st.session_state and st.session_state.log_df is not None
    
    if not (has_rules and has_logs):
        st.warning("Please upload valid Sigma rules and a Log file before executing tests.")
        return
        
    st.info(f"Ready to test {len(st.session_state.rules)} rules against {len(st.session_state.log_df)} log records.")
    
    if st.button("Run Detection Test", type="primary"):
        with st.spinner("Executing detection logic..."):
            engine = DetectionEngine(st.session_state.rules, st.session_state.log_df)
            results, exec_time = engine.run()
            
            st.session_state.results = results
            st.session_state.execution_time = exec_time
            
            st.success(f"Execution completed in {exec_time:.2f} seconds.")