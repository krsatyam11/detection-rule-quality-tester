import streamlit as st
from utils.file_handler import parse_logs

def render_log_analyzer():
    st.title("Security Log Analyzer")
    
    uploaded_file = st.file_uploader("Upload Log File (CSV, JSON, JSONL)", type=['csv', 'json', 'jsonl', 'txt'])
    
    if uploaded_file and st.button("Parse Logs"):
        with st.spinner("Parsing logs..."):
            df, error = parse_logs(uploaded_file, uploaded_file.name)
            if error:
                st.error(f"Failed to parse logs: {error}")
            else:
                st.session_state.log_df = df
                st.success(f"Successfully parsed {len(df)} records.")
    
    if 'log_df' in st.session_state and st.session_state.log_df is not None:
        st.subheader("Log Data Overview")
        df = st.session_state.log_df
        
        st.write(f"**Total Records:** {len(df)}")
        st.write(f"**Available Fields:** {', '.join(df.columns.tolist())}")
        
        st.write("### Sample Records")
        st.dataframe(df.head(10))
        
        if st.button("Clear Log Data"):
            st.session_state.log_df = None
            st.rerun()