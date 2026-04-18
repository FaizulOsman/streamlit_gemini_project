import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image

st.title("Note Summary and Quiz Generator")
st.markdown("Upload 3 images")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload photos",
        type=["jpg", "png", "jpeg"],
        accept_multiple_files=True
    )

    if images:
        if len(images) > 3:
            st.error("Please upload only 3 images")
        else:
            st.subheader("Uploaded Images")
            cols = st.columns(len(images))
            for idx, image in enumerate(images):
                cols[idx].image(image)

    # Difficulty
    selected_option = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"], index=None)
    
    pressed = st.button("Click to initiate AI", type="primary")


if pressed:
    if not images:
        st.error("You must upload at least 1 image")
    if not selected_option:
        st.error("You must select a difficulty level")
    
    if images and selected_option:
        pil_images = [Image.open(image) for image in images]
        # Note
        with st.container(border=True):
            st.subheader("Your note")

            # Here will show the response data of api call
            with st.spinner("AI is writing notes for you..."):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)

        # Audio Transcript
        with st.container(border=True):
            st.subheader("Audio Transcription")

            # Here will show the response data of api call
            with st.spinner("AI is transcribing audio for you..."):
                # Clearing markdowns
                generated_notes = generated_notes.replace("#", "")
                generated_notes = generated_notes.replace("*", "")
                generated_notes = generated_notes.replace("-", "")
                generated_notes = generated_notes.replace("`", "")

                st.audio(audio_transcription(generated_notes))

        # Quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Diffuculty)")

            # Here will show the response data of api call
            with st.spinner("AI is generating quizzes for you..."):
                quizzes = quiz_generator(pil_images, selected_option)
                st.markdown(quizzes)


