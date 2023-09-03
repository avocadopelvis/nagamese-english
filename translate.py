import streamlit as st
import sentencepiece as spm
import ctranslate2
from nltk import sent_tokenize

# Run the below command on command line to convert OpenNMT model to CTranslate2 format
# ct2-opennmt-py-converter --model_path nmt/models/eng-naga/model.fren_step_3000.pt --output_dir eng-naga --quantization int8

def translate(source, translator, sp_source_model, sp_target_model):
    """Use CTranslate model to translate a sentence

    Args:
        source (str): Source sentences to translate
        translator (object): Object of Translator, with the CTranslate2 model
        sp_source_model (object): Object of SentencePieceProcessor, with the SentencePiece source model
        sp_target_model (object): Object of SentencePieceProcessor, with the SentencePiece target model
    Returns:
        Translation of the source text
    """

    source_sentences = sent_tokenize(source)
    source_tokenized = sp_source_model.encode(source_sentences, out_type=str)
    translations = translator.translate_batch(source_tokenized)
    translations = [translation[0]["tokens"] for translation in translations]
    translations_detokenized = sp_target_model.decode(translations)
    translation = " ".join(translations_detokenized)

    return translation


# [Modify] File paths here to the CTranslate2 SentencePiece models.
# ct_model_path = "eng-naga/"
# sp_source_model_path = "nmt/target.model"
# sp_target_model_path = "nmt/source.model"

# # Create objects of CTranslate2 Translator and SentencePieceProcessor to load the models
# translator = ctranslate2.Translator(ct_model_path, "cpu")    # or "cuda" for GPU
# sp_source_model = spm.SentencePieceProcessor(sp_source_model_path)
# sp_target_model = spm.SentencePieceProcessor(sp_target_model_path)

def load_models(option):
    if option == "English-to-Nagamese":
        ct_model_path = "ctranslate2-models/eng-naga/"
        sp_source_model_path = "nmt/target.model"
        sp_target_model_path = "nmt/source.model"
    elif option == "Nagamese-to-English":
        ct_model_path = "ctranslate2-models/naga-eng/"
        sp_source_model_path = "nmt/source.model"
        sp_target_model_path = "nmt/target.model"

    translator = ctranslate2.Translator(ct_model_path)
    sp_source_model = spm.SentencePieceProcessor(sp_source_model_path)
    sp_target_model = spm.SentencePieceProcessor(sp_target_model_path)

    return translator, sp_source_model, sp_target_model


# Title for the page and nice icon
st.set_page_config(page_title="NMT", page_icon="🤖")
# Header
st.title("Translate")

# Form to add your items
with st.form("my_form"):
    # Dropdown menu to select a language pair
    option = st.selectbox(
    "Select Language Pair",
    ("English-to-Nagamese", "Nagamese-to-English"))
    #st.write('You selected:', option)

    # Textarea to type the source text.
    user_input = st.text_area("Source Text", max_chars=200)

    # Load models
    translator, sp_source_model, sp_target_model = load_models(option)

    # Translate with CTranslate2 model
    translation = translate(user_input, translator, sp_source_model, sp_target_model)

    # Create a button
    submitted = st.form_submit_button("Translate")
    # If the button pressed, print the translation
    # Here, we use "st.info", but you can try "st.write", "st.code", or "st.success".
    if submitted:
        st.write("Translation")
        st.info(translation)


# Optional Style
# Source: https://towardsdatascience.com/5-ways-to-customise-your-streamlit-ui-e914e458a17c
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
