import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import plotly.express as px
from typing import Dict, Any

# Page configuration
st.set_page_config(
    page_title="US Neighborhood Comparison",
    page_icon="🏘️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    .stButton>button {
        width: 100%;
        background-color: #0f172a;
        color: white;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        border-radius: 0.5rem;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #1e293b;
        transform: translateY(-1px);
    }
    .comparison-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12);
        margin-bottom: 1rem;
        border: 1px solid #e5e7eb;
    }
    .metric-title {
        color: #4b5563;
        font-size: 0.875rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .metric-value {
        color: #111827;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .section-title {
        color: #111827;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e5e7eb;
    }
    .stMarkdown {
        padding: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header with improved styling
st.markdown("""
    <h1 style='text-align: center; color: #111827; margin-bottom: 2rem;'>
        🏘️ US Neighborhood Comparison Tool
    </h1>
""", unsafe_allow_html=True)

st.markdown("""
    <p style='text-align: center; font-size: 1.1rem; color: #4b5563; margin-bottom: 2rem;'>
        Compare any two locations across the United States based on key metrics:
    </p>
""", unsafe_allow_html=True)

# Create metrics list with improved styling
metrics_list = """
<div style='display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem;'>
    <div>📚 Education & Schools</div>
    <div>🏠 Real Estate Market</div>
    <div>👥 Demographics</div>
    <div>🚓 Safety & Crime</div>
    <div>✨ Quality of Life</div>
</div>
"""
st.markdown(metrics_list, unsafe_allow_html=True)

# Input fields in two columns with improved styling
col1, col2 = st.columns(2)
with col1:
    location1 = st.text_input(
        "First Location",
        "Seattle, WA",
        help="Enter city and state (e.g., Seattle, WA)"
    )

with col2:
    location2 = st.text_input(
        "Second Location",
        "Portland, OR",
        help="Enter city and state (e.g., Portland, OR)"
    )

def get_location_data(location: str) -> Dict[Any, Any]:
    """
    Simulate getting data for a location (replace with actual API calls)
    """
    import random
    
    # More detailed and realistic data simulation
    population = random.randint(100000, 1000000)
    median_income = random.randint(50000, 120000)
    
    return {
        "education": {
            "avg_school_rating": round(random.uniform(7, 10), 1),
            "top_school": f"{location.split(',')[0]} High School",
            "student_teacher_ratio": f"{random.randint(12, 20)}:1",
            "college_readiness": f"{random.randint(75, 95)}%",
            "graduation_rate": f"{random.randint(80, 98)}%",
            "ap_participation": f"{random.randint(30, 70)}%",
            "test_scores": f"{random.randint(1000, 1400)} SAT avg"
        },
        "real_estate": {
            "median_price": f"${random.randint(300000, 900000):,}",
            "price_trend": f"{random.uniform(2, 8):.1f}% increase",
            "avg_days_on_market": random.randint(20, 60),
            "price_per_sqft": random.randint(200, 500),
            "inventory": random.randint(100, 1000),
            "new_listings": f"+{random.randint(10, 50)}% YoY",
            "price_cuts": f"{random.randint(5, 25)}% of listings"
        },
        "demographics": {
            "population": f"{population:,}",
            "population_growth": f"{random.uniform(-0.5, 3.0):.1f}% annual",
            "median_age": random.randint(30, 45),
            "median_income": f"${median_income:,}",
            "education_level": f"{random.randint(30, 60)}% college degree",
            "employment_rate": f"{random.randint(90, 97)}%",
            "diversity_index": f"{random.randint(50, 90)}/100"
        },
        "safety": {
            "crime_index": random.randint(1, 100),
            "safety_score": f"{random.randint(60, 95)}%",
            "violent_crime_rate": f"{random.uniform(1, 5):.1f} per 1,000",
            "property_crime_rate": f"{random.uniform(10, 30):.1f} per 1,000",
            "police_response": f"{random.randint(3, 10)} min avg",
            "crime_trend": f"{random.uniform(-10, 5):.1f}% YoY",
            "neighborhood_watch": f"{random.randint(10, 50)} active groups"
        },
        "quality_of_life": {
            "walkability": f"{random.randint(50, 100)}/100",
            "air_quality": f"{random.randint(70, 100)}/100",
            "parks_nearby": random.randint(5, 20),
            "restaurants": random.randint(100, 500),
            "commute_time": f"{random.randint(15, 45)} min avg",
            "public_transit": f"{random.randint(50, 95)}/100",
            "healthcare_access": f"{random.randint(70, 95)}/100"
        }
    }

# Initialize data in session state
if 'data1' not in st.session_state:
    st.session_state.data1 = None
if 'data2' not in st.session_state:
    st.session_state.data2 = None

# Compare button with improved styling
if st.button("Compare Locations", help="Click to compare the two locations"):
    with st.spinner("Gathering data..."):
        try:
            # Get data for both locations and store in session state
            st.session_state.data1 = get_location_data(location1)
            st.session_state.data2 = get_location_data(location2)
        except Exception as e:
            st.error(f"An error occurred while comparing locations: {str(e)}")
            st.session_state.data1 = None
            st.session_state.data2 = None

# Display comparison if data exists in session state
if st.session_state.data1 and st.session_state.data2:
    # Display comparison sections
    sections = ["education", "real_estate", "demographics", "safety", "quality_of_life"]
    section_icons = {
        "education": "📚", 
        "real_estate": "🏠",
        "demographics": "👥", 
        "safety": "🚓",
        "quality_of_life": "✨"
    }
    section_titles = {
        "education": "Education & Schools",
        "real_estate": "Real Estate Market",
        "demographics": "Demographics & Community",
        "safety": "Safety & Crime",
        "quality_of_life": "Quality of Life"
    }
    
    # Display timestamp
    st.markdown(f"""
        <p style='text-align: center; color: #6b7280; font-size: 0.875rem; margin: 2rem 0;'>
            Data updated: {datetime.now().strftime('%B %d, %Y %I:%M %p')}
        </p>
    """, unsafe_allow_html=True)
    
    for section in sections:
        st.markdown(
            f"<h2 class='section-title'>{section_icons[section]} {section_titles[section]}</h2>",
            unsafe_allow_html=True
        )
        
        # Create three columns for better layout
        col1, col_spacer, col2 = st.columns([10, 1, 10])
        
        with col1:
            st.markdown(
                f"""
                <div class='comparison-card'>
                    <h3 style='color: #111827; margin-bottom: 1rem;'>{location1}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
            for key, value in st.session_state.data1[section].items():
                st.markdown(
                    f"""
                    <div class='metric-title'>{key.replace('_', ' ').title()}</div>
                    <div class='metric-value'>{value}</div>
                    """,
                    unsafe_allow_html=True
                )
        
        with col2:
            st.markdown(
                f"""
                <div class='comparison-card'>
                    <h3 style='color: #111827; margin-bottom: 1rem;'>{location2}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )
            for key, value in st.session_state.data2[section].items():
                st.markdown(
                    f"""
                    <div class='metric-title'>{key.replace('_', ' ').title()}</div>
                    <div class='metric-value'>{value}</div>
                    """,
                    unsafe_allow_html=True
                )
        
        if section != sections[-1]:
            st.markdown("<br>", unsafe_allow_html=True)

# Add chatbot interface in sidebar with improved styling
st.sidebar.markdown("""
    <h2 style='color: #111827; margin-bottom: 1rem;'>🤖 AI Assistant</h2>
""", unsafe_allow_html=True)

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Show different messages based on comparison state
if not st.session_state.data1 or not st.session_state.data2:
    st.sidebar.warning("⚠️ First step: Click the 'Compare Locations' button to load the data!")
    st.sidebar.info("Once the comparison is loaded, you can ask questions here about schools, safety, prices, and more.")
    user_question = st.sidebar.text_input(
        "Ask me anything about these locations:",
        placeholder="First, compare locations...",
        key="user_input",
        disabled=True
    )
else:
    user_question = st.sidebar.text_input(
        "Ask me anything about these locations:",
        placeholder="E.g., Which location has better schools?",
        key="user_input"
    )

# Add a submit button to prevent auto-refresh
if st.sidebar.button("Ask", disabled=not (st.session_state.data1 and st.session_state.data2)):
    if user_question:
        response = f"Based on the comparison between {location1} and {location2}, "
        if "school" in user_question.lower():
            response += f"{location1 if st.session_state.data1['education']['avg_school_rating'] > st.session_state.data2['education']['avg_school_rating'] else location2} has higher-rated schools overall."
        elif "safe" in user_question.lower() or "crime" in user_question.lower():
            response += f"{location1 if st.session_state.data1['safety']['safety_score'] > st.session_state.data2['safety']['safety_score'] else location2} has a higher safety score."
        elif "cost" in user_question.lower() or "price" in user_question.lower():
            response += f"The median home price in {location1} is {st.session_state.data1['real_estate']['median_price']} compared to {st.session_state.data2['real_estate']['median_price']} in {location2}."
        else:
            response += "both locations have their unique advantages. For specific details, please refer to the comparison above."
        
        # Add to chat history
        st.session_state.chat_history.append({"question": user_question, "answer": response})
    elif user_question:
        st.sidebar.error("⚠️ Please click 'Compare Locations' first to load the data!")

# Display chat history
if st.session_state.chat_history:
    st.sidebar.markdown("### Previous Questions")
    for chat in st.session_state.chat_history:
        st.sidebar.markdown(f"""
            <div style='background-color: #f8fafc; padding: 0.5rem; border-radius: 0.5rem; margin-bottom: 0.5rem;'>
                <p style='color: #4b5563; font-size: 0.875rem; margin-bottom: 0.25rem;'><strong>Q:</strong> {chat['question']}</p>
                <p style='color: #111827; margin: 0;'><strong>A:</strong> {chat['answer']}</p>
            </div>
        """, unsafe_allow_html=True)
