import streamlit as st
import pandas as pd
import plotly.express as px

def render_results():
    st.title("Detection Results")
    
    if 'results' not in st.session_state or not st.session_state.results:
        st.info("No test results available. Run a test first.")
        return
        
    results = st.session_state.results
    
    st.sidebar.subheader("Result Filters")
    min_matches = st.sidebar.number_input("Minimum Matches", min_value=0, value=0)
    filtered_results = [r for r in results if r["match_count"] >= min_matches]
    
    df_chart = pd.DataFrame([{ "Rule": r["title"], "Matches": r["match_count"], "Level": r["level"]} for r in filtered_results if r["match_count"] > 0])
    
    if not df_chart.empty:
        fig = px.bar(df_chart, x="Matches", y="Rule", color="Level", orientation='h', title="Matches by Rule")
        st.plotly_chart(fig)
    else:
        st.write("No rules generated matches based on current filters.")
        
    st.divider()
    
    for res in filtered_results:
        with st.expander(f"{res['title']} ({res['match_count']} matches)"):
            st.write(f"**Rule ID:** {res['rule_id']}")
            st.write(f"**Level:** {res['level']}")
            st.write(f"**Techniques:** {', '.join(res['techniques'])}")
            if res["match_count"] > 0:
                st.write("**Matching Records:**")
                st.dataframe(pd.DataFrame(res["matches"]))