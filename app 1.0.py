import streamlit as st
from PIL import Image
import io
import pandas as pd



def project_desc():
    project_desc = """
        <div style = 'text-align: justify;'>
            AquaSense addresses the critical challenge of accurately mapping and monitoring water regions in real time. 
            With approximately <strong>1,000 floods</strong> occurring annually and affecting over <strong>1.5 billion people</strong>, effective flood management is essential. 
            Floods can disrupt urban infrastructure and impact agricultural productivity in rural areas. 
            AquaSense utilizes advanced deep learning models like <strong>U-Net</strong> and <strong>DeepLabV3+</strong> for precise water region mapping from aerial imagery. 
            By employing <strong>semantic segmentation</strong>, AquaSense enables <strong>pixel-level identification</strong> of water bodies, providing valuable insights for disaster management and sustainable water resource planning.
        </div>
    """
    st.markdown(project_desc, unsafe_allow_html = True)



def unet_model_desc():
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



def deeplabv_model_desc():
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



def metric_comparison():
    # Comparison Table Data
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
                background-color: #cf7540}
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

    st.subheader("Model Performance Comparison")
    st.markdown(comparison_html, unsafe_allow_html=True)



def model_selection():
    st.subheader("Models:")
    selectBox = st.selectbox("Choose Models: ", ["U-Net", "DeepLabV3+"])
    st.write("Models selected :", selectBox)

    return selectBox



def application_and_future():
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



def main():
    st.title("Welcome to AquaSense: A Water Region Mapping Tool 🌊")
    st.markdown("#### Harness the power of Deep Learning to map water regions with precision!")

    # Model Description
    project_desc()
    st.markdown("---")

    # Model Description
    unet_model_desc()
    st.markdown("---")
    deeplabv_model_desc()
    st.markdown("---")

    # Model Comparison
    metric_comparison()
    st.markdown("---")

    # Model Selection
    model = model_selection()
    st.text(model)

    # File uploader
    uploaded_file = st.file_uploader("Upload Image:", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)

        # Create two columns
        col1, col2 = st.columns(2)

        # Display original image
        with col1:
            st.subheader("Original Image")
            st.image(image, use_column_width=True)

        # Display the same image in the second column
        with col2:
            st.subheader("Masked Image")
            st.image(image, use_column_width=True)
    st.markdown("---")
    
    # Application and Future Prospects
    application_and_future()



if __name__ == "__main__":
    main()