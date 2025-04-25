import streamlit as st
import argparse
from streamlit.components.v1 import html

# PWA Configuration Functions
def set_pwa_meta():
    """Sets PWA meta tags"""
    meta_html = """
    <link rel="manifest" href="/manifest.json">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#4b8bf5"/>
    """
    html(meta_html)

def setup_pwa():
    """Injects PWA service worker registration"""
    pwa_js = """
    <script>
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/sw.js')
                    .then(reg => console.log('Service Worker registered'))
                    .catch(err => console.log('Service Worker registration failed: ', err));
            });
        }
    </script>
    """
    html(pwa_js)

# Set page config MUST be the first Streamlit command
st.set_page_config(
    page_title="Exam Scheduling System",
    layout="wide",
    menu_items={
        'Get Help': 'https://example.com/help',
        'Report a bug': "https://example.com/bug",
        'About': "# Exam Scheduling System v1.0"
    }
)

# Initialize PWA
set_pwa_meta()
setup_pwa()

# Now import other components AFTER set_page_config
from interfaces.admin import admin_interface
from interfaces.invigilator import invigilator_interface
from interfaces.student import student_interface
from database.init_db import reset_database
from database.init_db import initialize_db

def main():
    # Initialize session state
    if 'admin_logged_in' not in st.session_state:
        st.session_state['admin_logged_in'] = False
    if 'invigilator_logged_in' not in st.session_state:
        st.session_state['invigilator_logged_in'] = False
    if 'student_logged_in' not in st.session_state:
        st.session_state['student_logged_in'] = False
    
    # Database file
    db_file = "database/exam_scheduler.db"
    
    # Role selection
    st.sidebar.title("Exam Scheduling System")
    role = st.sidebar.radio("Select Role", ["Student", "Invigilator", "Admin"])
    
    if role == "Admin":
        admin_interface(db_file)
    elif role == "Invigilator":
        invigilator_interface(db_file)
    elif role == "Student":
        student_interface(db_file)

if __name__ == "__main__":
    # For testing/reset purposes
    parser = argparse.ArgumentParser()
    parser.add_argument('--reset', action='store_true', help='Completely reset the database')
    parser.add_argument('--clear', action='store_true', help='Clear all data but keep tables')
    args = parser.parse_args()
    
    if args.reset:
        reset_database("database/exam_scheduler.db")
    elif args.clear:
        initialize_db("database/exam_scheduler.db")
    else:
        main()
