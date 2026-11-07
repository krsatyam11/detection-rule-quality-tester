import streamlit as st
import pandas as pd
import json
from fpdf import FPDF

def render_reporting():
    st.title("Reports & Export")
    
    if 'results' not in st.session_state or not st.session_state.results:
        st.info("No test results available to export.")
        return
        
    st.write("Generate standardized reports from the latest test execution.")
    results = st.session_state.results
    
    # CSV Export
    df_export = pd.DataFrame([{
        "Rule_ID": r["rule_id"],
        "Title": r["title"],
        "Level": r["level"],
        "Match_Count": r["match_count"],
        "Techniques": ", ".join(r["techniques"])
    } for r in results])
    
    st.download_button("Download Summary (CSV)", data=df_export.to_csv(index=False), file_name="detection_summary.csv", mime="text/csv")
    
    # JSON Export
    json_data = json.dumps(results, indent=4, default=str)
    st.download_button("Download Full Results (JSON)", data=json_data, file_name="detection_results.json", mime="application/json")
    
    # PDF Export
    if st.button("Generate PDF Summary"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Detection Rule Quality Tester - Execution Report", ln=True, align='C')
        pdf.ln(10)
        
        for idx, row in df_export.iterrows():
            # Clean string to ensure standard PDF font compatibility
            clean_title = str(row['Title']).encode('ascii', 'ignore').decode('ascii')
            pdf.cell(200, 10, txt=f"Rule: {clean_title} | Matches: {row['Match_Count']} | Level: {row['Level']}", ln=True)
            
        # Safely handle different versions of the FPDF library
        pdf_out = pdf.output()
        
        if isinstance(pdf_out, str):
            # Older FPDF version returns a string
            pdf_bytes = pdf_out.encode('latin1')
        else:
            # Newer FPDF2 version returns a bytearray
            pdf_bytes = bytes(pdf_out)
            
        st.download_button("Download PDF", data=pdf_bytes, file_name="report.pdf", mime="application/pdf")