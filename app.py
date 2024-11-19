import streamlit as st
from ui_components import home_page, unet_page, deeplabv_page, model_comparison_page, application_and_future_page

# Main function to control the app flow
def main():
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Select a page:", ["Home Page", "U-Net Model", "DeepLabV3+ Model", "Model Comparison", "Application and Future"])

    if page == "Home Page":
        home_page()
    elif page == "U-Net Model":
        unet_page()
    elif page == "DeepLabV3+ Model":
        deeplabv_page()
    elif page == "Model Comparison":
        model_comparison_page()
    elif page == "Application and Future":
        application_and_future_page()

if __name__ == "__main__":
    main()