import streamlit as st

# Import the internal Streamlit app from your project
try:
    from src.detector.streamlit_app.app import main as vehicle_ai_main
except Exception as e:
    st.error(f"Failed to load the internal app: {e}")
    st.stop()

def main():
    vehicle_ai_main()

if __name__ == "__main__":
    main()
