import streamlit
from PIL import Image
from img_search import similar_five_prediction

def run():
  streamlit.title('Zalando Fashion Items Image Search')
  uploaded_file = streamlit.file_uploader("Choose an image of clothing and search five similar", type=["png", "jpg"])
  if uploaded_file is not None:
    img = Image.open(uploaded_file)
    streamlit.image(img, caption='Uploaded pic.', use_column_width=True)
  if streamlit.button('Search five similar pics'):
    similar_five_prediction(img)
    streamlit.pyplot
if __name__=='__main__':
  run()