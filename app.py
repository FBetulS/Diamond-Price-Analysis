import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="Diamond Price Predictor", page_icon="💎", layout="wide")

# Load the pre-trained model
@st.cache_resource
def load_model():
    try:
        model = joblib.load('xgb_regressor_model.pkl')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Prepare mappings for categorical variables
CUT_MAPPING = {
    'Ideal': 5,
    'Premium': 4,
    'Very Good': 3,
    'Good': 2,
    'Fair': 1
}

COLOR_MAPPING = {
    'D': 7, 'E': 6, 'F': 5, 
    'G': 4, 'H': 3, 'I': 2, 'J': 1
}

CLARITY_MAPPING = {
    'IF': 8, 'VVS1': 7, 'VVS2': 6,
    'VS1': 5, 'VS2': 4, 
    'SI1': 3, 'SI2': 2, 'I1': 1
}

def main():
    st.title("💎 Diamond Price Predictor")
    
    # Sidebar for input features
    st.sidebar.header("Diamond Characteristics")
    
    # Input features
    carat = st.sidebar.slider("Carat Weight", min_value=0.1, max_value=5.0, step=0.1, value=1.0)
    cut = st.sidebar.selectbox("Cut Quality", list(CUT_MAPPING.keys()))
    color = st.sidebar.selectbox("Color", list(COLOR_MAPPING.keys()))
    clarity = st.sidebar.selectbox("Clarity", list(CLARITY_MAPPING.keys()))
    depth = st.sidebar.slider("Depth Percentage", min_value=50.0, max_value=70.0, step=0.1, value=61.5)
    table = st.sidebar.slider("Table Percentage", min_value=50.0, max_value=70.0, step=0.1, value=57.0)
    
    # Calculate volume (x * y * z approximation)
    volume = carat * 6.5  # Rough approximation based on average diamond density
    
    # Prepare input data
    input_data = pd.DataFrame({
        'carat': [carat],
        'cut': [CUT_MAPPING[cut]],
        'color': [COLOR_MAPPING[color]],
        'clarity': [CLARITY_MAPPING[clarity]],
        'depth': [depth],
        'table': [table],
        'volume': [volume]
    })
    
    # Prediction
    model = load_model()
    if model is not None:
        if st.sidebar.button("Predict Diamond Price"):
            try:
                prediction = model.predict(input_data)[0]
                st.success(f"Estimated Diamond Price: ${prediction:,.2f}")
                
                # Additional insights
                st.subheader("Price Insights")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Carat Weight", f"{carat} ct")
                
                with col2:
                    st.metric("Cut Quality", cut)
                
                with col3:
                    st.metric("Color Grade", color)
            
            except Exception as e:
                st.error(f"Prediction error: {e}")
    
    # About section
    st.sidebar.markdown("---")
    st.sidebar.info("""
    ### About this App
    This Diamond Price Predictor uses an XGB Regressor model 
    trained on diamond characteristics to estimate prices.
    
    Factors affecting price include:
    - Carat Weight
    - Cut Quality
    - Color
    - Clarity
    - Depth
    - Table Percentage
    """)

if __name__ == "__main__":
    main()
    