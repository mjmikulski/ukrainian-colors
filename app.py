import cv2
import numpy as np
import streamlit as st

from ukraine import make_ukrainian_colors

st.title('Ukraine colors on your avatar')

POSSIBLE_EXTENSIONS = ('png', 'jpg', 'jpeg')

input_file = st.file_uploader('Upload your image', type=POSSIBLE_EXTENSIONS)

st.sidebar.markdown("""

If you want to give feedback or have any problems with this app, create an issue [here](https://github.com/mjmikulski/ukrainian-colors/issues).

You can support Ukrainian Army by making a transfer [here](https://bank.gov.ua/en/news/all/natsionalniy-bank-vidkriv-spetsrahunok-dlya-zboru-koshtiv-na-potrebi-armiyi).

**Слава Україні!**
""")

if input_file is not None:
    type_, extension = input_file.type.lower().split('/')

    if type_ != 'image':
        st.error('Wrong input_file type.')
        st.stop()

    if extension not in POSSIBLE_EXTENSIONS:
        st.error(f'Unknown extension of the uploaded input_file: {extension}')
        st.stop()

    output_filename = f'SlavaUkraini--{input_file.name}'

    file_bytes = np.asarray(bytearray(input_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    img_ua = make_ukrainian_colors(img, saturate=True)

    temp_file = f'temp.{extension}'
    cv2.imwrite(temp_file, img_ua)

    st.image(img_ua, channels='bgr')

    with open(temp_file, 'rb') as output_file:
        st.download_button('Download', output_file, file_name=output_filename, mime=input_file.type)
