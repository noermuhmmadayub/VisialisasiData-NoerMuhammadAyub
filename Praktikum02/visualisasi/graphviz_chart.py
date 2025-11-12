import streamlit as st
import graphviz as graphviz

# --- Identitas Kelompok ---
st.title("Graphiz")
st.write("Kelompok 28 - Visualisasi Data")
st.markdown("""
**Nama Kelompok:**
- Muhammad Ayub (NIM: 12345678)
- Rahmi Atika (NIM: 0110222279)
- Saskia Putri Ananda (NIM: 0110222159)
""")

st.graphviz_chart("""
diagraph {
"Training Data" -> "ML Algorithm"
"ML Algorithm" -> "Model"
"Model" -> "Result Forecasting"
"New Data" -> "Model"
}
""")

graph = graphviz.Digraph()
graph.edge('Training Data', 'ML Algorithm')
graph.edge("ML Algorithm", "Model")
graph.edge("Model", "Result Forecasting")
graph.edge("New Data", "Model")
st.graphviz_chart(graph)