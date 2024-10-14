import streamlit as st
from PIL import Image

# Model Selection
def model_selection():
    st.subheader("Models:")
    selectBox = st.selectbox("Choose Models: ", ["U-Net", "DeepLabV3+"])

    return selectBox

# Function for Home Page
def home_page():
    st.title("Welcome to AquaSense: A Water Region Mapping Tool 🌊")
    st.markdown("#### Harness the power of Deep Learning to map water regions with precision!")
    st.markdown("""
        AquaSense addresses the critical challenge of accurately mapping and monitoring water regions in real time. 
        With approximately **1,000 floods** occurring annually and affecting over **1.5 billion people**, effective flood management is essential.
    """)

    model_selected = model_selection()
    st.write(f"Model Selected: {model_selected}")

    uploaded_file = st.file_uploader("Upload Image:", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image, use_column_width=True)

        with col2:
            st.subheader("Masked Image")
            st.image(image, use_column_width=True)

# Function for U-Net Model Description Page
def unet_page():
    st.header("U-Net Model")
    desc = """
        <div style = 'text-align: justify;'>
            <strong>U-Net</strong> is designed for semantic segmentation and features a <strong>symmetrical encoder-decoder design</strong>. The 
            encoder captures detailed features through <strong>downsampling</strong>, while the decoder reconstructs the image using <strong>upsampling</strong>
            and incorporates these features through <strong>skip connections</strong>. These connections improve the precision of segmentation by 
            linking parts of the encoder and decoder. For flood water mapping, U-Net excels in providing detailed, accurate pixel-level classifications.
        </div>
    """
    st.markdown(desc, unsafe_allow_html = True)
    st.subheader("Architecture:")
    image_path = r"Image\UNET Model Architecture.drawio.png"
    image = Image.open(image_path)

    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="Architecture", use_column_width=False, width = 700)
    st.markdown("</div>", unsafe_allow_html=True)

# Function for DeeplabV3+ Model Description Page
def deeplabv_page():
    st.header("DeeplabV3+ Model")
    desc = """
        <div style = 'text-align: justify;'>
            <strong>DeepLabV3+</strong> uses <strong>atrous convolutions</strong> and <strong>spatial pyramid pooling</strong> to handle 
            complex segmentation tasks. Its <strong>ResNet50-based encoder</strong> extracts deep features, and the decoder applies spatial
            pyramid pooling to keep high-resolution details intact. While it does not use skip connections, it excels at combining contextual 
            information across different scales. In flood mapping, DeepLabV3+ provides precise segmentation with detail and effective multi-scale context.
        </div>
    """
    st.markdown(desc, unsafe_allow_html = True)
    st.subheader("Architecture:")
    image_path = r"Image\DeepLabV3+ Model Architecture (UP).drawio.png"
    image = Image.open(image_path)

    image = Image.open(image_path)

    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption="Architecture", use_column_width=False, width = 700)
    st.markdown("</div>", unsafe_allow_html=True)

# Function for Model Comparison Page
def model_comparison_page():
    st.subheader("Model Performance Comparison")
    
    comparison_html = """
        <style>
            .table-container {
                font-family: Arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
                margin: 20px 0;
            }
            .table-container th, .table-container td {
                border: 1px solid green;
                padding: 10px;
                text-align: center;
            }
            .table-container th {
                background-color: #ffba76;
                color: white;
            }
            .table-container tr:nth-child(even) {
                background-color: #b15900;
            }
            .table-container tr:nth-child(odd) {
                background-color: #cf7540;
            }
            .table-container tr:hover {
                background-color: #159965;
            }
        </style>

        <table class="table-container">
            <tr>
                <th>Metric</th>
                <th>U-Net</th>
                <th>DeepLabV3+</th>
            </tr>
            <tr>
                <td><strong>Accuracy</strong></td>
                <td>93.93%</td>
                <td>95.47%</td>
            </tr>
            <tr>
                <td><strong>IoU</strong></td>
                <td>89.77%</td>
                <td>95.27%</td>
            </tr>
            <tr>
                <td><strong>Precision</strong></td>
                <td>95.40%</td>
                <td>97.95%</td>
            </tr>
            <tr>
                <td><strong>Recall</strong></td>
                <td>95.28%</td>
                <td>97.93%</td>
            </tr>
            <tr>
                <td><strong>F1 Score</strong></td>
                <td>95.34%</td>
                <td>97.94%</td>
            </tr>
        </table>
    """

    st.markdown(comparison_html, unsafe_allow_html=True)

# Function for Applications and Future Prospects Page
def application_and_future_page():
    st.header("🌐 Real-World Applications & Future Prospects")

    st.markdown("### **Where Can AquaSense Make a Difference?**")
    st.markdown("""
    - 🌊 **Flood Management**: Get real-time insights to mitigate disaster impacts.
    - 🏞️ **Wetland Conservation**: Monitor the health of essential ecosystems.
    - 🚜 **Agricultural Water Management**: Ensure efficient water usage for crops.
    - 🏙️ **Urban Planning**: Help cities plan smarter by understanding water distribution.
    """)

    st.markdown("### **Future Enhancements**:")  
    st.markdown("""
    We will be working on **change detection in aquatic bodies** using satellite or aerial images, employing various efficient deep learning methods.
    """)

    st.markdown("*See how these innovations could shape the future of water region mapping!*")

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