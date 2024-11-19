import streamlit as st
from PIL import Image
import io
from utils import (
    load_keras_model,
    preprocess_image,
    postprocess_prediction,
    create_overlay,
    create_mask_visualization
)

def model_selection():
    st.subheader("Models:")
    selectBox = st.selectbox("Choose Models: ", ["U-Net", "DeepLabV3+"])
    return selectBox

def home_page():
    st.title("Welcome to AquaSense: A Water Region Mapping Tool 🌊")
    st.markdown("#### Harness the power of Deep Learning to map water regions with precision!")
    st.markdown("""
        AquaSense addresses the critical challenge of accurately mapping and monitoring water regions in real time. 
        With approximately **1,000 floods** occurring annually and affecting over **1.5 billion people**, effective flood management is essential.
    """)

    model_selected = model_selection()
    st.write(f"Model Selected: {model_selected}")

    # Load selected model
    with st.spinner('Loading model...'):
        model = load_keras_model(model_selected)

    uploaded_file = st.file_uploader("Upload Image:", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None and model is not None:
        # Read and display the image
        image = Image.open(uploaded_file)
        
        # Create a container for results
        st.subheader("Water Region Detection Results")
        results_container = st.container()
        
        # Process image
        processed_image, original_size = preprocess_image(image)
        
        # Make prediction
        with st.spinner('Detecting water regions...'):
            prediction = model.predict(processed_image)
        
        # Post-process prediction
        mask_image = postprocess_prediction(prediction, original_size)
        
        # Create visualizations
        colored_mask = create_mask_visualization(mask_image)
        overlay_image = create_overlay(image, mask_image)
        
        # Display results row by row with download buttons
        with results_container:
            # Display Original Image
            st.markdown("**Original Image**")
            col1, col2 = st.columns([3, 1])
            with col1:
                st.image(image, width=350)
            with col2:
                buffered = io.BytesIO()
                image.save(buffered, format="PNG")
                st.download_button(
                    label="Download Original",
                    data=buffered.getvalue(),
                    file_name="original_image.png",
                    mime="image/png"
                )

            # Display Segmentation Mask
            st.markdown("**Segmentation Mask**")
            col1, col2 = st.columns([3, 1])
            with col1:
                st.image(colored_mask, width=350)
            with col2:
                buffered = io.BytesIO()
                colored_mask.save(buffered, format="PNG")
                st.download_button(
                    label="Download Mask",
                    data=buffered.getvalue(),
                    file_name="segmentation_mask.png",
                    mime="image/png"
                )

            # Display Overlay Result
            st.markdown("**Overlay Result**")
            col1, col2 = st.columns([3, 1])
            with col1:
                st.image(overlay_image, width=350)
            with col2:
                buffered = io.BytesIO()
                overlay_image.save(buffered, format="PNG")
                st.download_button(
                    label="Download Overlay",
                    data=buffered.getvalue(),
                    file_name="overlay_result.png",
                    mime="image/png"
                )

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