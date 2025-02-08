from PIL import Image
import io
import streamlit as st


def apply_frame(image: Image):
    # Read the predefined frame using PIL (already saved in the project)
    frame = Image.open("frame.png")

    # Resize the frame to match the image dimensions
    frame = frame.resize((image.width, image.height))

    # Place from on top of the image
    image.paste(frame, (0,0), mask = frame)

    return image

def main():
    st.title("Add a Palestine frame to your photo")

    st.image(Image.open("thumbnail.png"), caption="", use_column_width=True)

    # Upload image through Streamlit
    uploaded_image = st.file_uploader("Upload an image with 1:1 aspect ratio", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:

        # Apply the frame to the image
        result = apply_frame(Image.open(uploaded_image))

        st.markdown("##### Click the button below to download the image")

        # Convert the PIL Image to bytes
        image_bytes = io.BytesIO()
        result.save(image_bytes, format='PNG')

        # Offer the image for download
        st.download_button(
            label="Save Image",
            data=image_bytes.getvalue(),
            file_name="framed.png",
            key="save_button"
        )

        # Display the framed image
        st.image(result, caption="#IStandWithPalestine", use_column_width=True)


    st.markdown("---")
    st.markdown('<p style="text-align: center; color: gray;"><a style="color: gray; font-weight:600;" href="https://donate.unrwa.org/int/en/general">Donate for Palestine</a></p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
